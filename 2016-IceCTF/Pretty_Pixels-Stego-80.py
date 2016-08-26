#!/usr/bin/env python

from PIL import Image
from sys import stdout

img = Image.open('pretty_pixels_604e889db44de75ea4541a23e344b80eb315f0faf4136abc6d40e1fff8802c9f.png')
img = img.convert("RGB")

pix = img.load()
x_size, y_size = img.size[0], img.size[1]

def parse_pixels():
  for y in range(y_size):
    for x in range(x_size):
      stdout.write( chr(pix[x,y][0]) + chr(pix[x,y][1]) + chr(pix[x,y][2]) )

parse_pixels();
