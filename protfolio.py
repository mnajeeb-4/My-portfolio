# portfolio_app.py
# Ultra-premium Portfolio GUI using Streamlit + Custom HTML/CSS
# Design philosophy: Modern + Classic Professional

import streamlit as st
from datetime import datetime

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Elite Portfolio | Your Name",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# CUSTOM CSS INJECTION (Tailwind-style + bespoke)
# -----------------------------------------------------------------------------
custom_css = """
/* ----- GLOBAL RESET & FONTS ----- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Playfair+Display:wght@400;700&family=Montserrat:wght@400;600&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', sans-serif;
    background-color: #0f172a;   /* Midnight slate */
    color: #f8fafc;
    line-height: 1.6;
    overflow-x: hidden;
}

/* ----- HIDE DEFAULT STREAMLIT ELEMENTS ----- */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
.stApp { background: #0f172a; }

/* ----- SCROLLBAR CUSTOMIZATION ----- */
::-webkit-scrollbar {
    width: 10px;
}
::-webkit-scrollbar-track {
    background: #1e293b;
}
::-webkit-scrollbar-thumb {
    background: #fbbf24;  /* gold accent */
    border-radius: 5px;
}
::-webkit-scrollbar-thumb:hover {
    background: #f59e0b;
}

/* ----- GLASSMORPHISM NAVBAR ----- */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    padding: 1rem 2rem;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.3s ease;
}

.navbar .logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    font-weight: 700;
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.5px;
}

.navbar .nav-links {
    display: flex;
    gap: 2rem;
    list-style: none;
}

.navbar .nav-links a {
    color: #cbd5e1;
    text-decoration: none;
    font-size: 0.95rem;
    font-weight: 500;
    transition: color 0.3s;
    position: relative;
}

.navbar .nav-links a::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 0;
    height: 2px;
    background: #fbbf24;
    transition: width 0.3s ease;
}

.navbar .nav-links a:hover {
    color: #f8fafc;
}

.navbar .nav-links a:hover::after {
    width: 100%;
}

.navbar .nav-links a.active {
    color: #fbbf24;
}

/* Responsive navbar */
@media (max-width: 768px) {
    .navbar {
        flex-direction: column;
        padding: 0.8rem 1rem;
    }
    .navbar .nav-links {
        flex-wrap: wrap;
        justify-content: center;
        gap: 1rem;
        margin-top: 0.5rem;
    }
}

/* ----- HERO SECTION ----- */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 6rem 2rem 4rem;
    background: radial-gradient(ellipse at 30% 50%, rgba(34, 211, 238, 0.05) 0%, transparent 60%),
                radial-gradient(ellipse at 70% 80%, rgba(251, 191, 36, 0.05) 0%, transparent 50%);
    text-align: center;
}

.hero-content {
    max-width: 900px;
}

.hero .greeting {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.2rem;
    color: #22d3ee;  /* neon-cyan */
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 10vw, 5.5rem);
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 0.5rem;
}

.hero .typewriter {
    display: inline-block;
    overflow: hidden;
    white-space: nowrap;
    border-right: 3px solid #fbbf24;
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

.hero .subtitle {
    font-size: 1.2rem;
    color: #94a3b8;
    max-width: 600px;
    margin: 1.5rem auto;
}

.hero .cta-btn {
    display: inline-block;
    padding: 0.9rem 2.5rem;
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    color: #0f172a;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 4px 15px rgba(251, 191, 36, 0.3);
    text-decoration: none;
}

.hero .cta-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(251, 191, 36, 0.4);
}

/* Responsive hero */
@media (max-width: 480px) {
    .hero .typewriter {
        white-space: normal;
        border-right: none;
        animation: none;
        width: auto;
        display: block;
    }
    .hero h1 {
        font-size: 2.5rem;
    }
}

/* ----- EXPERTISE GRID (3D Hover Cards) ----- */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 5vw, 3rem);
    text-align: center;
    margin-bottom: 3rem;
    position: relative;
}

.section-title::after {
    content: '';
    display: block;
    width: 80px;
    height: 3px;
    background: linear-gradient(90deg, #fbbf24, #22d3ee);
    margin: 0.5rem auto 0;
}

.expertise-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    padding: 0 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.expertise-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    padding: 2rem 1.5rem;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    perspective: 1000px;
    transform-style: preserve-3d;
}

.expertise-card:hover {
    transform: rotateY(5deg) rotateX(5deg) scale(1.03);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    border-color: rgba(251, 191, 36, 0.3);
}

.expertise-card .icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    display: block;
}

.expertise-card h3 {
    font-size: 1.3rem;
    margin-bottom: 0.5rem;
    color: #f8fafc;
}

.expertise-card p {
    font-size: 0.95rem;
    color: #94a3b8;
}

/* ----- EXPERIENCE TIMELINE ----- */
.timeline {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 2rem;
    position: relative;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(to bottom, #fbbf24, #22d3ee, #34d399);
    transform: translateX(-50%);
}

.timeline-item {
    display: flex;
    justify-content: flex-end;
    padding: 1.5rem 0;
    position: relative;
    width: 50%;
}

.timeline-item:nth-child(odd) {
    justify-content: flex-start;
    padding-left: 3rem;
    padding-right: 0;
    align-self: flex-start;
    margin-left: 0;
}

.timeline-item:nth-child(even) {
    justify-content: flex-end;
    padding-right: 3rem;
    padding-left: 0;
    align-self: flex-end;
    margin-left: 50%;
}

.timeline-item .dot {
    position: absolute;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #fbbf24;
    border: 3px solid #0f172a;
    top: 2rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1;
}

.timeline-item:nth-child(odd) .dot {
    left: calc(50% - 7px);
}

.timeline-item:nth-child(even) .dot {
    left: calc(50% - 7px);
}

.timeline-item .content {
    background: rgba(255, 255, 255, 0.04);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    padding: 1.5rem;
    max-width: 350px;
    transition: transform 0.3s;
}

.timeline-item .content:hover {
    transform: scale(1.02);
    border-color: rgba(34, 211, 238, 0.3);
}

.timeline-item .content .year {
    font-weight: 700;
    color: #22d3ee;
    font-size: 1.1rem;
}

.timeline-item .content h4 {
    font-size: 1.2rem;
    margin: 0.3rem 0;
    color: #f8fafc;
}

.timeline-item .content p {
    font-size: 0.9rem;
    color: #94a3b8;
}

/* Responsive timeline */
@media (max-width: 768px) {
    .timeline::before {
        left: 20px;
    }
    .timeline-item {
        width: 100%;
        padding-left: 3rem !important;
        padding-right: 0 !important;
        justify-content: flex-start !important;
        margin-left: 0 !important;
    }
    .timeline-item .dot {
        left: 20px !important;
        transform: translateX(-50%);
    }
    .timeline-item:nth-child(odd) .dot,
    .timeline-item:nth-child(even) .dot {
        left: 20px !important;
    }
}

/* ----- PROJECTS SHOWCASE ----- */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding: 0 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.project-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.project-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
    border-color: rgba(251, 191, 36, 0.2);
}

.project-card .img-wrapper {
    width: 100%;
    height: 200px;
    overflow: hidden;
    background: #1e293b;
    position: relative;
}

.project-card .img-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.project-card:hover .img-wrapper img {
    transform: scale(1.05);
}

.project-card .body {
    padding: 1.5rem;
}

.project-card .body h3 {
    font-size: 1.3rem;
    margin-bottom: 0.5rem;
    color: #f8fafc;
}

.project-card .body p {
    font-size: 0.95rem;
    color: #94a3b8;
    margin-bottom: 1rem;
}

.project-card .tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.project-card .tags span {
    background: rgba(34, 211, 238, 0.15);
    color: #22d3ee;
    padding: 0.2rem 0.8rem;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 500;
}

.project-card .links {
    display: flex;
    gap: 1rem;
}

.project-card .links a {
    color: #94a3b8;
    text-decoration: none;
    transition: color 0.3s;
    font-size: 0.9rem;
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
}

.project-card .links a:hover {
    color: #fbbf24;
}

/* ----- CONTACT SECTION ----- */
.contact-section {
    max-width: 600px;
    margin: 0 auto;
    padding: 0 2rem 3rem;
}

.contact-section form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.contact-section .form-group {
    display: flex;
    flex-direction: column;
}

.contact-section label {
    font-weight: 500;
    color: #94a3b8;
    margin-bottom: 0.3rem;
}

.contact-section input,
.contact-section textarea {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 0.9rem 1.2rem;
    color: #f8fafc;
    font-size: 1rem;
    transition: border-color 0.3s, box-shadow 0.3s;
    outline: none;
    font-family: inherit;
}

.contact-section input:focus,
.contact-section textarea:focus {
    border-color: #fbbf24;
    box-shadow: 0 0 0 3px rgba(251, 191, 36, 0.1);
}

.contact-section textarea {
    min-height: 120px;
    resize: vertical;
}

.contact-section .submit-btn {
    padding: 0.9rem 2rem;
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
    color: #0f172a;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 4px 15px rgba(251, 191, 36, 0.2);
    align-self: flex-start;
}

.contact-section .submit-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(251, 191, 36, 0.3);
}

.contact-section .social-icons {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 2rem;
}

.contact-section .social-icons a {
    color: #94a3b8;
    font-size: 1.6rem;
    transition: color 0.3s, transform 0.3s;
    display: inline-block;
}

.contact-section .social-icons a:hover {
    color: #fbbf24;
    transform: translateY(-3px);
}

/* ----- FOOTER ----- */
.footer {
    text-align: center;
    padding: 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    color: #64748b;
    font-size: 0.9rem;
}

/* ----- UTILITY CLASSES ----- */
.section-padding {
    padding: 4rem 0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}

.glow-gold {
    color: #fbbf24;
    text-shadow: 0 0 20px rgba(251, 191, 36, 0.3);
}

.glow-cyan {
    color: #22d3ee;
    text-shadow: 0 0 20px rgba(34, 211, 238, 0.3);
}

/* ----- RESPONSIVE TWEAKS ----- */
@media (max-width: 480px) {
    .expertise-grid {
        grid-template-columns: 1fr;
    }
    .projects-grid {
        grid-template-columns: 1fr;
    }
}
"""

# -----------------------------------------------------------------------------
# INJECT CSS
# -----------------------------------------------------------------------------
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# NAVBAR (HTML)
# -----------------------------------------------------------------------------
navbar_html = """
<nav class="navbar">
    <div class="logo">✦ Portfolio</div>
    <ul class="nav-links">
        <li><a href="#hero">Home</a></li>
        <li><a href="#expertise">Expertise</a></li>
        <li><a href="#experience">Experience</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
</nav>
"""
st.markdown(navbar_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HERO SECTION
# -----------------------------------------------------------------------------
hero_html = """
<section id="hero" class="hero">
    <div class="hero-content">
        <div class="greeting">✦ Welcome</div>
        <h1>
            <span class="typewriter">I'm John Doe</span>
        </h1>
        <p class="subtitle">
            Senior Full-Stack Developer & UI/UX Architect — crafting digital experiences
            that blend modern aesthetics with executive-level sophistication.
        </p>
        <a href="#projects" class="cta-btn">View My Work →</a>
    </div>
</section>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# EXPERTISE SECTION
# -----------------------------------------------------------------------------
expertise_html = """
<section id="expertise" class="section-padding">
    <div class="container">
        <h2 class="section-title">Core Expertise</h2>
        <div class="expertise-grid">
            <div class="expertise-card">
                <span class="icon">⚡</span>
                <h3>Full-Stack Development</h3>
                <p>Python, React, Node.js, and cloud-native architectures</p>
            </div>
            <div class="expertise-card">
                <span class="icon">🎨</span>
                <h3>UI/UX Design</h3>
                <p>Human-centered design, prototyping, and design systems</p>
            </div>
            <div class="expertise-card">
                <span class="icon">🚀</span>
                <h3>DevOps & CI/CD</h3>
                <p>Docker, Kubernetes, and automated deployment pipelines</p>
            </div>
            <div class="expertise-card">
                <span class="icon">📊</span>
                <h3>Data & Analytics</h3>
                <p>Big data processing, visualization, and machine learning</p>
            </div>
        </div>
    </div>
</section>
"""
st.markdown(expertise_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# EXPERIENCE TIMELINE
# -----------------------------------------------------------------------------
timeline_html = """
<section id="experience" class="section-padding">
    <div class="container">
        <h2 class="section-title">Professional Journey</h2>
        <div class="timeline">
            <div class="timeline-item">
                <div class="dot"></div>
                <div class="content">
                    <div class="year">2023 – Present</div>
                    <h4>Lead Architect</h4>
                    <p>TechCorp Inc. – Leading a team of 10, designing microservices and cloud infrastructure.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="dot"></div>
                <div class="content">
                    <div class="year">2020 – 2023</div>
                    <h4>Senior Developer</h4>
                    <p>Innovate Solutions – Full-stack development for fintech platforms.</p>
                </div>
            </div>
            <div class="timeline-item">
                <div class="dot"></div>
                <div class="content">
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
# PROJECTS SHOWCASE
# -----------------------------------------------------------------------------
projects_html = """
<section id="projects" class="section-padding">
    <div class="container">
        <h2 class="section-title">Featured Projects</h2>
        <div class="projects-grid">
            <div class="project-card">
                <div class="img-wrapper">
                    <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&h=400&fit=crop" alt="Project 1">
                </div>
                <div class="body">
                    <h3>AI-Powered Dashboard</h3>
                    <p>Real-time analytics with predictive insights and interactive visualizations.</p>
                    <div class="tags">
                        <span>React</span>
                        <span>Python</span>
                        <span>TensorFlow</span>
                    </div>
                    <div class="links">
                        <a href="#">🔗 Live Demo</a>
                        <a href="#">📂 GitHub</a>
                    </div>
                </div>
            </div>
            <div class="project-card">
                <div class="img-wrapper">
                    <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&h=400&fit=crop" alt="Project 2">
                </div>
                <div class="body">
                    <h3>E-Commerce Platform</h3>
                    <p>Scalable online store with microservices and real-time inventory.</p>
                    <div class="tags">
                        <span>Node.js</span>
                        <span>React</span>
                        <span>MongoDB</span>
                    </div>
                    <div class="links">
                        <a href="#">🔗 Live Demo</a>
                        <a href="#">📂 GitHub</a>
                    </div>
                </div>
            </div>
            <div class="project-card">
                <div class="img-wrapper">
                    <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600&h=400&fit=crop" alt="Project 3">
                </div>
                <div class="body">
                    <h3>Design System UI Kit</h3>
                    <p>Comprehensive component library with dark/light mode and accessibility.</p>
                    <div class="tags">
                        <span>Figma</span>
                        <span>CSS</span>
                        <span>Storybook</span>
                    </div>
                    <div class="links">
                        <a href="#">🔗 Live Demo</a>
                        <a href="#">📂 GitHub</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""
st.markdown(projects_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# CONTACT SECTION (with Streamlit Form + Custom CSS)
# -----------------------------------------------------------------------------
st.markdown("""
<section id="contact" class="section-padding">
    <div class="container">
        <h2 class="section-title">Get In Touch</h2>
        <div class="contact-section">
""", unsafe_allow_html=True)

# We'll use a Streamlit form for backend handling.
# The form will be styled using the custom CSS above (class names already applied).
with st.form("contact_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name", placeholder="John Doe", label_visibility="collapsed")
    with col2:
        email = st.text_input("Your Email", placeholder="john@example.com", label_visibility="collapsed")
    message = st.text_area("Message", placeholder="Tell me about your project...", label_visibility="collapsed")
    submitted = st.form_submit_button("Send Message ✦", use_container_width=False)

    if submitted:
        # Here you would integrate with an email service or database.
        # For demo, we just show a success toast.
        st.success("Thank you! I'll get back to you within 24 hours.")

st.markdown("""
            <div class="social-icons">
                <a href="#" aria-label="GitHub">🐙</a>
                <a href="#" aria-label="LinkedIn">🔗</a>
                <a href="#" aria-label="Twitter">🐦</a>
                <a href="#" aria-label="Dribbble">🏀</a>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
footer_html = f"""
<footer class="footer">
    <p>&copy; {datetime.now().year} John Doe. Crafted with Streamlit & ✦.</p>
</footer>
"""
st.markdown(footer_html, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SMOOTH SCROLLING SCRIPT (optional enhancement)
# -----------------------------------------------------------------------------
smooth_scroll_js = """
<script>
    // Smooth scroll for internal links
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
st.markdown(smooth_scroll_js, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# END OF SCRIPT
# -----------------------------------------------------------------------------
