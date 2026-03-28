import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Result", layout="centered")

# -----------------------------
# Title
# -----------------------------
st.title("Result")

# -----------------------------
# Check session
# -----------------------------
if "pred_label" not in st.session_state:
    st.warning("No result yet. Please analyse first.")
    if st.button("Go to Diagnose"):
        st.switch_page("pages/2_Diagnose.py")
    st.stop()

# -----------------------------
# Data
# -----------------------------
pred_label = st.session_state["pred_label"]
img_bytes = st.session_state["uploaded_image_bytes"]
img = Image.open(io.BytesIO(img_bytes))

# -----------------------------
# Show image
# -----------------------------
st.image(img, width=350)

# -----------------------------
# Results
# -----------------------------
st.subheader("Hair Loss Condition")
st.write(pred_label)

analysis_map = {
    "Normal Hair": "Norwood 1-2",
    "Moderate Loss": "Norwood 3-4",
    "Heavy Loss": "Norwood 5-6",
    "Bald": "Norwood 7"
}

st.subheader("Norwood Stage")
st.write(analysis_map.get(pred_label, "Unknown"))

# -----------------------------
# Note
# -----------------------------
st.info("This is an AI-based analysis. Not medical advice.")

# -----------------------------
# Buttons
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🔁 Back"):
        st.switch_page("pages/2_Diagnose.py")

with col2:
    if st.button("🏠 Home"):
        st.switch_page("Home.py")