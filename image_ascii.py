from PIL import Image
import numpy as np

ASCII_CHARS = "@%#*+=-:. "   
NEW_WIDTH = 100              
INVERT = False               

def resize_image(img, new_width=NEW_WIDTH):
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)  
    return img.resize((new_width, new_height))

def pixel_to_ascii_array(pixels, ascii_chars=ASCII_CHARS):
    scale = (len(ascii_chars) - 1) / 255
    indices = (pixels * scale).astype(int)
    return indices

def image_to_ascii(path, new_width=NEW_WIDTH, invert=INVERT):
    img = Image.open(path).convert('L')   
    img = resize_image(img, new_width)
    pixels = np.array(img)

    indices = pixel_to_ascii_array(pixels)
    ascii_chars = ASCII_CHARS

    if invert:
        ascii_chars = ascii_chars[::-1]  

    ascii_art = "\n".join("".join(ascii_chars[i] for i in row) for row in indices)
    return ascii_art

def save_ascii_art(ascii_art, filename='output.txt'):
    with open(filename, 'w') as f:
        f.write(ascii_art)

if __name__ == "__main__":
    image_path = 'hik.png'  
    ascii_art = image_to_ascii(image_path)

    print(ascii_art)
    save_ascii_art(ascii_art)
    print("\n✅ ASCII Art saved to output.txt")
