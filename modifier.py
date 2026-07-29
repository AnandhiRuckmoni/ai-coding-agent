import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class Modifier:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)

    def modify_file(self, filepath, execution_plan, user_request):

        with open(filepath, "r", encoding="utf-8") as f:
            file_contents = f.read()

        prompt = f"""
You are an experienced Node.js developer.

User request:
{user_request}

Execution plan:
{execution_plan}

Current file:
{filepath}

Current code:
{file_contents}

Modify ONLY this file.

Return ONLY the complete updated file.
Do not explain anything.
Do not wrap the code in markdown.
"""

        response = self.client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
        )

        updated_code = response.text

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated_code)

        #print(f"Updated {filepath}")
        print(f"✓ {filepath}") 
