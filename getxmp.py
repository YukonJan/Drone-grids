# import numpy as np
# import os

#Pillow import
from PIL import Image, ImageDraw
from PIL.ExifTags import TAGS

Image.MAX_IMAGE_PIXELS = None #gets rid of warning about max pixel size

path = r'C:/Oceanography_data/drone_grids/grid4n4s5/DJI_20230912141305_0001_W.JPG'

with Image.open(path) as image:
        xmp = image.getxmp()['xmpmeta']['RDF']['Description']

print(xmp)