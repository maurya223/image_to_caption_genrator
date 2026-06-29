import io

import ollama

from config import VISION_MODEL


def analyze_product_image(image, prompt):
    """Analyze a product image using the vision model.

    Args:
        image: PIL.Image.Image
        prompt: Vision prompt

    Returns:
        str: Model response
    """

    # The Ollama Python client validates `images` and expects values it can serialize
    # (e.g., file paths or bytes). Passing a PIL.Image directly causes a pydantic
    # validation error.
    img_bytes_io = io.BytesIO()
    image.save(img_bytes_io, format="PNG")
    img_bytes = img_bytes_io.getvalue()

    response = ollama.chat(
        model=VISION_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [img_bytes],
            }
        ],
    )

    return response["message"]["content"]

