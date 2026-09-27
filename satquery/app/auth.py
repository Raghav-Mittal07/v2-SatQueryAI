import os

from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase credentials are not configured.")


supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def send_otp(email):
    return supabase.auth.sign_in_with_otp({
        "email": email,
        "options": {
            "should_create_user": True
        }
    })


def verify_otp(email, otp):
    return supabase.auth.verify_otp({
        "email": email,
        "token": otp,
        "type": "email"
    })


def logout():
    supabase.auth.sign_out()
