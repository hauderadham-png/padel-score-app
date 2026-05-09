import streamlit as st
import pandas as pd
import time

# Config el page
st.set_page_config(page_title="Padel Live Score", layout="wide")

# El link CSV elli l9ineh fi tsawrek el 9dom
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSZw9lGlEStl8TfH3yhLPyTjK_fBWKEa4wG0gLfONdas2PEEqtn36isJwCHggLWR6lO4jh97kMUNunP/pub?output=csv"

# Style CSS 
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .match-container {
        background-color: #1f2937;
        padding: 50px;
        border-radius: 30px;
        border: 5px solid #00FF00;
        text-align: center;
        margin-top: 40px;
    }
    .team-text { color: white; font-size: 65px; font-weight: bold; }
    .score-text { color: #00FF00; font-size: 160px; font-weight: bold; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

def load_data():
    # Zidna timestamp bech maadech yarja3 score 9dim
    return pd.read_csv(f"{sheet_url}&cache={time.time()}")

try:
    df = load_data()
    for index, row in df.iterrows():
        st.markdown(f"""
            <div class="match-container">
                <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
            </div>
        """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Fama mochkla: {e}")

# Refresh kol 5 thwani
time.sleep(10)
st.rerun()
