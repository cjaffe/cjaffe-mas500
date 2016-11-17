#Setting up environment and instantiating media cloud

import mediacloud, json, datetime, ConfigParser

#Read in config values
Config = ConfigParser.ConfigParser()
Config.read("settings.ini")
api_key = Config.get("MainSettings", "api-key")

mc = mediacloud.api.MediaCloud(api_key)

#Did media talk about Clinton or Trump more in September 2016?
#plan: get values for each using "sentencecount" API call, then compare those values, and print out answer

clinton = mc.sentenceCount('clinton', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
clinton = clinton['count']

trump = mc.sentenceCount('trump', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
trump = trump['count']

#Playing around with ternary operator here: a if condition else b

print "In September 2016, the media wrote more stories about: "
print "Clinton" if clinton > trump else "Trump"

print "In September, 2016, there were " + str(trump) + " stories written about Trump and " + str(clinton) + " stories written about Clinton."