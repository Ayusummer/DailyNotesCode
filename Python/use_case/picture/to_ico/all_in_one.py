from PIL import Image
import sys


def convert_to_ico(
    input_file,
    output_file,
    sizes=[(256, 256), (64, 64), (48, 48), (32, 32), (24, 24), (20, 20), (16, 16)],
):
    """Convert an image file to ico format with multiple sizes.

    Args:
        input_file (str): The path to the input image file.
        output_file (str): The path to the output ico file.
        sizes (list of tuple, optional): The sizes of the ico file. Defaults to [(256, 256), (64, 64), (48, 48), (32, 32), (24, 24), (20, 20), (16, 16)].
    """
    img = Image.open(input_file)
    img.save(output_file, "ICO", sizes=sizes)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_to_ico.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_to_ico(input_file, output_file)
