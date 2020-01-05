import os


for f in os.listdir("./data/valid/player"):
    os.rename(f"./data/valid/player/{f}", f"./newdata/players/{f}")