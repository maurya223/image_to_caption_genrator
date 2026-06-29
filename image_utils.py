from PIL import Image


def load_image(uploaded_file):
    """
    Load uploaded image and convert it to RGB.

    Args:
        uploaded_file: Streamlit uploaded file

    Returns:
        PIL.Image.Image
    """
    image = Image.open(uploaded_file)

    if image.mode != "RGB":
        image = image.convert("RGB")

    return image


def get_image_info(image):
    """
    Return image metadata.
    """

    return {
        "width": image.width,
        "height": image.height,
        "mode": image.mode,
        "format": image.format
    }