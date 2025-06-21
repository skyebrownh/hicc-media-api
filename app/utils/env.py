import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", verbose=True)

SUPABASE_URL = str(os.getenv("SUPABASE_URL"))
SUPABASE_API_KEY = str(os.getenv("SUPABASE_API_KEY"))

load_dotenv(dotenv_path="test.env", verbose=True)

SUPABASE_TEST_URL = str(os.getenv("SUPABASE_TEST_URL"))
SUPABASE_TEST_API_KEY = str(os.getenv("SUPABASE_TEST_API_KEY"))