"""Login page for CoTrial RAG System."""

import streamlit as st

st.set_page_config(
    page_title="Login - CoTrial RAG",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS matching the theme
st.markdown(
    """
    <style>
    /* Main background - coral/salmon color */
    .stApp {
        background: linear-gradient(135deg, #FA8072 0%, #F5A097 100%);
        background-attachment: fixed;
    }
    
    /* Main container - off-white */
    .main .block-container {
        background-color: #FAF9F7;
        border-radius: 24px;
        padding: 3rem 4rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        max-width: 450px;
        margin: 4rem auto;
    }
    
    /* Title styling */
    h1 {
        color: #2C3E50;
        font-weight: 600;
        letter-spacing: -0.5px;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background-color: #FFFFFF;
        border: 2px solid #E8E6E3;
        border-radius: 12px;
        font-size: 15px;
        padding: 14px 18px;
        color: #2C3E50;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #FA8072;
        box-shadow: 0 0 0 3px rgba(250, 128, 114, 0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #FA8072 0%, #F5A097 100%);
        color: white;
        border: none;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 500;
        padding: 14px 24px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(250, 128, 114, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(250, 128, 114, 0.4);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Login form
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="font-size: 2rem; margin-bottom: 0.5rem;">CoTrial RAG</h1>
        <p style="color: #5A6C7D; font-size: 1rem;">Clinical Trial Data Query System</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("login_form"):
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    submitted = st.form_submit_button("Sign In", use_container_width=True)
    
    if submitted:
        # Stubbed login - accept any credentials
        if username and password:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("✅ Login successful!")
            st.rerun()
        else:
            st.error("Please enter both username and password")

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

