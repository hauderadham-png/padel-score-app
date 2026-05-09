import streamlit as st
import pandas as pd
import time

sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSZw9lGlEStl8TfH3yhLPyTjK_fBWKEa4wG0gLfONdas2PEEqtn36isJwCHggLWR6lO4jh97kMUNunP/pub?output=csv"

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .match-container {
        background-color: #1f2937;
        padding: 50px;
        border-radius: 30px;
        border: 4px solid #00FF00;
        text-align: center;
        margin-bottom: 30px;
    }
    .team-text { color: white; font-size: 60px; font-weight: bold; }
    .score-text { color: #00FF00; font-size: 150px; font-weight: bold; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

def load_data():
    return pd.read_csv(f"{sheet_url}&cache={time.time()}")

try:
    df = load_data()
    # N'warriw el matches lkoll elli fil Sheet
    for _, row in df.iterrows():
        st.markdown(f"""
            <div class="match-container">
                <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
            </div>
        """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Thabbet fil Google Sheet: {e}")

time.sleep(5)
st.rerun()
