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

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = password
    save_users(users)
    return True

st.title("🌱 SmartAgriApp - Register")

new_user = st.text_input("Username")
new_pass = st.text_input("Password", type="password")

if st.button("Register"):
    if register_user(new_user, new_pass):
        st.success("Account created successfully! Go to Login page.")
    else:
        st.warning("Username already exists. Try a different one.")
