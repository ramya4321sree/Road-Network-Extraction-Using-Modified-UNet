import cv2
import numpy as np

def preprocess_data(image_path, mask_path):
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    image = cv2.resize(image, (256, 256))
    mask = cv2.resize(mask, (256, 256))

    image = image.astype("float32") / 255.0
    mask = mask.astype("float32") / 255.0

    mask = np.expand_dims(mask, axis=-1)

    return image, mask