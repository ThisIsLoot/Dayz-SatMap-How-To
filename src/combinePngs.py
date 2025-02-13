from PIL import Image, ImageDraw
import os
import re

# Disable the decompression bomb check
Image.MAX_IMAGE_PIXELS = None

print("Combining .pngs..")

#! Define the folder containing .png files and output path
input_folder = r"C:\Users\[YOU]\Desktop\test\satTiles\chernarusplus" # TODO change to your username or it won't work, or define a different path
output_image_path = r"C:\Users\[YOU]\Desktop\test\chernarusplus_sat_map_final.png" # TODO change to your username or it won't work, or define a different path
grid_size = 32  # Number of rows and columns

# Image filename pattern to extract row and column numbers
# Change the "S" to "M" if you are doing the mask tiles
pattern = re.compile(r"S_(\d{3})_(\d{3})_lco\.png", re.IGNORECASE)

# Dictionary to store cropped images by position
image_grid = {}

# Load and crop images, then store them in the dictionary by (column, row)
for filename in os.listdir(input_folder):
    match = pattern.match(filename)
    if match:
        col = int(match.group(1))
        row = int(match.group(2))
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Crop 16 pixels from all sides of the tile
        cropped_img = img.crop((16, 16, img.width - 16, img.height - 16))
        image_grid[(col, row)] = cropped_img

# Get the size of one cropped tile (assuming all tiles are the same size)
tile_width, tile_height = next(iter(image_grid.values())).size

# Create a new blank image for the combined map
combined_image = Image.new("RGBA", (tile_width * grid_size, tile_height * grid_size))

# Paste each cropped tile into the correct position on the combined image
for row in range(grid_size):
    for col in range(grid_size):
        # Get the cropped image for this tile
        img = image_grid.get((col, row))
        
        if img:
            x = col * tile_width
            y = row * tile_height
            combined_image.paste(img, (x, y))

            # Debug output for each tile placement
            print(f"Placing tile at row {row}, col {col}: x = {x}, y = {y}")

print("Creating the final image. Takes a minute...")

# Save the combined map image
combined_image.save(output_image_path)
print("Combined map saved as:", output_image_path)
