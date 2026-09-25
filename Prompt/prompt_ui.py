


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()


st.set_page_config(
    page_title="Research Assistant",
    page_icon="◆",
    layout="wide",
)


st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

<style>
:root {
    --cyan: #2dd4f0;
    --violet: #b088ff;
    --pink: #ff6fb0;
    --text: #f6f6f9;
    --muted: #a3a3b0;
    --glass: rgba(255,255,255,0.075);
    --glass-strong: rgba(255,255,255,0.1);
    --glass-border: rgba(255,255,255,0.16);
}

#MainMenu, footer {visibility: hidden;}
* { font-family: 'Inter', sans-serif; }

header[data-testid="stHeader"] { background: transparent; }
header[data-testid="stHeader"] * { color: var(--text) !important; fill: var(--text) !important; }

.stApp { background: #08080b; }
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    background:
        radial-gradient(circle at 10% 10%, rgba(45,212,240,0.38), transparent 42%),
        radial-gradient(circle at 90% 15%, rgba(176,136,255,0.42), transparent 46%),
        radial-gradient(circle at 30% 95%, rgba(255,111,176,0.24), transparent 42%),
        radial-gradient(circle at 80% 85%, rgba(45,212,240,0.18), transparent 40%),
        #08080b;
    filter: blur(70px);
    pointer-events: none;
}

.block-container { padding-top: 2.2rem; max-width: 980px; position: relative; z-index: 1; }

/* ---------- Masthead ---------- */
.masthead {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.1rem 1.7rem;
    border-radius: 16px;
    margin-bottom: 1.2rem;
    background: var(--glass-strong);
    border: 1px solid var(--glass-border);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow: 0 4px 30px rgba(0,0,0,0.3);
}
.masthead .brand {
    font-family: 'Sora', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    letter-spacing: -0.01em;
    background: linear-gradient(90deg, var(--cyan), var(--violet) 60%, var(--pink));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.masthead .tag { color: var(--muted); font-size: 0.82rem; }

/* ---------- Top toolbar (replaces sidebar) ---------- */
.toolbar-wrap {
    background: var(--glass);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 1.3rem 1.6rem 0.4rem 1.6rem;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    margin-bottom: 1.6rem;
}
label p {
    color: var(--muted) !important;
    font-weight: 700 !important;
    font-size: 0.72rem !important;
    text-transform: uppercase;
    letter-spacing: 0.07em;
}
div[data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
    border: 1px solid var(--glass-border) !important;
    color: var(--text) !important;
}
div[data-baseweb="select"] svg { fill: var(--muted) !important; }
ul[role="listbox"] { background: #16161d !important; border: 1px solid var(--glass-border) !important; }

div.stButton > button {
    padding: 0.65rem 1.6rem;
    border-radius: 10px;
    border: 1px solid var(--glass-border);
    font-weight: 700;
    font-size: 0.9rem;
    color: var(--text);
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    transition: 0.25s ease;
}
div.stButton > button:hover {
    border-color: transparent;
    background: linear-gradient(90deg, var(--cyan), var(--violet));
    color: #08080b;
    box-shadow: 0 0 26px rgba(45,212,240,0.4), 0 0 26px rgba(176,136,255,0.3);
}
div.stDownloadButton > button {
    background: transparent;
    border: 1px solid var(--glass-border);
    color: var(--muted);
    border-radius: 10px;
    font-size: 0.82rem;
}
div.stDownloadButton > button:hover { border-color: var(--cyan); color: var(--text); }

/* ---------- Meta chips ---------- */
.meta-row { display: flex; gap: 0.5rem; flex-wrap: wrap; margin: 0 0 1.4rem 0; }
.chip {
    font-size: 0.76rem;
    color: var(--muted);
    border: 1px solid var(--glass-border);
    padding: 0.3rem 0.75rem;
    border-radius: 999px;
    background: var(--glass);
}
.chip b { color: var(--text); font-weight: 700; }
.chip.c-cyan { border-color: rgba(45,212,240,0.45); }
.chip.c-violet { border-color: rgba(176,136,255,0.45); }
.chip.c-pink { border-color: rgba(255,111,176,0.45); }

/* ---------- Glass article panel ---------- */
.article {
    background: var(--glass-strong);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 2.4rem 2.8rem 2.8rem 2.8rem;
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    box-shadow: 0 8px 40px rgba(0,0,0,0.4);
}
.article .eyebrow {
    font-size: 0.76rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    background: linear-gradient(90deg, var(--cyan), var(--violet));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}
.article h1 {
    font-family: 'Sora', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.7rem !important;
    color: var(--text) !important;
    margin-bottom: 1.1rem !important;
}
.article p { font-size: 1.03rem; line-height: 1.85; color: #dcdce3; }
.article strong { color: #fff; }
.article code {
    background: rgba(255,255,255,0.1);
    padding: 0.15rem 0.4rem;
    border-radius: 5px;
    color: var(--cyan);
}
.article pre {
    border: 1px solid var(--glass-border) !important;
    border-radius: 12px !important;
}

/* ---------- Empty state ---------- */
.empty-state {
    border: 1px dashed var(--glass-border);
    border-radius: 20px;
    padding: 4rem 2rem;
    text-align: center;
    color: var(--muted);
    background: var(--glass);
    backdrop-filter: blur(18px);
}
.empty-state .glyph {
    font-size: 2rem;
    background: linear-gradient(90deg, var(--cyan), var(--violet));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.6rem;
}
.empty-state p { font-size: 0.92rem; max-width: 380px; margin: 0.3rem auto 0 auto; }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="masthead">
    <div class="brand">◆ Research Assistant</div>
    <div class="tag">Research, made legible</div>
</div>
""", unsafe_allow_html=True)


model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")


st.markdown('<div class="toolbar-wrap">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns([2.2, 1.4, 1.4, 1])

with c1:
    paper_input = st.selectbox(
        "Paper",
        [
          "Attention Is All You Need",
            "BERT: Pre-training of Deep Bidirectional Transformers",
            "GPT-3: Language Models are Few-Shot Learners",
            "Diffusion Models Beat GANs on Image Synthesis",
            "ResNet: Deep Residual Learning for Image Recognition",
            "Generative Adversarial Networks (GANs)",
            "Denoising Diffusion Probabilistic Models (DDPM)",
            "Vision Transformer (ViT): An Image is Worth 16x16 Words",
            "AlphaFold: Highly Accurate Protein Structure Prediction",
            "InstructGPT: Training Language Models to Follow Instructions",
            "LoRA: Low-Rank Adaptation of Large Language Models",
            "Chain-of-Thought Prompting Elicits Reasoning in LLMs",
            "RAG: Retrieval-Augmented Generation for Knowledge-Intensive NLP",
            "CLIP: Learning Transferable Visual Models from Natural Language",
            "Word2Vec: Efficient Estimation of Word Representations",
            "AlexNet: ImageNet Classification with Deep CNNs",
            "Adam: A Method for Stochastic Optimization",
            "Dropout: A Simple Way to Prevent Overfitting",
            "Batch Normalization: Accelerating Deep Network Training",
            "PPO: Proximal Policy Optimization Algorithms",
        ]
    )
with c2:
    style_input = st.selectbox(
        "Style",
        ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
    )
with c3:
    length_input = st.selectbox(
        "Length",
        ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"],
    )
with c4:
    st.markdown("<div style='height:1.62rem'></div>", unsafe_allow_html=True)
    generate = st.button("Generate")

st.markdown('</div>', unsafe_allow_html=True)


st.markdown(
    f"""
    <div class="meta-row">
        <div class="chip c-cyan">Paper &nbsp;<b>{paper_input.split(':')[0]}</b></div>
        <div class="chip c-violet">Style &nbsp;<b>{style_input}</b></div>
        <div class="chip c-pink">Length &nbsp;<b>{length_input.split(' (')[0]}</b></div>
    </div>
    """,
    unsafe_allow_html=True,
)


if "summary" not in st.session_state:
    st.session_state.summary = None

if generate:
    template = load_prompt("template.json")
    chain = template | model

    with st.spinner("Reading the paper..."):
        result = chain.invoke(
            {
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input,
            }
        )

    content = result.content
    if isinstance(content, list):
        text_out = "".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in content
        )
    else:
        text_out = content

    st.session_state.summary = text_out
    st.session_state.summary_meta = (paper_input, style_input, length_input)

if st.session_state.summary:
    paper_shown, style_shown, _ = st.session_state.summary_meta


    header_html = (
        f'<div class="eyebrow">{style_shown} explanation</div>'
        f'<h1>{paper_shown}</h1>'
    )
    article_html = f'<div class="article">{header_html}\n\n{st.session_state.summary}</div>'
    st.markdown(article_html, unsafe_allow_html=True)

    st.write("")
    st.download_button(
        "Download as text",
        data=st.session_state.summary,
        file_name=f"{paper_shown[:30].strip()}.txt",
        mime="text/plain",
    )
else:
    st.markdown("""
    <div class="empty-state">
        <div class="glyph">◆</div>
        <p>Pick a paper and a style above, then hit Generate.
        The summary will appear here as a clean, readable article.</p>
    </div>
    """, unsafe_allow_html=True)
