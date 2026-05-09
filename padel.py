import streamlit as st

# 1. El data mta3 el rounds mel image PHOTO-2026-05-08-23-13-48.jpg
rounds = {
    "Round 1": {"T1": ("Tarek - Adam", "Stéphane - Anissa"), "T2": ("Oussama - Ahmed", "Eric - Valérie")},
    "Round 2": {"T1": ("Achref - Samy", "Mouhamed Hedi - Ouassim"), "T2": ("Jihed - Alexis", "Marwene - Anis")},"Round 3": {"T1": ("Tarek - Adam", "Eric - Valérie"), "T2": ("Stéphane - Anissa", "Mouhamed Hedi - Ouassim")},
    "Round 4": {"T1": ("Oussama - Ahmed", "Marwene - Anis"), "T2": ("Achref - Samy", "Jihed - Alexis")},
    "Round 5": {"T1": ("Tarek - Adam", "Mouhamed Hedi - Ouassim"), "T2": ("Eric - Valérie", "Marwene - Anis")},
    "Round 6": {"T1": ("Stéphane - Anissa", "Jihed - Alexis"), "T2": ("Oussama - Ahmed", "Achref - Samy")},
    "Round 7": {"T1": ("Tarek - Adam", "Marwene - Anis"), "T2": ("Mouhamed Hedi - Ouassim", "Jihed - Alexis")},
    "Round 8": {"T1": ("Eric - Valérie", "Achref - Samy"), "T2": ("Stéphane - Anissa", "Oussama - Ahmed")},
    "Round 9": {"T1": ("Tarek - Adam", "Jihed - Alexis"), "T2": ("Marwene - Anis", "Achref - Samy")},
    "Round 10": {"T1": ("Mouhamed Hedi - Ouassim", "Oussama - Ahmed"), "T2": ("Eric - Valérie", "Stéphane - Anissa")},
    "Round 11": {"T1": ("Tarek - Adam", "Achref - Samy"), "T2": ("Jihed - Alexis", "Oussama - Ahmed")},
    "Round 12": {"T1": ("Marwene - Anis", "Stéphane - Samy"), "T2": ("Mouhamed Hedi - Ouassim", "Eric - Valérie")},
    "Round 13": {"T1": ("Tarek - Adam", "Oussama - Ahmed"), "T2": ("Achref - Samy", "Stéphane - Anissa")},
    "Round 14": {"T1": ("Jihed - Alexis", "Eric - Valérie"), "T2": ("Marwene - Anis", "Mouhamed Hedi - Ouassim")}
} # Zid el rounds lokhrin houni baad

st.title("Padel Scoreboard 🎾")

# 2. Ekhtar el Mode
mode = st.sidebar.radio("Chnwa t7eb t'7el?", ["Admin (Tlfoun)", "TV Terrain 1", "TV Terrain 2"])

# 3. Logic mta3 el Admin
if mode == "Admin (Tlfoun)":
    st.subheader("T9ayed el score houni")
    rd = st.selectbox("Ekhtar el Round", list(rounds.keys()))
    tr = st.radio("Ekhtar el Terrain", ["T1", "T2"])
    
    t1, t2 = rounds[rd][tr]
    st.info(f"Match: {t1} VS {t2}")
    
    score1 = st.number_input(f"Score {t1}", 0, 10)
    score2 = st.number_input(f"Score {t2}", 0, 10)
    
    if st.button("Abat el Score lel TV"):
        st.session_state[f"score_{tr}"] = f"{score1} - {score2}"
        st.success("Tbaat!")

# 4. Logic mta3 el TV
else:
    tr_id = "T1" if "1" in mode else "T2"
    st.header(f"Terrain {tr_id}")
    live_score = st.session_state.get(f"score_{tr_id}", "0 - 0")
    st.markdown(f"<h1 style='text-align: center; font-size: 150px;'>{live_score}</h1>", unsafe_allow_html=True)
