from PIL import Image
import os
import csv
import os, shutil
import random

# The splitter separates the images which have player coordinates into 10x10px images for training.
def split(filename, player_grids, k):
    s = 0
    grids = [int(i) for i in player_grids.split(" ")]

    height = 10
    width = 10
    im = Image.open(f"./coordinate_images/{filename}")
    imgwidth, imgheight = im.size
    for i in range(0, imgheight, height):
        for j in range(0, imgwidth, width):
            box = (j, i, j + width, i + height)
            a = im.crop(box)
            try:
                type = "terrain"
                set = "train"
                if random.randrange(0, 5) < 1:
                    set = "valid"
                if (j*1000/width + i//height) in grids:
                    type = "player"
                a.save(f"./split/{set}/{type}/sp-{k}{s}.png")
            except:
                pass
            s += 1


# Clear the existing files
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

print("starting splitter...")

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

k = 0
with open('./coordinates.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    for r in reader:
        try:
            split(r[0], r[1], k)
        except:
            print(f"invalid row: {r}")
        k+=1

        if k%50 == 0:
            print(k)

print("done splitting!")
