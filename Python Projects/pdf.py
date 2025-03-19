from PIL import Image
import os
from tqdm import tqdm  # Progress bar library

# Define standard paper sizes (300 DPI)
PAPER_SIZES = {
    "A0": (9933, 14043),
    "A1": (7016, 9933),
    "A2": (4961, 7016),
    "A3": (3508, 4961),
    "A4": (2480, 3508),
    "A5": (1748, 2480),
    "A6": (1240, 1748),
}

def images_to_pdf(folder_path, output_pdf, paper_size="A4"):
    paper_size = paper_size.upper()
    if paper_size not in PAPER_SIZES:
        print(f"Invalid paper size! Choose from: {', '.join(PAPER_SIZES.keys())}")
        return

    page_size = PAPER_SIZES[paper_size]

    # Get all image files
    image_files = sorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'tiff'))]
    )

    if not image_files:
        print("No images found in the folder!")
        return

    pages = []
    print(f"Processing {len(image_files)} images...")

    for file in tqdm(image_files, desc="Converting Images", unit="image"):
        img = Image.open(os.path.join(folder_path, file)).convert("RGB")

        # If image is larger than the paper size, resize while keeping aspect ratio
        if img.width > page_size[0] or img.height > page_size[1]:
            img.thumbnail(page_size)

        # Create a blank white page of the target size
        page = Image.new("RGB", page_size, "white")

        # Center the image on the page
        x_offset = (page_size[0] - img.width) // 2
        y_offset = (page_size[1] - img.height) // 2
        page.paste(img, (x_offset, y_offset))

        pages.append(page)

    print("Saving PDF...")
    pages[0].save(output_pdf, save_all=True, append_images=pages[1:], quality=100)

    print(f"✅ PDF saved successfully as {output_pdf}")

# Example usage:
# images_to_pdf("path/to/image_folder", "output.pdf", paper_size="A3")
images_to_pdf("H:\manga\Kimi-No-Na-Wa\Chapter_0001", "output2.pdf")
