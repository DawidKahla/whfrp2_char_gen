"""
This module provides functions for fill baseform png files
"""
from PIL import Image, ImageDraw
from constants import basic_skills

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
        writer.text((10, 10), char.name, "black")
        writer.text((10, 10), char.race, "black")
        writer.text((10, 10), char.profession, "black")
        writer.text((10, 10), char.age, "black")
        writer.text((10, 10), char.eye, "black")
        writer.text((10, 10), char.hair, "black")
        writer.text((10, 10), char.star, "black")
        writer.text((10, 10), char.sex, "black")
        writer.text((10, 10), char.weight, "black")
        writer.text((10, 10), char.height, "black")
        writer.text((10, 10), char.siblings, "black")
        writer.text((10, 10), char.birthplace, "black")
        writer.text((10, 10), char.special, "black")
        for idx, atrribute in enumerate(char.atrributes_main):
            writer.text((10, 10+10*idx), char.atrributes_main[atrribute].initial, "black")
            if char.atrributes_main[atrribute].potential != 0:
                writer.text((20, 10+10*idx), char.atrributes_main[atrribute].potential, "black")
        for idx, atrribute in enumerate(char.atrributes_sec):
            writer.text((10, 10+10*idx), char.atrributes_sec[atrribute].initial, "black")
            if char.atrributes_sec[atrribute].potential != 0:
                writer.text((20, 10+10*idx), char.atrributes_sec[atrribute].potential, "black")
        
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
        for skill in character.skills:
            if skill in basic_skills:
                y = 10+10*basic_skills.index(skill)
            else:
                y = 10+10*number_of_advanced_skills
                # here consider adjusting text size by text length
                writer.text((10, y), skill, "black")
                number_of_advanced_skills += 1
            writer.text((10, y), "X", "black")
            if character.skills[skills] == "+10":
                writer.text((20, y), "X", "black")
            if character.skills[skills] == "+20":
                writer.text((20, y), "X", "black")
                writer.text((30, y), "X", "black")
        for idx, ability in enumerate(char.abilities):
            writer.text((40, 10+10*idx), ability, "black")
        for idx, trapping in enumerate(char.trappings):
            writer.text((40, 10+10*idx), trapping, "black")
        writer.text((40, 10), char.money, "black")
        base.save(output_file_name)
        base.show()