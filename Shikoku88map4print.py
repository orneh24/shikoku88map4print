#!/usr/bin/env python
# Generated by BigMap 2 - https://github.com/zverik/bigmap2 - Permalink: http://bigmap.osmz.ru/bigmap.php?xmin=3548&xmax=3585&ymin=1630&ymax=1653&zoom=12&scale=256&tiles=landscape
# Customized by orneh24 for https://github.com/orneh24/shikoku88map4print
# Script below will create a 19456 x 12288 pixel map of Shikoku roughly usable for A1 print
# Using a 512 tile OpenStreepMap server, like Maptiler's Outdoor tileset, will produce a 38912 x 24576 pixel (~560-600 MB) (map designed for A0 printing with some cutting of the edges

import io, urllib.request, datetime, time, re, random
from PIL import Image, ImageDraw
# ^^^^^^ install "python-pillow" package | pip install Pillow | easy_install Pillow

# Coordinates for map
(zoom, xmin, ymin, xmax, ymax) = (13, 7096, 3260, 7171, 3307)
# demo map using default openstreetmap tiles (256px tiles)
layers = ["https://tile.openstreetmap.org/!z/!x/!y.png"]
tilesize = 256
# customized tileset based off Maptiler's Outdoor tileset
#layers = ["https://api.maptiler.com/maps/d13bb37e-ea9c-41d1-933e-4e36c785a0bf/!z/!x/!y.png?key=YOUR-API-KEY"]
#tilesize = 512
attribution = 'Map data (c) OpenStreetMap'
xsize = xmax - xmin + 1
ysize = ymax - ymin + 1

resultImage = Image.new("RGBA", (xsize * tilesize, ysize * tilesize), (0,0,0,0))
counter = 0
for x in range(xmin, xmax+1):
	for y in range(ymin, ymax+1):
		for layer in layers:
			url = layer.replace("!x", str(x)).replace("!y", str(y)).replace("!z", str(zoom))
			match = re.search("{([a-z0-9]+)}", url)
			if match:
				url = url.replace(match.group(0), random.choice(match.group(1)))
			print(url, "... ");
			try:
				req = urllib.request.Request(url, headers={'User-Agent': 'BigMap/2.0'})
				tile = urllib.request.urlopen(req).read()
			except Exception as e:
				print("Error", e)
				continue;
			image = Image.open(io.BytesIO(tile))
			resultImage.paste(image, ((x-xmin)*tilesize, (y-ymin)*tilesize), image.convert("RGBA"))
			counter += 1
			if counter == 10:
				time.sleep(2);
				counter = 0

draw = ImageDraw.Draw(resultImage)
draw.text((5, ysize*tilesize-15), attribution, (0,0,0))
draw = ImageDraw.Draw(resultImage)
# Add a 252x252 px grid to map (2km across)
y_start = 0
y_end = resultImage.height
step_size = 252
for x in range(0, resultImage.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=0)
        x_start = 0
        x_end = resultImage.width

for y in range(0, resultImage.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=0)

del draw

scaleimage = Image.open("scale_100km.png")
# Create a mask from the alpha channel of the km scale image
_, _, _, mask = scaleimage .split()
# Paste the km scale image onto the new image with the mask
resultImage.paste(scaleimage , (0, 0), mask)
now = datetime.datetime.now()
outputFileName = "shikoku88map%02d-%02d%02d%02d-%02d%02d.png" % (zoom, now.year % 100, now.month, now.day, now.hour, now.minute)
resultImage.save(outputFileName)
