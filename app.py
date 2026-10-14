import streamlit as st
import numpy as np
from PIL import Image
from src.preprocessing import preprocess_image

st.set_page_config(
    page_title="AI Manufacturing Defect Detection",
    page_icon="🏭",
    layout="wide"
)

st.title("AI-Based Manufacturing Defect Detection System")

st.write(
    "An intelligent visual inspection platform for manufacturing "
    "quality control using image processing and deep learning."
)

st.info(
    "Prototype version: Image preprocessing and analysis are available. "
    "AI-based defect classification will be added after model training."
)

st.sidebar.header("Inspection Settings")

image_size = st.sidebar.selectbox(
    "Image Size",
    [128, 224, 256, 512],
    index=1
)

uploaded_file = st.file_uploader(
    "Upload a component image",
    type=["jpg", "jpeg", "png", "bmp"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        processed_image = preprocess_image(image, image_size)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image, use_container_width=True)

        with col2:
            st.subheader("Preprocessed Image")
            st.image(processed_image, clamp=True, use_container_width=True)

        image_array = np.asarray(image)

        height, width = image_array.shape[:2]
        brightness = float(np.mean(image_array))
        contrast = float(np.std(image_array))

        st.subheader("Image Analysis")

        col1, col2, col3 = st.columns(3)

        col1.metric("Width", f"{width} px")
        col2.metric("Height", f"{height} px")
        col3.metric("Mean Brightness", f"{brightness:.2f}/255")

        st.write(f"Image contrast: {contrast:.2f}")

        st.warning(
            "No AI prediction has been generated. Image statistics alone "
            "cannot reliably determine whether a component is defective."
        )

    except Exception as error:
        st.error(f"Error processing image: {error}")

else:
    st.write("Upload an image to begin inspection.")

st.markdown("---")
st.caption("Mechanical Engineering | Manufacturing Quality Inspection")
