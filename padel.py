import streamlit as st
import pandas as pd
import time
import datetime

# El link mte3ek
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSZw9lGlEStl8TfH3yhLPyTjK_fBWKEa4wG0gLfONdas2PEEqtn36isJwCHggLWR6lO4jh97kMUNunP/pub?output=csv"

st.set_page_config(page_title="Padel Live Score", layout="wide")

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

# Function bech dima tjib el jdid
def load_data():
    # N'zidou ra9em 3achwa'i fil ekher mta3 el link bech Google ma ya3tinach version m'khazna (cached)
    timestamp = int(time.time())
    final_url = f"{sheet_url}&cachebuster={timestamp}"
    return pd.read_csv(final_url)

try:
    df = load_data()
    for _, row in df.iterrows():
        st.markdown(f"""
            <div class="match-container">
                <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
            </div>
        """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Erreur: {e}")

# Refresh kol 3 thwani (fissa3 fissa3)
time.sleep(3)
st.rerun()    for _, row in df.iterrows():
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
