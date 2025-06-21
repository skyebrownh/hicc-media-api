from app.utils.supabase import SupabaseService 
from app.utils.env import SUPABASE_URL, SUPABASE_API_KEY

supabase = SupabaseService(url=SUPABASE_URL, key=SUPABASE_API_KEY)