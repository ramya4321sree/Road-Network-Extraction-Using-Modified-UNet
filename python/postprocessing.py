import cv2
import numpy as np

def finalize_output(binary_mask):

    kernel = np.ones((3, 3), np.uint8)

    closing = cv2.morphologyEx(
        binary_mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    final_output = cv2.morphologyEx(
        closing,
        cv2.MORPH_OPEN,
        kernel
    )

    return final_output