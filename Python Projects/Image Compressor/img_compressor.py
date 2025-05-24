from PIL import Image
import os
print("Current working directory:", os.getcwd())


def compress_image(input_path, quality=70, scale=0.5):
    
    im = Image.open(input_path)
    r,g,b = im.split()
    im.show()

    temp = Image.merge("RGB",(b,g,r))
    temp.show()


compress_image(r"I:\LeetCode\Python Projects\Image Compressor\raw_img.jpg", quality=50, scale=0.5)
