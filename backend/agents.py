import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env")

MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

print("✅ USING MODEL:", MODEL)

client = Groq(api_key=API_KEY)


def llm_call(prompt: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are an autonomous AI research assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


def research_coordinator(query):

    prompt = f"""
Break this research topic into:
- keywords
- subtopics
- important research areas

TOPIC:
{query}
"""

    return llm_call(prompt)


def content_analyzer(text):

    prompt = f"""
Analyze this content and extract:
- important insights
- key concepts
- notable findings

TEXT:
{text}
"""

    return llm_call(prompt)


def synthesis_agent(text):

    prompt = f"""
Write a professional research report with:

- Introduction
- Key Findings
- Analysis
- Conclusion

DATA:
{text}
"""

    return llm_call(prompt)