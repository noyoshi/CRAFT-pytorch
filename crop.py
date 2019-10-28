import cv2
import numpy as np
from rotate import rotate


"""
Assumes that the images are in ./result with format
res_n.jpg being the image, and res_n.txt being the file that
has the coordinates for the bounding boxes.

Outputs the data into the new folder ./cropped_images/res_n/ 
"""

def pair_up(cord_list):
    # return a list of paired up cords
    arr = []
    cord_list = list(cord_list)
    while cord_list:
        x = cord_list.pop(0)
        y = cord_list.pop(0)
        arr.append([x, y])

    return arr

def get_boxes(box_file):
    # If we have a txt file containing all of the pairs of cords we need, 
    # read it in here and return the list of lists (of lists)
    # this gets ALL of the boxes in the image BTW

    arr = []
    with open(box_file, "r") as f:
        for line in f:
            line = line.strip().split(',')
            arr.append(pair_up(line))

    return arr

# TODO this should be in le for loop

n = 0

# TODO make this work for multiple original images, or read from STDIN somehow,
# that way we can run all the images through it at once?
import os

file_names = set()
for item in os.listdir("./result"):
    # For each thing in here...
    file_name = item.strip().split(".")[0]
    if "mask" not in file_name and "original" not in file_name:
        file_names.add(file_name)

# Now we have the names of all the files
OUTPUT_DIR = "./cropped_images/"

for file_name in file_names:
    # make the directory
    img_dir = OUTPUT_DIR + file_name
    try:
        os.mkdir(img_dir)
    except Exception as e:
        print(e)
        continue
    verticies = []
    # img_file = f"./result/{file_name}.jpg" # NEED TO REFERENCE ORIGINAL IMAGES INSTEAD...
    file_numeric_id = file_name.replace("res_", "")
    # original_filepath = "/home/nyoshida/images/" + file_numeric_id + ".jpg"
    original_filepath = "/home/nyoshida/pewds/" + file_numeric_id + ".jpg"
    img_file = original_filepath
    print( f"./result/{file_name}.jpg")
    with open(f"./result/{file_name}.txt", "r") as f:
        n = 0
        original = cv2.imread(img_file)
        # Don't write the original image cuz OCR tool will DERP
        # cv2.imwrite(f'{img_dir}/original.png', original) # write the original file as well

        for line in f.readlines(): # for each cropped region in the file
            line = line.strip()
            line = line.split(",")
            max_x = 0
            max_y = 0
            min_x = 100000
            min_y = 100000
            while line:
                x = int(line.pop(0))
                y = int(line.pop(0))
                max_x = max(x, max_x)
                min_x = min(x, min_x)
                max_y = max(y, max_y)
                min_y = min(y, min_y)


            cropped_portion = original[min_y:max_y, min_x:max_x]
            cv2.imwrite(f'{img_dir}/output-{n}.png', cropped_portion)
            n += 1
