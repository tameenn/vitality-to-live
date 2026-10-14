import os
import sys
from dotenv import load_dotenv
import anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key is None:
    print("APIキーを読み込めません")
    sys.exit(1)
else:
    if api_key.startswith("sk-ant-"):
        print("APIキーを読み込めました")
    else:
        print("APIキーの形式が正しくありません")
        sys.exit(1)

client = anthropic.Anthropic()

log = []

while True:
    message = input("メッセージを入力:")
    message = message.strip()

    if message == "exit":
        break
    elif message == "":
        print("入力してください")
    else:
        log.append({"role": "user", "content": message})
        response = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=16000,
            messages=log
        )

        answer = ""

        for block in response.content:
            if block.type == "text":
                answer += block.text

        print(answer)

        log.append({"role": "assistant", "content": answer})
