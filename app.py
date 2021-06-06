from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('5YimAwxbmAaUYm4ZW5zlub3EZ0UokoagkSULauDj8hI3jvs3VPgDerXlgZ42ClYCW6N8M6S7fUzrJ0F4kwodjxV5REcrzSpJ43SDGxCl1QgNijQL5b9iIil9jC9/zYhJSvOJFAREDFz7sZ7jw8DviwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('17d4b0169979546c1dd6131833fe003b')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "很抱歉你在問甚麼?"

    if msg == 'hi':
        r == 'hi'
    elif msg == '吃飽沒':
        r == '還沒'
        
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()