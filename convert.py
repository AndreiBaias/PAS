
import numpy as np
import collections, numpy
import glob
from PIL import Image
from matplotlib.pyplot import cm
nrImages = 1
imageSize = 449
finalImageSize = 449
ImageNumber = 0

sourceFolder = 'images'
# sourceFolder = "testInput"
destinationFolder = 'final_text_files_2'
# destinationFolder = "testOutput"

def modifica(a):
    for i in range(imageSize):
        for j in range(imageSize):
            if a[i][j] > 170:
                a[i][j] = 255
            elif a[i][j] > 120:
                a[i][j] = 128
            else:
                a[i][j] = 0
    return a


def veciniNegrii(a, x, y):
    s = 0
    ValoareNegru = 0
    try:
        if a[x - 1][y - 1] == ValoareNegru:
            s += 1
    except:
        None
    try:
        if a[x - 1][y] == ValoareNegru:
            s += 1
    except:
        None
    try:
        if a[x - 1][y + 1] == ValoareNegru:
            s += 1
    except:
        None
    try:
        if a[x][y + 1] == ValoareNegru:
            s += 1
    except:
        None
    try:
        if a[x][y - 1] == ValoareNegru:
            s += 1
    except:
        None
    try:
        if a[x + 1][y + 1] == ValoareNegru:
            s += 1
    except:
        None
    try:
        if a[x + 1][y] == ValoareNegru:
            s += 1
    except:
        None
    try:
        if a[x + 1][y - 1] == ValoareNegru:
            s += 1
    except:
        None
    return s


def eliminaExtraCladiri(a):
    for i in range(imageSize):
        for j in range(imageSize):
            if a[i][j] == 128 and veciniNegrii(a, i, j) >= 2:
                a[i][j] = 255
    return a


# image = Image.open("1570.png").convert("L")
# print(np.asarray(image))

index = 0
for filename in glob.glob(sourceFolder + '/*.png'):
    image = Image.open(filename).convert("L")
    imageArray = np.asarray(image)
    imageArray = modifica(imageArray)
    eliminaExtraCladiri(imageArray)
    g = open("./" + destinationFolder + "/map" + str(index) + ".txt", "w")
    g.write("")
    g.close()
    g = open("./" + destinationFolder + "/map" + str(index) + ".txt", "a")
    g.write(str(len(imageArray)) + "\n" + str(len(imageArray)) + "\n")
    for x in imageArray:
        for y in x:
            g.write(str(y) + " ")
        g.write("\n")
    index += 1
    if index % 100 == 0:
        print(index)
print(index)



# for i in range(nrImages):
#     image = Image.open("./final_images/_2O7gRvMPVdPfW9Ql60S-w.png").convert("L")
#     # image = image.resize((imageSize, imageSize), Image.ANTIALIAS)
#
#     imageArray = np.asarray(image)
#     print(imageArray.shape)
#     imageArray = modifica(imageArray)
#     eliminaExtraCladiri(imageArray)
#     print(imageArray)
#     g = open("map2.txt", "w")
#     g.write("")
#     g.close()
#     g = open("map2.txt", "a")
#     g.write(str(len(imageArray)) + "\n" + str(len(imageArray)) + "\n")
#     for x in imageArray:
#         for y in x:
#             g.write(str(y) + " ")
#         g.write("\n")