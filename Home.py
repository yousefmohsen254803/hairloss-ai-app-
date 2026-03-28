import streamlit as st

st.set_page_config(page_title="Hair Loss Analyzer", layout="centered")

# -----------------------------
# Clean UI (NO BACKGROUND)
# -----------------------------
st.markdown(
    """
    <style>
    .main .block-container {
        max-width: 900px;
        padding-top: 2rem;
    }

    .title {
        text-align:center;
        font-size:52px;
        font-weight:700;
    }

    .subtitle {
        text-align:center;
        font-size:18px;
        color:#555;
        margin-top:5px;
    }

    div.stButton > button {
        border-radius:14px;
        padding:12px 16px;
        font-weight:700;
    }

    .example-img img {
        border-radius:16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Title
# -----------------------------
st.markdown('<div class="title">Hair Loss Analyzer</div>', unsafe_allow_html=True)

# -----------------------------
# Description
# -----------------------------
st.markdown(
    '<div class="subtitle">This AI tool analyzes your image to estimate your hair-loss stage and related factors.</div>',
    unsafe_allow_html=True
)

st.write("It predicts your stage using the **Norwood scale (1–7)**.")

# -----------------------------
# Image
# -----------------------------
st.markdown("### Example of Norwood Stages")
st.image("assets/example.png", use_container_width=True)

# -----------------------------
# Button
# -----------------------------
col1, col2, col3 = st.columns([1,1,1])
with col2:
    if st.button("🔍 Analyse My Hair Loss"):
        st.switch_page("pages/2_Diagnose.py")