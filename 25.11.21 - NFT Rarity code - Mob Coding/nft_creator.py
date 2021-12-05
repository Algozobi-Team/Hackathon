# --------------------------PEP-8 line limit--------------------------72
# This script randomly selects layers in the "img_layers" directory
# and merges them to a singel .png 
# The Collection limit is set with the "collection_count" variable
# --------------------------PEP-8 line limit--------------------------72

# Import modules
import random
from PIL import Image
import json

# Collection variables
collection_count = 4
nft_number = 1
nft_metadata = []
# List for checking if attributs combination has already been created
attributes_list = []

# Load dictionary of filepaths from filepaths.json and creating 
# list of filepaths
with open('./src/file_paths.json') as file_paths:
    img_dict = list(json.load(file_paths).items())

# Random choice function creating list of attributs for single nft
def attributes():
    attribute_list = []
    for i in range(2):
        attributes  = img_dict[i][1]
        random_int = random.randint(0, 3)
        if random_int in range(4):
            attribute_list.append(attributes[random_int])

    for i in range(2,4):
        attributes  = img_dict[i][1]
        random_int = random.randint(0, 7)
        if random_int in range(4):
            attribute_list.append(attributes[random_int])
    
    return attribute_list

# Merge attribute layers into one png
def merge_layers_a(layers, nft_number):
    a = Image.open(layers[0])
    b = Image.open(layers[1])
    nft = Image.alpha_composite(a,b)
    remove_layer(layers)
    merge_layers_b(nft, layers, nft_number)

def merge_layers_b(nft, layers, nft_number):
    if len(layers) == 0:
        file_name ='./nft_collection/' + str(nft_number) + '.png'
        nft.save(file_name)
    else:
        c = Image.open(layers[0])
        nft_2 = Image.alpha_composite(nft, c)
        remove_layer(layers)
        merge_layers_b(nft_2, layers, nft_number)

# Removes layer from layers list after layer has been merged
def remove_layer(layers):
    layers.remove(layers[0])

# Create list "atb" of dictionary's with with attributes 
# of every nft created
def metadata_json(layers):
    atb = [nft_number]
    for i in range(len(layers)):
        attribute = layers[i]
        split_list = attribute.split('/')
        trait_type = split_list[2]
        for i in range(3):
            split_list.remove(split_list[0])

        cleand_attribute = split_list[0].split('.')
        cleand_attribute.remove(cleand_attribute[1])
        atb.append({
            'trait_type' : trait_type,
            'value' : cleand_attribute[0]
        })
    nft_metadata.append(atb)

# Write "attributs.json" with all attributes of all nfts
def create_metadata_json(nft_metadata):
    with open('./src/attributes.json', 'a') as md:
        json.dump(nft_metadata, md, indent = 4)

# NFT creation loop
while nft_number <= collection_count:
    layers = attributes()
    if layers not in attributes_list:
        attributes_list.append(layers)
        metadata_json(layers)
        merge_layers_a(layers, nft_number)
        nft_number += 1

# Write "attributs.json" with all attributes of all nfts
create_metadata_json(nft_metadata)

# --------------------------PEP-8 line limit--------------------------72