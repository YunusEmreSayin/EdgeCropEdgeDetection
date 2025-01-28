import os
import cv2
import numpy as np


def remove_white_border(image_path, threshold=250):
    # Loading image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Edge controls / LEFT
    left = 0
    while np.all(img[:, left] >= threshold):
        left += 1

    # Edge controls / RIGHT

    right = img.shape[1] - 1
    while np.all(img[:, right] >= threshold):
        right -= 1

    # Edge controls / TOP
    top = 0
    while np.all(img[top, :] >= threshold):
        top += 1

    # Edge controls / BOTTOM
    bottom = img.shape[0] - 1
    while np.all(img[bottom, :] >= threshold):
        bottom -= 1

    # Get full-edge cropped_image
    cropped_img = img[top:bottom + 1, left:right + 1]

    return cropped_img


def process_images(input_folder, output_folder):
    """
        params:
        -input_folder: the input folder that contains raw images
        -output_folder: the result folder

        usage:
            ref struct:

        input_folder
            -class1
                -image1.jpeg
            -class2
                -image1.jpeg

        results will be stored like:
        output_folder:
            cropped
                -class1
                    -image1.jpeg
                -class2
                    -image1.jpeg
    """
    # Scan input Folder
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # Process image files
            if file.endswith(('.jpg', '.jpeg', '.png')):
                # Exact path of image
                input_image_path = os.path.join(root, file)

                # Put result image to same subfolder in outputs
                relative_path = os.path.relpath(root, input_folder)
                output_subfolder = os.path.join(output_folder, relative_path)
                os.makedirs(output_subfolder, exist_ok=True)

                # Remove white borders
                result_image = remove_white_border(input_image_path)

                # Create the result path
                output_image_path = os.path.join(output_subfolder, file)

                # Save result image
                cv2.imwrite(output_image_path, result_image)
                print(f"[LOG] Result image saved!: {output_image_path}")


# Run the process
input_folder = 'input'  # Path of input folder
output_folder = 'cropped_edges'  # Output folder contains that only edge-cropped images
process_images(input_folder, output_folder)
