import streamlit as st
from factorial import fact # Đảm bảo bạn đã có hàm fact() trong file factorial.py

st.set_page_config(
    page_title="Factorial Calculator",
    layout="centered"
)

# ─── TITLE ─────────────────────────────────────────────────────────────────────

st.markdown('<div class="pixel-divider">°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･</div>', unsafe_allow_html=True)
st.markdown("<h1> ✦ FACTORIAL ✦ CALCULATOR ✦ </h1>", unsafe_allow_html=True)
st.markdown('<div class="pixel-divider">°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･</div>', unsafe_allow_html=True)



# Body theme (background, font)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323:wght@400&display=swap');

/* Background */
[data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background-color: #f5f0e8;
}
[data-testid="stSidebar"] {
    background-color: #ede8dc;
}

/* Main font for everything just to be safe */
html, body, p, div, span, [class*="st-emotion-cache"] {
    font-family: 'Press Start 2P', monospace !important;
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
.stNumberInput label p, .stNumberInput label {
    font-family: 'Press Start 2P', monospace !important;
    color: #d4b896 !important;
}

            
/* Button */
.stButton > button, .stButton button p {
    background-color: #c9a97a !important;
    color: #fff8f0 !important;
    font-family: 'Press Start 2P', monospace !important;
    font-size: 10px !important;
    border: none;
    border-radius: 18px;
    padding: 4px 18px; /* Tinh chỉnh lại padding cho cân đối */
    width: 100%;
    cursor: pointer;
    transition: background 0.2s;
    image-rendering: pixelated;
}

.stNumberInput button {
    background-color: #c9a97a !important;
    color: #fff8f0 !important;
    border: none !important;
    border-radius: 6px !important;
}

.stButton > button:hover {
    background-color: #a07850 !important;
}


/* Pixel divider */
.pixel-divider {
    text-align: center;
    font-size: 22px;
    letter-spacing: 4px;
    color: #c9a97a;
    margin: 12px 0;
}
<\style>
""", unsafe_allow_html=True)

def main(): 
    number = st.number_input("Enter a number: ",
                             min_value=0,
                             max_value=900)
    
    if st.button("Calculate"): 
        result = fact(number)
        
        # Đã fix phần CSS inline ở đây
        st.markdown(f"""
    <div style="background-color: #fdf8f0; padding: 15px; border-radius: 10px; border: 2px dashed #c9a97a; text-align: center; margin-top: 15px;">
        <p style="color: #7a5c3a !important; font-family: 'Press Start 2P', monospace !important; font-size: 14px; margin: 0; line-height: 1.5;">
            🎉 Result:<br><br>{number}! = {result}
        </p>
    </div>
""", unsafe_allow_html=True)
        st.balloons()

if __name__ == "__main__":
    main()
