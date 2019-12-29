import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import os
import csv
import random
from datetime import datetime

random.seed(datetime.now())
grid_size = 10
grid_lines = int(150 / grid_size)
labeled_path = "./coordinate_images/"


def change_pic():
    root.img_index += 1
    draw_map()
    map_name_label.configure(text=root.image_list[root.img_index])


def undo():
    root.labels.pop()
    draw_map()


def draw_grid(draw, img_name):
    fill = (0, 0, 255, 96)
    for x in range(grid_lines):
        z = grid_size * x
        draw.line([z, 0, z, 150], fill=fill)
        draw.line([0, z, 150, z], fill=fill)

    labels = root.positions[img_name]
    labels = labels.split(" ")
    labels = [(int(l)//1000, int(l) % 1000) for l in labels]

    fill = (0, 255, 255, 96)
    for l in labels:
        x = l[0] * grid_size
        y = l[1] * grid_size
        draw.rectangle((x, y, x + grid_size, y + grid_size), fill=fill)


def draw_map():
    img_name = root.image_list[root.img_index]
    img = Image.open(labeled_path + img_name).convert('RGBA')
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    draw_grid(draw, img_name)
    out = Image.alpha_composite(img, overlay)
    root.photo = ImageTk.PhotoImage(out)
    map_label.configure(image=root.photo)


def fix():
    data = [root.image_list[root.img_index]]
    root.writer.writerow(data)
    change_pic()


root = tk.Tk()
images = os.listdir(labeled_path)
random.shuffle(images)
root.image_list = images
root.img_index = 0
root.positions = {}
root.fix = []

map_label = tk.Label(root)
map_label.pack()

map_name_label = tk.Label(root, text=images[0])
map_name_label.pack()

save_btn = tk.Button(root, text="Next", command=change_pic)
save_btn.pack()

save_btn = tk.Button(root, text="Fix", command=fix)
save_btn.pack()

with open("./coordinates.csv", "r") as csv_read_file:
    reader = csv.reader(csv_read_file, delimiter=',')
    positions = {}
    for r in reader:
        positions[r[0]] = r[1]
    root.positions = positions

with open("coordinates_broken.csv", "w") as csv_fix_file:
    writer = csv.writer(csv_fix_file, delimiter=',')
    root.writer = writer

    root.mainloop()
