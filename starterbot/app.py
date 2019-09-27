import sys
import os
import time
import logging
sys.path.append("app")
from slackclient import SlackClient
from app.fundosbot import FundosBot as mybot

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
logging.basicConfig()
# instantiate Slack client
starterbot_id = None
# starterbot's user ID in Slack: value is assigned after the bot starts up
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == "__main__":
  if slack_client.rtm_connect(with_team_state=False):
    print("Starter Bot connected and running!")
    print("Novidade")
    # Read bot's user ID by calling Web API method `auth.test`
    starterbot_id = slack_client.api_call("auth.test")["user_id"]

    bot = mybot(starterbot_id)
    while True:
      command, channel = bot.parse_bot_commands(slack_client.rtm_read())
      if command:
        print command
        print channel
        bot.handle_command(command, channel)
        time.sleep(RTM_READ_DELAY)
  else:
    print("Connection failed. Exception traceback printed above.")