import json

paths = []
xoneof_descriptions = {}

descriptions = set()


def describe_xoneof(field_name, field, discriminator, xoneof):
    sections = ''
    for el in xoneof:
        properties = ''
        for (name, prop) in el['properties'].items():
            items = []

            if ('description' in prop):
                items.append(prop['description'])

            if ('enum' in prop):
                if len(prop['enum']) == 1:
                    items.append("Value must be `%s`." % prop['enum'][0])
                else:
                    items.append("Possible values: (%s)." % (', '.join([f"`{s}`" for s in prop['enum']])))

            items_str = "\n".join(items)
            prop_str = f"""
  *`{name}`* {items_str}
            """

            properties += prop_str

        section = f"""
### {el['title']}
{el['description']}

{properties}
        """

        sections += section


    description = f"""
## {field['title']}
{field['description']}

Each object in this array has a field named `{discriminator['propertyName']}`, which determines the meaning of the other fields in the object.

Each section below will describe the value that should be set in `{discriminator['propertyName']}`, and the meanings of the fields when that value is set.

{sections}
    """

    descriptions.add(description)

def find_field(breadcrumb, path, obj):
    if type(obj) is dict:
        #print("%s %s: %s" % (' ' * len(breadcrumb), path[-1]['name'], path[-1]['obj'].keys()))
        for (name, sub) in obj.items():
            if name == 'x-oneOf':
                paths.append(reversed(breadcrumb))
                describe_xoneof(path[-2]['name'], path[-2]['obj'], path[-1]['obj']['x-discriminator'], sub)
            else:
                find_field(breadcrumb + [name], path + [{'name': name, 'obj': sub}], sub)
    elif type(obj) is list:
        breadcrumb.append('[]')
        for el in obj:
            find_field(breadcrumb, path + [{'name': 'array', 'obj': el}], el)

def parse_properties(prop, depth=0):
    print(' ' * depth + ",".join(prop.keys()))

    if 'properties' in prop:
        for (name, subprop) in prop['properties'].items():
            print(name)
            parse_properties(subprop, depth + 1)
    elif 'x-oneOf' in prop:
        exit(1)
        parse_properties(prop, depth + 1)

f = open('spec.json')

o = json.load(f)

find_field([], [{'name': 'root', 'obj': o}], o)
print("\n\n\n".join(descriptions))
