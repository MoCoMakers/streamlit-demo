import streamlit as st
import utils


def new_color():
    current_color = st.session_state['color_key']
    inverted_color = utils.invert_hex_color(current_color)
    st.info('You picked '+current_color+' perhaps you the opposite: '+inverted_color, icon="⚠️")


color = st.color_picker('Pick A Color', '#00f900', on_change=new_color, key='color_key')

with open('static/ninja.svg', mode='r') as f:
    svg_string = f.read()

svg_string = svg_string.replace('#000000', color)
html_string = utils.svg_to_html(svg_string)

st.markdown(html_string, unsafe_allow_html=True)

code = '''
import streamlit as st
import utils


def new_color():
    current_color = st.session_state['color_key']
    inverted_color = utils.invert_hex_color(current_color)
    st.info('You picked '+current_color+' perhaps you the opposite: '+inverted_color, icon="⚠️")


color = st.color_picker('Pick A Color', '#00f900', on_change=new_color, key='color_key')

with open('static/ninja.svg', mode='r') as f:
    svg_string = f.read()

svg_string = svg_string.replace('#000000', color)
html_string = utils.svg_to_html(svg_string)

st.markdown(html_string, unsafe_allow_html=True)
'''
st.code(code, language='python')
