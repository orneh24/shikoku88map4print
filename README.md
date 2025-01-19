# shikoku88map4print
Collection of various data, scripts and tools used for creating a A0 or A1 sized physical printed map of the Shikoku Henro pilgrimage trail

## Background
In 2024, I spent a total of 9 weeks, walking the Shikoku Pilgrimage - or Shikoku 88, as it is often known - https://en.wikipedia.org/wiki/Shikoku_Pilgrimage. The route is 1100km long and roughly follows the coast around the island of Shikoku in Japan.
In the months before leaving for Shikoku, I wanted to get a large printout of the island/route, just to hang on the wall. This turned into a fun, but quite timeconsuming project, that nontheless did result in a really-really-large printed map.

## Tools, scripts and datasources used
- OpenStreetMap - https://www.openstreetmap.org - the 'base' mapdata used
- bigmap2 - https://github.com/zverik/bigmap2 - for pulling down individual 256x256px grid images from OSM and pasting them together
- Toolforge / geoexport - https://geoexport.toolforge.org/ - exporting longitude/latitude coordinates of all 88 temples from Wikipedia and exporting to .geojson file
- Henro Helper app - https://play.google.com/store/apps/details?id=com.henrohelper100.app - difficulty markings on different sections of the route (spoiler alert; mountains)
- Henro.org - https://henro.org - overview of pilgrim shelters and housings with long/lati coordinates
- Maptiler - https://maptiler.com - the glue that binds everything together. Using the Maptiler 'outdoor' OSM tileset as a base, I created my own tileset and was able to tweak the look and design to look just the way I wanted it. Maptiler also support inserting custom datasets like the .geojson data collected above
