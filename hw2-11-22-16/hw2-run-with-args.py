#######################################
# Caroline Jaffe
# MAS.500, Fall 2016
# hw2-run-with-args.py
#	Run Media Cloud queries with 
#	command line inputs.
#######################################

#######################################
################ SETUP ################
#######################################

from hw2 import MediaCloud
import logging, sys, warnings

# Configure logging module
logging.basicConfig(filename='hw2.log', level=logging.DEBUG)


mc = MediaCloud()
logging.debug('MediaCloud object: ' + str(mc))

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

#######################################
############ MAIN PROGRAM #############
#######################################

#Did media talk about topic1 or topic2 in our given date range (set in config file)?
#plan: get values for each using "sentencecount" API call, then compare those values, and print out answer
with warnings.catch_warnings(): #Set this up to ignore specific MediaCloud warning
	warnings.simplefilter("ignore")
	topic1_count = mc.getSentenceCount(topic1)
	topic2_count = mc.getSentenceCount(topic2)

#Playing around with ternary operator here: a if condition else b

print "In September 2016, the media wrote more stories about: " + (topic1 if topic1_count > topic2_count else topic2)

print "There were " + str(topic1_count) + " stories written about " + topic1 + " and " + str(topic2_count) + " stories written about " + topic2 +"."
