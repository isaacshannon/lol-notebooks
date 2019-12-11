import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import os
import csv

grid_size = 10
grid_lines = int(150/grid_size)

unlabeled_path = "./unlabeled/"

def save_map_grid():
    root.labels = [str(l[0] * 1000 + l[1]) for l in root.labels]
    root.labels = list(set(root.labels))
    root.labels.sort()
    root.labels = " ".join(root.labels)
    data = [root.image_list[root.img_index], root.labels]
    root.writer.writerow(data)
    root.labels = []
    os.rename(unlabeled_path + root.image_list[root.img_index],
              "./coordinate_images/" + root.image_list[root.img_index])

def change_pic():
    save_map_grid()

    root.img_index += 1
    draw_map()

    map_name_label.configure(text=root.image_list[root.img_index])

def undo():
    root.labels.pop()
    draw_map()

def draw_grid(draw):
    fill = (0, 0, 255, 96)
    for x in range(grid_lines):
        z = grid_size*x
        draw.line([z, 0, z, 150], fill=fill)
        draw.line([0, z, 150, z], fill=fill)

    fill = (0, 255, 255, 96)
    for l in root.labels:
        x = l[0] * grid_size
        y = l[1] * grid_size
        draw.rectangle((x, y, x + grid_size, y + grid_size), fill=fill)

def printcoords(event):
    x = event.x-grid_size/2
    if x < 0: x=0
    x = int(x//grid_size)
    y = event.y-grid_size/2
    if y < 0: y=0
    y = int(y//grid_size)
    root.labels.append([x, y])
    draw_map()
    print (root.labels)

def draw_map():
    img = Image.open(unlabeled_path + root.image_list[root.img_index])
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    draw_grid(draw)
    out = Image.alpha_composite(img, overlay)
    root.photo = ImageTk.PhotoImage(out)
    map_label.configure(image=root.photo)

root = tk.Tk()
images = os.listdir(unlabeled_path)
images.sort()
root.image_list = images
root.img_index = 0
root.labels = []

map_label=tk.Label(root)
map_label.bind("<Button 1>", printcoords)
map_label.pack()
draw_map()

map_name_label=tk.Label(root, text=images[0])
map_name_label.pack()

save_btn=tk.Button(root, text="Save", command=change_pic)
save_btn.pack()
undo_btn=tk.Button(root, text="Undo", command=undo)
undo_btn.pack()

with open( "./coordinates.csv", "a") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    root.writer = writer

    root.mainloop()