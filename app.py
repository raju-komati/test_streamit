import streamlit as st
import requests
import pandas as pd


resp = requests.get(
    'https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json')
json = resp.json()
codes, emojis = zip(*json.items())
df_emoji = pd.DataFrame({
    'Emojis': emojis,
    'Shortcodes': [f':{code}:' for code in codes],
})

emoji1 = st.select_slider('Select emoji 1:', options = df_emoji['shortcodes'], value=':sunglasses:')
emoji2 = st.select_slider('Select emoji 2:', options = df_emoji['shortcodes'], value=':white_check_mark:')
emoji3 = st.select_slider('Select emoji 3:', options = df_emoji['shortcodes'], value=':coffee:')
    

st.table(emojis)
