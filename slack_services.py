import os
from slack_sdk import WebClient

# Slack Bot Token yahan dalein (xoxb-...)
SLACK_BOT_TOKEN = "xoxb-your-slack-bot-token"
client = WebClient(token=SLACK_BOT_TOKEN)

def handle_mentions(channel_id, text_to_send):
    # Yahan 'username' badalne se Slack par bot ka naam badal jayega
    # Yaad rahe: Slack App settings mein 'chat:write.customize' permission zaroori hai
    client.chat_postMessage(
        channel=channel_id,
        text=text_to_send,
        username="Jarvis AI",           # <-- Yahan jo naam likhenge wo dikhega
        icon_emoji=":robot_face:"        # <-- Bot ka avatar icon
    )