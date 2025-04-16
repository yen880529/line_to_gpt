
# LINE GPT Bot on Render

這是一個使用 Flask 建立的 LINE + OpenAI GPT 串接範例，可以部署到 Render。

## 使用方式

1. 把此專案 push 到 GitHub
2. Render 建立 Web Service 並填入環境變數：
   - `LINE_CHANNEL_ACCESS_TOKEN`
   - `OPENAI_API_KEY`
3. LINE Webhook 設定為：`https://你的服務網址/webhook`

## 測試

傳送訊息給你的 LINE Bot，會收到 GPT 回覆。
