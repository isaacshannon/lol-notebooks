import os

def rename():
    i = 0
    games_dir = "./games/"
    games = os.listdir(games_dir)
    for g in games:
        if "." in g:
            continue
        image_folder_dir = games_dir + g
        image_folders = os.listdir(image_folder_dir)
        for f in image_folders:
            images_dir = image_folder_dir + "/" + f
            images = os.listdir(images_dir)
            for img in images:
                num = img.replace(".jpg", "")
                if g not in img:
                    os.rename(images_dir + "/" + img, images_dir + "/" + g + "_" + num + ".jpg")
                i+=1

rename()