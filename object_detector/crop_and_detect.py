import os

from object_detector import detect_objects, process_images


def crop_and_detect(input_folder, output_folder):
    """

    :param input_folder: input folder that contains images
    :param output_folder: target output folder

    use-case:
    -input_folder
        -class1
            -image1.jpeg
        -class2
            -image1.jpeg

    results:
    -cropped_edges
        -class1
            -image1.jpeg
    -output_folder
        -cropped
            -class1
                -image1.jpeg
            -class2
                -image1.jpeg
        -detected
            -class1
                -image1.jpeg
            -class2
                -image1.jpeg

    """



    # Creating sub_result folder of edge cropped images
    cropped_folder = os.path.join(output_folder, "cropped")
    os.makedirs(cropped_folder, exist_ok=True)

    # Cropping edges
    process_images(input_folder, cropped_folder)


    # Optional, crops the edges of the detected object(with rectangle)
    # Detecting objects
    detect_objects(cropped_folder, output_folder)
