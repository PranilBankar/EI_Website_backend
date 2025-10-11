import os
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client, Client

# Ensure dotenv loads from project root
dotenv_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path)
# from website.supabase_client import SUPABASE_URL, SUPABASE_KEY
# print("SUPABASE_URL:", SUPABASE_URL)
# print("SUPABASE_KEY:", SUPABASE_KEY)
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

# Debug print
print("SUPABASE_URL:", SUPABASE_URL)
print("SUPABASE_KEY:", SUPABASE_KEY)

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Supabase URL or Key not found! Check your .env file.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
