SLACK_BOT_TOKEN='xoxb-5073600687504-5090105227682-dgsjOx8bsExdn7RUMuZjCK1v'
SIGNING_SECRET='c8a3410ceb8f32b13463477738b8c549'
SLACK_APP_TOKEN='xapp-1-A053BP16LC8-5093326479733-f85aeadbfffd0d48c3eb6b6c01e4d7d99a79963f467f7d1d95ed846f8b7971c2'

headers={'X-Rundeck-Auth-Token' : 'kJUIAvtWht594S56HxsHTk7W0JjUREsi'}

from slack_bolt import App
import os
from slack_bolt.adapter.socket_mode import SocketModeHandler
import http.client

app = App(token=SLACK_BOT_TOKEN,signing_secret=SIGNING_SECRET)

'''@app.command("/run-rundeck-job")
def run_rundk_job(ack,say,command):
    ack()
    say(f"{command['text']}")'''    

# Handle incoming slash commands
@app.command("/run-rundeck-job")
def handle_command(ack, respond, command):
    # Acknowledge command request
    ack()

if __name__ == "__main__":
    SocketModeHandler(app,SLACK_APP_TOKEN).start()