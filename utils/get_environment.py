from pathlib import Path
import os

from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parent.parent / '.env'

load_dotenv(ENV_PATH)

BOT_TOKEN = os.getenv('BOT_TOKEN')
