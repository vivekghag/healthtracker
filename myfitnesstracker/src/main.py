import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    page="about_app.py",
    title="About App",
    default=True,
)
activity_data = st.Page(
    page="form.py",
    title="Enter your activity data",
)
activity_dashboard = st.Page(
    page="dashboard.py",
    title="Check your progress",
)
# --- NAVIGATION SETUP ---
pg = st.navigation(pages=[about_page, activity_data, activity_dashboard])

# --- RUN NAVIGATION  ---
pg.run()