
from flask import Flask, request
import openai
import requests
import os

app = Flask(__name__)

# 使用 Render 設定的環境變數
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LINE_REPLY_ENDPOINT = "https://api.line.me/v2/bot/message/reply"

openai.api_key = OPENAI_API_KEY

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.json
    events = body.get("events", [])

    for event in events:
        if event["type"] == "message" and event["message"]["type"] == "text":
            user_message = event["message"]["text"]
            reply_token = event["replyToken"]
            gpt_reply = ask_gpt(user_message)

            headers = {
                "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
                "Content-Type": "application/json"
            }
            data = {
                "replyToken": reply_token,
                "messages": [{"type": "text", "text": gpt_reply}]
            }
            requests.post(LINE_REPLY_ENDPOINT, headers=headers, json=data)
    return "OK"

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是技術客服，請根據公司知識回應使用者問題。"},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

@app.route("/")
def home():
    return "LINE GPT Bot 正常運作中！"
