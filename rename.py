import os

def rename():
    games_dir = "./games/"
    games = os.listdir(games_dir)
    for g in games:
        if "." in g:
            continue
        image_folder_dir = games_dir + g
        image_folders = os.listdir(image_folder_dir)
        for f in image_folders:
            if "." in f:
                continue
            images_dir = image_folder_dir + "/" + f
            images = os.listdir(images_dir)
            for img in images:
                num = img.replace(".jpg", "")
                num = num.replace(".png", "")
                num = num.replace(g, "")
                num = num.replace("_", "")
                seq = format(int(num), '010d')
                os.rename(images_dir + "/" + img, images_dir + "/" + g + "_" + seq + ".png")

rename()