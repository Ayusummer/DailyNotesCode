from PIL import Image
import sys


def convert_to_ico(input_file, output_file, size=(32, 32)):
    """Convert an image file to ico format.

    Args:
        input_file (str): The path to the input image file.
        output_file (str): The path to the output ico file.
        size (tuple, optional): The size of the ico file. Defaults to (32, 32).
    """
    img = Image.open(input_file)
    img = img.resize(size, Image.LANCZOS)
    img.save(output_file, "ICO")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_to_ico.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_to_ico(input_file, output_file)
