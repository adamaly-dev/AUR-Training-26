from PIL import Image
from pathlib import Path

def main():      
    image = Image.open("img.png")
    bw_image = image.convert("L")
    bw_image.show()


main()