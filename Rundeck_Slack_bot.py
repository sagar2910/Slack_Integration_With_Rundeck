import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import requests
import json
from requests.auth import HTTPBasicAuth

#env_path = Path('.') / '.env'
#print(env_path)
#load_dotenv(dotenv_path=env_path)

SLACK_TOKEN='xoxb-5073600687504-5090105227682-dgsjOx8bsExdn7RUMuZjCK1v'
SIGNING_SECRET='c8a3410ceb8f32b13463477738b8c549'

headers={'X-Rundeck-Auth-Token' : 'kJUIAvtWht594S56HxsHTk7W0JjUREsi'}

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET,'/slack/events',app)

client = slack.WebClient(token=SLACK_TOKEN)
'''BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        client.chat_postMessage(channel='#execute_job', text=text)'''

@app.route('/Run-Rundeck-Job', methods=['POST'])
def run_rndk_job():
    data = request.form
    user_id = data.get('user_id') 
    channel_id = data.get('channel_id')

    url_post = "http://localhost:4440/api/11/job/1ea9039b-5f0c-4644-a5b6-b983f50b298d/run?kJUIAvtWht594S56HxsHTk7W0JjUREsi"

    post_response = requests.post(url_post,
                              headers= headers
                            )
    
    client.chat_postMessage(channel=channel_id, text="Job Executed") 
    
    return Response(), 200

if __name__ == "__main__":
    app.run(debug=True)