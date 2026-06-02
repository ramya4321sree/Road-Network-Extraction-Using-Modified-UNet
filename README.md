# Road Network Extraction Using Modified U-Net

## Overview

This project focuses on extracting road networks from satellite imagery using a Modified U-Net architecture.

The project compares:

* Traditional Otsu Thresholding
* Existing Simple U-Net
* Proposed Modified U-Net

The Modified U-Net uses residual connections and improved feature extraction for better segmentation performance.

---

## Technologies Used

* Python
* TensorFlow
* OpenCV
* NumPy
* MATLAB

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

## Dataset

**Dataset Used:** Massachusetts Roads Dataset

The dataset consists of satellite road images and corresponding ground truth masks used for semantic segmentation and road extraction tasks.

**Note:** The complete dataset is not included in this repository due to its large size.

---

## Evaluation Metrics

* Accuracy
* Dice Coefficient
* Intersection over Union (IoU)

---

## Performance Comparison

| Metric           | Existing System (Simple U-Net) | Proposed System (Modified U-Net) |
| ---------------- | ------------------------------ | -------------------------------- |
| Accuracy         | 96.0%                          | 97.1%                            |
| Dice Coefficient | 0.60                           | 0.72                             |
| IoU Score        | 0.43                           | 0.56                             |

---

## Results

The proposed Modified U-Net demonstrated better road extraction performance compared to the Existing Simple U-Net and Traditional Otsu Thresholding approach.

### Key Improvements

* Higher segmentation accuracy
* Better road continuity
* Reduced noise in extracted road networks
* Improved Dice Coefficient and IoU Score
* More reliable road extraction from satellite imagery

---

## Output Screenshots

The repository includes:

* Modified U-Net Prediction Results
* Existing U-Net Prediction Results
* Otsu Thresholding Results
* Training Progress Visualization
* Complexity vs Accuracy Analysis

All output screenshots are available in the **results** folder.

---

## Applications

* Geographic Information Systems (GIS)
* Smart City Development
* Urban Planning
* Disaster Management
* Navigation Systems
* Transportation Network Analysis

---

## Author

**Ramya Sree**

Electronics and Communication Engineering (ECE)

Research Project: Road Network Extraction Using Modified U-Net
