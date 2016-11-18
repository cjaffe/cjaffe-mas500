#######################################
# Caroline Jaffe
# MAS.500, Fall 2016
# HW2.py
#	Run Media Cloud queries with 
#	command line inputs. Also includes
# 	logging and companion unit tests
#######################################

#######################################
################ SETUP ################
#######################################

#Set up environment and instantiating media cloud
import mediacloud, datetime, ConfigParser, warnings, logging, sys

# Get command line args
try:
	topic1 = sys.argv[1]
	topic2 = sys.argv[2]
except Exception as err: 
	logging.warn('Error with command line arguments: ' + str(err))
	sys.exit(0)

if (len(sys.argv) > 3):
	logging.warn('Too many command line arguments, please run again with only two topics')
	sys.exit(0)

# Configure logging module
logging.basicConfig(filename='hw2.log', level=logging.DEBUG)

#Read in config values, create query dates
Config = ConfigParser.ConfigParser()
Config.read("settings.ini")
api_key = Config.get("MainSettings", "api-key")

# Read dates from config file, format them and create datetime objects
d1 = map(int, Config.get("QuerySettings", "date1").split('-'))
d2 = map(int, Config.get("QuerySettings", "date2").split('-'))
date1 = datetime.date(d1[0], d1[1], d1[2])
date2 = datetime.date(d2[0], d2[1], d2[2])

media_tag = Config.get("QuerySettings", "sources")

mc = mediacloud.api.MediaCloud(api_key)
logging.debug('MediaCloud object: ' + str(mc))

#######################################
############ MAIN PROGRAM #############
#######################################

def getSentenceCount(topic, date1, date2):
	logging.info('Entering getSentenceCount function')
	logging.debug('Topic argument: ' + topic)
	logging.debug('Date arguments: ' + str(date1) + ', ' + str(date2))
	return mc.sentenceCount(topic, solr_filter=[mc.publish_date_query( date1, date2 ), media_tag ])['count']

#Did media talk about Clinton or Trump more in September 2016?
#plan: get values for each using "sentencecount" API call, then compare those values, and print out answer

with warnings.catch_warnings(): #Set this up to ignore specific MediaCloud warning
	warnings.simplefilter("ignore")
	topic1_count = getSentenceCount(topic1, date1, date2 )
	topic2_count = getSentenceCount(topic2, date1, date2 )

#Playing around with ternary operator here: a if condition else b

print "In September 2016, the media wrote more stories about: " + (topic1 if topic1_count > topic2_count else topic2)

print "There were " + str(topic1_count) + " stories written about " + topic1 + " and " + str(topic2_count) + " stories written about " + topic2 +"."