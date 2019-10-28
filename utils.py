#!/usr/bin/env python3

import os
import sys
import json
import cv2

from shutil import copyfile

BASE_DIR = "/home/nyoshida/CRAFT-pytorch"
IMG_DIR = "/home/nyoshida/CRAFT-pytorch/images"
# Pipe in the text file that has all the image locations? 
def build_filepath(directory, file_name):
    arr = directory.split("/")
    arr.append(file_name)
    return "/".join(arr)


def update_filename(n, filepath):
    # n is the number, eg 0
    # filepath is eg /temp/filename.jpg
    # should return /temp/0.jpg
    arr = filepath.split("/")
    filename = arr.pop()
    filetype = filename.split(".")[-1]
    new_filename = str(n) + "." + filetype
    arr.append(new_filename)

    return "/".join(arr)


def read_metadata(directory):
    """Opens metadata.json file in directory, if present"""
    FNAME = "metadata.json"
    metadata = {
        
    }

    if not os.path.isfile(FNAME):
        pass


def write_metadata(directory, source, tag, n):
    """Writes the metadata.json file to a directory"""
    # Tag: the hashtag from instagram / twitter? or the board for 4chan
    # Source: Instagram, Twitter, 4chan, etc
    FNAME = "metadata.json"
    metadata = {
        "source": source, 
        "tag": tag,
        "n": n
    }

    with open(build_filepath(directory, FNAME), "w") as f:
        json.dump(metadata, f)


def extract_filename(path):
    return path.split("/")[-1]


def valid_locations(filelist):
    for file in filelist:
        if not os.path.isfile(file):
            return False
    return True


# moves images
def move_images(image_file_locations, destination_directory):
    """Input: list of image locations on disk, directory for these images to go to"""
    # Returns the number of files written
    n = 0
    for old_file_location in image_file_locations:
        old_filename = extract_filename(old_file_location)
        new_filepath = build_filepath(destination_directory, old_filename)
        new_filepath = update_filename(n, new_filepath) # updates name to be <NUM>.jpg
        
        if not valid_locations([old_file_location]):
            continue
        
        copyfile(old_file_location, new_filepath)
        n += 1
    
    return n


# writes np image maps to file locations
def write_cv_images(np_image_list, destination_directory):
    """Input: image_list has the np images"""
    n = 0
    for img in np_image_list:
        new_filepath = build_filepath(destination_directory, str(n) + ".png")
        
        cv2.imwrite(new_filepath, img)
        n += 1
    
    return n


old_file_locations = []
with open("text_images.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        old_file_locations.append(line)

move_images(old_file_locations, IMG_DIR)


