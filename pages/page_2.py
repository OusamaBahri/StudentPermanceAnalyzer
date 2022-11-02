import streamlit as st
import pandas as pd
import plotly.express as px

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#@st.experimental_memo
def load_data():
    return pd.read_csv('data/StudentsPerformance.csv')


data = load_data()
# calculate the percentage of missing values in the data
missing_values = data.isnull().sum().sum() / len(data) * 100
# calculate the percentage of duplicates values in the data
duplicates = data.duplicated().sum() / len(data) * 100
col1, col2, col3 = st.columns(3)
col1.metric("Missing Values", f"{missing_values}%")
col2.metric("Total Students", data.shape[0])
col3.metric("Duplicates", f"{duplicates}%")


st.dataframe(data)

st.sidebar.selectbox("Want to see more informations?", ["Inf1", "Inf2", "Inf3"])
# display the pourcentage of categorical variables and numerical variables in the data with pie plot
#fig = px.pie(data, values=data.dtypes.value_counts(), names=['categorical features','numerical features'], title="Count of categorical and numerical variables")
#st.plotly_chart(fig)
check = st.checkbox("Show the pourcentage of categorical variables and numerical variables in the data with pie plot")
if check:
    fig = px.pie(data, values=data.dtypes.value_counts(), names=['categorical features','numerical features'], title="Count of categorical and numerical variables")
    st.plotly_chart(fig)  # display the pourcentage of categorical variables and numerical variables in the data with pie plot

if st.button("uncheck me") :
    check = False
    st.write("uncheck")
    st.write(check)