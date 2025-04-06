import streamlit as st

# Set up page
st.set_page_config(page_title="ClearGlow", layout="centered")

# CSS copied and adapted from your HTML
st.markdown("""
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            background: 
                linear-gradient(rgba(173, 216, 230, 0.8), rgba(173, 216, 230, 0.8)),
                url("https://via.placeholder.com/1500") no-repeat center center fixed;
            background-size: cover;
            font-family: Arial, sans-serif;
        }

        .center {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            height: 90vh;
        }

        h1 {
            font-size: 4rem;
            font-weight: bold;
            color: black;
            -webkit-text-stroke: 1px white;
            margin: 0;
        }

        p {
            font-size: 1.2rem;
            margin-top: 10px;
            color: black;
        }

        .stButton>button {
            margin-top: 30px;
            padding: 15px 30px;
            font-size: 1rem;
            background-color: white;
            color: black;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #ccc;
        }
    </style>
""", unsafe_allow_html=True)

# Track button click
if "started" not in st.session_state:
    st.session_state.started = False

# Layout container
st.markdown('<div class="center">', unsafe_allow_html=True)

# Page 1: Welcome screen
if not st.session_state.started:
    st.markdown("<h1>ClearGlow</h1>", unsafe_allow_html=True)
    st.markdown("<p>Bringing clarity and light to your online presence.</p>", unsafe_allow_html=True)

    if st.button("Let's Get Started"):
        st.session_state.started = True

# Page 2: Upload screen
else:
    st.markdown("<h1>Upload an Image</h1>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

st.markdown('</div>', unsafe_allow_html=True)
