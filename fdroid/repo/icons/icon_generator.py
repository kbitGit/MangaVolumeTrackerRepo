from PIL import Image
import sys

sizes = [120,160,240,320,480,640]
def generate_icons(fileName):
    image = Image.open(fileName)
    for size in sizes:
        scaledImage = image.resize((size,size))
        print(f"../icons-{size}/{fileName}")
        scaledImage.save(f"../icons-{size}/{fileName}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        generate_icons(sys.argv[1])

