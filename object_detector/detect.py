import os
import cv2
import numpy as np


def detect_and_crop(image_path):
    # Load image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the white places on image (for borders)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    # Find contours(borders of rectangle)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Get contours shaped rectangle
        epsilon = 0.05 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:  # is rectangle?
            x, y, w, h = cv2.boundingRect(approx)

            # Calculate the area
            area = w * h
            if area >= 350:  # ignore below 350px2
                cropped_img = img[y:y + h, x:x + w]  # Crop inside of rectangle
                return cropped_img

    return None  # if there is no rectangle


def detect_objects(input_folder, output_folder):
    # Scan the folders
    for subfolder in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder)
        if os.path.isdir(subfolder_path):
            detected_folder = os.path.join(output_folder, 'detected', subfolder)
            os.makedirs(detected_folder, exist_ok=True)

            # Scan image files
            for image_name in os.listdir(subfolder_path):
                image_path = os.path.join(subfolder_path, image_name)
                if image_name.lower().endswith(('png', 'jpg', 'jpeg')):
                    cropped_img = detect_and_crop(image_path)

                    if cropped_img is not None:
                        output_path = os.path.join(detected_folder, image_name)
                        cv2.imwrite(output_path, cropped_img)
                    else:
                        print(f"[LOG] Rectangle is not found or area is so small: {image_path}")


# Paths of input / output folders
input_folder = 'cropped_edges'
output_folder = 'cropped_output'

detect_objects(input_folder, output_folder)
