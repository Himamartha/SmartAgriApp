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
from PIL import Image

# Hide sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# Login check
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

st.title("🌿 Plant Disease Detection")

model = tf.keras.models.load_model("plant_disease_model.h5")

file = st.file_uploader("Upload leaf image", type=["jpg","png","jpeg"])

if file:
    img = Image.open(file)
    st.image(img, width=300)

    img = img.resize((128,128))
    img = np.array(img)/255.0
    img = img.reshape(1,128,128,3)

    pred = model.predict(img)
    classes = ["Blight","Healthy","Leaf Spot"]
    result = classes[np.argmax(pred)]

    st.success(f"Disease: {result}")

    if result == "Blight":
        st.info("Use copper fungicide and remove infected leaves.")
    elif result == "Leaf Spot":
        st.info("Apply neem oil spray weekly.")
    else:
        st.info("Crop is healthy.")

st.markdown("---")
if st.button("⬅ Back to Home"):
    st.switch_page("pages/home.py")
