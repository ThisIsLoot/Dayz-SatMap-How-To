# Dayz SatMap How-To

This explains step-by-step how to create a high-resolution satellite map from the DayZ game files. If you need help or have any questions, feel free to ask in [Discord](https://discord.com/invite/676ASkJpa5).

## Find all of the satellite map tiles in the game files
This assumes you have your P: drive set up. If you don't, see [here](https://community.bistudio.com/wiki/DayZ:Modding_Basics#:~:text=on%20its%20track.-,Setting%20up%20the%20Project%20Drive,-Create%20a%20Project). 

The map is divided into tiles in the game files. They are located in the following folders:
- **Chenarus**: `P:\DZ\worlds\chernarusplus\data\layers`
- **Livonia**: `P:\DZ\worlds\enoch\data\layers`
- **Sakhal**: `P:\sakhal\Addons\worlds_sakhal_data\DZ\worlds\sakhal\data\layers`

In those folders, each .paa file is a map tile. The files that start with an "S", for example, `S_000_000_lco.paa` are sat map tiles. The files that start with "M" are mask tiles (which we won't discuss here but you can follow the same process if you want the mask map). The map is divided into a 32x32 grid and the numbers in the file names are that tile's place on the grid. So `S_000_000_lco.paa` is row 0, column 0. `S_000_001_lco.paa` is row 0, column 1, for example. 

*But the .paa format isn't helpful for our purposes. We need to convert .paa to .png in bulk since there are a ton of them (32`*`32 = 1,024 tiles)*

## Convert the .paa map tiles to .png
Luckily this is possible with a tool included in DayZ tools called ImagetoPAA. Despite the name, it can also convert the other direction from .paa to .png.

Find the ImagetoPAA executable on your computer. For me it was located here:

`C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA\ImagetoPAA.exe`

Note: if you need a tool that makes searching your Windows computer really really easy, I recommend [Everything](https://www.voidtools.com/support/everything/).

Now open the included `batchConvert.py` file in a text editor and define the paths at the beginning of the file (lines 7-9). 

Execute that file in a terminal/command window (you obvs need Python installed and working).

Be patient, it will take some time. When finished check your output folder and see all of the tiles in .png format. 

## Combine the .pngs into a single large map file
Finally, we need to stitch the files together to make the full high-resolution sat map. 

Open the included `combinePngs.py` file and set the input folder path where all of your map tile .pngs are located and set the output path where you want the final image to be stored (lines 11 and 12).

Execute the file. 

**Voilà**, if everything worked as it should, there should be a huge high-res sat map in the output location. 

## BONUS
If you want to now reslice the map into tiles to be sorted and formatted to use in a zoomable map like on the [ThisIsLoot website](https://thisisloot.com/guides/dayz-loot-finder) using a library like [Leaflet](https://leafletjs.com/), you can use the included `mapTileSlicer.py` file. Be sure to set the paths on line 9 and line 12 before executing the file. Not only will this generate the files, it will generate a simple html file that you can open in your browser to see the map. 
