import streamlit as st
import pandas as pd
import time

# 1. El lien mte3ek mrigel houni
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSZw9lGlEStl8TfH3yhLPyTjK_fBWKEa4wG0gLfONdas2PEEqtn36isJwCHggLWR6lO4jh97kMUNunP/pub?output=csv"

st.set_page_config(page_title="Padel Live Score", layout="wide")

# --- STYLE CSS (Bech yabda Pro fil TV) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .main-title { color: #00FF00; text-align: center; font-size: 60px; font-weight: bold; margin-bottom: 30px; }
    .match-container {
        background-color: #1f2937;
        padding: 40px;
        border-radius: 25px;
        border: 3px solid #00FF00;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 0px 20px rgba(0, 255, 0, 0.2);
    }
    .team-text { color: white; font-size: 45px; font-weight: bold; }
    .score-text { color: #00FF00; font-size: 110px; font-family: 'Courier New', Courier, monospace; font-weight: bold; }
    .terrain-label { color: #aaaaaa; font-size: 25px; text-transform: uppercase; letter-spacing: 2px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">LIVE PADEL SCOREBOARD 🎾</div>', unsafe_allow_html=True)

def load_data():
    # El trick hedhi tkhalli l'app dima tjib jdid mel Google Sheet
    return pd.read_csv(f"{sheet_url}&cache_buster={time.time()}")

# 2. Ekhtar el Mode (TV Terrain 1 walla 2)
mode = st.sidebar.radio("Chnwa t7eb t'7el?", ["Admin", "TV Terrain 1", "TV Terrain 2"])

try:
    df = load_data()
    
    if mode == "Admin":
        st.subheader("Admin View")
        st.write("Matchs en direct mel Google Sheet:")
        st.dataframe(df)
        st.info("Badel el scores mel app Google Sheets f'tlfounik, el TV taamel update wa7d'ha!")

    else:
        # Nekhdou el Terrain ID (T1 walla T2) mel klem elli ekhtartou
        tr_id = "T1" if "1" in mode else "T2"
        
        # Filtre el matches mta3 el terrain hedha barka
        # NOTE: Lezem 3andek column esmou 'Terrain' fil Google Sheet fih T1 walla T2
        match_data = df[df['Terrain'] == tr_id]
        
        if not match_data.empty:
            for _, row in match_data.iterrows():
                st.markdown(f"""
                    <div class="match-container">
                        <div class="terrain-label">Terrain {tr_id}</div>
                        <div class="team-text">{row['Team 1']} vs {row['Team 2']}</div>
                        <div class="score-text">{row['Score 1']} - {row['Score 2']}</div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning(f"Mafama 7atta match tawa fil Terrain {tr_id}")

except Exception as e:
    st.error(f"Fama mochkla f'el data: {e}")

# 3. Auto-refresh kol 5 thwani
time.sleep(5)
st.rerun()
