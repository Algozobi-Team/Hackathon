#  Import modules
from PIL import Image
import random

# list of filepath to individual image layers
img_layer_1 = [
    r'./space/space1.png',
    r'./space/space2.png',
    r'./space/space3.png',
    r'./space/space4.png',
]
img_layer_2 = [
    r'./body/body1.png',
    r'./body/body2.png',
    r'./body/body3.png',
    r'./body/body4.png',
]
img_layer_3 = [
    r'./eyes/eyes1.png',
    r'./eyes/eyes2.png',
    r'./eyes/eyes3.png',
    r'./eyes/eyes4.png'
]
img_layer_4 = [
    r'./mouth/mouth1.png',
    r'./mouth/mouth2.png',
    r'./mouth/mouth3.png',
    r'./mouth/mouth4.png'
]

nft_metadata = []
colletion_size = 40
nft_number = 0

while nft_number < colletion_size:
# randomize choice of all 4 layers
    l1 = random.choice(img_layer_1)
    l2 = random.choice(img_layer_2)
    l3 = random.choice(img_layer_3)
    l4 = random.choice(img_layer_4)

# randomize choice of layers with weights
    # body = random.choices(bodys, weights = (10, 10, 10, 70))[0]
    # eye = random.choices(eyes, weights = (5, 35, 15, 45))[0]
    # mouth = random.choices(mouths, weights = (20, 40, 10, 30))[0]

# check if combinations of layers exists in "nft_metadata"
    layer_combination = l1 + l2 + l3 + l4
    if layer_combination not in nft_metadata:
        
# compile layer_1 and layer_2 and sotring it as variable "l1_l2"
        layer_1 = Image.open(l1)
        layer_2 = Image.open(l2)
        l1_l2 = Image.alpha_composite(layer_1, layer_2)

# compile "l1_l2" with layer_3 and storing it as "l1_l2_l3"
        layer_3 = Image.open(l3)
        l1_l2_l3 = Image.alpha_composite(l1_l2, layer_3)

# compile "l1_l2_l3" with layer_4 and storing as final_nft
        layer_4 = Image.open(l4)
        final_nft = Image.alpha_composite(l1_l2_l3, layer_4)

# exporting "final_nft" as a .png file
        nft_number += 1
        file_extension = '.png'
        file_name = str(nft_number) + file_extension
        final_nft.save(file_name)
        
# append new nft to meta_data list
        nft_metadata.append(layer_combination)
