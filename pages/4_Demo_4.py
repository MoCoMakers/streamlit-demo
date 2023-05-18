import streamlit as st
import utils

color = st.color_picker('Pick A Color', '#00f900')

with open('static/ninja.svg', mode='r') as f:
    svg_string = f.read()

svg_string = svg_string.replace('#000000', color)
html_string = utils.svg_to_html(svg_string)

st.markdown(html_string, unsafe_allow_html=True)


code = '''
import streamlit as st
import utils

color = st.color_picker('Pick A Color', '#00f900')

with open('static/ninja.svg', mode='r') as f:
    svg_string = f.read()

svg_string = svg_string.replace('#000000', color)
html_string = utils.svg_to_html(svg_string)

st.markdown(html_string, unsafe_allow_html=True)
'''
st.code(code, language='python')