# Road Network Extraction Using Modified U-Net

## Overview

This project focuses on extracting road networks from satellite imagery using a Modified U-Net architecture.

The project compares:

- Traditional Otsu Thresholding
- Existing Simple U-Net
- Proposed Modified U-Net

The Modified U-Net uses residual connections and improved feature extraction for better segmentation performance.

---

## Technologies Used

- Python
- TensorFlow
- OpenCV
- NumPy
- MATLAB

---

## Project Structure

Road-Network-Extraction-Using-Modified-UNet

├── README.md

├── requirements.txt

├── matlab

│ └── otsu_thresholding.m

├── python

│ ├── preprocessing.py

│ ├── model.py

│ ├── postprocessing.py

│ └── evaluation.py

├── images

└── results

---

## Evaluation Metrics

- Accuracy
- Dice Coefficient
- Intersection over Union (IoU)

---

## Author

Ramya Sree