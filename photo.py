import cv2
from PIL import Image
import os

def separate_images(input_image_path, input_rows, input_cols):
    
    files = [f for f in os.listdir() if os.path.isdir(f)]
    base_dir = os.getcwd()
    output_dir = "Output/"
    output_path = os.path.join(base_dir, output_dir)
    if "Output" not in files:
        os.mkdir(output_path)

    dirs = os.listdir(output_path)
    photo_dir = os.path.join(output_path, f'{len(dirs) + 1}')
    os.mkdir(photo_dir)

    # Initialise no. of output
    ctr = 0

    # Open the input image using OpenCV
    input_image_cv = cv2.imread(input_image_path)

    # Get input file size in px count
    im = Image.open(input_image_path)
    width, height = im.size

    # Get row, col
    rows = input_rows
    cols = input_cols

    # Image output size thresholding
    x_min = width / (cols + 0.5)
    if cols > 1:
        x_max = width / (cols - 0.5)
    else:
        x_max = width 

    y_min = height / (rows + 0.5)
    if rows > 1:
        y_max = height / (rows - 0.5)
    else:
        y_max = height

    # Convert the image to grayscale for edge detection
    # gray_image = cv2.cvtColor(input_image_cv, cv2.COLOR_BGR2GRAY)
    # Might use next time 

    # Blur
    img_blur = cv2.medianBlur(input_image_cv, ksize=5) 

    # Apply edge detection (Canny edge detector) with adjusted lower thresholds
    edges = cv2.Canny(img_blur, 0, 150)  # Adjust the thresholds here

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through each contour and crop and save individual images
    for i, contour in enumerate(contours):
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        if x_min < w < x_max and y_max > h > y_min:

            # For file naming
            ctr += 1

            # Crop the individual image from the original input image
            cropped_image_cv = input_image_cv[y:y+h, x:x+w]

            # Convert the cropped image back to PIL format
            cropped_image_pil = Image.fromarray(cv2.cvtColor(cropped_image_cv, cv2.COLOR_BGR2RGB))


            output_image_path = f"{photo_dir}/img{ctr}.png"
            cropped_image_pil.save(output_image_path)

