import streamlit as st
import pandas as pd
st.set_page_config(page_title="PerformanceAnalyzer", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")
st.markdown("<h1 style='text-align: center; color: grey;'>Welcome to Student Performance Analyzer</h1>", unsafe_allow_html=True)



def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()