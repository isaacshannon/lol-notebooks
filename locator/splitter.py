from PIL import Image
import csv
import os, shutil
import random
import uuid


source_dir = "./newdata/minimaps"
dest_dir = "./newdata/split"


# The splitter separates the images which have player locator into 10x10px images for training.
def split(file):
    s = 0
    height = 10
    width = 10
    padding = 10  # Take a bigger image than the 10x10 box to make identification easier
    im = Image.open(file)
    img_width, img_height = im.size
    for i in range(0, img_height, height):
        for j in range(0, img_width, width):
            box = (j - padding, i - padding, j + width + padding, i + height + padding)
            a = im.crop(box)
            a.save(f"{dest_dir}/{uuid.uuid4()}.png")
            s += 1


# Clear the existing files
print("deleting existing split images...")
for filename in os.listdir(dest_dir):
    file_path = os.path.join(dest_dir, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


print("starting splitter...")
for f in os.listdir(source_dir):
    split(f"{source_dir}/{f}")
print("done splitting!")
