"""
This module contains translations.
"""
def race_translate(race):
    """
    Translate race from english to polish.

    :param race: Race to translate.
    :type race: str
    :return: Translated race.
    :r type: str
    :raises ValueError: If race is not human, halfling, dwarf or elf.
    """
    mapping = {
        "human": "Człowiek",
        "halfling": "Niziołek",
        "dwarf": "Krasnolud",
        "elf": "Elf",
    }
    if race not in mapping:
        raise ValueError(f"Wrong race in translation: {race}.")
    return mapping[race]


def sex_translate(sex):
        """
    Translate sex from english to polish.

    :param sex: Sex to translate.
    :type race: str
    :return: Translated sex.
    :r type: str
    :raises ValueError: If sex is not male or female.
    """
    mapping = {"male": "Mężczyzna", "female": "Kobieta"}
    if sex not in mapping:
        raise ValueError(f"Wrong sex in sex translation: {sex}.")
    return mapping[sex]