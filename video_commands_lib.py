from os import path
import re
from pathlib import Path

from PIL import Image, ImageOps, ImageColor
from rembg import remove

def remove_background(image_path, output_path):
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
    hex_color_pattern = re.compile(r'^[0-9a-fA-F]{6}$')
    hex_color_pattern_with_hastag = re.compile(r'^#[0-9a-fA-F]{6}$')
    if hex_color_pattern.match(color):
        color = f"#{color}"
        return color
    elif hex_color_pattern_with_hastag.match(color):
        return color
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
