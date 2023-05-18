import streamlit as st

code = '''
import streamlit as st

html_string = """
<h3>Getting HTML on the page</h3>

<p>
Let's dive into streamlits massive and auto-magical toolkit of widget and interactive features.<br>
Let's visit: <a href="https://docs.streamlit.io/library/api-reference" target="_blank">https://docs.streamlit.io/library/api-reference</a>
</p>
"""
st.markdown(html_string, unsafe_allow_html=True)
'''

st.code(code, language='python')

html_string = """
<h3>Getting HTML on the page</h3>

<p>
Let's dive into streamlits massive and auto-magical toolkit of widget and interactive features.<br>
Let's visit: <a href="https://docs.streamlit.io/library/api-reference" target="_blank">https://docs.streamlit.io/library/api-reference</a>
</p>
"""
st.markdown(html_string, unsafe_allow_html=True)

