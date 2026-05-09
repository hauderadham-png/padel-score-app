import streamlit as st
import pandas as pd
import time

# Config el page bech el score yetla3 kbir
st.set_page_config(page_title="Padel Score Live", layout="wide")

# El link el s7i7 mta3 el CSV
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSZw9lGlEStl8TfH3yhLPyTjK_fBWKEa4wG0gLfONdas2PEEqtn36isJwCHggLWR6lO4jh97kMUNunP/pub?output=csv"

# Style CSS bech tatla3 mrigla fil TV
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .match-container {
        background-color: #1f2937;
        padding: 60px;
        border-radius: 40px;
        border: 6px solid #00FF00;
        text-align: center;
        margin-top: 50px;
    }
    .team-text { color: white; font-size: 80px; font-weight: bold; }
    .score-text { color: #00FF00; font-size: 200px; font-weight: bold; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

def load_data():
    # Cache buster bech Google ma i'khabich el score el kdim
    return pd.read_csv(f"{sheet_url}&t={time.time()}")

try:
    df = load_data()
    # N'warriw kan el match mta3 Terrain T1 (kima fil Sheet row 2)
    match = df[df['Terrain'] == 'T1'].iloc[0]
    
    st.markdown(f"""
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
