import os

API_ID    = os.environ.get("API_ID", "28817205")
API_HASH  = os.environ.get("API_HASH", "f319d02866bf7b83e4de31002f6ba8a3")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7737490454:AAE5VVCe8R6xnvy6yFPp320i1JH_dZSDOqk") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set
