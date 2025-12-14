# Pill Detection and Counting with OpenCV

This project implements a classical image processing pipeline to detect
and count pill-shaped objects in a static image using OpenCV.

The implementation was developed independently as a standalone project
to apply and reinforce fundamental image processing concepts.

---

## Pipeline Overview

The object detection and counting process consists of the following steps:

- Conversion to grayscale to simplify intensity-based processing
- Gaussian blur for noise reduction while preserving object boundaries
- Inverted binary thresholding using Otsu’s method for robust segmentation
- Contour detection to identify object boundaries
- Area-based filtering to eliminate noise and non-pill regions

---

## Key Design Decisions

- Grayscale conversion was preferred to improve the reliability of
  thresholding and contour detection.

- A Gaussian blur with a 5×5 kernel was applied to reduce noise.
  The sigma value was automatically determined by OpenCV.

- Inverted Otsu thresholding was selected due to uniform lighting
  conditions and a bright background.

- Contour area thresholds were selected empirically based on contour
  statistics to handle noise and minor over-segmentation.

---

## Results

The algorithm correctly detects and counts **4 pill-shaped objects**
in the provided sample image.

The detected pills are visualized by drawing contours on the original
image and saved as an output file.

---


---

## Possible Improvements

- Shape-based classification (circular vs. capsule-shaped pills)
- Improved handling of overlapping objects
- Extension to real-time video processing


## Project Structure

