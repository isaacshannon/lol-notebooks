from subprocess import call
from time import sleep
import os

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
    teams = "dfm_spy_worlds_2019"
    directory = "games/" + teams
    make_dirs(directory)

    sleep(5)

    for i in range(1200):
        seq = format(i, '010d')
        call(["screencapture",  "-R815,665,150,150", "-x", f"{directory}/full/{teams}_{seq}.png"])
        call(["screencapture", "-R1770,675,150,150", "-x", f"{directory}/team/{teams}_{seq}.png"])
        sleep(1)

capture()