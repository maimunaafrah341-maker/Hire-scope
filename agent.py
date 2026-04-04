# =========================
# agent.py (FINAL VERSION)
# =========================

import streamlit as st
from google import genai

# Get API key from Streamlit Secrets
API_KEY = st.secrets.get("GEMINI_API_KEY", None)

# Initialize client only if key exists
if API_KEY:
    client = genai.Client(api_key=API_KEY)


def analyse_candidate(candidate, use_ai=False):

    # 🟢 Fallback (always works)
    def fallback(message="Demo mode active"):
        return {
            "analysis": f"⚠️ {message}\n\n- Basic profile analysis based on available data",
            "risks": "- Limited experience or data\n- Skill gaps may exist",
            "decision": "Neutral Hire (5/10)"
        }

    # If AI disabled or no key → fallback
    if not use_ai or not API_KEY:
        return fallback("AI disabled or API key missing")

    try:
        prompt = f"""
        You are a senior hiring expert.

        Analyse the following candidate:
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
        Hire/No Hire - short reason - score X/10
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=prompt
        )

        text = response.text

        # 🔍 Parse structured output
        try:
            analysis = text.split("Analysis:")[1].split("Risks:")[0].strip()
            risks = text.split("Risks:")[1].split("Decision:")[0].strip()
            decision = text.split("Decision:")[1].strip()
        except:
            return fallback("AI response format error")

        return {
            "analysis": analysis,
            "risks": risks,
            "decision": decision
        }

    except Exception as e:
        error_msg = str(e)

        # 🚨 Handle quota error nicely
        if "429" in error_msg or "quota" in error_msg.lower():
            return fallback("Gemini quota exceeded")

        return fallback("AI request failed")