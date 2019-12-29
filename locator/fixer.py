import csv
import os

# This script will remove files marked in the coordinates_broken.csv from the locator.csv file.
# Also the file will be moved from the `coordinate_images` directory to `unlabeled` directory.
print(os.listdir())
broken_files = []
with open('coordinates_broken.csv', 'r') as broken:
    for r in broken:
        r = r.replace("\n", "")
        broken_files.append(r)

with open('coordinates.csv', 'r') as inp, open('coordinates_fixed.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[0] not in broken_files:
            writer.writerow(row)
        else:
            os.rename(f"./coordinate_images/{row[0]}", f"./unlabeled/{row[0]}")

os.rename(f"./coordinates_fixed.csv", f"./coordinates.csv")
os.remove('coordinates_broken.csv')