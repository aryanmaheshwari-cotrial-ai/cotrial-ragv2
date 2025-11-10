"""Login page for CoTrial RAG System."""

import streamlit as st

st.set_page_config(
    page_title="Login - CoTrial RAG",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS matching the rich theme
st.markdown(
    """
    <style>
    /* Elegant serif typography */
    * {
        font-family: "Baskerville", "Libre Baskerville", "Times New Roman", serif !important;
    }
    
    /* Rich gradient background - deep burgundy to warm cream */
    .stApp {
        background: linear-gradient(135deg, #8B4513 0%, #A0522D 50%, #CD853F 100%);
        background-attachment: fixed;
    }
    
    /* Main container - premium parchment */
    .main .block-container {
        background: rgba(253, 250, 246, 0.98);
        border-radius: 24px;
        padding: 3.5rem 4rem;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.25), 0 0 0 2px rgba(139, 69, 19, 0.3);
        border: 2px solid rgba(205, 133, 63, 0.4);
        max-width: 480px;
        margin: 4rem auto;
        backdrop-filter: blur(10px);
    }
    
    /* Title styling */
    h1 {
        color: #2C1810;
        font-weight: 600;
        letter-spacing: 1px;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.95);
        border: 2px solid rgba(139, 69, 19, 0.3);
        border-radius: 12px;
        font-size: 1rem;
        padding: 1rem 1.25rem;
        color: #2C1810;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8B4513;
        box-shadow: 0 0 0 3px rgba(139, 69, 19, 0.15);
        background: rgba(255, 255, 255, 1);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #8B7355;
        font-style: italic;
    }
    
    /* Remove eye icon from password fields */
    button[data-testid="baseButton-secondary"],
    button[kind="secondary"] {
        display: none !important;
    }
    
    /* Hide all input action buttons */
    .stTextInput button,
    .stTextInput [role="button"] {
        display: none !important;
    }
    
    /* Button styling - luxurious gold accent */
    .stButton > button {
        background: linear-gradient(135deg, #8B4513 0%, #A0522D 100%) !important;
        color: #F5E6D3 !important;
        border: 2px solid rgba(205, 133, 63, 0.4) !important;
        border-radius: 12px !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        padding: 1rem 2rem !important;
        width: 100%;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(139, 69, 19, 0.3) !important;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(139, 69, 19, 0.5) !important;
        border-color: rgba(205, 133, 63, 0.7) !important;
        background: linear-gradient(135deg, #A0522D 0%, #CD853F 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 8px rgba(139, 69, 19, 0.3);
    }
    
    /* Alert boxes */
    .stSuccess {
        background: rgba(245, 238, 220, 0.9) !important;
        border-left: 4px solid #8B4513 !important;
        color: #2C1810 !important;
        border-radius: 8px;
    }
    
    .stError {
        background: rgba(255, 240, 240, 0.9) !important;
        border-left: 4px solid #8B0000 !important;
        color: #2C1810 !important;
        border-radius: 8px;
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
    <div style="text-align: center; margin-bottom: 2.5rem;">
        <h1 style="font-size: 2.5rem; margin-bottom: 0.75rem; color: #2C1810; font-weight: 600; letter-spacing: 1px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);">CoTrial RAG</h1>
        <p style="color: #5D4E37; font-size: 1.15rem; font-weight: 500; letter-spacing: 0.5px; margin: 0; font-style: italic;">Clinical Trial Data Query System</p>
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
            st.switch_page("pages/trials.py")
        else:
            st.error("Please enter both username and password")

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

