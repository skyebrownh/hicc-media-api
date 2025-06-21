from app.utils.supabase import SupabaseService 
from app.utils.env import SUPABASE_URL, SUPABASE_API_KEY

def get_supabase_service():
    return SupabaseService(url=SUPABASE_URL, key=SUPABASE_API_KEY)