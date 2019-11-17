from PIL import Image


def combine():
    directory = "games/mmm_uol_worlds_2019/bottom"

    image1 = Image.open(directory+"/105.jpg")
    image2 = Image.open(directory+"/106.jpg")
    image3 = Image.open(directory + "/107.jpg")
    image4 = Image.open(directory + "/108.jpg")
    image5 = Image.open(directory + "/109.jpg")
    image6 = Image.open(directory + "/110.jpg")
    image7 = Image.open(directory + "/111.jpg")
    image8 = Image.open(directory + "/112.jpg")
    image9 = Image.open(directory + "/113.jpg")


    image11 = image1.convert("RGBA")
    image22 = image2.convert("RGBA")
    image33 = image3.convert("RGBA")
    image44 = image4.convert("RGBA")
    image55 = image5.convert("RGBA")
    image66 = image6.convert("RGBA")
    image77 = image7.convert("RGBA")
    image88 = image8.convert("RGBA")
    image99 = image9.convert("RGBA")


    alphaBlended1 = Image.blend(image11, image22, alpha=0.5)
    alphaBlended2 = Image.blend(image33, image44, alpha=0.5)
    alphaBlended3 = Image.blend(image55, image66, alpha=0.5)
    alphaBlended4 = Image.blend(image77, image88, alpha=0.5)

    alphaBlended5 = Image.blend(alphaBlended1, alphaBlended2, alpha=0.5)
    alphaBlended6 = Image.blend(alphaBlended3, alphaBlended4, alpha=0.5)
    alphaBlended7 = Image.blend(alphaBlended5, alphaBlended6, alpha=0.5)

    alphaBlended4 = Image.blend(alphaBlended7, image99, alpha=0.5)

    alphaBlended4.save("games/mmm_uol_worlds_2019/blended_bottom/blended.png")

combine()