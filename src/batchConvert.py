# This file batch converts .paa files to .png files

import os
import subprocess

#! Define paths
input_folder = r"P:\DZ\worlds\chernarusplus\data\layers" # Location of the map tile .paa files
output_folder = r"C:\Users\[YOU]\Desktop\test\satTiles\chernarusplus" #TODO Change your name or it won't work...obviously Or set a different path
exe_path = r"C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA\ImagetoPAA.exe" # Path to ImageToPAA.exe

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through each .paa file in the input folder
for filename in os.listdir(input_folder):

    
    if filename.endswith(".paa") and filename.lower().startswith("s"): # Change the "s" to "m" if you want to convert mask tiles
        # Define input and output paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".paa", ".png"))
        
        # Run ImageToPAA.exe with the input and output paths
        subprocess.run([exe_path, input_path, output_path])
        
        print(f"Converted {filename} to PNG format.")

print("Batch conversion completed.")





