import streamlit as st

st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}

.main {
    max-width: 420px;
    margin: auto;
}

button {
    width: 100%;
    height: 70px;
    font-size: 18px !important;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)
import streamlit as st
import json
import os

# ---------------- HIDE SIDEBAR ----------------
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="SmartAgriApp - Login", layout="centered")

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# UI
st.title("🌱 SmartAgriApp")
st.subheader("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    users = load_users()
    if username in users and users[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.switch_page("pages/home.py")
    else:
        st.error("Invalid credentials")

st.markdown("New user? Register first.")
