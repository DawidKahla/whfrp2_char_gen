"""
This module provides functions for fill baseform png files
"""
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
from constants import basic_skills, armors, weapons
import translations


def fill_character_card_front(input_file_name, output_file_name, char) -> str:
    """
    Fills the front character card PNG file with character fields.

    Parameters:
        input_file_name (str): The name of the PNG file to fill.
        output_file_name (str): The name of the filled PNG file.
        char (Character): Character containing fields to fill PNG file.

    Returns:
        str: The name of the filled PNG file.

    """
    with Image.open(input_file_name).convert("RGBA") as base:
        writer = ImageDraw.Draw(base)
        font = ImageFont.truetype("fonts\\Anonymous_Pro.ttf", 14, encoding="utf-8")
        max_x, max_y = base.size
        # basics
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
        writer.text((0.068 * max_x, 0.169 * max_y), str(char.age), "black", font=font)
        writer.text((0.09 * max_x, 0.191 * max_y), char.eye, "black", font=font)
        writer.text((0.1 * max_x, 0.213 * max_y), char.hair, "black", font=font)
        if len(char.star) > 15:
            font_for_star = font.font_variant(size=int(font.size - len(char.star) / 8))
        else:
            font_for_star = font
        writer.text(
            (0.106 * max_x, 0.235 * max_y), char.star, "black", font=font_for_star
        )
        writer.text(
            (0.27 * max_x, 0.169 * max_y),
            translations.sex_translate(char.sex),
            "black",
            font=font,
        )
        writer.text(
            (0.275 * max_x, 0.191 * max_y), f"{char.weight} kg", "black", font=font
        )
        writer.text(
            (0.29 * max_x, 0.213 * max_y), f"{char.height} cm", "black", font=font
        )
        writer.text(
            (0.31 * max_x, 0.235 * max_y), str(char.siblings), "black", font=font
        )
        writer.text((0.125 * max_x, 0.257 * max_y), char.birthplace, "black", font=font)
        writer.text((0.123 * max_x, 0.279 * max_y), char.special, "black", font=font)
        # attributes
        for idx, attribute in enumerate(char.attributes_main):
            writer.text(
                (0.1 * max_x + 0.043 * max_x * idx, max_y * 0.358),
                str(char.attributes_main[attribute].initial),
                "black",
                font=font,
            )
            if char.attributes_main[attribute].potential != 0:
                writer.text(
                    (0.095 * max_x + 0.043 * max_x * idx, max_y * 0.38),
                    f"+{char.attributes_main[attribute].potential}",
                    "black",
                    font=font,
                )
            else:
                writer.text(
                    (0.105 * max_x + 0.043 * max_x * idx, max_y * 0.38),
                    "-",
                    "black",
                    font=font,
                )
        for idx, attribute in enumerate(char.attributes_sec):
            writer.text(
                (0.103 * max_x + 0.043 * max_x * idx, max_y * 0.448),
                str(char.attributes_sec[attribute].initial),
                "black",
                font=font,
            )
            if char.attributes_sec[attribute].potential != 0:
                writer.text(
                    (0.098 * max_x + 0.043 * max_x * idx, max_y * 0.47),
                    f"+{char.attributes_sec[attribute].potential}",
                    "black",
                    font=font,
                )
            else:
                writer.text(
                    (0.105 * max_x + 0.043 * max_x * idx, max_y * 0.47),
                    "-",
                    "black",
                    font=font,
                )
        # weapons
        for idx, weapon in enumerate(char.weapon_list):
            if len(weapon) > 12 and len(weapon) < 19:
                font_for_weapon = font.font_variant(
                    size=int(font.size - len(weapon) / 5)
                )
            elif len(weapon) >= 19:
                font_for_weapon = font.font_variant(
                    size=int(font.size - len(weapon) / 3.3)
                )
            else:
                font_for_weapon = font
            writer.text(
                (0.03 * max_x, 0.57 * max_y + idx * 0.022 * max_y),
                weapon,
                "black",
                font=font_for_weapon,
            )
            for idx_det, detail in enumerate(weapons[weapon]):
                if detail:
                    if isinstance(detail, list):
                        for temp_idx, attr in enumerate(detail):
                            font_for_attr = font.font_variant(
                                size=int(font.size - 1.8 * len(detail))
                            )
                            writer.text(
                                (
                                    0.141 * max_x + 0.043 * max_x * idx_det,
                                    0.5635 * max_y
                                    + max_y * 0.02 * temp_idx / len(detail)
                                    + idx * 0.022 * max_y,
                                ),
                                str(attr),
                                "black",
                                font_for_attr,
                            )
                    else:
                        font_for_detail = font
                        if idx_det == 4 and len(detail) > 4:
                            font_for_detail = font.font_variant(size=int(font.size - 4))
                        elif idx_det == 5 and len(detail) > 9:
                            font_for_detail = font.font_variant(
                                size=int(font.size - len(detail) / 4)
                            )
                            if len(detail) > 14:
                                font_for_detail = font.font_variant(
                                    size=int(font.size - len(detail) / 3)
                                )
                            if len(detail) > 18:
                                font_for_detail = font.font_variant(
                                    size=int(font.size - len(detail) / 2.7)
                                )
                        elif idx_det == 3 and len(detail) > 4:
                            font_for_detail = font.font_variant(size=int(font.size - 3))
                        elif idx_det == 1 and len(detail) > 5:
                            detail = detail[:3] + "."
                        writer.text(
                            (
                                0.141 * max_x + 0.043 * max_x * idx_det,
                                0.57 * max_y + idx * 0.022 * max_y,
                            ),
                            str(detail),
                            "black",
                            font_for_detail,
                        )
        # armors
        if char.basic_armor == 1:
            writer.text((0.1 * max_x, 0.754 * max_y), "Lekki", "black", font=font)
        elif char.basic_armor == 3:
            writer.text((0.1 * max_x, 0.754 * max_y), "Średni", "black", font=font)
        if char.basic_armor:
            writer.text(
                (0.3 * max_x, 0.754 * max_y), f"{char.basic_armor}", "black", font=font
            )
        for idx, armor in enumerate(char.armor_list):
            font_for_name = font
            font_for_location = font
            if len(armor) > 14:
                font_for_name = font.font_variant(size=int(font.size - 3))
            if len(", ".join(armors[armor][0])) > 24:
                font_for_location = font.font_variant(size=int(font.size - 2))
            writer.text(
                (0.03 * max_x, 0.81 * max_y + 0.022 * max_y * idx),
                armor,
                "black",
                font=font_for_name,
            )
            writer.text(
                (0.195 * max_x, 0.81 * max_y + 0.022 * max_y * idx),
                ", ".join(armors[armor][0]),
                "black",
                font=font_for_location,
            )
            writer.text(
                (0.41 * max_x, 0.81 * max_y + 0.022 * max_y * idx),
                f"{armors[armor][1]}",
                "black",
                font=font,
            )
            writer.text(
                (0.16 * max_x, 0.81 * max_y + 0.022 * max_y * idx),
                f"{armors[armor][2]}",
                "black",
                font=font,
            )
        writer.text(
            (0.513 * max_x, 0.37 * max_y),
            f"{char.advanced_armor['head']}",
            "black",
            font=font,
        )
        writer.text(
            (0.827 * max_x, 0.37 * max_y),
            f"{char.advanced_armor['body']}",
            "black",
            font=font,
        )
        writer.text(
            (0.513 * max_x, 0.526 * max_y),
            f"{char.advanced_armor['arms']}",
            "black",
            font=font,
        )
        writer.text(
            (0.827 * max_x, 0.526 * max_y),
            f"{char.advanced_armor['arms']}",
            "black",
            font=font,
        )
        writer.text(
            (0.513 * max_x, 0.69 * max_y),
            f"{char.advanced_armor['legs']}",
            "black",
            font=font,
        )
        writer.text(
            (0.827 * max_x, 0.69 * max_y),
            f"{char.advanced_armor['legs']}",
            "black",
            font=font,
        )
        # movement
        writer.text(
            (0.545 * max_x, 0.28 * max_y),
            f"{char.attributes_sec['Sz'].initial*2}m",
            "black",
            font=font,
        )
        writer.text(
            (0.64 * max_x, 0.28 * max_y),
            f"{char.attributes_sec['Sz'].initial*4}m",
            "black",
            font=font,
        )
        writer.text(
            (0.775 * max_x, 0.28 * max_y),
            f"{char.attributes_sec['Sz'].initial*6}m",
            "black",
            font=font,
        )

        base.save(output_file_name)
        return output_file_name


def fill_character_card_back(input_file_name, output_file_name, char) -> str:
    """
    Fills the back character card PNG file with character fields.

    Parameters:
        input_file_name (str): The name of the PNG file to fill.
        output_file_name (str): The name of the filled PNG file.
        char (Character): Character containing fields to fill PNG file.

    Returns:
        str: The name of the filled PNG file.

    """
    with Image.open(input_file_name).convert("RGBA") as base:
        writer = ImageDraw.Draw(base)
        font = ImageFont.truetype("fonts\\Anonymous_Pro.ttf", 14, encoding="utf-8")
        max_x, max_y = base.size
        number_of_advanced_skills = 0
        for skill in char.skills:
            if skill in basic_skills:
                y_skill = 0.084 * max_y + 0.023 * max_y * basic_skills.index(skill)
                x_bought = 0.2542 * max_x
                x_10 = 0.306 * max_x
                x_20 = 0.361 * max_x
            else:
                y_skill = 0.591 * max_y + 0.023 * max_y * number_of_advanced_skills
                x_bought = 0.263 * max_x
                x_10 = 0.324 * max_x
                x_20 = 0.373 * max_x
                if len(skill) > 18:
                    font_for_skill = font.font_variant(
                        size=int(font.size - len(skill) / 6)
                    )
                else:
                    font_for_skill = font
                writer.text((0.1 * max_x, y_skill), skill, "black", font=font_for_skill)
                number_of_advanced_skills += 1
            writer.text((x_bought, y_skill), "X", "black", font=font)
            if char.skills[skill] == "+10":
                writer.text((x_10, y_skill), "X", "black", font=font)
            if char.skills[skill] == "+20":
                writer.text((x_10, y_skill), "X", "black", font=font)
                writer.text((x_20, y_skill), "X", "black", font=font)
        for idx, ability in enumerate(char.abilities):
            writer.text(
                (0.569 * max_x, 0.089 * max_y + 0.023 * max_y * idx),
                ability,
                "black",
                font=font,
            )
        for idx, trapping in enumerate(char.trappings):
            if len(trapping) > 45:
                font_for_trapping = font.font_variant(
                    size=int(font.size - len(trapping) / 14)
                )
            else:
                font_for_trapping = font
            writer.text(
                (0.569 * max_x, 0.514 * max_y + 0.023 * max_y * idx),
                trapping,
                "black",
                font=font_for_trapping,
            )
        writer.text((0.64 * max_x, 0.882 * max_y), str(char.money), "black", font=font)
        base.save(output_file_name)
        return output_file_name


def generate_pdf(output_file_name, char):
    """
    Generate a complete 2-page character sheet as a PDF file.

    Parameters:
        output_file_name (str): The name of the PDF file with the character sheet.
        char (Character): Character containing fields to fill the PDF file.

    Returns:
        None

    """
    pdf = FPDF()
    pdf.set_margins(0, 0, 0)
    front_char_sheet = fill_character_card_front(
        input_file_name="imgs\\baseform-1.png",
        output_file_name="imgs\\output1.png",
        char=char,
    )
    back_char_sheet = fill_character_card_back(
        input_file_name="imgs\\baseform-2.png",
        output_file_name="imgs\\output2.png",
        char=char,
    )
    imagelist = [front_char_sheet, back_char_sheet]
    for image in imagelist:
        pdf.add_page()
        pdf.image(image, w=210, h=276)
    pdf.output(output_file_name, "F")
