        import speech_recognition as sr
        import requests
        import time

        # --- ここをあなたのPushbullet API情報に置き換えてください ---
        PUSHBULLET_API_KEY = "o.nKkKW3H3lSwX4xalCHKpUZF3kMKOoPNZ" # ← あなたのアクセストークンを貼り付ける
        # ----------------------------------------------------

        # Pushbullet APIの基本URL
        PUSHBULLET_PUSH_URL = "https://api.pushbullet.com/v2/pushes"

        # 関数: Pushbulletにノート（テキストメッセージ）を送信
        def send_pushbullet_note(api_key, title, body, device_iden=None):
            headers = {
                "Access-Token": api_key,
                "Content-Type": "application/json"
            }
            data = {
                "type": "note",
                "title": title,
                "body": body
            }
            if device_iden:
                data["device_iden"] = device_iden # 特定のデバイスに送る場合は指定

            try:
                response = requests.post(PUSHBULLET_PUSH_URL, headers=headers, json=data)
                response.raise_for_status()
                print(f"Pushbulletノートを送信しました。応答: {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"Pushbulletノートの送信中にエラーが発生しました: {e}")

        # 関数: 音声認識
        def recognize_speech():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("話してください...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)

            try:
                text = r.recognize_google(audio, language="ja-JP")
                print(f"認識されたテキスト: {text}")
                return text
            except sr.UnknownValueError:
                print("音声を認識できませんでした。もう一度お話しください。")
                return ""
            except sr.RequestError as e:
                print(f"Google Speech Recognition サービスにアクセスできませんでした; インターネット接続を確認してください: {e}")
                return ""

        if __name__ == "__main__":
            print("音声認識システムを開始します。")
            while True:
                recognized_text = recognize_speech()
                
                target_audio_file = None # 再生するファイル名を初期化

                # ここで「特定の言葉」を判定し、対応する録音ファイルを指定します
                # AndroidスマホのDownloadフォルダにあるファイルの正確なファイル名（拡張子含む）を指定
                if "悪魔モード" in recognized_text:
                    print("キーワード「悪魔モード」を検知しました！")
                    target_audio_file = "悪魔の声援.wav" # ← ファイル名を確認
                    
                elif "天使モード" in recognized_text:
                    print("キーワード「天使モード」を検知しました！")
                    target_audio_file = "天使の声援.wav" # ← ファイル名を確認

                elif "デスボ様、どうでございましたでしょうか" in recognized_text:
                    print("キーワード「デスボ様、どうでございましたでしょうか」を検記しました！")
                    target_audio_file = "終了ボイス 悪魔.wav" # ← ファイル名を確認

                elif "ルナボさん、どうでした" in recognized_text:
                    print("キーワード「ルナボさん、どうでした」を検知しました！")
                    target_audio_file = "終了ボイス 天使.wav" # ← ファイル名を確認

                elif "終了" in recognized_text: # 「終了」と話すとプログラムが停止
                    print("「終了」を検知しました。プログラムを停止します。")
                    break
                
                # どのキーワードにもマッチせず、かつ「終了」でもない場合
                if target_audio_file: # 再生するファイルが指定された場合のみPushbulletを送信
                    send_pushbullet_note(
                        PUSHBULLET_API_KEY,
                        title="Tasker Command", # Taskerの「タイトル」フィルターと一致させる
                        body=f"file:{target_audio_file}" # ← ここが変更点: "command:play_audio," を削除
                    )
                    time.sleep(5) # 連続トリガーを防ぐため
                
                time.sleep(1) # 次の認識までの短い待機