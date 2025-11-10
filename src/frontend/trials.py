"""Trials selection page for CoTrial RAG System."""

import streamlit as st

st.set_page_config(
    page_title="Trials - CoTrial RAG",
    page_icon="📊",
    layout="wide",
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
        padding: 2rem 3rem;
        max-width: 1400px;
    }
    
    /* Title styling */
    h1 {
        color: #2C3E50;
        font-weight: 600;
        letter-spacing: -0.5px;
        margin-bottom: 0.5rem;
    }
    
    /* Trial card styling */
    .trial-card {
        background-color: #FFFFFF;
        border: 2px solid rgba(0, 0, 0, 0.08);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .trial-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        border-color: #FA8072;
    }
    
    .trial-card.stubbed {
        opacity: 0.6;
        cursor: not-allowed;
    }
    
    .trial-card.stubbed:hover {
        transform: none;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        border-color: rgba(0, 0, 0, 0.08);
    }
    
    .trial-title {
        color: #2C3E50;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .trial-subtitle {
        color: #5A6C7D;
        font-size: 1rem;
        margin-bottom: 1rem;
    }
    
    .trial-meta {
        display: flex;
        gap: 2rem;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid #E8E6E3;
    }
    
    .trial-meta-item {
        display: flex;
        flex-direction: column;
    }
    
    .trial-meta-label {
        color: #5A6C7D;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 0.25rem;
    }
    
    .trial-meta-value {
        color: #2C3E50;
        font-size: 1rem;
        font-weight: 600;
    }
    
    .stubbed-badge {
        display: inline-block;
        background-color: #F8F6F4;
        color: #5A6C7D;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-left: 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #FA8072 0%, #F5A097 100%);
        color: white;
        border: none;
        border-radius: 12px;
        font-size: 15px;
        font-weight: 500;
        padding: 12px 24px;
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

# Initialize session state
if "selected_trial" not in st.session_state:
    st.session_state.selected_trial = None

# Header
st.markdown(
    """
    <div style="margin-bottom: 2rem;">
        <h1>Clinical Trials</h1>
        <p style="color: #5A6C7D; font-size: 1.1rem;">Select a trial to query data and documents</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Trial data
trials = [
    {
        "id": "S130",
        "title": "H3E-US-S130",
        "subtitle": "Non-Small Cell Lung Cancer Study",
        "status": "Active",
        "patients": "150+",
        "phase": "Phase III",
        "stubbed": False,
    },
    {
        "id": "S131",
        "title": "H3E-US-S131",
        "subtitle": "Advanced Melanoma Study",
        "status": "Active",
        "patients": "200+",
        "phase": "Phase II",
        "stubbed": True,
    },
    {
        "id": "S132",
        "title": "H3E-US-S132",
        "subtitle": "Breast Cancer Study",
        "status": "Recruiting",
        "patients": "180+",
        "phase": "Phase III",
        "stubbed": True,
    },
    {
        "id": "S133",
        "title": "H3E-US-S133",
        "subtitle": "Colorectal Cancer Study",
        "status": "Active",
        "patients": "120+",
        "phase": "Phase II",
        "stubbed": True,
    },
]

# Display trials in a grid
cols = st.columns(2)

for idx, trial in enumerate(trials):
    col = cols[idx % 2]
    
    with col:
        st.markdown(
            f"""
            <div class="trial-card {'stubbed' if trial['stubbed'] else ''}" onclick="window.location.href='{'#' if trial['stubbed'] else 'Chat' if not trial['stubbed'] else '#'}'">
                <div class="trial-title">
                    {trial['title']}
                    {f'<span class="stubbed-badge">Coming Soon</span>' if trial['stubbed'] else ''}
                </div>
                <div class="trial-subtitle">{trial['subtitle']}</div>
                <div class="trial-meta">
                    <div class="trial-meta-item">
                        <div class="trial-meta-label">Status</div>
                        <div class="trial-meta-value">{trial['status']}</div>
                    </div>
                    <div class="trial-meta-item">
                        <div class="trial-meta-label">Patients</div>
                        <div class="trial-meta-value">{trial['patients']}</div>
                    </div>
                    <div class="trial-meta-item">
                        <div class="trial-meta-label">Phase</div>
                        <div class="trial-meta-value">{trial['phase']}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        if not trial['stubbed']:
            if st.button(f"Open {trial['title']}", key=f"trial_{trial['id']}", use_container_width=True):
                st.session_state.selected_trial = trial['id']
                st.switch_page("pages/app.py")

# Logout button in sidebar
with st.sidebar:
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.session_state.selected_trial = None
        st.switch_page("login.py")

