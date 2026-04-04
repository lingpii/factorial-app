import streamlit as st
from factorial import fact

st.set_page_config(
    page_title="Factorial Calculator",
    layout="centered"
)

#Body theme (backgrounf, font)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

    * {
        font-family: 'Press Start 2P', monospace !important;
    }

    /* Header, label, text → beige */
    h1, h2, h3, label, p, .stMarkdown, .stText {
        color: #d4b896 !important;
    }

    /* Input box */
    input[type="number"] {
        color: #d4b896 !important;
        background-color: #fdf8f0 !important;
    }

    /* Nút Calculate → chữ trắng, nền nâu */
    .stButton > button {
        color: #ffffff !important;
        background-color: #c9a97a !important;
        border: none !important;
    }

    .stButton > button:hover {
        background-color: #a07850 !important;
        color: #ffffff !important;
    }

    /* Nút +/- → chữ trắng, nền nâu đậm */
    .stNumberInput button {
        color: #ffffff !important;
        background-color: #2c1810 !important;
        border: none !important;
    }

    .stNumberInput button:hover {
        background-color: #4a2e20 !important;
    }
    </style>
""", unsafe_allow_html=True)
# ─── TITLE ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="pixel-divider">░░░░░░░░░░░░░░░░░░░░</div>', unsafe_allow_html=True)
st.markdown("<h1> FACTORIAL CALCULATOR</h1>", unsafe_allow_html=True)
st.markdown('<div class="pixel-divider">░░░░░░░░░░░░░░░░░░░░</div>', unsafe_allow_html=True)


def main(): 
    number = st.number_input("Enter a number: ",
                             min_value = 0,
                             max_value = 900)
    if st.button("Calculate"): 
        result = fact(number)
        st.write(f" 🎉 Result: {number}! = {result}")
        st.balloons()

if __name__   == "__main__":
    main()

