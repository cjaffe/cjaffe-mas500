#######################################
# Caroline Jaffe
# MAS.500, Fall 2016
# hw2.py
#	MediaCloud class to instantiate
# 	media cloud object and provide 
#	useful functions for a query
#######################################

import logging, mediacloud, ConfigParser, datetime

# Configure logging module
logging.basicConfig(filename='hw2.log', level=logging.DEBUG)

class MediaCloud:

	def __init__(self):
		#Read in config values, create query dates
		Config = ConfigParser.ConfigParser()
		Config.read("settings.ini")
		self.api_key = Config.get("MainSettings", "api-key")

		# Read dates from config file, format them and create datetime objects
		d1 = map(int, Config.get("QuerySettings", "date1").split('-'))
		d2 = map(int, Config.get("QuerySettings", "date2").split('-'))
		self.date1 = datetime.date(d1[0], d1[1], d1[2])
		self.date2 = datetime.date(d2[0], d2[1], d2[2])

		self.media_tag = Config.get("QuerySettings", "sources")
		self.mc = mediacloud.api.MediaCloud(self.api_key)


	def getSentenceCount(self, topic):
		logging.info('Entering getSentenceCount function')
		logging.debug('Topic argument: ' + topic)
		logging.debug('Date arguments: ' + str(self.date1) + ', ' + str(self.date2))
		return self.mc.sentenceCount(topic, solr_filter=[self.mc.publish_date_query( self.date1, self.date2 ), self.media_tag ])['count']