from PIL import Image
from os import listdir
import sys
path = "github/textToSymbols/images/"
imagelist = listdir(path)
stone = {}
symbolsUsed = []
text = str(input())

for image in imagelist:
    dicValues = image.split(".")
    stone[dicValues[0]] = image

text = text.split(" ")
for word in text:
    symbolsUsed.append(Image.open(path +stone[word]))

widths, heights = zip(*(i.size for i in symbolsUsed))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in symbolsUsed:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save(path + "file.jpg")
