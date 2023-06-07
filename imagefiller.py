"""
This module provides functions for fill baseform png files
"""
from PIL import Image, ImageDraw, ImageFont
from constants import basic_skills
import translations


def fill_character_card_front(input_file_name, output_file_name, char):
    """
    Construction in progress...
    Fills front character card PNG file with character fields.

    :param input_file_name: The name of the PNG file to fill.
    :type input_file_name: str
    :param output_file_name: The name of the filled PNG file.
    :type output_file_name: str
    :param char: Character containing fields to fill PNG file.
    :type char: Character
    :return: None
    """
    with Image.open(input_file_name).convert("RGBA") as base:
        writer = ImageDraw.Draw(base)
        # positions and font need to be adjusted
        font = ImageFont.truetype("Vera.ttf", 20)
        max_x = base.size[0]
        max_y = base.size[1]
        writer.text((0.07 * max_x, 0.049 * max_y), char.name, "black", font=font)
        writer.text(
            (0.07 * max_x, 0.07 * max_y),
            translations.race_translate(char.race),
            "black",
            font=font,
        )
        writer.text(
            (0.125 * max_x, 0.091 * max_y),
            char.profession.capitalize(),
            "black",
            font=font,
        )
        writer.text((10, 10), str(char.age), "black", font=font)
        writer.text((10, 10), char.eye, "black", font=font)
        writer.text((10, 10), char.hair, "black", font=font)
        writer.text((10, 10), char.star, "black", font=font)
        writer.text((10, 10), char.sex, "black", font=font)
        writer.text((10, 10), str(char.weight), "black", font=font)
        writer.text((10, 10), str(char.height), "black", font=font)
        writer.text((10, 10), str(char.siblings), "black", font=font)
        writer.text((10, 10), char.birthplace, "black", font=font)
        writer.text((10, 10), char.special, "black", font=font)
        for idx, attribute in enumerate(char.attributes_main):
            writer.text(
                (0.1 * max_x + 0.043 * max_x * idx, max_y * 0.358),
                str(char.attributes_main[attribute].initial),
                "black",
                font=font,
            )
            if char.attributes_main[attribute].potential != 0:
                writer.text(
                    (0.1 * max_x + 0.043 * max_x * idx, max_y * 0.38),
                    str(char.attributes_main[attribute].potential),
                    "black",
                    font=font,
                )
        for idx, attribute in enumerate(char.attributes_sec):
            writer.text(
                (0.1 * max_x + 0.043 * max_x * idx, max_y * 0.448),
                str(char.attributes_sec[attribute].initial),
                "black",
                font=font,
            )
            if char.attributes_sec[attribute].potential != 0:
                writer.text(
                    (0.1 * max_x + 0.043 * max_x * idx, max_y * 0.47),
                    str(char.attributes_sec[attribute].potential),
                    "black",
                    font=font,
                )

        base.save(output_file_name)
        base.show()


def fill_character_card_back(input_file_name, output_file_name, char):
    """
    Construction in progress...
    Fills back character card PNG file with character fields.

    :param input_file_name: The name of the PNG file to fill.
    :type input_file_name: str
    :param output_file_name: The name of the filled PNG file.
    :type output_file_name: str
    :param char: Character containing fields to fill PNG file.
    :type char: Character
    :return: None
    """
    with Image.open(input_file_name).convert("RGBA") as base:
        writer = ImageDraw.Draw(base)
        # positions and font need to be adjusted
        number_of_advanced_skills = 0
        for skill in char.skills:
            if skill in basic_skills:
                y = 10 + 10 * basic_skills.index(skill)
            else:
                y = 10 + 10 * number_of_advanced_skills
                # here consider adjusting text size by text length
                writer.text((10, y), skill, "black")
                number_of_advanced_skills += 1
            writer.text((10, y), "X", "black")
            if char.skills[skill] == "+10":
                writer.text((20, y), "X", "black")
            if char.skills[skill] == "+20":
                writer.text((20, y), "X", "black")
                writer.text((30, y), "X", "black")
        for idx, ability in enumerate(char.abilities):
            writer.text((40, 10 + 10 * idx), ability, "black")
        for idx, trapping in enumerate(char.trappings):
            writer.text((40, 10 + 10 * idx), trapping, "black")
        writer.text((40, 10), char.money, "black")
        base.save(output_file_name)
        base.show()
