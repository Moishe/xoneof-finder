# MAJOR HEADER: Segment Type
 The `array` array. Segment match conditions.
## Title: Aim Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Aim`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a specific campaign(s).. Value must be `aim`.
### Segment Operator
 `op` a string. The status of the member with regard to their campaign interaction. One of the following: opened, clicked, was sent, didn't open, didn't click, or was not sent.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. Either the web id value for a specific campaign or 'any' to account for subscribers who have/have not interacted with any campaigns.. 

## Title: Automation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Automation`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with an Automation workflow.. Value must be `automation`.
### Segment Operator
 `op` a string. The status of the member with regard to the automation workflow. One of the following: has started the workflow, has completed the workflow, has not started the workflow, or has not completed the workflow.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The web id for the automation workflow to segment against.. 

## Title: Poll Activity Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `CampaignPoll`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `poll`.
### Segment Operator
 `op` a string. Members have/have not interacted with a specific poll in a Mailchimp email.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the poll.. 

## Title: Conversation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Conversation`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a campaign via 'Converstaions'.. Value must be `conversation`.
### Segment Operator
 `op` a string. The status of a member's interaction with a conversation. One of the following: has replied or has not replied.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The web id value for a specific campaign or 'any' to account for subscribers who have/have not interacted with any campaigns.. 

## Title: Date Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Date`.
### Segment Field
 `field` a string. The type of date field to segment on: The opt-in time for a signup, the date the subscriber was last updated, or the date of their last ecomm purchase.. Possible values: (`%s`, `%s`, `%s`).
### Segment Operator
 `op` a string. When the event took place:  Before, after, is a specific date, is not a specific date, is blank, or is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. What type of data to segment on: a specific date, a specific campaign, or the last campaign sent.. 
### Segment Extra Value
 `extra` a string. When segmenting on 'date' or 'campaign', the date for the segment formatted as YYYY-MM-DD or the web id for the campaign.. 

## Title: Email Client Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EmailClient`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a specific campaign(s).. Value must be `email_client`.
### Segment Operator
 `op` a string. The status of the member with regard to their campaign interaction. One of the following: opened, clicked, was sent, didn't open, didn't click, or was not sent.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The name of the email client.. 

## Title: Language Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Language`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's language.. Value must be `language`.
### Segment Operator
 `op` a string. Whether the member's language is or is not set to a specific language.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. A two-letter language identifier.. 

## Title: Member Rating Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `MemberRating`.
### Segment Field
 `field` a string. Used for segmenting by member rating.. Value must be `rating`.
### Segment Operator
 `op` a string. Members who have have a rating that is/not exactly a given number or members who have a rating greater/less than a given number.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. The star rating number to segment against.. 

## Title: Signup Source Segment
## Description: An individual segment condition
### Type
 `condition_type` a string. Value must be `SignupSource`.
### Segment Field
 `field` a string. Value must be `source`.
### Segment Operator
 `op` a string. Whether the member's signup source was/was not a particular value.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The signup source.. 

## Title: Survey Monkey Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SurveyMonkey`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a survey monkey survey.. Value must be `survey_monkey`.
### Segment Operator
 `op` a string. The status of the member with regard to the survey.One of the following: has started the survey, has completed the survey, has not started the survey, or has not completed the survey.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Survey ID
 `value` a string. The unique ID of the survey monkey survey.. 

## Title: VIP Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `VIP`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's VIP status.. Value must be `gmonkey`.
### Segment Operator
 `op` a string. Whether the member is or is not marked as VIP.. Possible values: (`%s`, `%s`).

## Title: Interests Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Interests`.
### Segment Field
 `field` a string. Segmenting based on interest group information. This should start with 'interests-' followed by the grouping id. Ex. 'interests-123'.. 
### Segment Operator
 `op` a string. Whether the member is a part of one, all, or none of the groups.. Possible values: (`%s`, `%s`, `%s`).
### Segment Value
 `value` a array. An array containing strings, each representing a group id.. 

## Title: Ecommerce Category Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommCategory`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not purchased specific items or categories.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. A member who has purchased from a category/specific item that is/is not a specific name, where the category/item name contains/doesn't contain a specific phrase or string, or a category/item name that starts/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The ecommerce category/item information.. 

## Title: Ecommerce Number Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommNumber`.
### Segment Field
 `field` a string. Used for segmenting members have an average spent total, a total number of orders, total number of products purchased, or average number of products per order.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `op` a string. Members who have spent exactly, have not spent exactly, spent more, or spent less than the segment value.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. Members who have spent exactly, have not spent exactly, spent more, or spent less than this amount.. 

## Title: Ecommerce Purchased Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommPurchased`.
### Segment Field
 `field` a string. Used for segmenting members who have/have not purchased anything.. Value must be `ecomm_purchased`.
### Segment Operator
 `op` a string. Members who have have ('member') or have not ('notmember') purchased.. Possible values: (`%s`, `%s`).

## Title: Ecommerce Spent Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommSpent`.
### Segment Field
 `field` a string. Used for segmenting members who have spent a specific amount on a single order or over their lifetime.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. Members who have spent 'more' or 'less' than then specified value.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The total amount a member spent.. 

## Title: Ecommerce Purchased Store Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommStore`.
### Segment Field
 `field` a string. Used for segmenting members have purchased from a specific store.. Value must be `ecomm_store`.
### Segment Operator
 `op` a string. Members who have or have not purchased from a specific store.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The store id to segment against.. 

## Title: Goal Activity Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `GoalActivity`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's Goal activity.. Value must be `goal`.
### Segment Operator
 `op` a string. Whether the website URL is/not exactly, contains/doesn't contain, starts with/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The URL to check Goal activity against.. 

## Title: Goal Timestamp Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `GoalTimestamp`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's last interaction with a website.. Value must be `goal_last_visited`.
### Segment Operator
 `op` a string. Whether the website activity happened after, before, or at a given timestamp.. Possible values: (`%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The date to check Goal activity against.. 

## Title: Similar Subscribers Segment Member Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `FuzzySegment`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `fuzzy_segment`.
### Segment Operator
 `op` a string. Members who are/are not apart of a 'similar subscribers' segment.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the 'similar subscribers' segment.. 

## Title: Static Segment Member Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `StaticSegment`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `static_segment`.
### Segment Operator
 `op` a string. Members who are/are not apart of a static segment.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the static segment.. 

## Title: Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoCountryState`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific country or US state.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The two-letter country code or US state abbreviation.. 

## Title: Geolocation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoIn`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific geographic region.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The radius of the target location.. 
### Segment Location Address
 `addr` a string. The address of the target location.. 
### Segment Location Latitude
 `lat` a string. The latitude of the target location.. 
### Segment Location Longitude
 `lng` a string. The longitude of the target location.. 

## Title: US Zip Code Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoInZip`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific US zip code.. Value must be `ipgeoinzip`.
### Segment Data
 `value` a integer. The radius of the target location.. 
### Extra Data
 `extra` a integer. The zip code to segment against.. 

## Title: Unknown Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoUnknown`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members for which locaiton information is unknown.. Value must be `ipgeounknown`.

## Title: Zip Code Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoZip`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are/are not within a specific US zip code.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The 5-digit zip code.. 

## Title: Social Profiles Age Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialAge`.
### Segment Field
 `field` a string. Used for segmenting members based age ranges in Social Profiles data.. Value must be `social_age`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The age range to segment.. Possible values: (`%s`, `%s`, `%s`, `%s`).

## Title: Social Profiles Gender Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialGender`.
### Segment Field
 `field` a string. Used for segmenting members based on listed gender in Social Profiles data.. Value must be `social_gender`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The Social Profiles gender to segment.. Possible values: (`%s`, `%s`).

## Title: Social Profiles Influence Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialInfluence`.
### Segment Field
 `field` a string. Used for segmenting members based on influence rating in Social Profiles data.. Value must be `social_influence`.
### Segment Operator
 `op` a string. Members who have a rating that is/not or greater/less than the rating provided.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. The Social Profiles influence rating to segment.. 

## Title: Social Profiles Social Network Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialNetworkMember`.
### Segment Field
 `field` a string. Used for segmenting members based on social network in Social Profiles data.. Value must be `social_network`.
### Segment Operator
 `op` a string. Members who are/not on a given social network.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The social network to segment against.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).

## Title: Social Profiles Social Network Follow Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialNetworkFollow`.
### Segment Field
 `field` a string. Used for segmenting members based on social network in Social Profiles data.. Value must be `social_network`.
### Segment Operator
 `op` a string. Members who are/not following a linked account on a given social network.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The social network to segment against.. Value must be `twitter_follow`.

## Title: Address Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `AddressMerge`.
### Segment Field
 `field` a string. An address-type merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's address merge field contains/does not contain a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text merge field with.. 

## Title: Address/Zip Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `ZipMerge`.
### Segment Field
 `field` a string. An address or zip-type merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's address merge field is within a given distance from a city or zip.. Value must be `geoin`.
### Segment Value
 `value` a string. The distance from the city/zip.. 
### Segment Extra
 `extra` a string. The city or the zip being used to segment against.. 

## Title: Birthday Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `BirthdayMerge`.
### Segment Field
 `field` a string. A date merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's birthday merge information is/is not a certain date or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. A date to segment against (mm/dd).. 

## Title: Date Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `DateMerge`.
### Segment Field
 `field` a string. A date merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not, is greater/less than a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. A date to segment against.. 

## Title: Dropdown/Radio Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SelectMerge`.
### Segment Field
 `field` a string. A merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text merge field with.. 

## Title: Text or Number Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `TextMerge`.
### Segment Field
 `field` a string. A text or number merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not, contains/does not contain, starts/ends with, or is greater/less than a value. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text or number merge field with.. 

## Title: Email Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EmailAddress`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's email address.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. Whether the email address is/not exactly, contains/doesn't contain, starts/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to compare the email against.. 

## Title: Predicted Gender Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `PredictedGender`.
### Segment Field
 `field` a string. Used for segmenting members based on predicted gender.. Value must be `predicted_gender`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The predicted gender to segment.. Possible values: (`%s`, `%s`).

## Title: Predicted Age Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `PredictedAge`.
### Segment Field
 `field` a string. Used for segmenting members based on predicted age. Value must be `predicted_age_range`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Value must be `is`.
### Segment Operator
 `value` a string. The predicted age to segment.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).

## Title: New Subscribers Prebuilt Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `NewSubscribers`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have subscribed within a given time frame.. Value must be `timestamp_opt`.
### Segment Operator
 `op` a string. Whe the event took place, namely within a time frame.. Value must be `date_within`.
### Segment Data
 `value` a string. What type of data to segment on: a specific date, a specific campaign, or the last campaign sent.. 



# MAJOR HEADER: Preview Segment Type
 The `conditions` array. An array of possible segment conditions.
## Title: Signup Source Segment
## Description: An individual segment condition
### Type
 `condition_type` a string. Value must be `SignupSource`.
### Segment Field
 `field` a string. Value must be `source`.
### Segment Operator
 `op` a string. Whether the member's signup source was/was not a particular value.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The signup source.. 

## Title: Landing Page Activity Segment
## Description: An individual segment condition
### Type
 `condition_type` a string. Value must be `LandingPageActivity`.
### Segment Field
 `field` a string. Value must be `landing_page`.
### Segment Operator
 `op` a string. Whether the member signed up with a particular page. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. Page ID. Use the ID of the page to segment on. 



# MAJOR HEADER: Segment Type
 The `SegmentCondition` array. Segment match conditions.
## Title: Aim Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Aim`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a specific campaign(s).. Value must be `aim`.
### Segment Operator
 `op` a string. The status of the member with regard to their campaign interaction. One of the following: opened, clicked, was sent, didn't open, didn't click, or was not sent.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. Either the web id value for a specific campaign or 'any' to account for subscribers who have/have not interacted with any campaigns.. 

## Title: Automation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Automation`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with an Automation workflow.. Value must be `automation`.
### Segment Operator
 `op` a string. The status of the member with regard to the automation workflow. One of the following: has started the workflow, has completed the workflow, has not started the workflow, or has not completed the workflow.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The web id for the automation workflow to segment against.. 

## Title: Poll Activity Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `CampaignPoll`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `poll`.
### Segment Operator
 `op` a string. Members have/have not interacted with a specific poll in a Mailchimp email.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the poll.. 

## Title: Conversation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Conversation`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a campaign via 'Converstaions'.. Value must be `conversation`.
### Segment Operator
 `op` a string. The status of a member's interaction with a conversation. One of the following: has replied or has not replied.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The web id value for a specific campaign or 'any' to account for subscribers who have/have not interacted with any campaigns.. 

## Title: Date Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Date`.
### Segment Field
 `field` a string. The type of date field to segment on: The opt-in time for a signup, the date the subscriber was last updated, or the date of their last ecomm purchase.. Possible values: (`%s`, `%s`, `%s`).
### Segment Operator
 `op` a string. When the event took place:  Before, after, is a specific date, is not a specific date, is blank, or is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. What type of data to segment on: a specific date, a specific campaign, or the last campaign sent.. 
### Segment Extra Value
 `extra` a string. When segmenting on 'date' or 'campaign', the date for the segment formatted as YYYY-MM-DD or the web id for the campaign.. 

## Title: Email Client Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EmailClient`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a specific campaign(s).. Value must be `email_client`.
### Segment Operator
 `op` a string. The status of the member with regard to their campaign interaction. One of the following: opened, clicked, was sent, didn't open, didn't click, or was not sent.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The name of the email client.. 

## Title: Language Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Language`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's language.. Value must be `language`.
### Segment Operator
 `op` a string. Whether the member's language is or is not set to a specific language.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. A two-letter language identifier.. 

## Title: Member Rating Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `MemberRating`.
### Segment Field
 `field` a string. Used for segmenting by member rating.. Value must be `rating`.
### Segment Operator
 `op` a string. Members who have have a rating that is/not exactly a given number or members who have a rating greater/less than a given number.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. The star rating number to segment against.. 

## Title: Signup Source Segment
## Description: An individual segment condition
### Type
 `condition_type` a string. Value must be `SignupSource`.
### Segment Field
 `field` a string. Value must be `source`.
### Segment Operator
 `op` a string. Whether the member's signup source was/was not a particular value.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The signup source.. 

## Title: Survey Monkey Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SurveyMonkey`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a survey monkey survey.. Value must be `survey_monkey`.
### Segment Operator
 `op` a string. The status of the member with regard to the survey.One of the following: has started the survey, has completed the survey, has not started the survey, or has not completed the survey.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Survey ID
 `value` a string. The unique ID of the survey monkey survey.. 

## Title: VIP Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `VIP`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's VIP status.. Value must be `gmonkey`.
### Segment Operator
 `op` a string. Whether the member is or is not marked as VIP.. Possible values: (`%s`, `%s`).

## Title: Interests Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Interests`.
### Segment Field
 `field` a string. Segmenting based on interest group information. This should start with 'interests-' followed by the grouping id. Ex. 'interests-123'.. 
### Segment Operator
 `op` a string. Whether the member is a part of one, all, or none of the groups.. Possible values: (`%s`, `%s`, `%s`).
### Segment Value
 `value` a array. An array containing strings, each representing a group id.. 

## Title: Ecommerce Category Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommCategory`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not purchased specific items or categories.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. A member who has purchased from a category/specific item that is/is not a specific name, where the category/item name contains/doesn't contain a specific phrase or string, or a category/item name that starts/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The ecommerce category/item information.. 

## Title: Ecommerce Number Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommNumber`.
### Segment Field
 `field` a string. Used for segmenting members have an average spent total, a total number of orders, total number of products purchased, or average number of products per order.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `op` a string. Members who have spent exactly, have not spent exactly, spent more, or spent less than the segment value.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. Members who have spent exactly, have not spent exactly, spent more, or spent less than this amount.. 

## Title: Ecommerce Purchased Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommPurchased`.
### Segment Field
 `field` a string. Used for segmenting members who have/have not purchased anything.. Value must be `ecomm_purchased`.
### Segment Operator
 `op` a string. Members who have have ('member') or have not ('notmember') purchased.. Possible values: (`%s`, `%s`).

## Title: Ecommerce Spent Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommSpent`.
### Segment Field
 `field` a string. Used for segmenting members who have spent a specific amount on a single order or over their lifetime.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. Members who have spent 'more' or 'less' than then specified value.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The total amount a member spent.. 

## Title: Ecommerce Purchased Store Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommStore`.
### Segment Field
 `field` a string. Used for segmenting members have purchased from a specific store.. Value must be `ecomm_store`.
### Segment Operator
 `op` a string. Members who have or have not purchased from a specific store.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The store id to segment against.. 

## Title: Goal Activity Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `GoalActivity`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's Goal activity.. Value must be `goal`.
### Segment Operator
 `op` a string. Whether the website URL is/not exactly, contains/doesn't contain, starts with/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The URL to check Goal activity against.. 

## Title: Goal Timestamp Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `GoalTimestamp`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's last interaction with a website.. Value must be `goal_last_visited`.
### Segment Operator
 `op` a string. Whether the website activity happened after, before, or at a given timestamp.. Possible values: (`%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The date to check Goal activity against.. 

## Title: Similar Subscribers Segment Member Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `FuzzySegment`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `fuzzy_segment`.
### Segment Operator
 `op` a string. Members who are/are not apart of a 'similar subscribers' segment.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the 'similar subscribers' segment.. 

## Title: Static Segment Member Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `StaticSegment`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `static_segment`.
### Segment Operator
 `op` a string. Members who are/are not apart of a static segment.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the static segment.. 

## Title: Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoCountryState`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific country or US state.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The two-letter country code or US state abbreviation.. 

## Title: Geolocation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoIn`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific geographic region.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The radius of the target location.. 
### Segment Location Address
 `addr` a string. The address of the target location.. 
### Segment Location Latitude
 `lat` a string. The latitude of the target location.. 
### Segment Location Longitude
 `lng` a string. The longitude of the target location.. 

## Title: US Zip Code Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoInZip`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific US zip code.. Value must be `ipgeoinzip`.
### Segment Data
 `value` a integer. The radius of the target location.. 
### Extra Data
 `extra` a integer. The zip code to segment against.. 

## Title: Unknown Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoUnknown`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members for which locaiton information is unknown.. Value must be `ipgeounknown`.

## Title: Zip Code Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoZip`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are/are not within a specific US zip code.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The 5-digit zip code.. 

## Title: Social Profiles Age Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialAge`.
### Segment Field
 `field` a string. Used for segmenting members based age ranges in Social Profiles data.. Value must be `social_age`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The age range to segment.. Possible values: (`%s`, `%s`, `%s`, `%s`).

## Title: Social Profiles Gender Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialGender`.
### Segment Field
 `field` a string. Used for segmenting members based on listed gender in Social Profiles data.. Value must be `social_gender`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The Social Profiles gender to segment.. Possible values: (`%s`, `%s`).

## Title: Social Profiles Influence Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialInfluence`.
### Segment Field
 `field` a string. Used for segmenting members based on influence rating in Social Profiles data.. Value must be `social_influence`.
### Segment Operator
 `op` a string. Members who have a rating that is/not or greater/less than the rating provided.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. The Social Profiles influence rating to segment.. 

## Title: Social Profiles Social Network Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialNetworkMember`.
### Segment Field
 `field` a string. Used for segmenting members based on social network in Social Profiles data.. Value must be `social_network`.
### Segment Operator
 `op` a string. Members who are/not on a given social network.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The social network to segment against.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).

## Title: Social Profiles Social Network Follow Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialNetworkFollow`.
### Segment Field
 `field` a string. Used for segmenting members based on social network in Social Profiles data.. Value must be `social_network`.
### Segment Operator
 `op` a string. Members who are/not following a linked account on a given social network.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The social network to segment against.. Value must be `twitter_follow`.

## Title: Address Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `AddressMerge`.
### Segment Field
 `field` a string. An address-type merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's address merge field contains/does not contain a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text merge field with.. 

## Title: Address/Zip Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `ZipMerge`.
### Segment Field
 `field` a string. An address or zip-type merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's address merge field is within a given distance from a city or zip.. Value must be `geoin`.
### Segment Value
 `value` a string. The distance from the city/zip.. 
### Segment Extra
 `extra` a string. The city or the zip being used to segment against.. 

## Title: Birthday Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `BirthdayMerge`.
### Segment Field
 `field` a string. A date merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's birthday merge information is/is not a certain date or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. A date to segment against (mm/dd).. 

## Title: Date Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `DateMerge`.
### Segment Field
 `field` a string. A date merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not, is greater/less than a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. A date to segment against.. 

## Title: Dropdown/Radio Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SelectMerge`.
### Segment Field
 `field` a string. A merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text merge field with.. 

## Title: Text or Number Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `TextMerge`.
### Segment Field
 `field` a string. A text or number merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not, contains/does not contain, starts/ends with, or is greater/less than a value. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text or number merge field with.. 

## Title: Email Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EmailAddress`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's email address.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. Whether the email address is/not exactly, contains/doesn't contain, starts/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to compare the email against.. 

## Title: Predicted Gender Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `PredictedGender`.
### Segment Field
 `field` a string. Used for segmenting members based on predicted gender.. Value must be `predicted_gender`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The predicted gender to segment.. Possible values: (`%s`, `%s`).

## Title: Predicted Age Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `PredictedAge`.
### Segment Field
 `field` a string. Used for segmenting members based on predicted age. Value must be `predicted_age_range`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Value must be `is`.
### Segment Operator
 `value` a string. The predicted age to segment.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).

## Title: New Subscribers Prebuilt Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `NewSubscribers`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have subscribed within a given time frame.. Value must be `timestamp_opt`.
### Segment Operator
 `op` a string. Whe the event took place, namely within a time frame.. Value must be `date_within`.
### Segment Data
 `value` a string. What type of data to segment on: a specific date, a specific campaign, or the last campaign sent.. 



# MAJOR HEADER: Activity
 The `activity` array. An array of objects, each representing a contact's event.
## Title: Email Opens
## Description: Activity feed item representing opening an email.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `open`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Campaign ID
 `campaign_id` a string. The campaign's unique id.. 
### Campaign Title
 `campaign_title` a string. The title of the campaign.. 

## Title: Email Clicks
## Description: Activity feed item representing having a link clicked by a contact.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `click`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Campaign ID
 `campaign_id` a string. The campaign's unique id.. 
### Campaign Title
 `campaign_title` a string. The title of the campaign.. 
### Link Clicked
 `link_clicked` a string. The URL of the link that was clicked.. 

## Title: Email Bounced
## Description: Activity feed item representing an email to this contact bouncing.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `bounce`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Campaign ID
 `campaign_id` a string. The campaign's unique id.. 
### Campaign Title
 `campaign_title` a string. The title of the campaign.. 
### Bounce Type
 `bounce_type` a string. The type of bounce.. Possible values: (`%s`, `%s`).
### Bounce Has Open Activity
 `bounce_has_open_activity` a boolean. Indicates if the email associated with this bounce also has open activity on the same campaign.. 

## Title: List Unsubscribed
## Description: Activity feed item representing this contact unsubscribing from a list.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `unsub`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Campaign ID
 `campaign_id` a string. The campaign's unique id.. 
### Campaign Text
 `campaign_title` a string. The title of the campaign.. 
### Is Admin Unsubscribed
 `is_admin_unsubscribed` a boolean. Indicates if an admin unsubscribed a contact.. 
### Unsubscribe Reason
 `unsubscribe_reason` a string. Indicates the reason that the contact was unsubscribed.. 

## Title: Email Sent
## Description: Activity feed item representing having an email sent to the contact.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `sent`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Campaign ID
 `campaign_id` a string. The campaign's unique id.. 
### Campaign Title
 `campaign_title` a string. The title of the campaign.. 

## Title: Email Conversation
## Description: Activity feed item representing an individual reply in a conversation.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `conversation`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Campaign ID
 `campaign_id` a string. The campaign's unique id.. 
### Campaign Title
 `campaign_title` a string. The title of the campaign.. 
### Thread ID
 `thread_id` a string. The thread's unique id of the conversation referenced in this event.. 
### Message Text
 `message_text` a string. The body of the message in this conversation.. 
### Created By
 `created_by` a string. The username of the person who created this event.. 
### Is User
 `is_user` a boolean. Indicates that the message created by a user (as opposed to a contact).. 
### Has Read
 `has_read` a boolean. Indicates that the message has been read.. 
### From Email
 `from_email` a string. The email of the contact who sent the reply.. 
### Avatar URL
 `avatar_url` a string. The gravatar URL of the contact who sent the reply.. 

## Title: Note
## Description: Activity feed item representing a note on the contact record.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `note`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Updated At Timestamp
 `updated_at_timestamp` a string. The updated at timestamp in ISO8601.. 
### Note ID
 `note_id` a string. The note's unique id.. 
### Note Text
 `note_text` a string. The note's text.. 
### Created By
 `created_by` a string. The person who created the note.. 
### Avatar URL
 `avatar_url` a string. The URL of the contact's profile gravatar image.. 

## Title: Marketing Permission
## Description: Activity feed item indicating if a marketing permission was added or updated.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `marketing_permission`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Marketing Permission Text
 `marketing_permisson_text` a string. The text describing this marketing permission.. 
### Updated By
 `updated_by` a string. The name of the contact who updated this permission.. 
### Marketing Permission Opted In
 `marketing_permission_opted_in` a boolean. Indicates if the marketing permission is enabled or not.. 

## Title: Postcard Sent
## Description: Activity feed item representing a time when a contact was sent a particular postcard.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `postcard_sent`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Outreach ID
 `outreach_id` a string. The outreach's unique id.. 
### Outreach Title
 `outreach_title` a string. The title of the outreach.. 

## Title: Squatter Signup
## Description: Activity feed item to representing a contact signing up for the audience from a squatter page.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `squatter_signup`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Outreach ID
 `outreach_id` a string. The outreach's unique id.. 
### Outreach Title
 `outreach_title` a string. The title of the outreach.. 

## Title: Website Signup
## Description: Activity feed item to representing a contact signing up for the contact through a website page.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `website_signup`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Outreach ID
 `outreach_id` a string. The outreach's unique id.. 
### Outreach Title
 `outreach_title` a string. The title of the outreach.. 

## Title: Landing Page Signup
## Description: Activity feed item to representing a contact signing up for the list via a landing page.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `landing_page_signup`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Outreach ID
 `outreach_id` a string. The outreach's unique id.. 
### Outreach Title
 `outreach_title` a string. The title of the outreach.. 

## Title: Ecommerce Signup
## Description: Activity feed item to representing a contact signing up for the list via a ecommerce store.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `ecommerce_signup`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Store Name
 `store_name` a string. The name of the store.. 

## Title: Generic Signup
## Description: Activity feed item that represents a contact signing up for the audience via a generic some generic method (specifically, one we can't link to).
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `generic_signup`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Signup Category
 `signup_category` a string. How was this user added to the list.. 

## Title: Ecommerce Order
## Description: Activity feed item that represents an order.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `order`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Outreach ID
 `outreach_id` a string. The outreach's unique id.. 
### Outreach Type
 `outreach_type` a string. The type of outreach that triggered the event.. 
### Outreach Title
 `outreach_title` a string. The title of the outreach.. 
### Order ID
 `order_id` a string. The unique order id.. 
### Order Total
 `order_total` a string. The order total formatted as a string.. 
### Order Items
 `order_items` a array. An array of items that have been ordered.. 
### Store Name
 `store_name` a string. The name of the store for an order.. 
### Order URL
 `order_url` a string. The order URL.. 

## Title: Contact Activity Event
## Description: Activity feed item that represents a generic event.
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `event`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Event Name
 `event_name` a string. The name of the event.. 
### Event Properties
 `event_properties` a array. An arbitrary datastore containing properties for the given event.. 

## Title: Survey response
## Description: Represents when a contact completes and submits a survey
### activity_type
 `activity_type` a string. The type of event activity.. Value must be `survey_response`.
### Created At Timestamp
 `created_at_timestamp` a string. The created at timestamp in ISO8601.. 
### Survey ID
 `survey_id` a string. The survey's unique id.. 
### Survey Title
 `survey_title` a string. The title of the survey.. 



# MAJOR HEADER: Segment Type
 The `conditions` array. Segment match conditions.
## Title: Aim Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Aim`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a specific campaign(s).. Value must be `aim`.
### Segment Operator
 `op` a string. The status of the member with regard to their campaign interaction. One of the following: opened, clicked, was sent, didn't open, didn't click, or was not sent.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. Either the web id value for a specific campaign or 'any' to account for subscribers who have/have not interacted with any campaigns.. 

## Title: Automation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Automation`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with an Automation workflow.. Value must be `automation`.
### Segment Operator
 `op` a string. The status of the member with regard to the automation workflow. One of the following: has started the workflow, has completed the workflow, has not started the workflow, or has not completed the workflow.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The web id for the automation workflow to segment against.. 

## Title: Poll Activity Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `CampaignPoll`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `poll`.
### Segment Operator
 `op` a string. Members have/have not interacted with a specific poll in a Mailchimp email.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the poll.. 

## Title: Conversation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Conversation`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a campaign via 'Converstaions'.. Value must be `conversation`.
### Segment Operator
 `op` a string. The status of a member's interaction with a conversation. One of the following: has replied or has not replied.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The web id value for a specific campaign or 'any' to account for subscribers who have/have not interacted with any campaigns.. 

## Title: Date Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Date`.
### Segment Field
 `field` a string. The type of date field to segment on: The opt-in time for a signup, the date the subscriber was last updated, or the date of their last ecomm purchase.. Possible values: (`%s`, `%s`, `%s`).
### Segment Operator
 `op` a string. When the event took place:  Before, after, is a specific date, is not a specific date, is blank, or is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. What type of data to segment on: a specific date, a specific campaign, or the last campaign sent.. 
### Segment Extra Value
 `extra` a string. When segmenting on 'date' or 'campaign', the date for the segment formatted as YYYY-MM-DD or the web id for the campaign.. 

## Title: Email Client Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EmailClient`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a specific campaign(s).. Value must be `email_client`.
### Segment Operator
 `op` a string. The status of the member with regard to their campaign interaction. One of the following: opened, clicked, was sent, didn't open, didn't click, or was not sent.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The name of the email client.. 

## Title: Language Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Language`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's language.. Value must be `language`.
### Segment Operator
 `op` a string. Whether the member's language is or is not set to a specific language.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. A two-letter language identifier.. 

## Title: Member Rating Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `MemberRating`.
### Segment Field
 `field` a string. Used for segmenting by member rating.. Value must be `rating`.
### Segment Operator
 `op` a string. Members who have have a rating that is/not exactly a given number or members who have a rating greater/less than a given number.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. The star rating number to segment against.. 

## Title: Signup Source Segment
## Description: An individual segment condition
### Type
 `condition_type` a string. Value must be `SignupSource`.
### Segment Field
 `field` a string. Value must be `source`.
### Segment Operator
 `op` a string. Whether the member's signup source was/was not a particular value.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The signup source.. 

## Title: Survey Monkey Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SurveyMonkey`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a survey monkey survey.. Value must be `survey_monkey`.
### Segment Operator
 `op` a string. The status of the member with regard to the survey.One of the following: has started the survey, has completed the survey, has not started the survey, or has not completed the survey.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Survey ID
 `value` a string. The unique ID of the survey monkey survey.. 

## Title: VIP Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `VIP`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's VIP status.. Value must be `gmonkey`.
### Segment Operator
 `op` a string. Whether the member is or is not marked as VIP.. Possible values: (`%s`, `%s`).

## Title: Interests Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Interests`.
### Segment Field
 `field` a string. Segmenting based on interest group information. This should start with 'interests-' followed by the grouping id. Ex. 'interests-123'.. 
### Segment Operator
 `op` a string. Whether the member is a part of one, all, or none of the groups.. Possible values: (`%s`, `%s`, `%s`).
### Segment Value
 `value` a array. An array containing strings, each representing a group id.. 

## Title: Ecommerce Category Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommCategory`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not purchased specific items or categories.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. A member who has purchased from a category/specific item that is/is not a specific name, where the category/item name contains/doesn't contain a specific phrase or string, or a category/item name that starts/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The ecommerce category/item information.. 

## Title: Ecommerce Number Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommNumber`.
### Segment Field
 `field` a string. Used for segmenting members have an average spent total, a total number of orders, total number of products purchased, or average number of products per order.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `op` a string. Members who have spent exactly, have not spent exactly, spent more, or spent less than the segment value.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. Members who have spent exactly, have not spent exactly, spent more, or spent less than this amount.. 

## Title: Ecommerce Purchased Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommPurchased`.
### Segment Field
 `field` a string. Used for segmenting members who have/have not purchased anything.. Value must be `ecomm_purchased`.
### Segment Operator
 `op` a string. Members who have have ('member') or have not ('notmember') purchased.. Possible values: (`%s`, `%s`).

## Title: Ecommerce Spent Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommSpent`.
### Segment Field
 `field` a string. Used for segmenting members who have spent a specific amount on a single order or over their lifetime.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. Members who have spent 'more' or 'less' than then specified value.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The total amount a member spent.. 

## Title: Ecommerce Purchased Store Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommStore`.
### Segment Field
 `field` a string. Used for segmenting members have purchased from a specific store.. Value must be `ecomm_store`.
### Segment Operator
 `op` a string. Members who have or have not purchased from a specific store.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The store id to segment against.. 

## Title: Goal Activity Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `GoalActivity`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's Goal activity.. Value must be `goal`.
### Segment Operator
 `op` a string. Whether the website URL is/not exactly, contains/doesn't contain, starts with/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The URL to check Goal activity against.. 

## Title: Goal Timestamp Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `GoalTimestamp`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's last interaction with a website.. Value must be `goal_last_visited`.
### Segment Operator
 `op` a string. Whether the website activity happened after, before, or at a given timestamp.. Possible values: (`%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The date to check Goal activity against.. 

## Title: Similar Subscribers Segment Member Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `FuzzySegment`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `fuzzy_segment`.
### Segment Operator
 `op` a string. Members who are/are not apart of a 'similar subscribers' segment.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the 'similar subscribers' segment.. 

## Title: Static Segment Member Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `StaticSegment`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `static_segment`.
### Segment Operator
 `op` a string. Members who are/are not apart of a static segment.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the static segment.. 

## Title: Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoCountryState`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific country or US state.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The two-letter country code or US state abbreviation.. 

## Title: Geolocation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoIn`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific geographic region.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The radius of the target location.. 
### Segment Location Address
 `addr` a string. The address of the target location.. 
### Segment Location Latitude
 `lat` a string. The latitude of the target location.. 
### Segment Location Longitude
 `lng` a string. The longitude of the target location.. 

## Title: US Zip Code Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoInZip`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific US zip code.. Value must be `ipgeoinzip`.
### Segment Data
 `value` a integer. The radius of the target location.. 
### Extra Data
 `extra` a integer. The zip code to segment against.. 

## Title: Unknown Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoUnknown`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members for which locaiton information is unknown.. Value must be `ipgeounknown`.

## Title: Zip Code Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoZip`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are/are not within a specific US zip code.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The 5-digit zip code.. 

## Title: Social Profiles Age Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialAge`.
### Segment Field
 `field` a string. Used for segmenting members based age ranges in Social Profiles data.. Value must be `social_age`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The age range to segment.. Possible values: (`%s`, `%s`, `%s`, `%s`).

## Title: Social Profiles Gender Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialGender`.
### Segment Field
 `field` a string. Used for segmenting members based on listed gender in Social Profiles data.. Value must be `social_gender`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The Social Profiles gender to segment.. Possible values: (`%s`, `%s`).

## Title: Social Profiles Influence Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialInfluence`.
### Segment Field
 `field` a string. Used for segmenting members based on influence rating in Social Profiles data.. Value must be `social_influence`.
### Segment Operator
 `op` a string. Members who have a rating that is/not or greater/less than the rating provided.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. The Social Profiles influence rating to segment.. 

## Title: Social Profiles Social Network Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialNetworkMember`.
### Segment Field
 `field` a string. Used for segmenting members based on social network in Social Profiles data.. Value must be `social_network`.
### Segment Operator
 `op` a string. Members who are/not on a given social network.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The social network to segment against.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).

## Title: Social Profiles Social Network Follow Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialNetworkFollow`.
### Segment Field
 `field` a string. Used for segmenting members based on social network in Social Profiles data.. Value must be `social_network`.
### Segment Operator
 `op` a string. Members who are/not following a linked account on a given social network.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The social network to segment against.. Value must be `twitter_follow`.

## Title: Address Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `AddressMerge`.
### Segment Field
 `field` a string. An address-type merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's address merge field contains/does not contain a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text merge field with.. 

## Title: Address/Zip Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `ZipMerge`.
### Segment Field
 `field` a string. An address or zip-type merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's address merge field is within a given distance from a city or zip.. Value must be `geoin`.
### Segment Value
 `value` a string. The distance from the city/zip.. 
### Segment Extra
 `extra` a string. The city or the zip being used to segment against.. 

## Title: Birthday Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `BirthdayMerge`.
### Segment Field
 `field` a string. A date merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's birthday merge information is/is not a certain date or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. A date to segment against (mm/dd).. 

## Title: Date Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `DateMerge`.
### Segment Field
 `field` a string. A date merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not, is greater/less than a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. A date to segment against.. 

## Title: Dropdown/Radio Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SelectMerge`.
### Segment Field
 `field` a string. A merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text merge field with.. 

## Title: Text or Number Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `TextMerge`.
### Segment Field
 `field` a string. A text or number merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not, contains/does not contain, starts/ends with, or is greater/less than a value. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text or number merge field with.. 

## Title: Email Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EmailAddress`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's email address.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. Whether the email address is/not exactly, contains/doesn't contain, starts/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to compare the email against.. 

## Title: Predicted Gender Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `PredictedGender`.
### Segment Field
 `field` a string. Used for segmenting members based on predicted gender.. Value must be `predicted_gender`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The predicted gender to segment.. Possible values: (`%s`, `%s`).

## Title: Predicted Age Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `PredictedAge`.
### Segment Field
 `field` a string. Used for segmenting members based on predicted age. Value must be `predicted_age_range`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Value must be `is`.
### Segment Operator
 `value` a string. The predicted age to segment.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).

## Title: New Subscribers Prebuilt Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `NewSubscribers`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have subscribed within a given time frame.. Value must be `timestamp_opt`.
### Segment Operator
 `op` a string. Whe the event took place, namely within a time frame.. Value must be `date_within`.
### Segment Data
 `value` a string. What type of data to segment on: a specific date, a specific campaign, or the last campaign sent.. 



# MAJOR HEADER: Segment Type
 The `items` array. Segment match conditions.
## Title: Aim Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Aim`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a specific campaign(s).. Value must be `aim`.
### Segment Operator
 `op` a string. The status of the member with regard to their campaign interaction. One of the following: opened, clicked, was sent, didn't open, didn't click, or was not sent.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. Either the web id value for a specific campaign or 'any' to account for subscribers who have/have not interacted with any campaigns.. 

## Title: Automation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Automation`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with an Automation workflow.. Value must be `automation`.
### Segment Operator
 `op` a string. The status of the member with regard to the automation workflow. One of the following: has started the workflow, has completed the workflow, has not started the workflow, or has not completed the workflow.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The web id for the automation workflow to segment against.. 

## Title: Poll Activity Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `CampaignPoll`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `poll`.
### Segment Operator
 `op` a string. Members have/have not interacted with a specific poll in a Mailchimp email.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the poll.. 

## Title: Conversation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Conversation`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a campaign via 'Converstaions'.. Value must be `conversation`.
### Segment Operator
 `op` a string. The status of a member's interaction with a conversation. One of the following: has replied or has not replied.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The web id value for a specific campaign or 'any' to account for subscribers who have/have not interacted with any campaigns.. 

## Title: Date Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Date`.
### Segment Field
 `field` a string. The type of date field to segment on: The opt-in time for a signup, the date the subscriber was last updated, or the date of their last ecomm purchase.. Possible values: (`%s`, `%s`, `%s`).
### Segment Operator
 `op` a string. When the event took place:  Before, after, is a specific date, is not a specific date, is blank, or is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. What type of data to segment on: a specific date, a specific campaign, or the last campaign sent.. 
### Segment Extra Value
 `extra` a string. When segmenting on 'date' or 'campaign', the date for the segment formatted as YYYY-MM-DD or the web id for the campaign.. 

## Title: Email Client Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EmailClient`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a specific campaign(s).. Value must be `email_client`.
### Segment Operator
 `op` a string. The status of the member with regard to their campaign interaction. One of the following: opened, clicked, was sent, didn't open, didn't click, or was not sent.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The name of the email client.. 

## Title: Language Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Language`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's language.. Value must be `language`.
### Segment Operator
 `op` a string. Whether the member's language is or is not set to a specific language.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. A two-letter language identifier.. 

## Title: Member Rating Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `MemberRating`.
### Segment Field
 `field` a string. Used for segmenting by member rating.. Value must be `rating`.
### Segment Operator
 `op` a string. Members who have have a rating that is/not exactly a given number or members who have a rating greater/less than a given number.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. The star rating number to segment against.. 

## Title: Signup Source Segment
## Description: An individual segment condition
### Type
 `condition_type` a string. Value must be `SignupSource`.
### Segment Field
 `field` a string. Value must be `source`.
### Segment Operator
 `op` a string. Whether the member's signup source was/was not a particular value.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a string. The signup source.. 

## Title: Survey Monkey Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SurveyMonkey`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not interacted with a survey monkey survey.. Value must be `survey_monkey`.
### Segment Operator
 `op` a string. The status of the member with regard to the survey.One of the following: has started the survey, has completed the survey, has not started the survey, or has not completed the survey.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Survey ID
 `value` a string. The unique ID of the survey monkey survey.. 

## Title: VIP Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `VIP`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's VIP status.. Value must be `gmonkey`.
### Segment Operator
 `op` a string. Whether the member is or is not marked as VIP.. Possible values: (`%s`, `%s`).

## Title: Interests Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `Interests`.
### Segment Field
 `field` a string. Segmenting based on interest group information. This should start with 'interests-' followed by the grouping id. Ex. 'interests-123'.. 
### Segment Operator
 `op` a string. Whether the member is a part of one, all, or none of the groups.. Possible values: (`%s`, `%s`, `%s`).
### Segment Value
 `value` a array. An array containing strings, each representing a group id.. 

## Title: Ecommerce Category Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommCategory`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have/have not purchased specific items or categories.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. A member who has purchased from a category/specific item that is/is not a specific name, where the category/item name contains/doesn't contain a specific phrase or string, or a category/item name that starts/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The ecommerce category/item information.. 

## Title: Ecommerce Number Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommNumber`.
### Segment Field
 `field` a string. Used for segmenting members have an average spent total, a total number of orders, total number of products purchased, or average number of products per order.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `op` a string. Members who have spent exactly, have not spent exactly, spent more, or spent less than the segment value.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. Members who have spent exactly, have not spent exactly, spent more, or spent less than this amount.. 

## Title: Ecommerce Purchased Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommPurchased`.
### Segment Field
 `field` a string. Used for segmenting members who have/have not purchased anything.. Value must be `ecomm_purchased`.
### Segment Operator
 `op` a string. Members who have have ('member') or have not ('notmember') purchased.. Possible values: (`%s`, `%s`).

## Title: Ecommerce Spent Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommSpent`.
### Segment Field
 `field` a string. Used for segmenting members who have spent a specific amount on a single order or over their lifetime.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. Members who have spent 'more' or 'less' than then specified value.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The total amount a member spent.. 

## Title: Ecommerce Purchased Store Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EcommStore`.
### Segment Field
 `field` a string. Used for segmenting members have purchased from a specific store.. Value must be `ecomm_store`.
### Segment Operator
 `op` a string. Members who have or have not purchased from a specific store.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The store id to segment against.. 

## Title: Goal Activity Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `GoalActivity`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's Goal activity.. Value must be `goal`.
### Segment Operator
 `op` a string. Whether the website URL is/not exactly, contains/doesn't contain, starts with/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The URL to check Goal activity against.. 

## Title: Goal Timestamp Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `GoalTimestamp`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's last interaction with a website.. Value must be `goal_last_visited`.
### Segment Operator
 `op` a string. Whether the website activity happened after, before, or at a given timestamp.. Possible values: (`%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The date to check Goal activity against.. 

## Title: Similar Subscribers Segment Member Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `FuzzySegment`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `fuzzy_segment`.
### Segment Operator
 `op` a string. Members who are/are not apart of a 'similar subscribers' segment.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the 'similar subscribers' segment.. 

## Title: Static Segment Member Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `StaticSegment`.
### Segment Field
 `field` a string. Used for segmenting by Mandrill activity.. Value must be `static_segment`.
### Segment Operator
 `op` a string. Members who are/are not apart of a static segment.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a number. The id for the static segment.. 

## Title: Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoCountryState`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific country or US state.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Data
 `value` a string. The two-letter country code or US state abbreviation.. 

## Title: Geolocation Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoIn`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific geographic region.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The radius of the target location.. 
### Segment Location Address
 `addr` a string. The address of the target location.. 
### Segment Location Latitude
 `lat` a string. The latitude of the target location.. 
### Segment Location Longitude
 `lng` a string. The longitude of the target location.. 

## Title: US Zip Code Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoInZip`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are within a specific US zip code.. Value must be `ipgeoinzip`.
### Segment Data
 `value` a integer. The radius of the target location.. 
### Extra Data
 `extra` a integer. The zip code to segment against.. 

## Title: Unknown Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoUnknown`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members for which locaiton information is unknown.. Value must be `ipgeounknown`.

## Title: Zip Code Location-Based Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `IPGeoZip`.
### Segment Field
 `field` a string. Segmenting subscribers who are within a specific location.. Value must be `ipgeo`.
### Segment Operator
 `op` a string. Segment members who are/are not within a specific US zip code.. Possible values: (`%s`, `%s`).
### Segment Data
 `value` a integer. The 5-digit zip code.. 

## Title: Social Profiles Age Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialAge`.
### Segment Field
 `field` a string. Used for segmenting members based age ranges in Social Profiles data.. Value must be `social_age`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The age range to segment.. Possible values: (`%s`, `%s`, `%s`, `%s`).

## Title: Social Profiles Gender Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialGender`.
### Segment Field
 `field` a string. Used for segmenting members based on listed gender in Social Profiles data.. Value must be `social_gender`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The Social Profiles gender to segment.. Possible values: (`%s`, `%s`).

## Title: Social Profiles Influence Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialInfluence`.
### Segment Field
 `field` a string. Used for segmenting members based on influence rating in Social Profiles data.. Value must be `social_influence`.
### Segment Operator
 `op` a string. Members who have a rating that is/not or greater/less than the rating provided.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Operator
 `value` a number. The Social Profiles influence rating to segment.. 

## Title: Social Profiles Social Network Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialNetworkMember`.
### Segment Field
 `field` a string. Used for segmenting members based on social network in Social Profiles data.. Value must be `social_network`.
### Segment Operator
 `op` a string. Members who are/not on a given social network.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The social network to segment against.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).

## Title: Social Profiles Social Network Follow Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SocialNetworkFollow`.
### Segment Field
 `field` a string. Used for segmenting members based on social network in Social Profiles data.. Value must be `social_network`.
### Segment Operator
 `op` a string. Members who are/not following a linked account on a given social network.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The social network to segment against.. Value must be `twitter_follow`.

## Title: Address Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `AddressMerge`.
### Segment Field
 `field` a string. An address-type merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's address merge field contains/does not contain a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text merge field with.. 

## Title: Address/Zip Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `ZipMerge`.
### Segment Field
 `field` a string. An address or zip-type merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's address merge field is within a given distance from a city or zip.. Value must be `geoin`.
### Segment Value
 `value` a string. The distance from the city/zip.. 
### Segment Extra
 `extra` a string. The city or the zip being used to segment against.. 

## Title: Birthday Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `BirthdayMerge`.
### Segment Field
 `field` a string. A date merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's birthday merge information is/is not a certain date or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. A date to segment against (mm/dd).. 

## Title: Date Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `DateMerge`.
### Segment Field
 `field` a string. A date merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not, is greater/less than a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. A date to segment against.. 

## Title: Dropdown/Radio Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `SelectMerge`.
### Segment Field
 `field` a string. A merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not a value or is/is not blank.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text merge field with.. 

## Title: Text or Number Merge Field Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `TextMerge`.
### Segment Field
 `field` a string. A text or number merge field to segment.. 
### Segment Operator
 `op` a string. Whether the member's merge information is/is not, contains/does not contain, starts/ends with, or is greater/less than a value. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to segment a text or number merge field with.. 

## Title: Email Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `EmailAddress`.
### Segment Field
 `field` a string. Segmenting based off of a subscriber's email address.. Possible values: (`%s`, `%s`).
### Segment Operator
 `op` a string. Whether the email address is/not exactly, contains/doesn't contain, starts/ends with a string.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`, `%s`).
### Segment Value
 `value` a string. The value to compare the email against.. 

## Title: Predicted Gender Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `PredictedGender`.
### Segment Field
 `field` a string. Used for segmenting members based on predicted gender.. Value must be `predicted_gender`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Possible values: (`%s`, `%s`).
### Segment Operator
 `value` a string. The predicted gender to segment.. Possible values: (`%s`, `%s`).

## Title: Predicted Age Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `PredictedAge`.
### Segment Field
 `field` a string. Used for segmenting members based on predicted age. Value must be `predicted_age_range`.
### Segment Operator
 `op` a string. Members who are/not the exact criteria listed.. Value must be `is`.
### Segment Operator
 `value` a string. The predicted age to segment.. Possible values: (`%s`, `%s`, `%s`, `%s`, `%s`, `%s`).

## Title: New Subscribers Prebuilt Segment
## Description: An individual segment condition
### condition_type
 `condition_type` a string. Value must be `NewSubscribers`.
### Segment Field
 `field` a string. Used for segmenting subscribers who have subscribed within a given time frame.. Value must be `timestamp_opt`.
### Segment Operator
 `op` a string. Whe the event took place, namely within a time frame.. Value must be `date_within`.
### Segment Data
 `value` a string. What type of data to segment on: a specific date, a specific campaign, or the last campaign sent.. 

