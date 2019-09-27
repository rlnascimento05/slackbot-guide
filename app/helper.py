import os
from slackclient import SlackClient

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def sendMessage(message, channel):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=message
    )
