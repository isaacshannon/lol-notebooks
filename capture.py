from time import sleep
import os
import pyscreenshot
import random
from datetime import datetime
from shutil import copyfile

random.seed(datetime.now())


def make_dirs(directory):
    try:
        os.makedirs(directory)
    except:
        pass

    try:
        os.makedirs(directory + "/full")
    except:
        pass

    try:
        os.makedirs(directory + "/team")
    except:
        pass


def capture():
    teams = "lcs_2020_jan26_dig_eg"
    num_shots = 1200
    directory = "games/" + teams
    make_dirs(directory)
    if len(os.listdir(directory)) > 100:
        print("The game directory isn't empty!!!")
        return
    random.seed()
    # 30 minutes 1200
    for i in range(num_shots):
        seq = format(i, '010d')

        x = 1471
        min_x = random.randrange(x, x+6)
        y = 763
        min_y = random.randrange(y, y+6)
        im_full = pyscreenshot.grab(bbox=(min_x, min_y, min_x + 150, min_y + 150))
        im_full.save(f"{directory}/full/{teams}_{seq}.png")

        x = 1280
        min_x = random.randrange(x, x + 6)
        y = 770
        min_y = random.randrange(y, y + 6)
        im_team = pyscreenshot.grab(bbox=(min_x, min_y, min_x + 150, min_y + 150))
        im_team.save(f"{directory}/team/{teams}_{seq}.png")

        print(f"screenshot: {i}")
        sleep(1)

    # Grab a small sample of the screenshots to feed into 10x10 player locator.
    files = os.listdir(directory + "/full")
    file_indexes = random.sample(range(0, len(files)), 10)
    for i in file_indexes:
        copyfile(directory + "/full/" + files[i], "locator/unlabeled/" + files[i])


capture()
