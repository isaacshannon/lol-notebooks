import os
from PIL import Image

def resize():
    i = 0
    dirs = ["./games/lk_mg_worlds_2019/team"]
    for d in dirs:
        images = os.listdir(d)
        for img in images:
            path = d + "/" + img
            im = Image.open(path)
            width, height = im.size
            if width is not 150 or height is not 150:
                i+=1
                im = im.resize((150, 150))
                im.save(d + "-resized/" + img.replace(".jpg", ".png"))
                print(f"{i} resizing: {path}")

resize()