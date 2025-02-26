# Added to as an example of how to track your app using Umami
import streamlit as st
import os
import re
import streamlit.components.v1 as components
max_width = 3000
padding_top = 10
padding_right = 5
padding_left = 5
padding_bottom = 10
COLOR = 'black'
BACKGROUND_COLOR = 'white'
st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {max_width}px;
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
    .reportview-container .main {{
        color: {COLOR};
        background-color: {BACKGROUND_COLOR};
    }}
</style>
""",
        unsafe_allow_html=True,
    )


code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YG9L2B01SW"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-YG9L2B01SW');
</script>"""
code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-215848812-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-215848812-1');
</script>
"""
# a=os.path.dirname(st.__file__)+'/static/index.html'
# with open(a, 'r') as f:
#     data=f.read()
#     if len(re.findall('UA-', data))==0 and len(re.findall('G-', data))==0:
#         with open(a, 'w') as ff:
#             newdata=re.sub('<head>','<head>'+code,data)
#             ff.write(newdata)
            
google_analytics_js = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YG9L2B01SW"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-YG9L2B01SW');
</script>"""

# components.html(f"<!-- Global site tag (gtag.js) - Google Analytics --> <script async src='https://www.googletagmanager.com/gtag/js?id=G-1PLZC4XB4D'></script><script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'G-1PLZC4XB4D');</script>")

st.write("Streamlit and Umami integration demo.")
if st.button('Clickme'):
    st.write("Hello")

components.html("""<img src="https://www.google-analytics.com/collect?v=1&tid=UA-215848812-1&cid=1885418923.1520692526&aip=1&a=834238095&t=pageview&ec=email&ea=open&dp=%2Femail%2Fnewsletter&dt=My%20Newsletter">
""")
