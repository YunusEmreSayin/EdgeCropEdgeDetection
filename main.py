from object_detector import crop_and_detect

input_folder = "input"
output_folder = "cropped_output"

if __name__ == "__main__":
    print("[LOG] Processing Images....")
    crop_and_detect(input_folder, output_folder)
    print("[LOG] Image process completed")

