import tkinter as tk
import time # 待機時間をシミュレートするため

def send_message():
    # 入力欄からテキストを取得
    user_text = entry.get()
    if not user_text:
        return

    send_btn.config(text="問い合わせ中..." )

    # 画面に自分の発言を表示
    chat_box.insert(tk.END, "You: " + user_text + "\n")
    entry.delete(0, tk.END)
    chat_box.see(tk.END) # 自動で一番下までスクロール

    # UIの変更を即座に画面に反映させる
    root.update()

    # AIからの回答待ちをシミュレート（後でAPI通信の処理が入ります）
    time.sleep(1) # 1秒待機

    # AIの返事を表示
    chat_box.insert(tk.END, "AI: 準備中です...\n\n")
    chat_box.see(tk.END)

    send_btn.config(text="送信" )

# ウィンドウの作成
root = tk.Tk()
root.title("Mini Chappy!")
root.resizable(False, False) # ウィンドウのサイズ変更を無効化（固定）

# チャットの履歴を表示するテキストエリア
chat_box = tk.Text(root, width=50, height=15 )
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 入力欄とボタンを横に並べるためのフレーム
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.X)

# メッセージを入力する入力欄
entry = tk.Entry(frame )
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

# 送信ボタン
send_btn = tk.Button(frame, text="送信", command=send_message, width=12 )
send_btn.pack(side=tk.RIGHT)

# アプリを起動したままにする
root.mainloop()