import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv("./data/activity_data.csv")
df.columns=['Date','Activity','Steps']
st.dataframe(df[df.columns],hide_index=True)
mygraph = px.bar(df,x="Date",y="Steps",title="<b>My activity Records</b>")
st.plotly_chart(mygraph)