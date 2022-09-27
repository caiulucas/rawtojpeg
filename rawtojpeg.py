from os import listdir, getcwd
from os.path import isfile, join, abspath

import rawpy
import imageio

path = getcwd()
arwfiles = [f for f in listdir(path) if f.endswith('.arw') or f.endswith('.ARW')]

for arw in arwfiles:
  with rawpy.imread(arw) as raw:
    rgb = raw.postprocess(use_auto_wb=True)

  imageio.imsave(arw.replace('.arw', '.jpeg').replace('.ARW', '.jpeg'), rgb)