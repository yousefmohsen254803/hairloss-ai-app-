import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Result", layout="centered")

if "pred_label" not in st.session_state:
    st.title("Result")
    st.warning("No result available yet")

    if st.button("Go to Diagnose"):
        st.switch_page("pages/2_Diagnose.py")

    st.stop()

pred_label = st.session_state["pred_label"]
img_bytes = st.session_state["uploaded_image_bytes"]
img = Image.open(io.BytesIO(img_bytes))

st.title("Result")

st.image(img, width=400)

analysis_map = {
    "Normal Hair": "Norwood 1-2",
    "Moderate Loss": "Norwood 3-4",
    "Heavy Loss": "Norwood 5-6",
    "Bald": "Norwood 7"
}

st.subheader("Hair Loss Condition")
st.write(pred_label)

st.subheader("Norwood Stage")
st.write(analysis_map.get(pred_label, "Unknown"))

st.info("This is an AI-based analysis. Not medical advice.")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔁 Back to Diagnose"):
        st.switch_page("pages/2_Diagnose.py")

with col2:
    if st.button("🏠 Home"):
        st.switch_page("Home.py")