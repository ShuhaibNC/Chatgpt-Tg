from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", 27788699))
API_HASH = getenv("API_HASH", "e2b420422f02f7cd461a509a1cbaa635")
BOT_TOKEN = getenv("BOT_TOKEN", "5910606904:AAG1nGoQ4qR-BilLxDXJZpfvwns7IkcYp0c")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
