from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key.startswith("sk-ant-usr"):
  print("True")
else:
  print("False")