"""Trials selection page for CoTrial RAG System."""

import streamlit as st

st.set_page_config(
    page_title="Trials - CoTrial RAG",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None,
)

# Check authentication
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.switch_page("pages/login.py")

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
    
    /* Sidebar - sophisticated dark wood panel aesthetic */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a1a 0%, #2d2d2d 100%) !important;
        border-right: 2px solid rgba(205, 133, 63, 0.3);
        box-shadow: 4px 0 20px rgba(0, 0, 0, 0.5);
    }
    
    [data-testid="stSidebar"] * {
        color: #F5E6D3 !important;
    }
    
    /* Main container - premium parchment */
    .main .block-container {
        background: rgba(253, 250, 246, 0.95);
        padding: 2.5rem 3rem;
        max-width: 1400px;
        margin: 0 auto;
        border-radius: 0;
    }
    
    /* Title styling */
    h1 {
        color: #2C1810;
        font-weight: 600;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Trial card styling */
    .trial-card {
        background: rgba(253, 250, 246, 0.98);
        border: 2px solid rgba(139, 69, 19, 0.2);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12);
        transition: all 0.3s ease;
        cursor: pointer;
        backdrop-filter: blur(10px);
    }
    
    .trial-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(139, 69, 19, 0.25);
        border-color: rgba(139, 69, 19, 0.4);
    }
    
    .trial-card.stubbed {
        opacity: 0.6;
        cursor: not-allowed;
    }
    
    .trial-card.stubbed:hover {
        transform: none;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.12);
        border-color: rgba(139, 69, 19, 0.2);
    }
    
    /* Button alignment */
    div[data-testid="column"] button[data-testid="baseButton-primary"] {
        margin-top: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    .trial-title {
        color: #2C1810;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        letter-spacing: 0.5px;
    }
    
    .trial-subtitle {
        color: #5D4E37;
        font-size: 1rem;
        margin-bottom: 1rem;
        font-style: italic;
    }
    
    .trial-meta {
        display: flex;
        gap: 2rem;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 2px solid rgba(139, 69, 19, 0.15);
    }
    
    .trial-meta-item {
        display: flex;
        flex-direction: column;
    }
    
    .trial-meta-label {
        color: #8B7355;
        font-size: 0.85rem;
        font-weight: 500;
        margin-bottom: 0.25rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .trial-meta-value {
        color: #2C1810;
        font-size: 1rem;
        font-weight: 600;
    }
    
    .trial-meta-value.status-active {
        color: #8B4513;
        font-weight: 600;
    }
    
    .trial-meta-value.status-other {
        color: #5D4E37;
        font-weight: 600;
    }
    
    .stubbed-badge {
        display: inline-block;
        background: rgba(139, 69, 19, 0.15);
        color: #8B7355;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-left: 1rem;
        border: 1px solid rgba(139, 69, 19, 0.2);
    }
    
    /* Button styling - luxurious gold accent */
    .stButton > button {
        background: linear-gradient(135deg, #8B4513 0%, #A0522D 100%) !important;
        color: #F5E6D3 !important;
        border: 2px solid rgba(205, 133, 63, 0.4) !important;
        border-radius: 12px !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        padding: 0.9rem 2rem !important;
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
    <div style="margin-bottom: 2.5rem;">
        <h1 style="color: #2C1810; letter-spacing: 1px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);">Clinical Trials</h1>
        <p style="color: #5D4E37; font-size: 1.15rem; font-style: italic; letter-spacing: 0.5px;">Select a trial to query data and documents</p>
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
        "status": "Recruiting",
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
        "status": "Recruiting",
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
        # Determine status styling - only S130 is Active
        is_active = trial['id'] == "S130" and trial['status'] == "Active"
        status_color = "#8B4513" if is_active else "#5D4E37"
        stubbed_class = "stubbed" if trial['stubbed'] else ""
        
        # Build clean HTML string
        title_html = f'{trial["title"]}'
        if trial['stubbed']:
            title_html += ' <span class="stubbed-badge">Coming Soon</span>'
        
        # Render the card HTML
        card_html = f'''<div class="trial-card {stubbed_class}"><div class="trial-title">{title_html}</div><div class="trial-subtitle">{trial["subtitle"]}</div><div class="trial-meta"><div class="trial-meta-item"><div class="trial-meta-label">Status</div><div class="trial-meta-value" style="color: {status_color};">{trial["status"]}</div></div><div class="trial-meta-item"><div class="trial-meta-label">Patients</div><div class="trial-meta-value">{trial["patients"]}</div></div><div class="trial-meta-item"><div class="trial-meta-label">Phase</div><div class="trial-meta-value">{trial["phase"]}</div></div></div></div>'''
        st.markdown(card_html, unsafe_allow_html=True)
        
        # Add button for non-stubbed trials
        if not trial['stubbed']:
            if st.button(f"Chat with {trial['title']}", key=f"trial_{trial['id']}", use_container_width=True, type="primary"):
                st.session_state.selected_trial = trial['id']
                st.switch_page("pages/Chat.py")

# Sidebar
with st.sidebar:
    st.markdown(
        """
        <div style="margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 2px solid rgba(205, 133, 63, 0.3);">
            <h2 style="color: #F5E6D3; font-size: 1.8rem; font-weight: 600; margin: 0; letter-spacing: 1px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);">CoTrial RAG</h2>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: rgba(245, 230, 211, 0.8); font-style: italic;">Professional Research Assistant</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.authenticated = False
        st.session_state.selected_trial = None
        st.switch_page("pages/login.py")

