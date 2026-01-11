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
import numpy as np
import tensorflow as tf

# Hide sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# Login protection
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

st.title("🌾 Crop Yield Prediction")

model = tf.keras.models.load_model("crop_yield_model.h5", compile=False)

area = st.number_input("Land Area (acres)", 0.1, 100.0, 1.0)
rainfall = st.number_input("Rainfall (mm)", 0.0, 500.0, 120.0)
temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)

if st.button("Predict Yield"):
    input_data = np.array([[area, rainfall, temperature]])
    prediction = model.predict(input_data)[0][0]

    st.success(f"Expected Yield: {prediction:.2f} kg")

    if prediction < 100:
        st.warning("Low yield expected. Increase irrigation.")
    elif prediction < 300:
        st.info("Average yield. Maintain fertilizer balance.")
    else:
        st.success("High yield expected!")

st.markdown("---")
if st.button("⬅ Back to Home"):
    st.switch_page("pages/home.py")
