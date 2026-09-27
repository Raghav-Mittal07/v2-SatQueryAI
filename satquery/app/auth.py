import os

from dotenv import load_dotenv
from supabase import create_client


load_dotenv()


def get_supabase():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    try:
        import streamlit as st

        if not url:
            url = st.secrets.get("SUPABASE_URL")

        if not key:
            key = st.secrets.get("SUPABASE_KEY")
    except Exception:
        pass

    if not url or not key:
        raise ValueError("Supabase credentials are not configured.")

    return create_client(url, key)


def send_otp(email):
    supabase = get_supabase()

    return supabase.auth.sign_in_with_otp({
        "email": email,
        "options": {
            "should_create_user": True
        }
    })


def verify_otp(email, otp):
    supabase = get_supabase()

    return supabase.auth.verify_otp({
        "email": email,
        "token": otp,
        "type": "email"
    })


def logout():
    supabase = get_supabase()
    supabase.auth.sign_out()
