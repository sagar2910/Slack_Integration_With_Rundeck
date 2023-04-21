import os
from venv import logger
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import logging
from slackeventsapi import SlackEventAdapter
import requests

logging.basicConfig(level=logging.DEBUG) 
# Import Needed to access env variables.
'''from dotenv import load_dotenv
from pathlib import Path
import slack
import os'''

#To Access Env varibales.
'''env_path = Path('.') / '.env'    
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])'''

SLACK_BOT_TOKEN='xoxb-5073600687504-5109738241266-2IM1unSzs5YPIMqRdcOJgwwN'
SIGNING_SECRET='134740eb8083ec4453b9a1d6f45550ce'
SLACK_APP_TOKEN='xapp-1-A05313PSJBY-5109811506034-bed8a0fe7aa18e5e649936ee660f2861d317b1f228f7d081b965d40aef76fe6a'

Callback_ID = 'Run_Rundeck_Modal'

# Install the Slack app
app = App(token=SLACK_BOT_TOKEN)

@app.shortcut("Run_Rundeck_Modal")
def Run_Rundeck_Modal(ack,client,shortcut,logger):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client

    # Call views_open with the built-in client
    result=client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=shortcut["trigger_id"],
        # View payload
    	view={
        "callback_id" : "View_1",
	"title": {
		"type": "plain_text",
		"text": "Rundeck Job Details"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"blocks": [
		{
			"type": "input",
            "block_id": "Server_IP",
			"element": {
				"type": "plain_text_input",
				"action_id": "Input_Server",
				"placeholder": {
					"type": "plain_text",
					"text": "Server IP address"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Server Details"
			}
		},
		{
			"type": "input",
            "block_id": "Job_ID",
			"element": {
				"type": "plain_text_input",
				"action_id": "Input_JOBID",
				"placeholder": {
					"type": "plain_text",
					"text": "Job ID"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "JOB UUID"
			}
		},
		{
			"type": "input",
            "block_id": "Channel_ID",
			"element": {
				"type": "multi_channels_select",
				"action_id": "Input_Channel",
				"placeholder": {
					"type": "plain_text",
					"text": "Channel Name / Channel ID"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Channel"
			}
		},
	],
	"type": "modal"
    }    
)
    
@app.view("View_1")
def handle_modal(ack, body, client, view, logger):
    ack()
    server_details = view["state"]["values"]["Server_IP"]["Input_Server"]
    job_details = view["state"]["values"]["Job_ID"]["Input_JOBID"]
    channel_details = view["state"]["values"]["Channel_ID"]["Input_Channel"]
    try:
        print("Server URL : ",server_details['value'])
        print("JOB UUID : ",job_details['value'])
        print("Channel ID : ",channel_details['selected_channels'])
        user = body["user"]["id"]
        client.chat_postMessage(channel=(channel_details['selected_channels'][0]), text="Information Received as below : ")
        client.chat_postMessage(channel=(channel_details['selected_channels'][0]), text=f"Server URL : {server_details['value']}")
        client.chat_postMessage(channel=(channel_details['selected_channels'][0]), text=f"Job ID : {job_details['value']}")
        client.chat_postMessage(channel=(channel_details['selected_channels'][0]), text="Job Initialization is in progress!! Please wait unti I fetch the job Result!")
        
    except Exception as e:
        print("There is a error with your submission!")
                
        
if __name__ == "__main__":
    handler = SocketModeHandler(app,SLACK_APP_TOKEN)
    handler.start()


