import streamlit as st
import pandas as pd
import time

# 1. Configuration
st.set_page_config(page_title="Padel Live Score", layout="wide")

# 2. El link mte3ek (CSV)
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSZw9lGlEStl8TfH3yhLPyTjK_fBWKEa4wG0gLfONdas2PEEqtn36isJwCHggLWR6lO4jh97kMUNunP/pub?output=csv"

# 3. CSS Style
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
    # Cache buster bech dima y'jiblek a7deth score
    return pd.read_csv(f"{sheet_url}&t={time.time()}")

# 4. Display Match
try:
    df = load_data()
    if not df.empty:
        # N'warriw el match el awel (Tarek vs anissa)
        row = df.iloc[0]
        st.markdown(f"""
            <div class="match-container">
                <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
            </div>
        """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Erreur: {e}")

# 5. Refresh (Lezem ikoun fi star wa7dou f'ekher el koud)
time.sleep(3)
st.rerun()
row = df.iloc[0]
        st.markdown(f"""
            <div class="match-container">
                <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
            </div>
        """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Erreur: {e}")

# 5. Refresh (Lezem koun fi star wa7dou f'ekher el koud)
time.sleep(3)
st.rerun()    st.markdown(f"""
        <div class="match-container">
            <div class="team-text">{match['Team 1']} vs {match['Team 2']}</div>
            <div class="score-text">{match['Score 1']} - {match['Score 2']}</div>
        </div>
    """, unsafe_allow_html=True)
except Exception as e:
    st.error("Yasta3na chwaya Google Sheet ya3mel update...")

# Refresh kol 3 thwani
time.sleep(3)
st.rerun()                <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
            </div>
        """, unsafe_allow_html=True)
except Exception as e:
    st.error(f"Fama mochkla: {e}")

# Refresh kol 5 thwani
time.sleep(10)
st.rerun()
