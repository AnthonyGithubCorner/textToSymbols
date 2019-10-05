from PIL import Image
from os import listdir
import sys
import os
path = "github/textToSymbols/images/"
imagelist = listdir(path)
stone = {}
pgNumber = 1
symbolsUsed = []
print("give text")
text = str(input())
print("give title:")
title = str(input())
os.mkdir(path+title)
for image in imagelist:
    dicValues = image.split(".")
    stone[dicValues[0]] = image

text = text.split(" ")

pageWidth = 450
pageHeight = 650
total_width = pageWidth
max_height = pageHeight

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
y_offset = 0
new_im.paste(Image.open(path+"page.jpg"), (0,0))
for word in text:
    im = Image.open(path +stone[word])

    if (x_offset > pageWidth - im.size[0]):
      y_offset += im.size[1]
      x_offset = 0
    new_im.paste(im, (x_offset,y_offset))
    print(im.size)
    x_offset += im.size[0]

    if (y_offset > pageHeight):
      new_im.save(path+title+"/" + "page" + str(pgNumber) + ".jpg")
      pgNumber += 1
      y_offset = 0
      x_offset = 0
      new_im = Image.new('RGB', (total_width, max_height))
      new_im.paste(Image.open(path+"page.jpg"), (0,0))
    im.close()

new_im.save(path+title+"/" + "page" + str(pgNumber) + ".jpg")
