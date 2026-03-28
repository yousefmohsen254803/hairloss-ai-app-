import streamlit as st

st.set_page_config(page_title="Hair Loss Analyzer", layout="centered")

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
        color: var(--text-color);
        font-weight:700;
    }

    .subtitle {
        text-align:center;
        font-size:18px;
        color: var(--text-color);
        opacity: 0.85;
        margin-top:5px;
    }

    .subtitle2 {
        text-align:center;
        font-size:18px;
        color: var(--text-color);
        opacity: 0.85;
        margin-top:-10px;
    }

    div.stButton > button {
        border-radius:14px;
        padding:12px 16px;
        font-weight:1200;
    }

    .example-img img {
        border-radius:16px;
        box-shadow:0 10px 30px rgba(0,0,0,0.20);
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Title
# -----------------------------
st.markdown(
"""
<div class="title">
Hair Loss Analyzer
</div>
""",
unsafe_allow_html=True
)


# -----------------------------
# Description
# -----------------------------
st.markdown(
"""
<div class="subtitle">
This AI tool analyzes your image to estimate your hair-loss stage and related factors such as hair density, graft requirements, and potential treatment cost.
</p></p>
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div style="
    max-width:850px;
    margin:10px auto 20px auto;
    color:var(--text-color);
    opacity:0.9;
    font-size:17px;
    line-height:1.6;
">

<p><p><p>
It predicts your stage using the <b>Norwood scale</b>, ranging from Stage 1 (no hair loss) to Stage 7 (advanced baldness).</p>

</div>
""",
unsafe_allow_html=True
)

# ----------------------------
# Norwood Example Image
# ----------------------------

st.markdown(
"""
<div style="
    max-width:850px;
    margin:20px auto 8px auto;
    color:var(--primary-color);
    font-size:18px;
    font-weight:600;
">
Example of Norwood Stages
</div>
""",
unsafe_allow_html=True
)

st.markdown('<div class="example-img">', unsafe_allow_html=True)

st.image(
    "assets/example.png",
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------
# Explanation section
# ---------------------------------
st.markdown(
"""
<div style="
    max-width:850px;
    margin:20px auto;
    color:var(--text-color);
    opacity:0.9;
    font-size:17px;
    line-height:1.6;
">

<p style="margin-top:0;">
<b>The also tool uses your image to estimate the following:</b>
</p>

<h4 style="color:var(--primary-color);margin-top:18px;">Hair Density</h4>

<p>
Hair density shows how much hair covers your scalp, measured in grafts per cm².
<a href="https://www.livingproof.com/blogs/hair-101/hair-density?srsltid=AfmBOoocBQ62rYxYNHldK9cz65LUF6uBrcgu7Zy29Kol2Gktl-iRaJe4" target="_blank" style="color:var(--primary-color); text-decoration:underline;">
Learn more
</a>
</p>

<h4 style="color:var(--primary-color);margin-top:18px;">Estimated Grafts</h4>

<p>
Estimated grafts indicate how many hair follicles may be needed if a transplant is considered.
</p>

</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Button
# -----------------------------
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🔍 Analyse My Hair Loss"):
        st.switch_page("pages/2_Diagnose.py")