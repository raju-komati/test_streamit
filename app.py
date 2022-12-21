import streamlit as st
import requests
import pandas as pd

@st.cache(ttl=60*60*12, allow_output_mutation=True)
def fetch_emojis():
    resp = requests.get(
        'https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json')
    json = resp.json()
    codes, emojis = zip(*json.items())
    return pd.DataFrame({
        'Emojis': emojis,
        'Shortcodes': [f':{code}:' for code in codes],
    })
    
emojis = fetch_emojis()

st.table(emojis)
