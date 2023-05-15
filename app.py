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

line_bot_api = LineBotApi('ZynaOeDIr3yRCNhQQx9pNL9fZrxSkYO+yg7+qeXsjoKrN9nre+5eegKubJQfoAhEm0J5C0/gZhRrZyjiDLZp2AG+Nuy4RjLIg1ihnvBokB2IakFUxDpppQeaabFm3qPUm7JRuLNqZeyXfH+PkuZvEwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3f04a7e82c0ff5e274e6f2bd39d3a883')


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
        r = 'hi'
    elif msg == '吃飽沒':
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
