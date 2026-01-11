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

# Hide sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# Login protection
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

st.set_page_config(page_title="Home")

st.title("🏡 Home")
st.success(f"Welcome {st.session_state.username}")

st.markdown("### Choose a service")

col1, col2 = st.columns(2)

with col1:
    if st.button("🌿 Disease Prediction"):
        st.switch_page("pages/disease.py")

with col2:
    if st.button("🌾 Yield Prediction"):
        st.switch_page("pages/yield.py")

st.markdown("---")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("app.py")
