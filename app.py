import streamlit as st
st.set_page_config(
        page_title="Main App Page",
)

html_string = "<h1>Streamlit for Team Research</h1>"

st.markdown(html_string, unsafe_allow_html=True)

