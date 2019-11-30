from fastai.vision import *

path = "./pills/images"
file=open(path+"/coordinates.csv", "r")
reader = csv.reader(file)
img_to_points = {}
for row in reader:
    points = [float(v) for v in row[1:]]
    coords = [[points[i], points[i+1]] for i in range(0, len(points), 2)]
    team1 = sorted(coords[:5] , key=lambda k: [k[1], k[0]])
    team2 = sorted(coords[5:], key=lambda k: [k[1], k[0]])
    coords = team1 + team2
    img_to_points[row[0]] = tensor(coords)

def get_points(f):
    return img_to_points[os.path.basename(f)]

data = (PointsItemList.from_folder(path)
        .split_by_rand_pct(0.15)
        .label_from_func(get_points)
        .transform([], size=(150,150))
        .databunch(bs=4).normalize(imagenet_stats)
       )

learn = cnn_learner(data, models.resnet34)
learn.lr_find()
learn.recorder.plot()
