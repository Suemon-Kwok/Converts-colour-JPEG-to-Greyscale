import cv2
import numpy as np

def process_image(image_path, output_path):
    # Load the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges in the image
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Parameters for line detection
    minLineLength = 100
    maxLineGap = 10

    # Apply Hough Line Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)

    # Draw the lines on the grayscale image
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(gray, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Hough Lines', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the result
    cv2.imwrite(output_path, gray)

# Ask the user for the image file path
image_path = input("Please enter the path to your image: ")

# Ask the user for the output file path
output_path = input("Please enter the path where you want to save the output image: ")

# Call the function with the user-provided paths
process_image(image_path, output_path)
