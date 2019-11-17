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
        os.makedirs(directory + "/full-pilled")
    except:
        pass

    try:
        os.makedirs(directory + "/team")
    except:
        pass

    try:
        os.makedirs(directory + "/team-pilled")
    except:
        pass

def capture():
    teams = "fla_ryl_worlds_2019"
    directory = "games/" + teams
    make_dirs(directory)

    sleep(5)

    for i in range(1500):
        call(["screencapture",  "-R815,665,150,150", "-x", f"{directory}/full/{teams}_{i}.png"])
        call(["screencapture", "-R1800,675,150,150", "-x", f"{directory}/team/{teams}_{i}.png"])
        sleep(1)

capture()