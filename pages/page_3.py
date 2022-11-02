import streamlit as st
import pandas as pd
import plotly.express as px
# exploring categorical data
# try modal-popup
st.sidebar.header("Categorical Data")
st.sidebar.markdown("Select the categorical features you want to explore")
def load_data():
    return pd.read_csv('data/StudentsPerformance.csv')

data = load_data()
categorical_features = data.select_dtypes(include=['object']).columns
selected_categorical_features = st.sidebar.multiselect("Select", categorical_features)
if len(selected_categorical_features) > 0:
    st.markdown("## Categorical Features")
    st.dataframe(data[selected_categorical_features])
    st.markdown("## Count Plot")
    for col in selected_categorical_features:
        fig = px.histogram(data, x=col, title=f"Count of {col}")
        st.plotly_chart(fig)