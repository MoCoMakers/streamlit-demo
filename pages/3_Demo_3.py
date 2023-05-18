import streamlit as st

code = '''
import streamlit as st

awesome_factor = st.slider('How awesome is this slider? (percent)', 0, 110, 25)  # (label, min, max, default value)
st.write("This slider is", awesome_factor, '% awesome')
'''

st.code(code, language='python')

awesome_factor = st.slider('How awesome is this slider? (percent)', 0, 110, 25)  # (label, min, max, default value)
st.write("This slider is", awesome_factor, '% awesome')

