# Added to as an example of how to track your app using Umami
import streamlit.components.v1 as components
components.html(f'<script async defer data-website-id="bd4bc597-839f-4f88-8c86-61b5785b8e03" src="https://umami-demo-production.up.railway.app/umami.js"></script>')

import streamlit as st

# Track custom event:

# <script>umami({name});</script>
def track(name):  
    pass

st.button("Click to track", key=None, on_click=track, args=("button click",))

st.write("Streamlit and Umami integration demo.")

st.markdown(
    f'''
        const button = document.getElementById('signup-button');

        button.onclick = () => umami('Signup button click mark');
    ''',
    unsafe_allow_html=True
)

components.html(
    '''
        <button id="signup-button" class="button umami--click--signup-button">Sign up</button>
    '''
)
