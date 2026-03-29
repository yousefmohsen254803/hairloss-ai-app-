import streamlit as st
from PIL import Image
import io

# MUST be first Streamlit call
st.set_page_config(page_title="Result", layout="centered")

st.markdown(
    f"""
    <style>
    .main .block-container {{
        max-width: 950px;
        padding-top: 2rem;
    }}

    .title {{
        text-align: center;
        font-size: 56px;
        color: inherit;
        font-weight: 900;
        margin-bottom: 6px;
    }}

    .subtitle {{
        text-align: center;
        font-size: 20px;
        color: inherit;
        opacity: 0.92;
        margin-top: 0px;
        margin-bottom: 18px;
    }}

    .result-card {{
        background: rgba(0, 0, 0, 0.65);
        border: 2px solid rgba(255,255,255,0.16);
        border-radius: 14px;
        padding: 16px 12px;
        text-align: center;
        min-height: 100px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 6px 16px rgba(0,0,0,0.25);
        margin-bottom: 12px;
    }}

    .card-title {{
        font-size: 20px;
        font-weight: 800;
        color: #9fffe0;
        margin-bottom: 8px;
    }}

    .card-value {{
        font-size: 20px;
        font-weight: 400;
        color: inherit;
    }}

    .card-value-small {{
        font-size: 18px;
        font-weight: 400;
        color: inherit;
    }}

    div.stButton > button {{
        border-radius: 18px;
        padding: 14px 18px;
        font-weight: 800;
        min-height: 56px;
        border: 1px solid rgba(255,255,255,0.16);
        background: rgba(18, 24, 38, 0.92);
        color: white;
        box-shadow: 0 8px 20px rgba(0,0,0,0.22);
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Guard: if opened directly
# -----------------------------
if "pred_label" not in st.session_state or "uploaded_image_bytes" not in st.session_state:

    st.markdown('<div class="title">Result</div>', unsafe_allow_html=True)

    st.markdown(
        "<h3 style='text-align:center; color:inherit; margin-top:40px; margin-bottom:10px;'>No result available yet</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; color:inherit; opacity:0.88; font-size:18px; line-height:1.6; max-width:720px; margin:0 auto 30px auto;'>Please go to the Diagnose page first and upload or take a photo to get your AI hair analysis.</p>",
        unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5 = st.columns([1.1, 1.5, 0.35, 1.5, 1.1])

    with col2:
        if st.button("↩️ Go to Diagnose", use_container_width=True):
            st.switch_page("pages/2_Diagnose.py")

    with col4:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("Home.py")

    st.stop()


pred_label = st.session_state["pred_label"]
img_bytes = st.session_state["uploaded_image_bytes"]
img = Image.open(io.BytesIO(img_bytes))


# -----------------------------
# Stage mapping
# -----------------------------
analysis_map = {
    "Normal Hair": {
        "norwood": "Norwood 1-2",
        "density": "High density (80-100 grafts/cm²)",
        "grafts": "No transplant needed"
    },
    "Moderate Loss": {
        "norwood": "Norwood 3-4",
        "density": "Medium density (60-80 grafts/cm²)",
        "grafts": "1000-2000 grafts"
    },
    "Heavy Loss": {
        "norwood": "Norwood 5-6",
        "density": "Low density (40-60 grafts/cm²)",
        "grafts": "2500-4000 grafts"
    },
    "Bald": {
        "norwood": "Norwood 7",
        "density": "Very low density (<40 grafts/cm²)",
        "grafts": "4500-6000 grafts"
    }
}

info = analysis_map.get(
    pred_label,
    {
        "norwood": "Unknown",
        "density": "Unknown",
        "grafts": "Unknown"
    }
)

# -----------------------------
# Transplant cost mapping
# -----------------------------
cost_map = {
    "Normal Hair": "No transplant needed",
    "Moderate Loss": "€2,500 - €4,500",
    "Heavy Loss": "€4,500 - €7,500",
    "Bald": "€7,500 - €12,000"
}

estimated_cost = cost_map.get(pred_label, "Unknown")


# -----------------------------
# Page UI
# -----------------------------
st.markdown('<div class="title">Result</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Here is your uploaded photo and the estimated hair-loss analysis.</div>',
    unsafe_allow_html=True
)

left, center, right = st.columns([1, 2, 1])
with center:
    st.image(img, width=400)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div class="result-card">
            <div class="card-title">Hair Loss Condition</div>
            <div class="card-value">{pred_label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="result-card">
            <div class="card-title">Norwood Stage</div>
            <div class="card-value">{info['norwood']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

col3, col4 = st.columns(2)

with col3:
    st.markdown(
        f"""
        <div class="result-card">
            <div class="card-title">Hair Density</div>
            <div class="card-value-small">{info['density']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="result-card">
            <div class="card-title">Estimated Grafts</div>
            <div class="card-value-small">{info['grafts']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

col5, col6, col7 = st.columns([1, 2, 1])

with col6:
    st.markdown(
        f"""
        <div class="result-card">
            <div class="card-title">Estimated Transplant Cost</div>
            <div class="card-value-small">{estimated_cost}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div style="
        max-width:850px;
        margin:20px auto;
        padding:6px 18px;
        background:rgba(255, 210, 80, 0.15);
        border-left:6px solid #FFD43B;
        border-radius:8px;
        font-size:16px;
        color:inherit;
        line-height:1.6;
    ">
        <b>Note:</b> This result is an <b>AI-based analysis</b>. It is not medical advice.
        For professional diagnosis or treatment, consult a healthcare professional.
    </div>
    """,
    unsafe_allow_html=True
)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔁 Back to Diagnose", use_container_width=True):
            st.switch_page("pages/2_Diagnose.py")

    with col2:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("Home.py")

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("📅 Book Appointment", use_container_width=True):
        st.write("This feature is not available at the moment.")