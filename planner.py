import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class Planner:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")

        self.client = genai.Client(api_key=api_key)

    def create_plan(self, repository_summary, user_request):

        prompt = f"""
You are a senior software engineer.

Repository Summary:
{repository_summary}

User Request:
{user_request}

Create a brief execution plan.

For organising notes, prefer implementing tags instead of categories unless there is a strong reason not to.


Return a valid JSON in the format:

{{
"feature":"",
"reason":"",
"files_to_modify":[],
"steps":[]
}}
Do not include markdown.
Do not include explanations.
Do NOT generate code.
"""

        response = self.client.models.generate_content(model="gemini-3.1-flash-lite",contents=prompt,)
        #print(response.text)

        return json.loads(response.text)
