# Added to as an example of how to track your app using Umami
import streamlit.components.v1 as components
components.html(f'<script async defer data-website-id="bd4bc597-839f-4f88-8c86-61b5785b8e03" src="https://umami-demo-production.up.railway.app/umami.js"></script>')

import streamlit as st

# Track custom event:

# 
def track(name):  
    components.html(
    f'''
        <script>
            umami({name});
            umami.trackEvent('Signup button click', 'signup', '/home', '94db1cb1-74f4-4a40-ad6c-962362670409');
        </script>
    '''
)

st.button("Click to track", key=None, on_click=track, args=("button click",))

st.write("Streamlit and Umami integration demo.")
