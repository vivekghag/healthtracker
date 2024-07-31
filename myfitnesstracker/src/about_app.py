import streamlit as st

# ---HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/fitness.jpg", width=230)
with col2:
    st.title("Fitness Goal", anchor=False)
    st.write("Let's make small changes everyday to achieve a Healthy lifestyle")