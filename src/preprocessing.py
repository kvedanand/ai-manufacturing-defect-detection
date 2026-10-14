import cv2
import numpy as np
from PIL import Image


def preprocess_image(
    image: Image.Image,
    image_size: int = 224
) -> np.ndarray:
    """
    Resize an image and normalize pixel values.

    Args:
        image: Input component image.
        image_size: Target image width and height.

    Returns:
        Normalized RGB image as a NumPy array.
    """
    if image is None:
        raise ValueError("Input image cannot be empty.")

    image_array = np.asarray(image.convert("RGB"))

    resized_image = cv2.resize(
        image_array,
        (image_size, image_size),
        interpolation=cv2.INTER_AREA
    )

    normalized_image = resized_image.astype(np.float32) / 255.0

    return normalized_image
