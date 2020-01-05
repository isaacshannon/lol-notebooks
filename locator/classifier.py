import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import os
import csv
import random

grid_size = 10
grid_lines = int(150 / grid_size)

source_dir = "./newdata/split"
dest_dir = "./newdata/train"


def next_img(dest):
    root.moved_images.append(dest)
    root.img_index += 1
    draw_map()
    img = root.image_list[root.img_index]
    map_name_label.configure(text=img)


def blue():
    img = root.image_list[root.img_index]
    dest = f"{dest_dir}/blue/{img}"
    os.rename(f"{source_dir}/{img}", dest)
    next_img(dest)


def red():
    img = root.image_list[root.img_index]
    dest = f"{dest_dir}/red/{img}"
    os.rename(f"{source_dir}/{img}", dest)
    next_img(dest)


def blue_red():
    img = root.image_list[root.img_index]
    dest = f"{dest_dir}/blue-red/{img}"
    os.rename(f"{source_dir}/{img}", dest)
    next_img(dest)


def terrain():
    img = root.image_list[root.img_index]
    dest = f"{dest_dir}/terrain/{img}"
    os.rename(f"{source_dir}/{img}", dest)
    next_img(dest)


def undo():
    img = root.moved_images.pop()
    name = img.split("/")[-1]
    root.img_index -= 1
    os.rename(img, f"{source_dir}/{name}")
    img = root.image_list[root.img_index]
    map_name_label.configure(text=img)
    draw_map()


def draw_grid(draw):
    fill = (255, 255, 255, 96)
    for x in range(grid_lines):
        z = grid_size * x
        draw.line([z, 0, z, 150], fill=fill)
        draw.line([0, z, 150, z], fill=fill)


def draw_map():
    img = Image.open(f"{source_dir}/{root.image_list[root.img_index]}").convert('RGBA')
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    draw_grid(draw)
    out = Image.alpha_composite(img, overlay)
    root.photo = ImageTk.PhotoImage(out)
    map_label.configure(image=root.photo)


root = tk.Tk()
images = os.listdir(source_dir)
random.shuffle(images)
root.image_list = images
root.img_index = 0
root.moved_images = []

map_label = tk.Label(root)
map_label.pack()
draw_map()

map_name_label = tk.Label(root, text=images[0])
map_name_label.pack()

terrain_btn = tk.Button(root, text="Terrain", command=terrain, bg="brown")
terrain_btn.pack()
blue_btn = tk.Button(root, text="Blue", command=blue, bg="blue")
blue_btn.pack()
red_btn = tk.Button(root, text="Red", command=red, bg="red")
red_btn.pack()
blue_red_btn = tk.Button(root, text="Blue Red", command=blue_red, bg="purple")
blue_red_btn.pack()


undo_btn = tk.Button(root, text="Undo", command=undo)
undo_btn.pack()

with open("./coordinates.csv", "a") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    root.writer = writer

    root.mainloop()
