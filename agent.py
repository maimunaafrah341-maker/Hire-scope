import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("FEATHERLESS_API_KEY"),
    base_url="https://api.featherless.ai/v1"
)

MODEL = "mistralai/Mistral-Small-3.2-24B-Instruct-2506"

def analyse_candidate(candidate_data):
  
    candidate_text = str(candidate_data)

    step1 = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an expert hiring analyst."},
            {"role": "user", "content": f"Analyse this candidate profile and summarise their background in 3 bullet points:\n{candidate_text}"}
        ]
    )
    analysis = step1.choices[0].message.content
    print("Step 1 done: Profile analysed")

    step2 = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an expert hiring risk detector."},
            {"role": "user", "content": f"Based on this analysis, identify 3 hiring risks or blindspots a recruiter might miss:\n{analysis}"}
        ]
    )
    risks = step2.choices[0].message.content
    print("Step 2 done: Risks detected")

    step3 = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a senior hiring manager making final decisions."},
            {"role": "user", "content": f"Given these risks:\n{risks}\n\nGive a final hire/no-hire recommendation with a confidence score out of 10."}
        ]
    )
    decision = step3.choices[0].message.content
    print("Step 3 done: Decision made")

    return {
        "analysis": analysis,
        "risks": risks,
        "decision": decision
    }