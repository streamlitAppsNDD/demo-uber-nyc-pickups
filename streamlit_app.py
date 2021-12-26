# Added to as an example of how to track your app using Umami
import streamlit as st
import streamlit.components.v1 as components

components.html(f'<script async defer data-website-id="1282b964-ba71-4b0c-bae8-ac58fe2d1dd3" src="https://umami-production-7628.up.railway.app/umami.js"></script>')

st.write("Streamlit and Umami integration demo.")
