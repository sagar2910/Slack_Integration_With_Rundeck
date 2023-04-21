# Slack_Integration_With_Rundeck
Using Slack slash commands and Modal user can run a job on Rundeck Tool.

rundeck_request.py - To check status code of an end point.
rundeck_lib.py - to use pyrundeck ibluilt library to access rundeck URL.
.env - file to store app , bot and authentication token for api.
Rundeck_slack_bot.py - Working code to trigger job on rundeck using Flask.
Rundeck_bot_Bolt.py - Ignore this file.
modal.py - Working code of Modal , It takes user inputs and sends back to the slack channel.
