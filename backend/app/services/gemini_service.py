import os
import json

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv("backend/.env")


class GeminiService:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in backend/.env"
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-flash-latest"
        )

    def test_connection(self):

        response = self.model.generate_content(
            "Say Hello"
        )

        return response.text

    def generate_disease_recommendation(
        self,
        disease_name: str,
        language: str = "en"
    ):

        language_name = {
            "en": "English",
            "gu": "Gujarati",
            "hi": "Hindi"
        }.get(
            language,
            "English"
        )

        prompt = f"""
You are an expert agricultural scientist.

Disease Name:
{disease_name}

Generate recommendation in:
{language_name}

Return ALL text in {language_name}.

Generate recommendation in JSON format.

Required fields:

disease_name
description
severity
organic_treatment
chemical_treatment
preventive_measures
monitoring_actions

Rules:
- Return ONLY valid JSON.
- Return exactly ONE JSON object.
- Translate disease_name into the selected language.
- Return ALL fields in {language_name}.
- Do NOT return markdown.
- Do NOT return code blocks.
- Do NOT return explanations.
- Do NOT return any text before JSON.
- Do NOT return any text after JSON.
- Keep recommendations farmer-friendly.
- Keep recommendations concise.
- Return all content in {language_name}.

Example:

{{
    "disease_name": "...",
    "description": "...",
    "severity": "...",
    "organic_treatment": "...",
    "chemical_treatment": "...",
    "preventive_measures": "...",
    "monitoring_actions": "..."
}}
"""

        response = self.model.generate_content(
            prompt
        )

        text = response.text.strip()

        # Remove markdown if Gemini returns it

        if text.startswith("```json"):

            text = (
                text.replace(
                    "```json",
                    ""
                )
                .replace(
                    "```",
                    ""
                )
                .strip()
            )

        elif text.startswith("```"):

            text = (
                text.replace(
                    "```",
                    ""
                )
                .strip()
            )

        try:

            # Extract only JSON portion

            start = text.find("{")
            end = text.rfind("}") + 1

            clean_json = text[start:end]

            data = json.loads(
                clean_json
            )

        except Exception as e:

            print("\n===== INVALID GEMINI RESPONSE =====")
            print(text)
            print("==================================\n")

            raise Exception(
                f"Gemini JSON Parse Error: {e}"
            )

        

        data["treatment"] = (
            "Refer to organic and chemical treatment."
        )

        print("\n===== GEMINI RAW RESPONSE =====")
        print(text)
        print("===============================\n")

        return data