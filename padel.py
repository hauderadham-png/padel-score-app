import streamlit as st
import pandas as pd
import time

# 1. Configuration el Page
st.set_page_config(page_title="Padel Score Live", layout="wide")

# 2. El link mte3ek (CSV)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSZw9lGlEStl8TfH3yhLPyTjK_fBWKEa4wG0gLfONdas2PEEqtn36isJwCHggLWR6lO4jh97kMUNunP/pub?output=csv"

# 3. Style CSS (Nadhamna el Score kbir lel TV)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .match-container {
        background-color: #1f2937;
        padding: 30px;
        border-radius: 20px;
        border-left: 10px solid #00FF00;
        text-align: center;
        margin-bottom: 25px;
    }
    .terrain-label { color: #00FF00; font-size: 30px; font-weight: bold; }
    .team-text { color: white; font-size: 50px; font-weight: bold; }
    .score-text { color: #00FF00; font-size: 110px; font-weight: bold; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

def load_data():
    # Force Google update b'el timestamp
    return pd.read_csv(f"{sheet_url}&t={time.time()}")

# 4. Display
try:
    df = load_data()
    if not df.empty:
        # Houni l'app t'lawej 3al matches el kol w t'fara9hom
        for index, row in df.iterrows():
            st.markdown(f"""
                <div class="match-container">
                    <div class="terrain-label">Terrain: {row['Terrain']}</div>
                    <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                    <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
                </div>
            """, unsafe_allow_html=True)
except Exception as e:
    st.error("Google Sheet ba9i ya3mel fi update...")

# 5. Refresh kol 5 thwani (F'star wa7dou bech maadech ya3mel SyntaxError)
time.sleep(5)
st.rerun()
