# portfolio_app.py
# Hyper-modern, Apple-inspired, ultra-premium Streamlit portfolio.
# Design: Cyber-Luxury & Spatial UI with Bento Box layout.

import streamlit as st
from datetime import datetime

# -----------------------------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Cyber-Luxury Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# CUSTOM CSS – FULL OVERRIDE
# -----------------------------------------------------------------------------
custom_css = """
/* ----- RESET & FONTS ----- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }

body {
    font-family: 'Inter', sans-serif;
    background-color: #0a0a0a;
    color: #f0f0f0;
    line-height: 1.6;
    overflow-x: hidden;
}

/* ----- HIDE STREAMLIT DEFAULTS ----- */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
.stApp { background: #0a0a0a; padding: 0 !important; }
.stApp > div:first-child { padding-top: 0 !important; }
[data-testid="stToolbar"] { display: none !important; }

/* ----- CUSTOM SCROLLBAR ----- */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #1a1a1a; }
::-webkit-scrollbar-thumb { background: linear-gradient(135deg, #6c5ce7, #00cec9); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: #6c5ce7; }

/* ----- AMBIENT GLOW ORB ANIMATION ----- */
.orb {
    position: fixed;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(108, 92, 231, 0.3), rgba(0, 206, 201, 0.1));
    filter: blur(80px);
    top: -100px;
    right: -100px;
    z-index: -1;
    animation: orbFloat 12s ease-in-out infinite alternate;
}
.orb2 {
    position: fixed;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(253, 121, 168, 0.2), rgba(0, 206, 201, 0.05));
    filter: blur(60px);
    bottom: -50px;
    left: -50px;
    z-index: -1;
    animation: orbFloat2 15s ease-in-out infinite alternate;
}
@keyframes orbFloat {
    0% { transform: translate(0, 0) scale(1); }
    100% { transform: translate(-100px, 100px) scale(1.2); }
}
@keyframes orbFloat2 {
    0% { transform: translate(0, 0) scale(1); }
    100% { transform: translate(80px, -80px) scale(1.3); }
}

/* ----- FLOATING ISLAND HEADER ----- */
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
    justify-content: center;
    flex-direction: column;
    text-align: center;
    padding: 6rem 2rem 2rem;
    position: relative;
    z-index: 1;
}

.hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(3.5rem, 12vw, 7rem);
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 0.3rem;
    background: linear-gradient(135deg, #ffffff 30%, #6c5ce7 70%, #00cec9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero .subtitle {
    font-size: 1.3rem;
    color: rgba(255,255,255,0.6);
    max-width: 650px;
    margin: 1rem auto 2rem;
}

.hero .typewriter {
    display: inline-block;
    overflow: hidden;
    white-space: nowrap;
    border-right: 3px solid #6c5ce7;
    animation: typing 2.5s steps(30) 1s forwards, blink 0.75s step-end infinite;
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

/* ----- BENTO BOX CORE (Skills & About) ----- */
.bento-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
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

/* Sizing for bento */
.bento-item.span-2 { grid-column: span 2; }
.bento-item.span-3 { grid-column: span 3; }
.bento-item.span-row-2 { grid-row: span 2; }

@media (max-width: 900px) {
    .bento-grid { grid-template-columns: repeat(2, 1fr); }
    .bento-item.span-2 { grid-column: span 2; }
    .bento-item.span-3 { grid-column: span 2; }
}
@media (max-width: 480px) {
    .bento-grid { grid-template-columns: 1fr; }
    .bento-item.span-2, .bento-item.span-3 { grid-column: 1; }
}

/* ----- PARALLAX EXPERIENCE TIMELINE ----- */
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
    transition: transform 0.3s, opacity 0.5s, box-shadow 0.3s;
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

/* ----- CINEMA-GRADE PROJECT SHOWCASE ----- */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}
.project-card {
    position: relative;
    border-radius: 24px;
    overflow: hidden;
    background: #1a1a1a;
    cursor: pointer;
    aspect-ratio: 16 / 10;
    transition: transform 0.4s ease, box-shadow 0.4s;
}
.project-card:hover {
    transform: scale(1.02);
    box-shadow: 0 20px 40px rgba(0,0,0,0.7);
}
.project-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
}
.project-card:hover img {
    transform: scale(1.08);
}
.project-card .overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 2rem 1.5rem;
    background: linear-gradient(to top, rgba(10,10,10,0.9), transparent);
    opacity: 0;
    transition: opacity 0.4s ease;
}
.project-card:hover .overlay {
    opacity: 1;
}
.project-card .overlay h3 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4rem;
    margin-bottom: 0.3rem;
}
.project-card .overlay p {
    color: rgba(255,255,255,0.7);
    font-size: 0.9rem;
}
.project-card .overlay .tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 0.5rem 0;
}
.project-card .overlay .tags span {
    background: rgba(108,92,231,0.3);
    color: #fff;
    padding: 0.2rem 0.8rem;
    border-radius: 50px;
    font-size: 0.7rem;
    font-weight: 500;
}
.project-card .overlay .links {
    display: flex;
    gap: 1rem;
    margin-top: 0.8rem;
}
.project-card .overlay .links a {
    color: #fff;
    text-decoration: none;
    font-size: 0.9rem;
    background: rgba(255,255,255,0.1);
    padding: 0.3rem 1rem;
    border-radius: 50px;
    transition: background 0.3s;
}
.project-card .overlay .links a:hover {
    background: #6c5ce7;
}

@media (max-width: 600px) {
    .projects-grid { grid-template-columns: 1fr; }
    .project-card { aspect-ratio: auto; height: 250px; }
}

/* ----- MAGNETIC FOOTER & CONTACT ----- */
.footer-section {
    max-width: 600px;
    margin: 0 auto;
    padding: 4rem 2rem 2rem;
    text-align: center;
}
.footer-section h2 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}
.footer-section p {
    color: rgba(255,255,255,0.6);
    margin-bottom: 2rem;
}
.footer-section .email-form {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}
.footer-section .email-form input {
    flex: 1;
    min-width: 200px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 50px;
    padding: 0.8rem 1.5rem;
    color: #fff;
    font-size: 1rem;
    outline: none;
    transition: border-color 0.3s, box-shadow 0.3s;
}
.footer-section .email-form input:focus {
    border-color: #6c5ce7;
    box-shadow: 0 0 0 3px rgba(108,92,231,0.2);
}
.footer-section .email-form button {
    background: linear-gradient(135deg, #6c5ce7, #00cec9);
    border: none;
    border-radius: 50px;
    padding: 0.8rem 2rem;
    color: #0a0a0a;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 4px 15px rgba(108,92,231,0.3);
}
.footer-section .email-form button:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 30px rgba(108,92,231,0.4);
}
.footer-section .social-icons {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 2.5rem;
}
.footer-section .social-icons a {
    color: rgba(255,255,255,0.6);
    font-size: 1.8rem;
    transition: color 0.3s, transform 0.3s;
    display: inline-block;
}
.footer-section .social-icons a:hover {
    color: #6c5ce7;
    transform: translateY(-3px) scale(1.1);
}
.footer-bottom {
    text-align: center;
    padding: 1.5rem 0;
    border-top: 1px solid rgba(255,255,255,0.05);
    color: rgba(255,255,255,0.3);
    font-size: 0.8rem;
    margin-top: 3rem;
}

/* ----- UTILITY ----- */
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

/* ----- RESPONSIVE FINAL TOUCHES ----- */
@media (max-width: 480px) {
    .hero h1 { font-size: 2.5rem; }
    .hero .typewriter { white-space: normal; border-right: none; animation: none; width: auto; }
    .navbar { width: 95%; padding: 0.5rem 1rem; gap: 0.5rem; }
}
"""

st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# AMBIENT ORBS (Background)
# -----------------------------------------------------------------------------
st.markdown("""
<div class="orb"></div>
<div class="orb2"></div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# NAVBAR (Floating Island)
# -----------------------------------------------------------------------------
navbar_html = """
<nav class="navbar">
    <span class="logo">✦ CYBER</span>
    <a href="#hero">Home</a>
    <a href="#bento">About</a>
    <a href="#timeline">Experience</a>
    <a href="#projects">Work</a>
    <a href="#footer">Contact</a>
    <a href="#hero" class="cta-btn">Resume</a>
</nav>
"""
st.markdown(navbar_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HERO SECTION
# -----------------------------------------------------------------------------
hero_html = """
<section id="hero" class="hero">
    <h1>
        <span class="typewriter">Designing the Future</span>
    </h1>
    <p class="subtitle">
        I'm a Full-Stack Architect & UI/UX Designer — crafting digital experiences with
        spatial aesthetics and luxury minimalism.
    </p>
    <a href="#projects" class="resume-btn">Explore My Work →</a>
</section>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# BENTO BOX (Skills & About)
# We'll use pure HTML grid; no st.columns because we want full control.
# -----------------------------------------------------------------------------
bento_html = """
<section id="bento" class="section-padding">
    <div class="container">
        <h2 class="section-title">About & Skills</h2>
        <div class="bento-grid">
            <div class="bento-item span-2">
                <div class="icon">🧠</div>
                <h3>AI & Machine Learning</h3>
                <p>Building intelligent systems with TensorFlow, PyTorch, and custom models.</p>
            </div>
            <div class="bento-item">
                <div class="icon">⚡</div>
                <h3>Full-Stack</h3>
                <p>Python, React, Node.js, and cloud-native architectures.</p>
            </div>
            <div class="bento-item span-row-2">
                <div class="icon">🎨</div>
                <h3>UI/UX Design</h3>
                <p>Human-centered design, prototyping, and design systems.</p>
            </div>
            <div class="bento-item">
                <div class="icon">🚀</div>
                <h3>DevOps</h3>
                <p>Docker, Kubernetes, CI/CD pipelines.</p>
            </div>
            <div class="bento-item span-2">
                <div class="icon">📊</div>
                <h3>Data Analytics</h3>
                <p>Big data processing, visualization, and insights.</p>
            </div>
            <div class="bento-item">
                <div class="icon">🔒</div>
                <h3>Cybersecurity</h3>
                <p>Secure coding, penetration testing, and compliance.</p>
            </div>
        </div>
    </div>
</section>
"""
st.markdown(bento_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PARALLAX EXPERIENCE TIMELINE
# -----------------------------------------------------------------------------
timeline_html = """
<section id="timeline" class="section-padding">
    <div class="container">
        <h2 class="section-title">Experience</h2>
        <div class="timeline-section">
            <div class="timeline-line"></div>
            <div class="timeline-item">
                <div class="dot"></div>
                <div class="card">
                    <div class="year">2023 – Present</div>
                    <h4>Lead Architect</h4>
                    <p>TechCorp Inc. – Leading a team of 10, designing microservices and cloud infrastructure.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="dot"></div>
                <div class="card">
                    <div class="year">2020 – 2023</div>
                    <h4>Senior Developer</h4>
                    <p>Innovate Solutions – Full-stack development for fintech platforms.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="dot"></div>
                <div class="card">
                    <div class="year">2018 – 2020</div>
                    <h4>UI/UX Designer</h4>
                    <p>Design Studio – Crafted award-winning interfaces for global clients.</p>
                </div>
            </div>
        </div>
    </div>
</section>
"""
st.markdown(timeline_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PROJECT SHOWCASE
# -----------------------------------------------------------------------------
projects_html = """
<section id="projects" class="section-padding">
    <div class="container">
        <h2 class="section-title">Featured Work</h2>
        <div class="projects-grid">
            <div class="project-card">
                <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&h=500&fit=crop" alt="Project 1">
                <div class="overlay">
                    <h3>AI Dashboard</h3>
                    <p>Real-time analytics with predictive insights.</p>
                    <div class="tags">
                        <span>React</span>
                        <span>Python</span>
                        <span>TensorFlow</span>
                    </div>
                    <div class="links">
                        <a href="#">Live Demo</a>
                        <a href="#">GitHub</a>
                    </div>
                </div>
            </div>
            <div class="project-card">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=500&fit=crop" alt="Project 2">
                <div class="overlay">
                    <h3>E-Commerce Platform</h3>
                    <p>Scalable online store with microservices.</p>
                    <div class="tags">
                        <span>Node.js</span>
                        <span>React</span>
                        <span>MongoDB</span>
                    </div>
                    <div class="links">
                        <a href="#">Live Demo</a>
                        <a href="#">GitHub</a>
                    </div>
                </div>
            </div>
            <div class="project-card">
                <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=800&h=500&fit=crop" alt="Project 3">
                <div class="overlay">
                    <h3>Design System</h3>
                    <p>Comprehensive component library with dark/light mode.</p>
                    <div class="tags">
                        <span>Figma</span>
                        <span>CSS</span>
                        <span>Storybook</span>
                    </div>
                    <div class="links">
                        <a href="#">Live Demo</a>
                        <a href="#">GitHub</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""
st.markdown(projects_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MAGNETIC FOOTER & CONTACT (with Streamlit form for email)
# -----------------------------------------------------------------------------
st.markdown("""
<section id="footer" class="section-padding">
    <div class="container">
        <div class="footer-section">
            <h2>Let's Connect</h2>
            <p>Drop your email and I'll reach out within 24 hours.</p>
""", unsafe_allow_html=True)

# We'll embed a Streamlit form inside the HTML for backend processing.
with st.form("contact_form", clear_on_submit=True):
    col1, col2 = st.columns([3, 1])
    with col1:
        email = st.text_input("Email", placeholder="you@example.com", label_visibility="collapsed")
    with col2:
        submitted = st.form_submit_button("Send →", use_container_width=True)
    if submitted and email:
        st.success("Thanks! I'll get back to you soon.")

st.markdown("""
            <div class="social-icons">
                <a href="#" aria-label="GitHub">🐙</a>
                <a href="#" aria-label="LinkedIn">🔗</a>
                <a href="#" aria-label="Twitter">🐦</a>
                <a href="#" aria-label="Dribbble">🏀</a>
            </div>
            <div class="footer-bottom">
                &copy; 2026 Cyber-Luxury Portfolio. Crafted with Streamlit.
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SMOOTH SCROLLING JAVASCRIPT
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
# END
# -----------------------------------------------------------------------------
