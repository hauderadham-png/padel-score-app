import streamlit as st
import pandas as pd
import time
import datetime

# 1. El link mte3ek mrigel
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSZw9lGlEStl8TfH3yhLPyTjK_fBWKEa4wG0gLfONdas2PEEqtn36isJwCHggLWR6lO4jh97kMUNunP/pub?output=csv"

st.set_page_config(page_title="Padel Live Score", layout="wide")

# --- STYLE CSS (Professional TV Look) ---
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
        box-shadow: 0px 0px 30px rgba(0, 255, 0, 0.2);
    }
    .team-text { color: white; font-size: 75px; font-weight: bold; margin-bottom: 20px; }
    .score-text { color: #00FF00; font-size: 180px; font-weight: bold; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

def load_data():
    # El trick hedhi t'forsa el update dima
    return pd.read_csv(f"{sheet_url}&v={datetime.datetime.now().timestamp()}")

try:
    df = load_data()
    
    # N'tol3ou el matches lkoll (ken t'7eb terrain we7ed barka n'najmou n'زيدو filter)
    for _, row in df.iterrows():
        st.markdown(f"""
            <div class="match-container">
                <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
            </div>
        """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"Fama mochkla f'el Sheet: {e}")

# 2. Auto-refresh kol 5 thwani
time.sleep(5)
st.rerun()
