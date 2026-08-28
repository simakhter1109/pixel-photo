# Pixel Photo
From camera roll -> "PIXEL-CORE". Transform your photos into retro pixel art using Python + Pillow.
 
-------------------------------------------------------------------------------------------------------------------------
Pillow is a Python library for messing with images — resizing, cropping, filtering, transforming and saving them. Perfect for turning your normal pics into pixel-art.

## How it works ---
1. Shrinks the image down to a tiny resolution (creates the "pixel" blocks).
2. Reduces the color palette for a retro look.
3. Boosts contrast, saturation, and removes noise for cleaner results.
4. Scales the image back up using nearest-neighbor scaling to keep hard, blocky edges.

## Usage ---
1. Install dependencies: py -m pip install pillow
2. Put your photos (`.jpg`, `.jpeg`, `.png`) inside the `photos/` folder.
3. Run the script: py pixelate.py
4. Find your pixel-art results inside the `pixel_art/` folder.

## Customization ---
Adjust these values in `pixelate.py`:
- `pixel_size`: bigger = more blocky/pixelated (try 8–32).
- `num_colors`: smaller = more retro/limited palette (try 16–64).
