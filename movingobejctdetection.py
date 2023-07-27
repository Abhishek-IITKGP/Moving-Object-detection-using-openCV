import cv2
import time
import imutils

# Create a GMM-based background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

# Open the camera (webcam in this case). '0' denotes the default camera.
cam = cv2.VideoCapture(0)

# Initialize variables
area = 50  # Minimum contour area required to consider it as a moving object

while True:
    # Read a frame from the camera
    _, img = cam.read()

    text = 'Normal'  # Default status text when no moving object is detected
    print(text)

    # Resize the frame for faster processing
    img = imutils.resize(img, width=700)

    # Apply the GMM-based background subtraction
    fg_mask = bg_subtractor.apply(img)

    # Clean up the foreground mask by removing noise and shadows
    fg_mask = cv2.erode(fg_mask, None, iterations=6)
    fg_mask = cv2.dilate(fg_mask, None, iterations=6)

    # Find contours in the foreground mask
    cnts = cv2.findContours(fg_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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
    cv2.imshow('foreground', fg_mask)  # Foreground mask

    # Check for user input to break the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord('a'):
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
