# Moving-Object-detection-using-openCV


This repository contains a Python script that uses the OpenCV library to perform moving object detection using a webcam or camera feed. The script captures video frames, compares each frame with the initial frame (background), and detects moving objects in the scene.
# Requirements

    Python 3
    OpenCV library
    imutils library

You can install the required libraries using pip:

pip install opencv-python
pip install imutils

# How it works

    The code captures video frames from the webcam or camera.
    The first frame is saved as the reference background for comparison.
    Each subsequent frame is converted to grayscale and Gaussian blur is applied to reduce noise.
    The absolute difference between the current frame and the background frame is calculated.
    Thresholding is applied to create a binary image, where white pixels represent moving objects.
    Dilation is performed on the binary image to fill gaps and improve object detection.
    Contours are found in the binary image using OpenCV's findContours function.
    Each contour's area is calculated, and if it exceeds a specified threshold, it is considered a moving object.
    Rectangles are drawn around the detected moving objects, and a label is displayed near each object.
    The processed frames, along with the binary difference image and thresholded image, are displayed in separate windows.

# How to use

    Clone the repository to your local machine.
    Ensure you have Python 3 and the required libraries installed.
    Run the script:

python moving_object_detection.py

    The webcam feed will open, and the script will start detecting moving objects in the scene.
    As the script runs, it will draw green rectangles around the detected moving objects and display a label for each object.
    To stop the script, press the 'a' key in the OpenCV window.

# Customization

    You can adjust the area variable in the script to set the minimum contour area required to consider an object as moving. Smaller values will detect smaller objects as moving, but may also include noise.
    For different cameras or video sources, you can change the parameter in cv2.VideoCapture() to the appropriate source index or video file path.

# Contributions

Contributions to improve the code and its functionality are welcome. If you find any issues or have suggestions for enhancements, please feel free to open an issue or submit a pull request.
