# shikoku88map4print
Collection of various data, scripts and tools used for creating a A0 or A1 sized physical printed map of the Shikoku Henro pilgrimage trail

## Background
In 2024, I spent a total of 9 weeks, travelling (mostly walking) the Shikoku Pilgrimage - or Shikoku 88, as it is often known - https://en.wikipedia.org/wiki/Shikoku_Pilgrimage. The route is 1100km long and roughly follows the coast around the island of Shikoku in Japan.
In the months before leaving for Shikoku, I wanted to get a large printout of the island/route, just to hang on the wall. As things tend to, it slowly escalated into a larger project, as I kept coming up with extra details I wanted on the map. 
The methods used here could be applied to any XYZ Raster tile provider/server (https://wiki.openstreetmap.org/wiki/Raster_tile_providers) - personally I used Maptiler. *BIG* kudos to Maptiler support, who helped me out with a few smaller graphical technical issues - fast, efficient, competent support, from actual humans.
As a sample/demo, the .py contains code for the official OpenStreetMap site for basemap and waymarkedtrails.org for highlighting route.
All in all, this turned out to be a fun, but quite timeconsuming project, that nontheless did result in a really-really-large printed map (well, A0), now hanging on my wall. There are -without a doubt- smarter, faster and cleaner ways to achieve this (I am not a coder by day. And a bad one, by night) - the solution I wound up with, just sort of happened. I had zero experience with OpenStreetMap, OSM tiles, .geojson files, the local Japanese railway lines and Python-scripted image manipulation before starting this project.

## Final result (additional data added to map)
- The 1100km hiking trail (red trail marking)
- Most difficult sections (purple trail marking)
- All 88 temples with distance to next temple, on the ones far between
- Most important huts/shelters/camping sites marked
- Small tweaks and changes to colors, fonts, text sizes and icon scaling
- 'JR Shikoku' railway lines and stations along pilgrimage route highlighted
- Localization set to English, so Kanji characters will only be used if no translation exists

## Prerequisite
Python3 with Pillow library - pip3 install Pillow
Script tested and developed using Python 3.10.12 and Pillow 10.1.0

## Files contained in this project
- Shikoku88map4print.py - Python script based on bigmap2 doing the heavy lifting;
 - downloads individual image tiles and pastes them together
 - inserts/draws a 2x2km grid system across the map
 - inserts 10-50-100km scale distance ruler at the bottom
 - writes copyright attribution information
- HenroHuts.geojson - coordinates for shelters i .geojson format
- Shikoku88Temples.geojson - coordinates for all 88 temples
- ShikokuPilgrimageDifficultSections.geojson - 'MultiLineString' trail marking of hardest sections of the route
- demo_shikoku88map4print.png - .png sample, smaller, not all details included
- demo_shikoku88map4print_fullsize.jpeg - .jpeg compressed map sample
- scale_100km.png - Image pasted into final image for displaying a 100KM distance scale
- Roboto-Black.ttf - Font used for embedding text into image

## Tools, scripts and datasources used
- Maptiler - https://maptiler.com - the glue that binds everything together. Using the Maptiler 'outdoor' OSM tileset as a base, I created my own tileset and was able to tweak the look and design to look just the way I wanted it. Maptiler also support inserting custom datasets like the .geojson data collected above
- OpenStreetMap - https://www.openstreetmap.org - the 'base' mapdata used
- bigmap2 - https://github.com/zverik/bigmap2 - for pulling down individual 512x512px grid images from OSM and pasting them together
- Toolforge / geoexport - https://geoexport.toolforge.org/ - exporting longitude/latitude coordinates of all 88 temples from Wikipedia and exporting to .geojson file
- Henro Helper app - https://play.google.com/store/apps/details?id=com.henrohelper100.app - difficulty markings on different sections of the route (spoiler alert; mountains are tough)
- Henro.org - https://henro.org - overview of pilgrim shelters and housings with long/lati coordinates
