from PIL import Image
import csv
import os, shutil
import random


# The splitter separates the images which have player locator into 10x10px images for training.
def split(file, player_grids, k):
    s = 0
    grids = [int(i) for i in player_grids.split(" ")]

    height = 10
    width = 10
    padding = 10  # Take a bigger image than the 10x10 box to make identification easier
    im = Image.open(f"./coordinate_images/{file}")
    img_width, img_height = im.size
    for i in range(0, img_height, height):
        for j in range(0, img_width, width):
            box = (j - padding, i - padding, j + width + padding, i + height + padding)
            a = im.crop(box)
            try:
                img_type = "terrain"
                img_set = "train"
                if random.randrange(0, 5) < 1:
                    img_set = "valid"
                if (j * 1000 / width + i // height) in grids:
                    img_type = "player"
                a.save(f"./split/{img_set}/{img_type}/sp-{k}{s}.png")
            except:
                pass
            s += 1


# Clear the existing files
print("deleting existing split images...")
folder = './split'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

try:
    os.mkdir("./split/train")
except:
    pass
try:
    os.mkdir("./split/train/terrain")
except:
    pass
try:
    os.mkdir("./split/train/player")
except:
    pass

try:
    os.mkdir("./split/valid")
except:
    pass
try:
    os.mkdir("./split/valid/player")
except:
    pass
try:
    os.mkdir("./split/valid/terrain")
except:
    pass

print("starting splitter...")
k = 0
with open('./coordinates.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    for r in reader:
        try:
            split(r[0], r[1], k)
        except:
            print(f"invalid row: {r}")
        k += 1

        if k % 50 == 0:
            print(k)
print("done splitting!")
