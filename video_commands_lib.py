from os import path
import re
from pathlib import Path

from PIL import Image, ImageOps, ImageColor
from rembg import remove
# import autotrace

def vectorize_image(input_path, output_path):
    """Vectorize an image.

    If not given, it will be the same as the input file name
    with the extension ".svg".
    Args:
        image_path (str): The original file to process.
        output_path (str): The name of the file to generate.

    Returns:
        output_path (str): The name of the generated file.
    """
    if not output_path:
        filename = Path(image_path).stem
        output_path = f"{filename}.svg"
    autotrace.svg(input_path, output_path)
    return output_path


def remove_background(image_path, output_path=""):
    """Remove the background from an image using rembg.

    If not given, it will be the same as the input file name
    with the suffix "_removed".
    Args:
        image_path (str): The original file to process.
        output_path (str): The name of the file to generate.

    Returns:
        output_path (str): The name of the generated file.
    """
    if not output_path:
        filename = Path(image_path).stem
        output_path = f"{filename}_removed.png"

    with open(image_path, "rb") as i:
        with open(output_path, "wb") as o:
            input_data = i.read()
            output_data = remove(input_data)
            o.write(output_data)

    return output_path

def normalize_size(width, height, size, default_width, default_height):
    """ Checks if the user has indicated a certain image size, returning width and height.

    Args:
        width (int): The input width.
        height (int): The input height.
        size (str): The input size (in {width}x{height} format)
        default_width (int): Default width.
        default_height (int): Default height.

    Returns:
        width, height: The normalized size of image.
    """

    if not (width or height or size):
        return default_width, default_height
    elif width and height:
        if isinstance(width, int) and isinstance(height, int) and width > 0 and height > 0:
            return width, height
        else:
            return default_width, default_height
    elif size and "x" in size:
        try:
            width, height = map(int, size.split('x'))
            return width, height
        except ValueError:
            return default_width, default_height
    elif width and not height:
        return width, width
    elif not width and height:
        return height, height
    else:
        return default_width, default_height

def normalize_color(color):
    """Normalize and validate the input color.

    This function accepts color values in different formats: RGB hexadecimal,
    hexadecimal with a hashtag, or standard color names. It normalizes the color
    to the RGB hexadecimal format with a hashtag. If the provided color is not
    valid, it returns False.

    Args:
        color (str): The input color value.

    Returns:
        str or False: The normalized color if valid, False otherwise.
    """
    # TODO: Add transparent color.

    hex_color_pattern = re.compile(r'^[0-9a-fA-F]{6}$')
    hex_color_pattern_with_hastag = re.compile(r'^#[0-9a-fA-F]{6}$')
    if hex_color_pattern.match(color):
        color = f"#{color}"
        return color
    elif hex_color_pattern_with_hastag.match(color):
        return color
    # elif color.lower() == "transparent":
    #     return (0, 0, 0, 0)
    else:
        try:
            ImageColor.getrgb(color)
            return color
        except:
            return False


def tint_image(image_path, output_path, color, mode):
    """Tints an image with the indicated color.

    Args:
        image_path (str): Original image.
        output_path (str): Generated image.
        color (str): Color to tint.
        mode (str): Tinting mode (light or dark).

    Returns:
        str: Path to generated image.
    """

    if not output_path:
        filename = Path(image_path).stem
        output_path = f"{filename}_tinted.png"

    img = Image.open(image_path).convert("L")
    if mode.lower() == "dark":
        new_img = ImageOps.colorize(img, black="black", white=color)
    else:
        new_img = ImageOps.colorize(img, black=color, white="white")

    new_img.save(output_path)

    return output_path
