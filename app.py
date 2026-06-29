import streamlit as st
from PIL import Image

from prompts import VISION_PROMPT, LLM_PROMPT
from vission_client import analyze_product_image
from llm_client import generate_product_details

st.set_page_config(
    page_title="Product Analyzer",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ AI Product Analyzer")
st.write("Upload a product image to analyze it.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png", "JFIF"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    image = image.resize((300, 300))

    st.image(image, caption="Uploaded Image")

    if st.button("Analyze"):

        with st.spinner("Analyzing Product..."):

            # Vision Model
            vision_result = analyze_product_image(
                image=image,
                prompt=VISION_PROMPT
            )

            # LLM
            llm_result = generate_product_details(
                vision_json=vision_result,
                prompt=LLM_PROMPT
            )

        st.success("Analysis Completed!")

        
        st.subheader("Final Product Details")
        st.write(llm_result)