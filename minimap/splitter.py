import os
from PIL import Image
import random
from shutil import copyfile


def empty_dir(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


# The splitter separates the images which have player locator into 10x10px images for training.
def split(file):
    fname = file.replace(".png", "")
    height = 10
    width = 10
    padding = 10  # Take a bigger image than the 10x10 box to make identification easier
    im = Image.open(f"./images/raw_nomap/{file}")
    img_width, img_height = im.size
    for i in range(0, img_height, height):
        for j in range(0, img_width, width):
            box = (j - padding, i - padding, j + width + padding, i + height + padding)
            a = im.crop(box)
            try:
                a.save(f"./images/train/nomap/{fname}-{i}-{j}.png")
            except:
                pass


# Delete existing images in the train/validation sets
print("emptying existing screenshots...")
empty_dir("./images/train/nomap")
empty_dir("./images/train/map")
empty_dir("./images/valid/nomap")
empty_dir("./images/valid/map")

# Split the desktop screenshots without minimaps into 30x30 images.
print("splitting nomap screenshots...")
source_files = os.listdir("./images/raw_nomap")
for f in source_files:
    split(f)

# Gather the validation set from the player locator images.
print("copying minimap screenshots from player locator images...")
terrain_path = "../locator/split/valid/terrain"
source_files = os.listdir(terrain_path)
for f in source_files:
    copyfile(f"{terrain_path}/{f}", f"./images/train/map/{f}")

player_path = "../locator/split/valid/player"
source_files = os.listdir(player_path)
for f in source_files:
    copyfile(f"{player_path}/{f}", f"./images/train/map/{f}")

# Move 20% of the training set to the validation set.
print("creating validation set...")
map_path = "./images/train/map"
map_files = os.listdir(map_path)
for f in map_files:
    if random.randint(0, 4) > 3:
        os.rename(f"{map_path}/{f}", f"./images/valid/map/{f}")

nomap_path = "./images/train/nomap"
nomap_files = os.listdir(nomap_path)
for f in nomap_files:
    if random.randint(0, 4) > 3:
        os.rename(f"{nomap_path}/{f}", f"./images/valid/nomap/{f}")