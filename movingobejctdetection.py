import cv2
import time
import imutils

# Open the camera (webcam in this case). '0' denotes the default camera.
cam = cv2.VideoCapture(0)

# Initialize variables
firstFrame = None  # Store the first frame (background) to compare with subsequent frames
area = 10  # Minimum contour area required to consider it as a moving object

while True:
    # Read a frame from the camera
    _, img = cam.read()

    text = 'Normal'  # Default status text when no moving object is detected
    print(text)

    # Resize the frame for faster processing
    img = imutils.resize(img, width=700)

    # Convert the frame to grayscale
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve object detection
    grayimg = cv2.GaussianBlur(grayimg, (21, 21), 0)

    if firstFrame is None:
        # If this is the first frame, save it as the reference background
        firstFrame = grayimg
        continue

    # Calculate the absolute difference between the current frame and the reference background
    imgdiff = cv2.absdiff(firstFrame, grayimg)

    # Apply thresholding to create a binary image (black and white) for easy contour detection
    threshimg = cv2.threshold(imgdiff, 100, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image to fill gaps and improve object detection
    threshimg = cv2.dilate(threshimg, None, iterations=3)

    # Find contours in the thresholded image
    cnts = cv2.findContours(threshimg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        # Loop over each contour found

        # If the contour area is smaller than the specified area, ignore it (noise)
        if cv2.contourArea(c) < area:
            continue

        # Get the bounding box coordinates of the contour
        (x, y, w, h) = cv2.boundingRect(c)

        # Draw a rectangle around the detected moving object
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        text = 'Moving object detected'
        print(text)

        # Put a text label near the detected object
        cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Show the processed frames in separate windows
    cv2.imshow('cameraFeed', img)  # Original frame with rectangles drawn
    cv2.imshow('thresh', threshimg)  # Thresholded binary image
    cv2.imshow('image distance', imgdiff)  # Absolute difference image

    # Check for user input to break the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('a'):
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
