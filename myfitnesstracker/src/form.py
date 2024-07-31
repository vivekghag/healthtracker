import streamlit as st
import pandas as pd

with st.form("Enter Activity Data:"):
    activity_date = st.date_input("Select Activity Date")
    activity_name = st.text_input("Enter Activity Name")
    activity_stat = st.number_input("Enter measured steps")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        df = pd.read_csv("./data/activity_data.csv")
        #st.write(df)
        #st.write("Total data:", len(df.index))
        df.loc[len(df.index)] = [activity_date, activity_name, activity_stat]
        df.to_csv("./data/activity_data.csv",index=False)
        st.success("Data saved successfully!")