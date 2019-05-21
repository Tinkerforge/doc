#!/usr/bin/python3

import os
from PIL import Image

for root, dirs, files in os.walk('.'):
    for file in files:
        if '_100.' in file:
            path = os.path.join(root, file)
            width, height = Image.open(path).size

            if width != 100 or height != 100:
                print(path, width, height)
