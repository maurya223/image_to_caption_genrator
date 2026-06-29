import ollama
from config import TEXT_MODEL


def generate_product_details(vision_json, prompt):

    response = ollama.chat(
        model=TEXT_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"""
{prompt}

Vision JSON:

{vision_json}
"""
            }
        ]
    )

    return response["message"]["content"]