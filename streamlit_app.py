# Added to as an example of how to track your app using Umami
import streamlit as st
import streamlit.components.v1 as components

google_analytics_js = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YG9L2B01SW"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-YG9L2B01SW');
</script>"""
components.html(google_analytics_js)
# components.html(f"<!-- Global site tag (gtag.js) - Google Analytics --> <script async src='https://www.googletagmanager.com/gtag/js?id=G-1PLZC4XB4D'></script><script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'G-1PLZC4XB4D');</script>")

st.write("Streamlit and Umami integration demo.")

