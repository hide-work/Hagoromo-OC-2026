import os
import ai_tools
from openai import OpenAI

# AIを利用するための「窓口」を用意
client = None

# 会話の履歴を記憶するリスト
msgs = []

def initialize():
    global client

    os.environ["NO_PROXY"] = "localhost, 127.0.0.1"

    # AIに接続するための準備
    client = OpenAI(
        base_url = "http://172.31.0.9/ollama/v1",
        api_key = "dummy"
    )

def message(user_text):
    global msgs

    # 1. ユーザーのメッセージを履歴に追加
    msgs.append({"role": "user", "content": user_text})

    # 2. AIに履歴を渡して返答をもらう
    api_response = client.chat.completions.create(
        model = "llama3.2:3b",
        messages = msgs
    )

    # 3. 応答データから「メッセージオブジェクト」を取り出す
    assistant_msg = api_response.choices[0].message
    
    # 4. メッセージオブジェクトから「テキスト部分」だけを取り出して履歴に追加
    reply_text = assistant_msg.content
    msgs.append({"role": "assistant", "content": reply_text})

    # 5. 画面にAIの返答を通知
    return str(reply_text)