import streamlit as st
import pandas as pd
import plotly.express as px
# exploring categorical data
# try modal-popup
import streamlit_modal as modal

import streamlit.components.v1 as components
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
@st.experimental_singleton
def load_data():
    return pd.read_csv('data/StudentsPerformance.csv')

data = load_data()
categorical_features = data.select_dtypes(include=['object']).columns
if len(categorical_features) > 0:
    #st.markdown("## Categorical Features")
    #st.dataframe(data[selected_categorical_features])
    st.markdown("## Count Plot")
    for col in categorical_features:
        fig = px.histogram(data, x=col, title=f"Count of {col}")
        st.plotly_chart(fig)

cols = st.columns(2)


open_modal = st.button("Open")
if open_modal :
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")

        st.write("Some fancy text")
        value = st.checkbox("Check me")
