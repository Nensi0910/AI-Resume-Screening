# ==========================================================
# AI Resume Screening System
# Dashboard-inspired navy + light gray UI theme
# ==========================================================
import textwrap


def apply_styles():

    return textwrap.dedent("""

    <style>

    :root {
        --primary-color: #f4f7fb;
        --background-color: #17324d;
        --secondary-background-color: #ffffff;
        --text-color: #302C28;
        accent-color: #B86E4B;
        --sidebar-bg: #17324d;
        --sidebar-bg-2: #17324d;
        --page-bg: #f4f7fb;
        --card-bg: #ffffff;
        --card-border: #e3e6e8;
        --text-dark: #302C28;
        --text-soft: #302C28;
        --muted: #dfe4e8;
        --accent: #B86E4B;
        --accent-soft: rgba(184, 110, 75, 0.12);
        --dot-red: #f15b5b;
        --dot-white: #dfe6ec;
    }

    html, body, .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"] {
        background: var(--page-bg) !important;
        background-color: var(--page-bg) !important;
        color: var(--text-dark) !important;
    }

    [data-testid="stHeader"] {
        background: var(--page-bg) !important;
        box-shadow: none !important;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-left: 3.5rem;
        padding-right: 3.5rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }

    h1 {
        color: #000000 !important;
        text-align: center !important;
        font-size: 2.3rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.03em;
        margin-bottom: 0.4rem;
    }

    h2 {
        color: #000000 !important;
        font-size: 1.6rem !important;
        font-weight: 800 !important;
    }

    h3 {
        color: #000000 !important;
        font-size: 1.1rem !important;
        font-weight: 800 !important;
    }

    p, li, label {
        color: #000000 !important;
        font-size: 13px;
    }

    section[data-testid="stSidebar"] {
        background: #17324d !important;
        background-color: #17324d !important;
        border-right: none !important;
        width: 280px !important;
    }

    section[data-testid="stSidebar"] > div,
    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
        background: transparent !important;
    }

    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] .stRadio label {
        font-size: 13px !important;
        padding: 6px 0 !important;
        color: rgba(255,255,255,0.86) !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        border-radius: 8px;
        padding-left: 10px !important;
        padding-right: 10px !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
        background: rgba(255, 255, 255, 0.04) !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] input[type="radio"] {
        accent-color: white !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.13);
    }

    section[data-testid="stFileUploader"] {
        background: var(--card-bg) !important;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid var(--card-border);
        box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
    }

    [data-testid="stFileUploaderDropzone"] {
        background: #fafafa !important;
        border: 1px dashed #d1d7dd !important;
        border-radius: 10px !important;
    }

    [data-testid="stFileUploaderDropzone"] span,
    [data-testid="stFileUploaderDropzone"] button div p {
        color: var(--text-soft) !important;
    }

    [data-testid="stFileUploaderDropzone"] button {
        background: var(--card-bg) !important;
        border: 1px solid #d5dbe1 !important;
        color: var(--text-dark) !important;
        border-radius: 8px !important;
    }

    [data-testid="stFileUploaderDropzone"] svg {
        color: var(--accent) !important;
        fill: var(--accent) !important;
    }

    .stTextInput input {
        background: var(--card-bg) !important;
        color: var(--text-dark) !important;
        font-size: 13px !important;
        padding: 11px 13px !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 10px !important;
    }

    .stTextInput input:focus {
        border: 1px solid var(--accent) !important;
        box-shadow: 0 0 0 2px var(--accent-soft) !important;
    }

    .stTextInput input::placeholder {
        color: #8a9199 !important;
    }

    div[data-testid="metric-container"] {
        background: var(--card-bg) !important;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid var(--card-border);
        box-shadow: none;
    }

    div[data-testid="metric-container"] label {
        color: #000000 !important;
        font-size: 11px !important;
        font-weight: 700;
    }

    div[data-testid="metric-container"] div {
        color: #000000 !important;
        font-size: 22px !important;
        font-weight: 800;
    }

    .stButton button {
        background: linear-gradient(90deg, #B86E4B, #9D563A);
        color: #ffffff !important;
        border: none;
        border-radius: 9px;
        padding: 10px 24px;
        font-weight: 700;
    }

    .stButton button:hover {
        background: linear-gradient(90deg, #C17A55, #A85F40);
        color: white !important;
    }

    .stSuccess {
        background: #edf7ee !important;
        color: #1d5d36 !important;
        border: 1px solid #bfe3c8 !important;
        border-radius: 10px;
    }

    .stWarning {
        background: #fff7e5 !important;
        color: #7a5b16 !important;
        border: 1px solid #f0d98b !important;
        border-radius: 10px;
    }

    .stError {
        background: #fff1f1 !important;
        color: #8d2f2f !important;
        border: 1px solid #f0b8b8 !important;
        border-radius: 10px;
    }

    .stInfo {
        background: #eef5ff !important;
        color: #234d7d !important;
        border: 1px solid #cfe0ff !important;
        border-radius: 10px;
    }

    [data-testid="stCaptionContainer"],
    .stCaption {
        font-size: 12px !important;
        text-align: left !important;
    }

    [data-testid="stAlert"] {
        text-align: left !important;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid var(--card-border);
        border-radius: 10px;
        overflow: hidden;
        background: var(--card-bg) !important;
    }

    hr {
        border: none;
        border-top: 1px solid var(--card-border);
        margin-top: 20px;
        margin-bottom: 20px;
    }

    div[role="radiogroup"] label {
        color: var(--text-dark) !important;
    }

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #ececec;
    }

    ::-webkit-scrollbar-thumb {
        background: #b6bcc3;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #8d98a0;
    }

    header[data-testid="stHeader"] {
        background: var(--page-bg) !important;
    }

    </style>

    """)