import streamlit as st
import pandas as pd
import time
import datetime

# 1. El link mte3ek mrigel
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSZw9lGlEStl8TfH3yhLPyTjK_fBWKEa4wG0gLfONdas2PEEqtn36isJwCHggLWR6lO4jh97kMUNunP/pub?output=csv"

st.set_page_config(page_title="Padel Live Score", layout="wide")

# --- STYLE CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .match-container {
        background-color: #1f2937;
        padding: 60px;
        border-radius: 35px;
        border: 5px solid #00FF00;
        text-align: center;
        margin-top: 50px;
    }
    .team-text { color: white; font-size: 75px; font-weight: bold; }
    .score-text { color: #00FF00; font-size: 180px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

def load_data():
    # Cache buster bech dima y'jib el jdid
    timestamp = int(time.time())
    final_url = f"{sheet_url}&cachebuster={timestamp}"
    return pd.read_csv(final_url)

# --- EL LOGIC ---
try:
    df = load_data()
    # Thabbet houni: kol match fi row
    for index, row in df.iterrows():
        st.markdown(f"""
            <div class="match-container">
                <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
            </div>
        """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Fama mochkla fil Google Sheet: {e}")

# Refresh kol 5 thwani
time.sleep(5)
st.rerun()
