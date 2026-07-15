# portfolio_app.py
# Ultra-premium, production-ready Streamlit portfolio for Muhammad Najeeb Brohi.
# Design: Midnight Luxury & Spatial UI with glassmorphism, bento-grid, and premium animations.

import streamlit as st
from datetime import datetime

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Muhammad Najeeb Brohi | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# CUSTOM CSS – Complete Override
# -----------------------------------------------------------------------------
custom_css = """
/* ----- RESET & FONTS ----- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Inter', sans-serif;
    background-color: #0a0a0a; /* Absolute black */
    color: #f0f0f0;
    line-height: 1.6;
    overflow-x: hidden;
}

/* ----- HIDE DEFAULT STREAMLIT ELEMENTS ----- */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
.stApp { background: #0a0a0a; padding: 0 !important; }
.stApp > div:first-child { padding-top: 0 !important; }
[data-testid="stToolbar"] { display: none !important; }

/* ----- CUSTOM SCROLLBAR ----- */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #1a1a1a; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #6c5ce7, #00cec9);
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover { background: #6c5ce7; }

/* ----- FLOATING GLASS NAVBAR ----- */
.navbar {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1000;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 100px;
    padding: 0.7rem 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2.5rem;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
    width: auto;
    max-width: 90%;
}

.navbar a {
    color: rgba(255, 255, 255, 0.7);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
    letter-spacing: 0.5px;
    transition: color 0.3s, transform 0.2s;
    position: relative;
}

.navbar a::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 0;
    height: 2px;
    background: linear-gradient(90deg, #6c5ce7, #00cec9);
    transition: width 0.3s;
}

.navbar a:hover {
    color: #ffffff;
    transform: translateY(-1px);
}
.navbar a:hover::after { width: 100%; }

.navbar .logo {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 1.2rem;
    background: linear-gradient(135deg, #6c5ce7, #00cec9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.navbar .cta-btn {
    background: linear-gradient(135deg, #6c5ce7, #00cec9);
    color: #0a0a0a;
    padding: 0.4rem 1.2rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 0.85rem;
    transition: transform 0.2s, box-shadow 0.2s;
    text-decoration: none;
    -webkit-text-fill-color: #0a0a0a;
    box-shadow: 0 4px 15px rgba(108, 92, 231, 0.3);
}
.navbar .cta-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 30px rgba(108, 92, 231, 0.4);
}

@media (max-width: 768px) {
    .navbar {
        flex-wrap: wrap;
        gap: 0.8rem;
        padding: 0.6rem 1.2rem;
        border-radius: 30px;
        top: 10px;
    }
    .navbar a { font-size: 0.8rem; }
}

/* ----- HERO SECTION ----- */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 6rem 4rem 2rem;
    position: relative;
    z-index: 1;
}

.hero-left {
    flex: 1;
    padding-right: 2rem;
}

.hero-left h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(3rem, 8vw, 5.5rem);
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 0.5rem;
    background: linear-gradient(135deg, #ffffff 30%, #6c5ce7 70%, #00cec9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-left .subtitle {
    font-size: 1.3rem;
    color: rgba(255,255,255,0.6);
    margin: 1rem 0 1.5rem;
    max-width: 600px;
}

.typewriter-container {
    display: inline-block;
    font-size: 1.8rem;
    font-weight: 600;
    color: #00cec9;
    margin-bottom: 1.5rem;
    border-right: 3px solid #6c5ce7;
    white-space: nowrap;
    overflow: hidden;
    animation: typing 3s steps(30) 1s forwards, blink 0.75s step-end infinite;
    width: 0;
    animation-fill-mode: forwards;
}

@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}
@keyframes blink {
    50% { border-color: transparent }
}

.hero .resume-btn {
    display: inline-block;
    padding: 0.8rem 2.5rem;
    border-radius: 50px;
    background: #0a0a0a;
    color: #fff;
    font-weight: 600;
    font-size: 1rem;
    border: 2px solid transparent;
    background-image: linear-gradient(#0a0a0a, #0a0a0a), linear-gradient(135deg, #6c5ce7, #00cec9);
    background-origin: border-box;
    background-clip: padding-box, border-box;
    box-shadow: 0 0 20px rgba(108, 92, 231, 0.2);
    transition: all 0.3s ease;
    text-decoration: none;
    position: relative;
    overflow: hidden;
}
.hero .resume-btn::before {
    content: '';
    position: absolute;
    top: -2px; left: -2px; right: -2px; bottom: -2px;
    background: linear-gradient(135deg, #6c5ce7, #00cec9, #6c5ce7);
    background-size: 400% 400%;
    border-radius: 50px;
    z-index: -1;
    animation: gradientMove 4s ease infinite;
}
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.hero .resume-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 0 40px rgba(108, 92, 231, 0.4);
}

.hero-right {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}

/* 3D Glowing Sphere (AI Nodes) */
.sphere {
    width: 350px;
    height: 350px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #6c5ce7, #00cec9);
    filter: blur(40px);
    opacity: 0.6;
    animation: float 6s ease-in-out infinite alternate;
    position: relative;
}
.sphere::after {
    content: '';
    position: absolute;
    top: -20px; left: -20px; right: -20px; bottom: -20px;
    border-radius: 50%;
    background: radial-gradient(circle at 50% 50%, rgba(108,92,231,0.2), transparent 70%);
    animation: pulseGlow 4s ease-in-out infinite alternate;
}
@keyframes float {
    0% { transform: translate(0, 0) scale(1); }
    100% { transform: translate(20px, -20px) scale(1.1); }
}
@keyframes pulseGlow {
    0% { opacity: 0.3; transform: scale(1); }
    100% { opacity: 0.8; transform: scale(1.3); }
}

@media (max-width: 768px) {
    .hero {
        flex-direction: column;
        text-align: center;
        padding: 6rem 1.5rem 2rem;
    }
    .hero-left { padding-right: 0; }
    .hero-left .subtitle { margin-left: auto; margin-right: auto; }
    .typewriter-container { white-space: normal; border-right: none; animation: none; width: auto; }
    .sphere { width: 250px; height: 250px; margin-top: 2rem; }
}

/* ----- BENTO GRID (Skills) ----- */
.bento-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.bento-item {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 24px;
    padding: 2rem;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s;
    position: relative;
    overflow: hidden;
}

.bento-item:hover {
    transform: translateY(-4px);
    border-color: rgba(108, 92, 231, 0.4);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

.bento-item::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(135deg, rgba(108,92,231,0.1), rgba(0,206,201,0.05));
    opacity: 0;
    transition: opacity 0.4s;
    border-radius: 24px;
    pointer-events: none;
}
.bento-item:hover::after { opacity: 1; }

.bento-item .icon { font-size: 2.5rem; margin-bottom: 0.5rem; }
.bento-item h3 { font-family: 'Space Grotesk', sans-serif; font-size: 1.3rem; margin-bottom: 0.4rem; }
.bento-item p { color: rgba(255,255,255,0.6); font-size: 0.95rem; }
.bento-item .badge {
    display: inline-block;
    background: rgba(108,92,231,0.2);
    color: #6c5ce7;
    padding: 0.2rem 0.8rem;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-top: 0.5rem;
}

@media (max-width: 900px) {
    .bento-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 480px) {
    .bento-grid { grid-template-columns: 1fr; }
}

/* ----- PROJECT CARDS ----- */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.project-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 24px;
    overflow: hidden;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    padding: 0;
    display: flex;
    flex-direction: column;
}

.project-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.6);
    border-color: rgba(108, 92, 231, 0.3);
}

.project-card .card-header {
    padding: 1.5rem 1.5rem 0.5rem;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.project-card .card-header h3 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4rem;
    margin: 0;
}

.project-card .card-header .tag {
    background: rgba(0,206,201,0.2);
    color: #00cec9;
    padding: 0.2rem 0.8rem;
    border-radius: 50px;
    font-size: 0.7rem;
    font-weight: 600;
}

.project-card .card-body {
    padding: 0 1.5rem 1.5rem;
    flex: 1;
}

.project-card .card-body .subtitle {
    color: rgba(255,255,255,0.7);
    font-size: 0.95rem;
    margin-bottom: 0.5rem;
}

.project-card .card-body .tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin: 0.5rem 0;
}

.project-card .card-body .tech span {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    color: rgba(255,255,255,0.7);
    padding: 0.2rem 0.6rem;
    border-radius: 50px;
    font-size: 0.7rem;
}

.project-card .card-body .desc {
    color: rgba(255,255,255,0.6);
    font-size: 0.9rem;
    margin-top: 0.5rem;
}

@media (max-width: 600px) {
    .projects-grid { grid-template-columns: 1fr; }
}

/* ----- TIMELINE ----- */
.timeline-section {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 2rem;
    position: relative;
}

.timeline-line {
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(to bottom, #6c5ce7, #00cec9, #6c5ce7);
    transform: translateX(-50%);
    box-shadow: 0 0 20px rgba(108, 92, 231, 0.3);
}

.timeline-item {
    display: flex;
    justify-content: flex-end;
    padding: 2rem 0;
    position: relative;
    width: 50%;
}

.timeline-item:nth-child(odd) {
    justify-content: flex-start;
    padding-left: 3rem;
    padding-right: 0;
    margin-left: 0;
}

.timeline-item:nth-child(even) {
    justify-content: flex-end;
    padding-right: 3rem;
    padding-left: 0;
    margin-left: 50%;
}

.timeline-item .dot {
    position: absolute;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: #6c5ce7;
    border: 3px solid #0a0a0a;
    top: 2.3rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1;
    box-shadow: 0 0 20px rgba(108, 92, 231, 0.6);
}

.timeline-item .card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    padding: 1.5rem;
    max-width: 350px;
    transition: transform 0.3s, box-shadow 0.3s;
    opacity: 0;
    transform: translateY(20px);
    animation: fadeInUp 0.6s forwards;
}

.timeline-item .card:hover {
    transform: translateY(-5px) scale(1.02);
    border-color: rgba(0, 206, 201, 0.3);
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

@keyframes fadeInUp {
    to { opacity: 1; transform: translateY(0); }
}

.timeline-item:nth-child(1) .card { animation-delay: 0.1s; }
.timeline-item:nth-child(2) .card { animation-delay: 0.2s; }
.timeline-item:nth-child(3) .card { animation-delay: 0.3s; }

.timeline-item .card .year { font-weight: 700; color: #6c5ce7; font-size: 1.1rem; }
.timeline-item .card h4 { font-size: 1.2rem; margin: 0.3rem 0; color: #fff; }
.timeline-item .card p { color: rgba(255,255,255,0.6); font-size: 0.9rem; }

@media (max-width: 768px) {
    .timeline-line { left: 20px; }
    .timeline-item { width: 100%; padding-left: 3rem !important; padding-right: 0 !important; margin-left: 0 !important; justify-content: flex-start !important; }
    .timeline-item .dot { left: 20px !important; }
}

/* ----- CONTACT FOOTER ----- */
.contact-section {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 2rem 3rem;
}

.contact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
}

.contact-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    padding: 1.5rem;
    text-align: center;
    transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
    text-decoration: none;
    color: #f0f0f0;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
}

.contact-card:hover {
    transform: translateY(-4px);
    border-color: rgba(108, 92, 231, 0.4);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

.contact-card .icon {
    font-size: 2rem;
}
.contact-card .label {
    font-weight: 600;
    font-size: 1rem;
}
.contact-card .value {
    color: rgba(255,255,255,0.6);
    font-size: 0.9rem;
}

.footer-bottom {
    text-align: center;
    padding: 1.5rem 0;
    border-top: 1px solid rgba(255,255,255,0.05);
    color: rgba(255,255,255,0.3);
    font-size: 0.8rem;
    margin-top: 2rem;
}

/* ----- UTILITIES ----- */
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.5rem, 6vw, 4rem);
    text-align: center;
    margin-bottom: 3rem;
    background: linear-gradient(135deg, #fff 30%, #6c5ce7 70%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.container { max-width: 1200px; margin: 0 auto; }
.section-padding { padding: 5rem 0; }
"""

# Inject CSS
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# FLOATING NAVBAR (HTML)
# -----------------------------------------------------------------------------
navbar_html = """
<nav class="navbar">
    <span class="logo">✦ NB</span>
    <a href="#home">Home</a>
    <a href="#skills">Skills</a>
    <a href="#experience">Experience</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
    <a href="#home" class="cta-btn">Resume</a>
</nav>
"""
st.markdown(navbar_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HERO SECTION (Using columns)
# -----------------------------------------------------------------------------
# We'll use st.columns to create left/right layout, but inject custom HTML inside.
# Left column: text; Right column: 3D sphere.
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("""
    <div class="hero-left">
        <h1>Muhammad Najeeb Brohi</h1>
        <div class="typewriter-container">Python Developer & Automation Specialist</div>
        <p class="subtitle">
            Certified Python Programmer with a passion for core logic, workflow automation,
            and generative AI. Building intelligent systems that simplify complexity.
        </p>
        <a href="#" class="resume-btn">Download Resume →</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="hero-right">
        <div class="sphere"></div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SKILLS (BENTO GRID) SECTION
# -----------------------------------------------------------------------------
st.markdown("""
<section id="skills" class="section-padding">
    <div class="container">
        <h2 class="section-title">Core Expertise</h2>
        <div class="bento-grid">
            <div class="bento-item">
                <div class="icon">🐍</div>
                <h3>Python & Logic</h3>
                <p>Gexton Certified Python Developer with strong command over core Python, CLI tools, and workflow automations.</p>
                <span class="badge">Certified</span>
            </div>
            <div class="bento-item">
                <div class="icon">🤖</div>
                <h3>AI & Machine Learning</h3>
                <p>Foundations in ML, Deep Learning, LangChain, OpenAI APIs, and FAISS vector search. Building intelligent applications.</p>
                <span class="badge">In Progress</span>
            </div>
            <div class="bento-item">
                <div class="icon">🛠️</div>
                <h3>Dev Tools & Databases</h3>
                <p>SQLite, Git/GitHub, Streamlit, REST APIs, and modern development workflows.</p>
                <span class="badge">Proficient</span>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# EXPERIENCE & ACADEMIC TIMELINE
# -----------------------------------------------------------------------------
st.markdown("""
<section id="experience" class="section-padding">
    <div class="container">
        <h2 class="section-title">Journey & Education</h2>
        <div class="timeline-section">
            <div class="timeline-line"></div>
            <div class="timeline-item">
                <div class="dot"></div>
                <div class="card">
                    <div class="year">2026 – Present</div>
                    <h4>Specialization in Generative AI, ML & Automation</h4>
                    <p>Studying foundational ML/DL algorithms, neural networks, and building intelligent automation workflows using LLMs.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="dot"></div>
                <div class="card">
                    <div class="year">2025 – Early 2026</div>
                    <h4>Professional Certification in Python Programming</h4>
                    <p>Intensive hands-on training at Gexton Institute of Technology covering Python core, data structures, and advanced problem-solving.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="dot"></div>
                <div class="card">
                    <div class="year">2025</div>
                    <h4>Intermediate (Pre-Medical)</h4>
                    <p>Govt. Boys Higher Secondary School Garelo, Larkana. Completed 1st year.</p>
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PROJECTS SHOWCASE
# -----------------------------------------------------------------------------
projects_html = """
<section id="projects" class="section-padding">
    <div class="container">
        <h2 class="section-title">Featured Projects</h2>
        <div class="projects-grid">
            <div class="project-card">
                <div class="card-header">
                    <h3>Lumina AI</h3>
                    <span class="tag">Generative AI</span>
                </div>
                <div class="card-body">
                    <div class="subtitle">Streamlit + Glassmorphic AI Platform</div>
                    <div class="tech">
                        <span>LangChain</span>
                        <span>OpenAI</span>
                        <span>FAISS</span>
                        <span>SQLite</span>
                    </div>
                    <div class="desc">Advanced Retrieval-Augmented Generation (RAG) platform with seamless vector search and conversational memory.</div>
                </div>
            </div>
            <div class="project-card">
                <div class="card-header">
                    <h3>AI-Powered AMS</h3>
                    <span class="tag">Advanced Systems</span>
                </div>
                <div class="card-body">
                    <div class="subtitle">Futuristic School Analytics & Portal</div>
                    <div class="tech">
                        <span>Streamlit</span>
                        <span>SQLite</span>
                        <span>ML Classifiers</span>
                    </div>
                    <div class="desc">Attendance Management with AI Mood Check-In, Predictive Risk Assessment, Performance Advisor, and offline caching.</div>
                </div>
            </div>
            <div class="project-card">
                <div class="card-header">
                    <h3>Task Automation & File Organizer</h3>
                    <span class="tag">Automation</span>
                </div>
                <div class="card-body">
                    <div class="subtitle">Daily Workflow Optimizer</div>
                    <div class="tech">
                        <span>Python</span>
                        <span>OS Library</span>
                        <span>Custom Scripts</span>
                    </div>
                    <div class="desc">Automated file management, secure backup routines, and web scraping pipelines to eliminate repetitive manual tasks.</div>
                </div>
            </div>
        </div>
    </div>
</section>
"""
st.markdown(projects_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CONTACT FOOTER
# -----------------------------------------------------------------------------
st.markdown("""
<section id="contact" class="section-padding">
    <div class="container">
        <h2 class="section-title">Let's Connect</h2>
        <div class="contact-section">
            <div class="contact-grid">
                <a href="mailto:brohinajeeb10@gmail.com" class="contact-card">
                    <div class="icon">✉️</div>
                    <div class="label">Email</div>
                    <div class="value">brohinajeeb10@gmail.com</div>
                </a>
                <a href="tel:+923471115737" class="contact-card">
                    <div class="icon">📞</div>
                    <div class="label">Phone</div>
                    <div class="value">0347 1115737</div>
                </a>
                <a href="https://www.google.com/maps/place/Qasimabad,+Hyderabad" target="_blank" class="contact-card">
                    <div class="icon">📍</div>
                    <div class="label">Location</div>
                    <div class="value">Qasimabad, Hyderabad, Pakistan</div>
                </a>
                <a href="https://github.com/mnajeeb-4/" target="_blank" class="contact-card">
                    <div class="icon">🐙</div>
                    <div class="label">GitHub</div>
                    <div class="value">@mnajeeb-4</div>
                </a>
                <a href="https://www.linkedin.com/in/najeeb-brohi-07883939b/" target="_blank" class="contact-card">
                    <div class="icon">🔗</div>
                    <div class="label">LinkedIn</div>
                    <div class="value">najeeb-brohi</div>
                </a>
            </div>
            <div class="footer-bottom">
                &copy; 2026 Muhammad Najeeb Brohi. Built with Streamlit & ✦.
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SMOOTH SCROLLING JAVASCRIPT (for anchor links)
# -----------------------------------------------------------------------------
smooth_js = """
<script>
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});
</script>
"""
st.markdown(smooth_js, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# END OF SCRIPT
# -----------------------------------------------------------------------------
