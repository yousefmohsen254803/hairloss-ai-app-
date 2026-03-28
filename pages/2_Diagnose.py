import streamlit as st
from PIL import Image
import requests
import time

st.set_page_config(page_title="Diagnose", layout="centered")

# -----------------------------
# Clean UI
# -----------------------------
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 16px;
        color: #555;
        margin-bottom: 20px;
    }

    div.stButton > button {
        border-radius: 12px;
        padding: 10px;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Title
# -----------------------------
st.markdown('<div class="title">Diagnose</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Upload or take a photo to analyze your hair-loss stage</div>',
    unsafe_allow_html=True
)

st.info("Make sure the photo is clear and shows the top of your head.")

# -----------------------------
# Image Example
# -----------------------------
st.image("assets/hero.jpg", width=400)

# -----------------------------
# Upload
# -----------------------------
mode = st.radio("", ["📷 Take a photo", "🖼️ Upload"], horizontal=True)

uploaded_file = None

if mode == "📷 Take a photo":
    uploaded_file = st.camera_input("Take a photo")
else:
    uploaded_file = st.file_uploader("Upload image", type=["jpg", "png", "jpeg"])

API_URL = "https://hairloss-ai-app.onrender.com/predict"

# -----------------------------
# Prediction
# -----------------------------
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=300)

    if st.button("Analyse Photo"):
        with st.spinner("Analysing..."):
            try:
                uploaded_file.seek(0)
                files = {"file": uploaded_file.read()}
                response = requests.post(API_URL, files=files)

                data = response.json()
                st.session_state["pred_label"] = data["prediction"]
                st.session_state["uploaded_image_bytes"] = uploaded_file.getvalue()

                st.switch_page("pages/3_Result.py")

            except:
                st.error("Error connecting to API")

# -----------------------------
# Back button
# -----------------------------
if st.button("🏠 Home"):
    st.switch_page("Home.py")