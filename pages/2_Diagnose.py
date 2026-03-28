import streamlit as st
from PIL import Image
import requests
import time

st.set_page_config(page_title="Diagnose", layout="centered")

st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 56px;
    color:#111;
    font-weight: 900;
}

.subtitle {
    text-align: center;
    font-size: 16px;
    color:#333;
}

.radio-title {
    color:#111;
    font-size: 18px;
    font-weight: 800;
}

div.stButton > button {
    border-radius: 14px;
    padding: 12px 14px;
    font-weight: 1200;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Diagnose</div>', unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Take or upload a photo to estimate your hair-loss stage</div>',
unsafe_allow_html=True
)

st.warning("Make sure the photo is clear and shows the top of your head.")

st.image("assets/hero.jpg", width=450)

st.markdown('<div class="radio-title">Choose how to add a photo:</div>', unsafe_allow_html=True)

mode = st.radio("", ["📷 Take a photo", "🖼️ Choose from device"], horizontal=True)

uploaded_file = None

if mode == "📷 Take a photo":
    uploaded_file = st.camera_input("Take a photo")
else:
    uploaded_file = st.file_uploader("Upload your photo", type=["jpg", "jpeg", "png"])

API_URL = "https://hairloss-ai-app.onrender.com/predict"

def wait_for_api(api_url, max_wait=60):
    health_url = api_url.replace("/predict", "/health")
    start = time.time()

    while time.time() - start < max_wait:
        try:
            response = requests.get(health_url, timeout=5)
            if response.status_code == 200:
                return True
        except:
            pass
        time.sleep(2)

    return False

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, width=320)

    if st.button("Analyse Photo", use_container_width=True):
        with st.spinner("Analysing your photo..."):
            try:
                uploaded_file.seek(0)
                file_bytes = uploaded_file.read()

                if not wait_for_api(API_URL):
                    st.error("API is waking up, try again.")
                    st.stop()

                response = requests.post(API_URL, files={"file": file_bytes})

                data = response.json()
                st.session_state["pred_label"] = data.get("prediction", "Unknown")
                st.session_state["uploaded_image_bytes"] = file_bytes

                st.switch_page("pages/3_Result.py")

            except Exception as e:
                st.error(f"Error: {e}")

if st.button("🏠 Home"):
    st.switch_page("Home.py")