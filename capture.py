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

    # sleep(1)

    for i in range(1):
        j0 = str(random.randrange(0, 6))
        j1 = str(random.randrange(2, 8))
        j2 = str(random.randrange(46, 54))
        j3 = str(random.randrange(76, 84))
        seq = format(i, '010d')
        im2 = pyscreenshot.grab(bbox=(0, 0, 300, 300))
        im2.save("test.jpg")

        # call(["screencapture",  f"-R80{j0},57{j1},150,150", "-x", f"{directory}/full/{teams}_{seq}.png"])
        # call(["screencapture", f"-R17{j2},5{j3},150,150", "-x", f"{directory}/team/{teams}_{seq}.png"])
        sleep(1)

    # files = os.listdir(directory+"/full")
    # fileIndexes = random.sample(range(0, len(files)), 10)
    # for i in fileIndexes:
    #     copyfile(directory+"/full/"+files[i], "coordinates/unlabeled/"+files[i])


capture()