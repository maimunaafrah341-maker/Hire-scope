# =========================
# app.py (IMPROVED UI + GEMINI OUTPUT)
# =========================

import streamlit as st
from agent import analyse_candidate

CANDIDATES = [
    {
        "name": "Sundar Pichai",
        "headline": "CEO at Google & Alphabet",
        "experience": [
            {"title": "CEO", "company": "Google & Alphabet", "duration": "9 years"},
            {"title": "SVP", "company": "Google", "duration": "5 years"}
        ],
        "education": "MBA - Wharton, MS - Stanford, B.Tech - IIT",
        "skills": ["Leadership", "AI", "Cloud"]
    },
    {
        "name": "Junior Developer",
        "headline": "Entry Level Engineer",
        "experience": [
            {"title": "Intern", "company": "Startup", "duration": "6 months"}
        ],
        "education": "B.Tech",
        "skills": ["Python"]
    }
]

st.set_page_config(page_title="HireScope", layout="wide")

st.title("🔍 HireScope")
st.subheader("AI Hiring Risk & Blindspot Detector")

use_ai = st.toggle("Use Gemini AI", value=False)

st.markdown("---")

names = [c["name"] for c in CANDIDATES]
selected = st.selectbox("Choose a candidate", names)

candidate = next(c for c in CANDIDATES if c["name"] == selected)

if st.button("Analyse Candidate"):
    result = analyse_candidate(candidate, use_ai)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📋 Profile Analysis")
        st.markdown(result["analysis"])

    with col2:
        st.markdown("### ⚠️ Risks & Blindspots")
        st.markdown(result["risks"])

    with col3:
        st.markdown("### ✅ Hiring Decision")
        st.markdown(result["decision"])


# =========================
# agent.py (SMART GEMINI PROMPT + CLEAN PARSING)
# =========================

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyse_candidate(candidate, use_ai=False):

    def fallback():
        return {
            "analysis": "- Basic profile analysis (demo mode)",
            "risks": "- Limited data available",
            "decision": "No Hire (5/10)"
        }

    if not use_ai:
        return fallback()

    try:
        prompt = f"""
        You are a senior hiring expert.

        Analyse the following candidate in a structured way:
        {candidate}

        Follow EXACT format:

        Analysis:
        - Point 1
        - Point 2
        - Point 3

        Risks:
        - Risk 1
        - Risk 2
        - Risk 3

        Decision:
        Hire/No Hire - short justification - score X/10
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=prompt
        )

        text = response.text

        # Clean parsing
        try:
            analysis = text.split("Analysis:")[1].split("Risks:")[0].strip()
            risks = text.split("Risks:")[1].split("Decision:")[0].strip()
            decision = text.split("Decision:")[1].strip()
        except:
            return fallback()

        return {
            "analysis": analysis,
            "risks": risks,
            "decision": decision
        }

    except Exception as e:
        print("Gemini Error:", e)
        return fallback()


