# --------------------------PEP-8 line limit--------------------------72
# This script creates all metadata for each NFT.
# For this script to work "attributes.json" must first be created
# --------------------------PEP-8 line limit--------------------------72

# Importing modules
import json

# Metadata variables
BASE_IMAGE_URL = 'Replace with image URL'
BASE_NAME = ''

# Read "attributes.json"
with open('./src/attributes.json') as attr_list:
    attributes_list = json.load(attr_list)

# Creating metadata .json files for all NFTs
for i in range(len(attributes_list)):
    BASE_JSON = {
    'name' : attributes_list[i][0],
    'description' : 'Join the Bored Alien Space Club',
    'image' : BASE_IMAGE_URL + str(attributes_list[i][0]) + '.png',
    'attributes' : attributes_list[i][1:len(attributes_list[i])]
    }
    file_name = './metadata/' + str(attributes_list[i][0]) + '.json'
    with open(file_name, 'w') as new:
        json.dump(BASE_JSON, new, indent= 4)

# --------------------------PEP-8 line limit--------------------------72