# Pill Detection and Counting with OpenCV

This project presents a classical computer vision–based approach for
detecting and counting pill-shaped objects in a static image using OpenCV.

The implementation is designed as a lightweight prototype inspired by
visual inspection and counting tasks commonly encountered in
pharmaceutical production lines.

---

## Pipeline Overview

The object detection and counting pipeline consists of the following steps:

- Conversion to grayscale to simplify intensity-based processing
- Gaussian blur for noise reduction while preserving object boundaries
- Inverted binary thresholding using Otsu’s method for robust segmentation
- Contour detection to identify individual objects
- Area-based filtering to eliminate noise and non-pill regions

---

## Key Design Decisions

- Grayscale conversion was used to improve the robustness of thresholding
  and contour detection by reducing color-related variability.

- A Gaussian blur with a 5×5 kernel was applied to suppress noise while
  maintaining the integrity of object edges. The sigma value was
  automatically determined by OpenCV.

- Inverted Otsu thresholding was selected due to relatively uniform
  illumination conditions and a bright background.

- Contour area thresholds were determined empirically based on contour
  statistics to filter out small noise regions and irrelevant large areas.

---

## Results

The algorithm successfully detects and counts **4 pill-shaped objects**
in the provided sample image.

Detected pills are visualized by drawing contours on the original image.
The final count and inspection status (PASS / FAIL) are overlaid on the
output image, which is saved to the output directory.

---

## Possible Improvements

- Shape-based classification (e.g., circular vs. capsule-shaped pills)
- Improved handling of overlapping or touching objects
- Extension to real-time video or camera-based processing
