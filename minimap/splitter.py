import os
from PIL import Image


# The splitter separates the images which have player locator into 10x10px images for training.
def split(file):
    fname = file.replace(".png", "")
    height = 10
    width = 10
    padding = 10  # Take a bigger image than the 10x10 box to make identification easier
    im = Image.open(f"./images/nomap/{file}")
    img_width, img_height = im.size
    for i in range(0, img_height, height):
        for j in range(0, img_width, width):
            box = (j - padding, i - padding, j + width + padding, i + height + padding)
            a = im.crop(box)
            try:
                a.save(f"./images/nomap_split/{fname}-{i}-{j}.png")
            except:
                pass


source_files = os.listdir("./images/nomap")
for f in source_files:
    split(f)
