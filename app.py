import streamlit as st
import pandas as pd
import streamlit_modal as modal
import streamlit.components.v1 as components
st.set_page_config(page_title="PerformanceAnalyzer", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")
st.markdown("<h1 style='text-align: center; color: grey;'>Welcome to Student Performance Analyzer</h1>", unsafe_allow_html=True)
cols = st.columns(5)
with cols[4]:
    open_modal = st.button("Open")
    if open_modal:
        modal.open()

    if modal.is_open():
        with modal.container():
            st.write("Text goes here")

            html_string = '''
            <h1>HTML string in RED</h1>

            <script language="javascript">
            document.querySelector("h1").style.color = "red";
            </script>
            '''
            components.html(html_string)

            st.write("Some fancy text")
            value = st.checkbox("Check me")
            st.write(f"Checkbox checked: {value}")

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