import os
import cv2
import numpy as np
from alive_progress import alive_bar
images = os.listdir(".//input//split")
outputPath = ".//output//split//"
print(images)

for image_name in images:
    print(image_name)
    image = cv2.imread(f".//input//split//{image_name}")
    image_height = image.shape[0]
    image_width = image.shape[1]
    part_height = image_height//5
    for part in range(0,image_height,part_height):
        #print(f"part = {part}, image widtg = {image_width}, part height = {part_height}")
        cropped_image = image[part:part_height, 0:image_width]
        cv2.imwrite(f"{image_name}_part_{part}.png", cropped_image)