import sys
import os
from PIL import Image
import glob

path_read = sys.argv[1]
path_save = sys.argv[2]

if not os.path.exists(path_save):
    os.makedirs(path_save)

for file in os.listdir(path_read):  # glob.glob(path_read+ '*.png')
    if file.endswith('jpeg'):
        img = Image.open(f'{path_read}{file}')
        clean_name = os.path.splitext(file)[0] # 0 is filename and 1 is formate (JPEG or PNG etc)
        img.save(f'{path_save}{clean_name}.png', 'png')
        print('all done!')

