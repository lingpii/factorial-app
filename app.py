import streamlit as st
from factorial import fact

st.set_page_config(
    page_title="Factorial Calculator",
    layout="centered"
)

#Body theme (backgrounf, font)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323:wght@400&display=swap');

/* Background */
[data-testid="stAppViewContainer"] {
    background-color: #f5f0e8;
}
[data-testid="stHeader"] {
    background-color: #f5f0e8;
}
[data-testid="stSidebar"] {
    background-color: #ede8dc;
}

/* Main font */
html, body, [class*="css"] {
    font-family: 'Press Start 2P', monospace !important;
    font-size: 15px;
    color: #4a3f35;
}

/* Title */
h1 {
    font-family: 'Press Start 2P', monospace !important;
    font-size: 18px !important;
    color: #7a5c3a !important;
    text-align: center;
    padding: 10px 0 20px 0;
    line-height: 1.8;
}

h3 {
    font-family: 'Press Start 2P', monospace !important;
    font-size: 12px !important;
    color: #7a5c3a !important;
}

/* Input */
input[type="number"] {
    background-color: #fdf8f0 !important;
    border: 2px solid #c9a97a !important;
    border-radius: 6px !important;
    color: #4a3f35 !important;
    font-family: 'Press Start 2P', monospace !important;
    font-size: 15px !important;
}
            
/* Label "Enter a number" */
    .stNumberInput label, p {
        font-family: 'Press Start 2P', monospace !important;
    }
            
/* Button */
.stButton > button {
    background-color: #c9a97a;
    color: #fff8f0;
    font-family: 'Press Start 2P', monospace !important;
    font-size: 10px;
    border: none;
    border-radius: 10px;
    padding: 8px 18px;
    width: 100%;
    cursor: pointer;
    transition: background 0.2s;
    image-rendering: pixelated;
}
.stButton > button:hover {
    background-color: #a07850;
}


/* Pixel divider */
.pixel-divider {
    text-align: center;
    font-size: 22px;
    letter-spacing: 4px;
    color: #c9a97a;
    margin: 12px 0;
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

