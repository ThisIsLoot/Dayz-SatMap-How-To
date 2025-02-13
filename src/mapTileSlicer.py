from PIL import Image
import os
import shutil

# Increase the decompression bomb limit because the file is huge
Image.MAX_IMAGE_PIXELS = None  # Disables the limit

#! Set Path to your large sat map image
input_image_path = r"C:\Users\[YOU]\Desktop\test\chernarusplus_sat_map_final.png"

#! Set Output folder for tiles
output_folder = r"C:\Users\[YOU]\Desktop\test\chernarusplus_sat_map_tiles"
os.makedirs(output_folder, exist_ok=True)

#! Set Tile size (though you probably want 256)
tile_size = 256

def generate_html(output, max_zoom_level, tile_size):
    center = [-tile_size // 2, tile_size // 2]
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
        <meta charset="utf-8">
        <title>EXAMPLE MAP</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" ></script>
        <style>html, body {{height: 100%;margin: 0;padding: 0;}}</style>
        </head>
        <body>
            <div id="myMap" style="width:100%;height:100%"></div>
            <script type="text/javascript">
            var map = L.map('myMap', {{crs: L.CRS.Simple,minZoom: 1, maxZoom:{max_zoom_level-1}, maxNativeZoom:{max_zoom_level-1}}});
            var tile = {{tileSize: L.point({tile_size}, {tile_size})}};
            L.tileLayer('{{z}}/{{x}}/{{y}}.png', tile).addTo(map)
            map.setView({center}, 1);
            </script>
        </body>
    </html>
            """
    with open(f"{output}/index.html", "w") as f:
        f.write(html_content)

def generate_tiles(input_image_path, output_folder, max_zoom=6, tile_size=256):
    # Remove existing output directory and its contents, then recreate it
    if os.path.exists(output_folder):
        print('Clearing any output folder contents...')
        shutil.rmtree(output_folder)  # Deletes the folder and its contents
    os.makedirs(output_folder, exist_ok=True)

    # Open the input image
    original_img = Image.open(input_image_path)
    img_width, img_height = original_img.size
    
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    for z in range(max_zoom + 1):
        # Calculate the dimensions for this zoom level
        zoom_factor = 2 ** z
        scaled_width = tile_size * zoom_factor
        scaled_height = tile_size * zoom_factor

        # Resize the image to the dimensions for this zoom level
        scaled_img = original_img.resize((scaled_width, scaled_height), Image.Resampling.LANCZOS)

        # Calculate the number of tiles (always 2^z for both x and y)
        x_tiles = 2 ** z
        y_tiles = 2 ** z
        total_tiles = x_tiles * y_tiles

        print (f'Creating tiles for zoom level {z}. {x_tiles}x{y_tiles}, {total_tiles} tiles.')

        # Create the zoom-level directory
        zoom_dir = os.path.join(output_folder, str(z))
        os.makedirs(zoom_dir, exist_ok=True)

        # Generate the tiles
        for x in range(x_tiles):
            for y in range(y_tiles):
                # Define the tile's bounding box
                left = x * tile_size
                upper = y * tile_size
                right = left + tile_size
                lower = upper + tile_size

                # Crop the tile from the scaled image
                tile = scaled_img.crop((left, upper, right, lower))

                # Save the tile in the {z}/{x}/{y}.png format
                tile_dir = os.path.join(zoom_dir, str(x))
                os.makedirs(tile_dir, exist_ok=True)
                tile_path = os.path.join(tile_dir, f"{y}.png")
                tile.save(tile_path, "PNG")

    generate_html(output_folder, max_zoom, tile_size)
    print(f"Slicing completed.\nTiles saved in {output_folder}.\nOpen index.html in a browser to see the map.")

# Run the slicing function with max zoom level 6
print('Starting slicing...')
generate_tiles(input_image_path, output_folder, max_zoom=6, tile_size=256)