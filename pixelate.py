from PIL import Image, ImageEnhance, ImageFilter
import os


def pixelate(input_path, output_path, pixel_size=7, num_colors=48):
    """
    Convert a photo into pixel art.

    pixel_size: bigger = more pixelated/blocky (try 8, 16, 32)
    num_colors: smaller = more retro/limited palette (try 16, 32, 64)
    """
    img = Image.open(input_path).convert("RGB")
    original_size = img.size

    # Step 1: boost contrast and saturation BEFORE shrinking.
    img = ImageEnhance.Contrast(img).enhance(1.15)
    img = ImageEnhance.Color(img).enhance(1.3)

    # Step 1b: slight blur removes noise/graininess so color blocks
    # come out clean instead of speckled.
    img = img.filter(ImageFilter.GaussianBlur(radius=1))

    # Step 2: shrink down — this creates the "pixel" blocks
    small_size = (
        max(1, original_size[0] // pixel_size),
        max(1, original_size[1] // pixel_size)
    )
    small_img = img.resize(small_size, Image.BILINEAR)

    # Step 3: reduce color palette for a retro pixel-art feel
    small_img = small_img.quantize(
        colors=num_colors,
        method=Image.MAXCOVERAGE,
        dither=Image.NONE
    ).convert("RGB")

    # Step 4: scale back up using NEAREST so it stays blocky, not blurry
    pixel_img = small_img.resize(original_size, Image.NEAREST)

    pixel_img.save(output_path)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    input_folder = "photos"
    output_folder = "pixel_art"
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            in_path = os.path.join(input_folder, filename)
            out_path = os.path.join(output_folder, f"pixel_{filename}")
            pixelate(in_path, out_path, pixel_size=7, num_colors=48)