# ai_tools.py
from datetime import datetime

# 実際の処理を行う関数
def get_current_time():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")

# AIに渡すツールの説明書
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current system date and time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        }
    }
]

# ツール呼び出しの「割り込み処理」をまとめた関数
def handle_tool_call(client, model, msgs, reply_msg):
    # もしAIから「ツールを使いたい」という要求（tool_calls）があれば処理する
    if reply_msg.tool_calls:
        # 要求を履歴に追加
        msgs.append(reply_msg)
        
        tool_call = reply_msg.tool_calls[0]
        
        # 実際のPython関数を実行して時間を取得
        current_time = get_current_time()
        
        # ツールの結果を履歴に追加
        msgs.append({
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": tool_call.function.name,
            "content": current_time,
        })
        
        # ツールの結果を踏まえて、もう一度AIに文章を作ってもらう
        res = client.chat.completions.create(
            model = model,
            messages = msgs
        )
        return res.choices[0].message # 新しいAIの返答を返す
        
    return reply_msg # ツール要求がなければ、そのまま最初の返答を返す