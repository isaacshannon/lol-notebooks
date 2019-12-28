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
    teams = "test"
    directory = "games/" + teams
    make_dirs(directory)
    random.seed()

    for i in range(5):
        seq = format(i, '010d')

        full_x = random.randrange(800, 806)
        full_y = random.randrange(572, 578)
        im_full = pyscreenshot.grab(bbox=(full_x, full_y, full_x + 150, full_y + 150))
        im_full.save(f"{directory}/full/{teams}_{seq}.png")

        team_x = random.randrange(1746, 1754)
        team_y = random.randrange(576, 584)
        im_team = pyscreenshot.grab(bbox=(team_x, team_y, team_x + 150, team_y + 150))
        im_team.save(f"{directory}/team/{teams}_{seq}.png")

        print(f"screenshot: {i}")
        sleep(1)

    # Grab a small sample of the screenshots to feed into 10x10 player locator.
    files = os.listdir(directory + "/full")
    file_indexes = random.sample(range(0, len(files)), 10)
    for i in file_indexes:
        copyfile(directory + "/full/" + files[i], "coordinates/unlabeled/" + files[i])


capture()
