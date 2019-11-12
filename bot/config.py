###################################################################
######## Configuration files for Bot   ##########################
###################################################################

"""
    config.py 
    
    This files has all the configurations for your bot.
    
"""

import os
import watson_developer_cloud
from slackclient import SlackClient

location = "/Users/Naveen/Desktop/bot/"  # replace with the full folder path where you downloaded the github repo

###################################################################
######## Slack configuration   ##########################
###################################################################

SLACK_BOT_TOKEN='xoxb-817786803634-818640478114-P99hEi1iaU51Aoyk8CtpNUjl'
SLACK_VERIFICATION_TOKEN='K6rpo8Ieb2z76igvwn6DN0rj' 

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) # do not change this parameter

###################################################################
######## Watson service configuration   ##########################
###################################################################

service = watson_developer_cloud.AssistantV1(
    iam_apikey = 'x_DJpehGvqomJ2qqwNQApEAAZ-Y9j2vQa0TixvAhfhGp', # replace with Password
    version = '2018-09-20'
)

workspace_id = '000aed90-1c49-4970-b187-bd382d7990ea' # replace with Assistant ID

#from ibm_watson import AssistantV2
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#authenticator = IAMAuthenticator('x_DJpehGvqomJ2qqwNQApEAAZ-Y9j2vQa0TixvAhfhGp')
#assistant = AssistantV2(
#	version = '2018-09-20',
#	authenticator = authenticator
#)

#assistant.set_service_url('https://gateway-wdc.watsonplatform.net/assistant/api')
#assistant.set_disable_ssl_verification(True)

###################################################################
######## Log files configuration   ##########################
###################################################################

log_commands_path = location + "logs/log_commands.py" # do not change this parameter
follow_up_path = location + "logs/followup_email.py" # do not change this parameter

###################################################################
######## Temp files configuration   ##########################
###################################################################

onetime_path = location + "nlp/nlp_solutions/onetime_run_file.py" # do not change this parameter
onetime_file = location + "nlp/nlp_solutions/onetime.txt" # do not change this parameter