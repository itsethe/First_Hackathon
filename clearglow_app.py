import streamlit as st
import time

# Custom CSS for fade effect
st.markdown("""
    <style>
        .fade-in {
            animation: fadeIn 1s ease-in-out;
        }
        .fade-out {
            animation: fadeOut 1s ease-in-out forwards;
        }

        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }

        @keyframes fadeOut {
            from {opacity: 1;}
            to {opacity: 0;}
        }

        .center {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 90vh;
        }

        .clearglow-title {
            font-size: 4em;
            font-weight: bold;
            color: black;
            -webkit-text-stroke: 1px white;
        }

        .pastel-bg {
            background: linear-gradient(rgba(173,216,230,0.8), rgba(173,216,230,0.8)), url("https://your-image-url.com") no-repeat center center fixed;
            background-size: cover;
        }
    </style>
""", unsafe_allow_html=True)

# Session state to handle button click
if "started" not in st.session_state:
    st.session_state.started = False

# Welcome screen
if not st.session_state.started:
    with st.container():
        st.markdown('<div class="center fade-in">', unsafe_allow_html=True)
        st.markdown('<h1 class="clearglow-title">ClearGlow</h1>', unsafe_allow_html=True)
        st.markdown('<p>Bringing clarity and light to your online presence.</p>', unsafe_allow_html=True)
        if st.button("Let's Get Started"):
            st.session_state.started = True
            time.sleep(0.5)
        st.markdown('</div>', unsafe_allow_html=True)

# After button is clicked — show image uploader
else:
    st.markdown('<div class="center fade-in">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
