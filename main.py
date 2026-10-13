import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key is None:
    print("APIキーを読み込めません")
else:
    if api_key.startswith("sk-ant-"):
        print("APIキーを読み込めました")
    else:
        print("APIキーの形式が正しくありません")
