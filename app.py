"""
DNA-DRL Steganography - Project Documentation Portal
Single-file Streamlit application (M.Tech research project).

HOW TO EDIT CONTENT
-------------------
All editable content is in the CONFIG block directly below:
  * TEAM_DEFAULTS  -> student / guide details
  * PROGRESS       -> change a task's status to "completed", "ongoing" or "pending"
  * DOCUMENTS      -> document categories
  * GITHUB_URL     -> repository link
  * VIDEOS         -> YouTube video slots (paste URLs in "url")
  * METRICS        -> fill "value" only after real results are available
Team details, GitHub URL and video links can also be edited live from the
website itself (expanders marked "Edit ...") for the current session.
"""


import re
from html import escape

import streamlit as st

st.set_page_config(
    page_title="DNA-DRL Steganography | M.Tech Project",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# CONFIG - EDIT THIS BLOCK
# =============================================================================
PROJECT = {
    "short_title": "DNA-DRL Steganography",
    "title": "Intelligent Adaptive DNA Encoding Using Deep Reinforcement Learning for Secure Image Steganography",
    "subtitle": "Secure Image Steganography Using Deep Reinforcement Learning",
    "description": "A Content-Adaptive Approach Combining DNA Encoding, PPO-Based Decision-Making and Adaptive LSB Embedding.",
    "domain": "Network Systems and Security",
    "institution": "Amrita School of Computing, Amrita Vishwa Vidyapeetham, Coimbatore, Tamil Nadu",
    "programme": "M.Tech Computer Science and Engineering",
}

TEAM_DEFAULTS = {
    "student_name": "Nandhana Subhekshanan",
    "student_programme": "M.Tech Computer Science and Engineering",
    "student_department": "Computer Science and Engineering",
    "student_institution": "Amrita School of Computing, Amrita Vishwa Vidyapeetham, Coimbatore, Tamil Nadu",
    "guide_name": "Dr. Malathi P",
    "guide_designation": "Assistant Professor (Sr. Gd.)",
    "guide_department": "Amrita School of Computing",
    "guide_institution": "Amrita Vishwa Vidyapeetham, Coimbatore, Tamil Nadu",
}

# Status must be one of: "completed", "ongoing", "pending"
PROGRESS = [
    ("Literature survey and identification of research gaps.", "completed"),
    ("Selection of proposed DNA encoding and reinforcement learning approach.", "completed"),
    ("Dataset preparation and image preprocessing.", "completed"),
    ("Cover-image block division.", "completed"),
    ("Implementation of image feature extraction.", "completed"),
    ("DNA encoding and decoding components.", "completed"),
    ("Development of PPO-based reinforcement learning environment.", "completed"),
    ("Initial PPO training and testing.", "completed"),
    ("Development of embedding and extraction prototype.", "completed"),
    ("Initial image-quality and extraction experiments.", "completed"),
    ("Refinement of PPO reward design and adaptive embedding decisions.", "ongoing"),
    ("Evaluation of LSB depth selection and block-level behaviour.", "ongoing"),
    ("Improvement and verification of extraction pipeline.", "ongoing"),
    ("Comparative evaluation with conventional steganography techniques.", "ongoing"),
    ("Evaluation under Gaussian and salt-and-pepper noise.", "ongoing"),
    ("Independent receiver validation.", "ongoing"),
    ("Steganalysis-based security evaluation.", "pending"),
    ("Final performance analysis and result interpretation.", "pending"),
    ("Research paper finalisation.", "pending"),
    ("Final project demonstration and documentation.", "pending"),
]

DOCUMENTS = [
    ("Project Abstract", "Concise summary of the problem, approach and expected outcomes."),
    ("Problem Statement and Objectives", "Formal problem definition and the project objectives."),
    ("Literature Survey", "Review of existing steganography, DNA encoding and reinforcement learning work."),
    ("Proposed Methodology", "Detailed description of the proposed DNA-DRL framework."),
    ("System Architecture Diagram", "Architecture and workflow diagram of the complete system."),
    ("Implementation Documentation", "Implementation notes for the preprocessing, PPO, encoding and extraction modules."),
    ("Experimental Results and Analysis", "Experimental setup, metrics and analysis of results."),
    ("Research Paper", "Research paper (draft or final version)."),
    ("Final Project Report", "Complete M.Tech project report."),
]

GITHUB_URL = "https://github.com/NandhanaSubhekshanan/Intelligent-Adaptive-DNA-Steganography"  # <- replace


# Leave "value" as None until real, verified results exist. Do NOT enter dummy values.
METRICS = [
    {"name": "MSE", "desc": "Mean Squared Error between the cover image and the stego image.", "value": None},
    {"name": "PSNR", "desc": "Peak Signal-to-Noise Ratio, measuring stego-image visual quality.", "value": None},
    {"name": "SSIM", "desc": "Structural Similarity Index between cover and stego images.", "value": None},
    {"name": "BER", "desc": "Bit Error Rate between the original and the extracted secret data.", "value": None},
    {"name": "Exact Recovery Rate", "desc": "Rate at which the secret image is recovered exactly.", "value": None},
    {"name": "Embedding Capacity", "desc": "Amount of secret data that can be embedded in the cover image.", "value": None},
    {"name": "Noise-Based Extraction Performance", "desc": "Extraction behaviour under Gaussian and salt-and-pepper noise.", "value": None},
]

# =============================================================================
# STATIC CONTENT
# =============================================================================
SECTIONS = [  # (number, title, icon, short description)
    ("01", "Project Overview", "🔬", "What the project is about and its key technical choices."),
    ("02", "Project Objectives", "🎯", "Eight objectives and the expected outcomes."),
    ("03", "Problem Statement", "⚠️", "Limitations of conventional LSB steganography."),
    ("04", "Methodology", "🧬", "Architecture, eight stages and evaluation metrics."),
    ("05", "Team Details", "👥", "Student researcher, guide and project details."),
    ("06", "Project Progress", "📈", "Completed, ongoing and pending work."),
    ("07", "GitHub", "💻", "Source repository."),
]
HOME = "🏠 Home"


def page_label(s):
    return f"{s[0]} · {s[1]}"


PAGES = [HOME] + [page_label(s) for s in SECTIONS]

FLOW = [
    "Cover Image", "Preprocessing", "Block Division", "Feature Extraction",
    "PPO Agent", "DNA Encoding", "Adaptive LSB Embedding", "Stego Image",
]

STAGES = [
    ("Cover Image Preprocessing", "Preparation of the cover image before block-wise processing.", []),
    ("Block Division", "The cover image is divided into 8 × 8 pixel blocks.", []),
    ("Feature Extraction", "Content features are extracted from each image block.",
     ["Variance", "Shannon Entropy", "Canny Edge Density", "GLCM Contrast"]),
    ("PPO Agent", "The Proximal Policy Optimization agent makes embedding decisions from the extracted block features.",
     ["DNA encoding rule selection", "LSB depth selection", "Pixel location selection", "Embedding decision"]),
    ("DNA Encoding", "Secret image data is converted into a DNA-based representation.",
     ["Binary representation", "DNA mapping", "A, C, G and T nucleotides"]),
    ("Adaptive LSB Embedding", "DNA-encoded secret data is embedded using the LSB depth and pixel locations selected by the PPO agent.", []),
    ("Stego Image Generation", "The stego image carrying the hidden secret image is generated.", []),
    ("Secret Image Extraction", "The hidden secret image is recovered from the stego image using the corresponding extraction mechanism.", []),
]

OBJECTIVES = [
    "Develop a secure image steganography framework using DNA-based encoding.",
    "Integrate Deep Reinforcement Learning using PPO for intelligent embedding decisions.",
    "Extract image-block features such as variance, entropy, edge density and GLCM contrast for content-aware processing.",
    "Investigate adaptive LSB embedding based on image characteristics and payload requirements.",
    "Maintain a balance between embedding capacity and stego-image visual quality.",
    "Develop a corresponding extraction mechanism for recovering the hidden secret image.",
    "Evaluate the proposed framework using image-quality metrics, extraction accuracy, payload capacity and noise experiments.",
    "Compare the proposed approach with conventional steganography techniques.",
]

STATUS = {  # key: (heading, marker, colour)
    "completed": ("Completed Work", "✓", "#34D399"),
    "ongoing": ("Ongoing Work", "◐", "#FBBF24"),
    "pending": ("Pending Work", "○", "#94A3B8"),
}

# =============================================================================
# STYLING
# =============================================================================
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root{--navy:#0A192F;--panel:#0F2240;--line:#1E3A5F;--cyan:#22D3EE;--white:#F8FAFC;--text:#CBD5E1;--muted:#8CA0B8;--field:#0B1D38;}
.stApp{background:var(--navy);}
header[data-testid="stHeader"]{background:transparent;}
#MainMenu, .stDeployButton{display:none;}
.block-container{max-width:1180px;padding-top:2.2rem;padding-bottom:3rem;}
.stApp, .stApp p, .stApp li, .stApp label, .stApp [data-testid="stWidgetLabel"] p, .stApp [data-testid="stCaptionContainer"]{color:var(--text) !important;font-family:'Inter',sans-serif;}
.stApp h1,.stApp h2,.stApp h3,.stApp h4{color:var(--white) !important;font-family:'Space Grotesk','Inter',sans-serif;}
[data-testid="stSidebar"]{background:#071324;border-right:1px solid var(--line);}
[data-testid="stSidebar"] div[role="radiogroup"] label{padding:8px 10px;border-radius:8px;}
[data-testid="stSidebar"] div[role="radiogroup"] label:hover{background:#0F2240;}
.stApp input, .stApp textarea{background:var(--field) !important;color:var(--white) !important;border-color:var(--line) !important;}
.stApp [data-baseweb="input"], .stApp [data-baseweb="base-input"]{background:var(--field) !important;border-color:var(--line) !important;}
.stApp [data-testid="stExpander"]{background:var(--panel);border:1px solid var(--line);border-radius:12px;}
.stApp [data-testid="stExpander"] summary p{color:var(--white) !important;font-weight:600;}
.stApp [data-testid="stFileUploaderDropzone"]{background:var(--field);border:1px dashed var(--line);}
.stApp .stButton button, .stApp .stDownloadButton button, .stApp [data-testid="stLinkButton"] a, .stApp a[data-testid^="stBaseLinkButton"]{background:transparent !important;border:1px solid var(--cyan) !important;color:var(--cyan) !important;border-radius:10px;font-weight:600;}
.stApp .stButton button:hover, .stApp .stDownloadButton button:hover, .stApp [data-testid="stLinkButton"] a:hover, .stApp a[data-testid^="stBaseLinkButton"]:hover{background:var(--cyan) !important;color:var(--navy) !important;}
.stApp button p, .stApp a p{color:inherit !important;}
.stApp [data-testid="stLinkButton"] a[disabled], .stApp button:disabled{opacity:.4;}
.hero{padding:44px 40px;border:1px solid var(--line);border-radius:18px;background:linear-gradient(135deg,#102a4f 0%,#0A192F 70%);position:relative;overflow:hidden;margin-bottom:22px;}
.hero:before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--cyan);}
.eyebrow{color:var(--cyan);letter-spacing:.18em;font-size:.78rem;font-weight:600;text-transform:uppercase;}
.hero-title{font-family:'Space Grotesk',sans-serif;font-size:clamp(2rem,5vw,3.4rem);font-weight:700;color:var(--white);letter-spacing:.03em;line-height:1.1;margin:10px 0 10px;}
.hero-sub{font-size:clamp(1rem,2vw,1.3rem);color:#E2E8F0;font-weight:500;max-width:860px;line-height:1.45;}
.hero-desc{color:var(--muted);margin-top:14px;max-width:860px;line-height:1.6;}
.sec-head{display:flex;align-items:center;gap:16px;margin:4px 0 6px;}
.sec-num{font-family:'Space Grotesk',sans-serif;color:var(--cyan);border:1px solid var(--cyan);border-radius:10px;padding:6px 12px;font-weight:700;}
.sec-title{font-family:'Space Grotesk',sans-serif;font-size:clamp(1.6rem,3.5vw,2.3rem);font-weight:700;color:var(--white);}
.sec-tag{color:var(--muted);margin:0 0 22px;padding-bottom:18px;border-bottom:1px solid var(--line);}
.sub{font-family:'Space Grotesk',sans-serif;font-size:1.2rem;font-weight:600;color:var(--white);margin:30px 0 12px;border-left:3px solid var(--cyan);padding-left:12px;}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(var(--min,260px),1fr));gap:16px;margin:12px 0 8px;}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px 20px;height:100%;box-sizing:border-box;}
.card-icon{font-size:1.4rem;margin-bottom:6px;}
.card-title{color:var(--white);font-weight:600;font-family:'Space Grotesk',sans-serif;font-size:1.05rem;margin-bottom:6px;}
.card-body{color:var(--text);font-size:.95rem;line-height:1.6;}
.card-body ul{margin:6px 0 0 18px;padding:0;}
.prose div{margin-bottom:14px;line-height:1.75;color:var(--text);}
.kv{margin-bottom:12px;}
.kv-label{color:var(--cyan);font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;font-weight:600;}
.kv-value{color:var(--white);font-weight:500;margin-top:3px;}
.ph{color:#FBBF24;font-style:italic;}
.chip{display:inline-block;padding:4px 12px;margin:3px 4px 3px 0;border:1px solid var(--line);border-radius:999px;font-size:.82rem;color:var(--text);background:var(--field);}
.chip.cy{border-color:var(--cyan);color:var(--cyan);}
.step-num{font-family:'Space Grotesk',sans-serif;color:var(--cyan);font-weight:700;font-size:.78rem;letter-spacing:.14em;margin-bottom:4px;}
.flow{display:flex;flex-wrap:wrap;align-items:stretch;gap:8px;margin:12px 0 8px;}
.node{flex:1 1 100px;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 8px;text-align:center;color:var(--white);font-weight:600;font-size:.86rem;}
.node.hl{border-color:var(--cyan);color:var(--cyan);}
.node small{display:block;color:var(--muted);font-weight:500;font-size:.68rem;margin-bottom:4px;}
.arrow{align-self:center;color:var(--cyan);font-weight:700;}
.badge{display:inline-block;padding:3px 10px;border-radius:999px;font-size:.72rem;font-weight:600;}
.b-ok{background:rgba(52,211,153,.12);color:#34D399;border:1px solid rgba(52,211,153,.4);}
.b-wait{background:rgba(148,163,184,.1);color:#94A3B8;border:1px solid rgba(148,163,184,.35);}
.status-col{background:var(--panel);border:1px solid var(--line);border-top:3px solid var(--c);border-radius:14px;padding:18px 20px;}
.status-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;color:var(--white);font-family:'Space Grotesk',sans-serif;font-weight:600;font-size:1.05rem;}
.status-count{color:var(--c);font-weight:700;}
.task{display:flex;gap:10px;padding:9px 0;border-bottom:1px solid var(--line);color:var(--text);font-size:.92rem;line-height:1.5;}
.task:last-child{border-bottom:none;}
.dot{color:var(--c);font-weight:700;min-width:16px;}
.metric-val{font-family:'Space Grotesk',sans-serif;font-size:1.15rem;color:var(--muted);margin-top:10px;}
.metric-val.set{color:var(--cyan);}
.note{border:1px solid var(--line);border-left:3px solid var(--cyan);background:var(--field);border-radius:10px;padding:12px 16px;color:var(--text);font-size:.92rem;margin:10px 0;line-height:1.55;}
.doc-head{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin-top:14px;}
.video-ph{aspect-ratio:16/9;border:1px dashed var(--line);border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--muted);background:var(--field);text-align:center;padding:10px;}
.brand{display:flex;align-items:center;gap:12px;padding:6px 4px 14px;}
.brand-mark{font-size:1.8rem;}
.brand-name{font-family:'Space Grotesk',sans-serif;color:var(--white);font-weight:700;letter-spacing:.04em;line-height:1.1;}
.brand-sub{color:var(--cyan);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;}
.side-info{color:var(--muted);font-size:.78rem;line-height:1.6;border-top:1px solid var(--line);padding-top:12px;margin-top:14px;}
.footer{margin-top:56px;padding:22px 0 8px;border-top:1px solid var(--line);text-align:center;color:var(--muted);font-size:.85rem;line-height:1.7;}
.footer b{color:var(--white);}
@media (max-width:760px){.flow{flex-direction:column;}.arrow{transform:rotate(90deg);}.hero{padding:28px 22px;}}
</style>
"""

# =============================================================================
# HELPERS
# =============================================================================


def render(markup):
    """Render HTML safely (strip indentation so Markdown never treats it as code)."""
    st.markdown("\n".join(l.strip() for l in markup.splitlines() if l.strip()), unsafe_allow_html=True)


def esc(x):
    return escape(str(x))


def card(title, body="", icon="", extra=""):
    parts = ['<div class="card">']
    if icon:
        parts.append('<div class="card-icon">' + icon + "</div>")
    parts.append('<div class="card-title">' + esc(title) + "</div>")
    if body:
        parts.append('<div class="card-body">' + esc(body) + "</div>")
    parts.append(extra)
    parts.append("</div>")
    return "".join(parts)


def grid(cards, min_w=260):
    return '<div class="grid" style="--min:' + str(min_w) + 'px">' + "".join(cards) + "</div>"


def bullets(items):
    return '<div class="card-body"><ul>' + "".join("<li>" + esc(i) + "</li>" for i in items) + "</ul></div>"


def chips(items, cyan=False):
    cls = "chip cy" if cyan else "chip"
    return "".join('<span class="' + cls + '">' + esc(i) + "</span>" for i in items)


def kv(label, value):
    placeholder = str(value).strip().startswith("[")
    cls = "kv-value ph" if placeholder else "kv-value"
    shown = value if str(value).strip() else "—"
    return ('<div class="kv"><div class="kv-label">' + esc(label) + '</div><div class="' + cls + '">'
            + esc(shown) + "</div></div>")


def sec_head(num, title, tagline):
    render('<div class="sec-head"><span class="sec-num">' + esc(num) + '</span><span class="sec-title">'
           + esc(title) + '</span></div><div class="sec-tag">' + esc(tagline) + "</div>")


def sub(title):
    render('<div class="sub">' + esc(title) + "</div>")


def note(text):
    render('<div class="note">' + esc(text) + "</div>")


def go(page):
    """Navigation callback used by the Home page buttons."""
    st.session_state.page = page


def init_state():
    ss = st.session_state
    ss.setdefault("page", HOME)
    if "store" not in ss:
        store = dict(TEAM_DEFAULTS)
        store["github_url"] = GITHUB_URL
        ss.store = store
    ss.setdefault("docs", {})
    ss.setdefault("up_ver", {})


def editable(field, label, placeholder=""):
    """Text input whose value survives page changes (kept in session store)."""
    key = "w_" + field

    def _save():
        st.session_state.store[field] = st.session_state[key]

    st.text_input(label, value=st.session_state.store.get(field, ""), key=key,
                  on_change=_save, placeholder=placeholder)


YT_RE = re.compile(r"(?:youtube\.com/(?:watch\?(?:.*&)?v=|embed/|shorts/|live/)|youtu\.be/)([A-Za-z0-9_-]{11})")


def youtube_id(url):
    m = YT_RE.search((url or "").strip())
    return m.group(1) if m else None


def valid_http_url(url):
    return bool(re.match(r"^https?://[^\s/$.?#].[^\s]*$", (url or "").strip()))




# =============================================================================
# PAGES
# =============================================================================


def page_home():
    render(
        '<div class="hero"><div class="eyebrow">M.Tech Research Project · ' + esc(PROJECT["domain"]) + "</div>"
        '<div class="hero-title">DNA-DRL STEGANOGRAPHY</div>'
        '<div class="hero-sub">' + esc(PROJECT["title"]) + "</div>"
        '<div class="hero-desc">' + esc(PROJECT["description"]) + "</div></div>"
    )
    render(
        '<div class="card"><div class="card-title">Introduction</div><div class="card-body">'
        "This portal documents an M.Tech research project on an intelligent image steganography framework that "
        "securely hides a secret image within a cover image. DNA-based encoding is combined with a Proximal Policy "
        "Optimization (PPO) agent that makes block-wise embedding decisions, including the DNA encoding rule and the "
        "number of least significant bits used for embedding, based on the characteristics of each image block. "
        "The project is in progress; this portal reports completed, ongoing and pending work as it stands."
        "</div><div style='margin-top:12px'>"
        + chips(["Deep Reinforcement Learning", "PPO", "DNA Encoding", "Adaptive LSB", "Image Steganography"], cyan=True)
        + "</div></div>"
    )
    render(grid([
        card("", "").replace('<div class="card-title"></div>', kv("Domain", PROJECT["domain"])),
        card("", "").replace('<div class="card-title"></div>', kv("Programme", PROJECT["programme"])),
        card("", "").replace('<div class="card-title"></div>', kv("Institution", PROJECT["institution"])),
    ], 240))
    sub("Explore the Portal")
    for row in (SECTIONS[:4], SECTIONS[4:]):
        cols = st.columns(4)
        for col, s in zip(cols, row):
            with col:
                render(card(s[0] + " · " + s[1], s[3], icon=s[2]))
                st.button("Open section →", key="open_" + s[0], on_click=go, args=(page_label(s),))
        st.write("")


def page_overview():
    sec_head("01", "Project Overview", "About the project, its technical approach and key information.")
    sub("About the Project")
    render(
        '<div class="card"><div class="prose">'
        "<div>The project focuses on developing an intelligent image steganography framework that securely hides "
        "secret image data within a cover image.</div>"
        "<div>The proposed approach combines DNA-based encoding techniques with Proximal Policy Optimization (PPO), "
        "a reinforcement learning algorithm, to make embedding decisions based on image-block characteristics.</div>"
        "<div>The cover image is divided into smaller blocks, and important features such as variance, entropy, edge "
        "density and GLCM contrast are extracted.</div>"
        "<div>The PPO agent uses these features to make embedding decisions, including the selection of DNA encoding "
        "rules and the number of least significant bits (LSBs) used for embedding.</div>"
        "<div>The objective is to develop a content-adaptive framework that balances embedding capacity, visual "
        "quality and reliable secret image extraction.</div></div></div>"
    )
    sub("Project Information")
    info = [
        ("Project Domain", "Network Systems and Security", "🌐"),
        ("Research Areas", "Deep Learning, Reinforcement Learning and Image Steganography", "🧠"),
        ("Proposed Algorithm", "PPO-based adaptive embedding", "🤖"),
        ("Encoding Technique", "DNA Encoding", "🧬"),
        ("Embedding Technique", "Adaptive Least Significant Bit (LSB)", "🖼️"),
        ("Implementation", "Python", "🐍"),
    ]
    render(grid([card("", icon=i, extra=kv(k, v)).replace('<div class="card-title"></div>', "") for k, v, i in info], 280))


def page_objectives():
    sec_head("02", "Project Objectives", "Eight objectives guiding the design, implementation and evaluation.")
    cards = []
    for n, text in enumerate(OBJECTIVES, 1):
        cards.append(card("", extra='<div class="step-num">OBJECTIVE ' + "%02d" % n + '</div><div class="card-body">'
                          + esc(text) + "</div>").replace('<div class="card-title"></div>', ""))
    render(grid(cards, 320))
    sub("Expected Outcomes")
    outcomes = [
        "Functional image steganography framework.",
        "Intelligent block-wise embedding decisions.",
        "DNA-based secret data representation.",
        "Reliable secret image extraction.",
        "Quantitative evaluation of image quality and embedding performance.",
    ]
    render('<div class="card">' + bullets(outcomes) + "</div>")


def page_problem():
    sec_head("03", "Problem Statement", "Why fixed, content-unaware embedding is not enough.")
    sub("Problem Statement")
    render(
        '<div class="card"><div class="prose">'
        "<div>Confidential visual information must often be transmitted over open networks, which creates a need for "
        "secure transmission that conceals not only the content of the data but also the existence of the "
        "communication. Image steganography addresses this need by hiding secret data inside a cover image so that "
        "the resulting stego image appears unchanged to an observer.</div>"
        "<div>Traditional LSB steganography replaces the least significant bits of pixel values with secret data. "
        "Most such approaches rely on fixed embedding strategies, using the same embedding depth and a predetermined "
        "pixel order across the entire image. They do not consider the characteristics of local image regions, "
        "although smooth and textured regions respond very differently to modification.</div>"
        "<div>As a result, image distortion becomes more noticeable at higher embedding capacities, and the "
        "statistical traces left in the stego image make it vulnerable to statistical detection. A content-adaptive "
        "approach that decides where and how deeply to embed, based on local image characteristics and payload "
        "requirements, is therefore required.</div></div></div>"
    )
    sub("Key Limitations of Conventional Approaches")
    limits = [
        ("Secure Transmission Need", "Confidential visual information requires concealment during transmission.", "🔐"),
        ("Traditional LSB Steganography", "Simple replacement of least significant bits with secret data.", "🧩"),
        ("Fixed Embedding Strategies", "The same embedding approach is applied regardless of image content.", "📏"),
        ("No Local Region Awareness", "Local image-region characteristics are not taken into account.", "🗺️"),
        ("Distortion at Higher Capacity", "Image distortion increases as the embedding capacity grows.", "📉"),
        ("Statistical Detectability", "Vulnerability to statistical detection of the hidden data.", "🕵️"),
    ]
    render(grid([card(t, b, icon=i) for t, b, i in limits], 280))
    sub("Research Challenges")
    challenges = [
        "Maintaining visual quality while embedding secret information.",
        "Selecting suitable image regions for data embedding.",
        "Adapting embedding depth according to payload requirements.",
        "Achieving reliable secret image extraction.",
        "Evaluating the effect of noise on recovered information.",
    ]
    render('<div class="card">' + bullets(challenges) + "</div>")


def page_methodology():
    sec_head("04", "Methodology", "Proposed architecture, processing stages and evaluation metrics.")
    sub("Proposed Architecture")
    parts = []
    for i, name in enumerate(FLOW):
        cls = "node hl" if name in ("PPO Agent", "DNA Encoding", "Adaptive LSB Embedding") else "node"
        parts.append('<div class="' + cls + '"><small>STEP ' + str(i + 1) + "</small>" + esc(name) + "</div>")
        if i < len(FLOW) - 1:
            parts.append('<div class="arrow">→</div>')
    render('<div class="flow">' + "".join(parts) + "</div>")
    st.caption("Secret Image Extraction (Stage 8) recovers the hidden secret image from the stego image.")

    sub("Methodology Stages")
    cards = []
    for n, (title, desc, items) in enumerate(STAGES, 1):
        extra = '<div class="step-num">STAGE ' + "%02d" % n + "</div>"
        body = '<div class="card-title">' + esc(title) + '</div><div class="card-body">' + esc(desc) + "</div>"
        if items:
            body += bullets(items)
        cards.append('<div class="card">' + extra + body + "</div>")
    render(grid(cards, 330))

    sub("System Evaluation")
    cards = []
    for m in METRICS:
        has = m["value"] not in (None, "")
        val = ('<div class="metric-val set">' + esc(m["value"]) + "</div>") if has else ""
        cards.append(card(m["name"], m["desc"], extra=val))
    render(grid(cards, 250))
    


def page_team():
    sec_head("05", "Team Details", "Student researcher, project guide and project information.")
    s = st.session_state.store
    student = card("Student Researcher", icon="🎓", extra=(
        kv("Name", s["student_name"]) + kv("Programme", s["student_programme"])
        + kv("Department", s["student_department"]) + kv("Institution", s["student_institution"])))
    guide = card("Project Guide", icon="🧑‍🏫", extra=(
        kv("Name", s["guide_name"]) + kv("Designation", s["guide_designation"])
        + kv("Department", s["guide_department"]) + kv("Institution", s["guide_institution"])))
    render(grid([student, guide], 320))
    sub("Project Details")
    details = card("Project Information", icon="📘", extra=(
        kv("Degree", "Master of Technology") + kv("Research Area", PROJECT["domain"])
        + kv("Project Title", PROJECT["title"])))
    render(details)

    


def page_progress():
    sec_head("06", "Project Progress", "Current status of the project, grouped by completed, ongoing and pending work.")
    groups = {k: [] for k in STATUS}
    for task, status in PROGRESS:
        key = status.strip().lower() if isinstance(status, str) else "pending"
        groups[key if key in STATUS else "pending"].append(task)
    total = sum(len(v) for v in groups.values())

    render(grid([card(STATUS[k][0], extra='<div class="metric-val set" style="color:' + STATUS[k][2] + '">'
                      + str(len(groups[k])) + " of " + str(total) + " tasks</div>") for k in STATUS], 200))
    cols = st.columns(3)
    for col, k in zip(cols, STATUS):
        heading, marker, colour = STATUS[k]
        with col:
            if groups[k]:
                tasks = "".join('<div class="task"><span class="dot">' + marker + "</span><span>" + esc(t) + "</span></div>"
                                for t in groups[k])
            else:
                tasks = '<div class="task">No tasks in this category.</div>'
            render('<div class="status-col" style="--c:' + colour + '"><div class="status-head"><span>'
                   + esc(heading) + '</span><span class="status-count">' + str(len(groups[k])) + "</span></div>"
                   + tasks + "</div>")
    st.write("")
    





def video_card(i, v):
    store = st.session_state.store
    url = str(store.get("video_%d" % i, "")).strip()
    render('<div class="card"><div class="card-title">🎬 ' + esc(v["title"]) + '</div><div class="card-body">'
           + esc(v["description"]) + "</div></div>")
    vid = youtube_id(url)
    if vid:
        try:
            st.video("https://www.youtube.com/watch?v=" + vid)
        except Exception:  # noqa: BLE001
            note("The video could not be embedded. Open it directly: " + url)
    elif url:
        render('<div class="video-ph"><div style="font-size:1.6rem">⚠️</div>Invalid YouTube link.<br>'
               "Please check the URL.</div>")
    else:
        render('<div class="video-ph"><div style="font-size:1.8rem">▶</div>Video not available yet</div>')
    with st.expander("Edit video link"):
        editable("video_%d" % i, "YouTube URL", "https://www.youtube.com/watch?v=...")


def page_github():
    sec_head("07", "GitHub", "Source code repository for the project implementation.")
    sub("GitHub Repository")
    render(card(
        "DNA-DRL Image Steganography Repository",
        "The repository contains the implementation of the DNA-DRL image steganography framework, including "
        "preprocessing, feature extraction, DNA encoding, PPO-based embedding, extraction and evaluation modules.",
        icon="💻",
        extra="<div style='margin-top:12px'>" + chips(
            ["Preprocessing", "Feature Extraction", "DNA Encoding", "PPO-Based Embedding", "Extraction", "Evaluation"],
            cyan=True) + "</div>"))
    st.write("")
    url = str(st.session_state.store.get("github_url", "")).strip()
    is_set = valid_http_url(url) and "your-username" not in url
    if is_set:
        st.link_button("Open GitHub Repository ↗", url)
        st.caption(url)
    else:
        st.link_button("Open GitHub Repository ↗", "https://github.com", disabled=True)
        note("Repository link not set yet.")
   

def footer():
    render('<div class="footer"><b>' + esc(PROJECT["title"]) + "</b><br>" + esc(PROJECT["programme"]) + " · "
           + esc(PROJECT["institution"]) + "</div>")

# =============================================================================
# MAIN
# =============================================================================


def main():
    init_state()
    render(CSS)

    with st.sidebar:
        render('<div class="brand"><div class="brand-mark">🧬</div><div><div class="brand-name">DNA-DRL</div>'
               '<div class="brand-sub">Steganography</div></div></div>')
        st.radio("Navigate", PAGES, key="page", label_visibility="collapsed")
        render('<div class="side-info">' + esc(PROJECT["subtitle"]) + "<br>" + esc(PROJECT["domain"]) + "<br>"
               + esc(PROJECT["institution"]) + "</div>")

    routes = {
        HOME: page_home,
        page_label(SECTIONS[0]): page_overview,
        page_label(SECTIONS[1]): page_objectives,
        page_label(SECTIONS[2]): page_problem,
        page_label(SECTIONS[3]): page_methodology,
        page_label(SECTIONS[4]): page_team,
        page_label(SECTIONS[5]): page_progress,
        page_label(SECTIONS[6]): page_github,
    }

    try:
        routes.get(st.session_state.page, page_home)()
    except Exception as exc:  # noqa: BLE001
        st.error("Something went wrong while loading this section: " + str(exc))
    footer()


main()
