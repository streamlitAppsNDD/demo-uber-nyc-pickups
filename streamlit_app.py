# Added to as an example of how to track your app using Umami
import streamlit.components.v1 as components
components.html(f'<script async defer data-website-id="bd4bc597-839f-4f88-8c86-61b5785b8e03" src="https://umami-demo-production.up.railway.app/umami.js"></script>')

"""An example of showing geographic data."""

import streamlit as st

# Track custom event:
def track(name):
    components.html(f'<script>umami({name});</script>')    

st.button("Click to track", key=None, on_click=track, args=("button click",))

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

st.write("Streamlit and Umami integration demo.")
