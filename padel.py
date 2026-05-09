import streamlit as st
import pandas as pd
import time

# 1. Config el Page
st.set_page_config(page_title="Padel Live Score", layout="wide")

# 2. El link el s7i7 (Export mode bech maadech yabta)
sheet_id = "1SZw9lGlEStl8TfH3yhLPyTjK_fBWKEa4wG0gLfONdas2PEEqtn36isJwCHggLWR6lO4jh97kMUNunP"
sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

# 3. Style CSS
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

# 4. Function ta9ra el data
def load_data():
    t = int(time.time())
    return pd.read_csv(f"{sheet_url}&cachebuster={t}")

# 5. Affichage
try:
    df = load_data()
    if not df.empty:
        for index, row in df.iterrows():
            st.markdown(f"""
                <div class="match-container">
                    <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                    <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
                </div>
            """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Fama mochkla: {e}")

# 6. Refresh kol 3 thwani (MARRA WA7DA FI EKHER EL FICHIÉ)
time.sleep(3)
st.rerun()
