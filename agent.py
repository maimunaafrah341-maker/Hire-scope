import os
from google import genai
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
          model="gemini-2.0-flash",
          contents=f"""
          Analyse this candidate: {candidate}

         Return STRICT format:
         Analysis: ...
         Risks: ...
         Decision: ...
         """
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

