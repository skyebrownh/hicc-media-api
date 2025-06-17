import os

from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = str(os.getenv("SUPABASE_URL"))
SUPABASE_API_KEY = str(os.getenv("SUPABASE_API_KEY"))