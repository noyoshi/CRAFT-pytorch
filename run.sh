#!/bin/bash

# Results saved to ./results
# Input: images in the images/ folder for processing
# Output: images in ./result, named res_n.jpg with data as res_n.txt for the
# bounding boxes

# To use, run this, then run crop.py (make sure the cropped_images folder is
# created)
python3 test.py --trained_model=craft_mlt_25k.pth --test_folder=images/ --cuda=False
