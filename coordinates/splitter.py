from PIL import Image
import os
import csv



def split(filename, player_grids, k):
    s = 0
    grids = [int(i) for i in player_grids.split(" ")]
    print(grids)

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
                if (j*1000/width + i//height) in grids:
                    type = "player"
                a.save(f"./split/{type}/sp-{k}{s}.png")
            except:
                pass
            s += 1

k = 0
with open('./coordinates.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    for r in reader:
        split(r[0], r[1], k)
        k+=1
