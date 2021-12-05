# --------------------------PEP-8 line limit--------------------------72
# This program is a pipline that creates a .json file containing filepaths
# from all images in the in the "img_layers" folder
# --------------------------PEP-8 line limit--------------------------72

from os import listdir
from os.path import isfile, join
import json

# dictionary with file paths
file_paths = {}

# list of img directory
def dir_list(dir):
    onlydir = [f for f in listdir(dir)]
    return onlydir

# list och folder names
img_folder_list = dir_list('./img_layers')
img_folder_list.sort()
# remove .DS_Store file in mac OS folders
if '.DS_Store' in img_folder_list:
    img_folder_list.remove('.DS_Store')
print('Image folder list created: ' + str(img_folder_list))

# # list of file paths
def file_list(dir):
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    # remove .DS_Store file in mac OS folders   
    if '.DS_Store' in onlyfiles:
        onlyfiles.remove('.DS_Store')
    print('Images filename list created: ' + str(onlyfiles))
    return onlyfiles

# create filepath string for each image in folders
def file_path_string(file, file_path_format):
    temporay_list = []
    for i in range(len(file)):
        file_path = file_path_format + '/' + file[i]
        temporay_list.append(file_path)
    return temporay_list

# create dictionary of all filepaths
def create_dict(folder_list):
    for i in range(len(folder_list)):
        file_path_format = './img_layers/' + folder_list[i]
        file = file_list(file_path_format)
        temporay_list = file_path_string(file, file_path_format)
        # print(temp_list)
        file_paths[folder_list[i]] = temporay_list
        

create_dict(img_folder_list)


# write file paths to .json file
with open('./src/filepaths.json', 'w') as file:
    json.dump(file_paths, file, indent=4)

print('FINISHED -- file_paths.json -- CREATED')

# --------------------------PEP-8 line limit--------------------------72
