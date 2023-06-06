"""
This module provides functions for fill baseform png files
"""
from PIL import Image, ImageDraw


def fill_character_card(input_file_name, output_file_name, character):
    """
    Contruction in progress...
    Fills specific PNG file with character fields.

    :param input_file_name: The name of the PNG file to fill.
    :type input_file_name: str
    :param output_file_name: The name of the filled PNG file.
    :type output_file_name: str
    :param character: Character containing fields to fill PNG file.
    :type character: Character
    :return: None
    """
    with Image.open(input_file_name).convert("RGBA") as base:
        writer = ImageDraw.Draw(base)
        writer.text((10, 10), "Hello", "black")
        writer.text((10, 60), "World", "black")
        base.save(output_file_name)
        base.show()
