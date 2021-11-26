#importing libraries
from PIL import Image
import random

#diffrent layers
body = [
    r'./body/b1.pgn',
    r'./body/b2.pgn',
    r'./body/b3.pgn',
    r'./body/b4.pgn',
]
eyes = [
    r'./eyes/e1.pgn',
    r'./eyes/e2.pgn',
    r'./eyes/e3.pgn',
    r'./eyes/e4.pgn'
]
body = [
    r'./mouth/m1.pgn',
    r'./mouth/m2.pgn',
    r'./mouth/m3.pgn',
    r'./mouth/m4.pgn'
]

#merging layers 
img1 = Image.open(r'/body/b1.pgn')
img2 = Image.open(r'/eyes/e1.pgn')

intermedia = Image.alpha_composite(img1, img2)

img3 = Image.open(r'/mouth/m1.pgn')

final = Image.alpha_composite(intermedia, img3)

#saving file
final.save('final.png')