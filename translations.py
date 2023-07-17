"""
This module contains translations.
"""


def race_translate(race):
    """
    Translate race from English to Polish and from Polish to English

    Parameters:
        race (str): Race to translate.

    Returns:
        str: Translated race.

    Raises:
        ValueError: If race is not human, halfling, dwarf or elf.

    """
    mapping = {
        "human": "Człowiek",
        "halfling": "Niziołek",
        "dwarf": "Krasnolud",
        "elf": "Elf",
        "Człowiek": "human",
        "Niziołek": "halfling",
        "Krasnolud": "dwarf",
        "Elf": "elf",
    }
    if race not in mapping:
        raise ValueError(f"Wrong race in translation: {race}.")
    return mapping[race]


def sex_translate(sex):
    """
    Translate sex from English to Polish.

    Parameters:
        sex (str): Sex to translate.

    Returns:
        str: Translated sex.

    Raises:
        ValueError: If sex is not male or female.

    """
    mapping = {
        "male": "Mężczyzna",
        "female": "Kobieta",
        "Mężczyzna": "male",
        "Kobieta": "female"
        }
    if sex not in mapping:
        raise ValueError(f"Wrong sex in sex translation: {sex}.")
    return mapping[sex]
