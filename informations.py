"""
This module provides Informations class.
"""
from random import randint
from myrandom import d10, random_choose, mapping_roll
import constants

class Informations:
    """
    Includes a set of additional information on the character.

    Atrributes:
        race (str): The race of the character.
        profession (str): The profession of the character.
        name (str): The name of the character.
        age (int): The age of the character.
        siblings (int): The number of siblings the character has.
        birthplace (str): The birthplace of the character.
        star (str): The star sign of the character.

    """
    
    def __init__(self) -> None:
        """
        Initializes a new instance of the Informations class.
        """
        self.race = None
        self.profession = None
        self.name = None
        self.age = None
        self.star = None
        self.siblings = None
        self.birthplace = None

    def roll_race(self):
        """
        Rolls the race for the character.

        Randomly determines character race
        which can be human, elf, dwarf or halfling.
        Roll chances are set arbitrarily.
        """
        roll = randint(1, 100)
        if roll == 1:
            output = "elf"
        elif roll < 5:
            output = "dwarf"
        elif roll < 11:
            output = "halfling"
        else:
            output = "human"
        self.race = output

    def roll_profession(self):
        """
        Rolls the profession for the character based on the character's race.

        Raises:
            ValueError: If the race is invalid.

        Returns:
            None

        """
        if self.race == "elf":
            mapping = constants.elf_profession_mapping
        elif self.race == "dwarf":
            mapping = constants.dwarf_profession_mapping
        elif self.race == "halfling":
            mapping = constants.halfling_profession_mapping
        elif self.race == "human":
            mapping = constants.human_profession_mapping
        else:
            raise ValueError(f"Wrong race in roll_profession {self.race}")

        roll = randint(1, 1000)
        self.profession = mapping_roll(roll, mapping)

    def roll_name(self):
        """
        Roll the character's name based on race and sex.

        Generates the character's name based on random selections
        from predefined name lists specific to their race and sex.
        The generated name is stored in the 'name' attribute of the character.
        """
        if self.race == "human":
            surname = random_choose(constants.human_surname_list)
            if self.sex == "male":
                firstname = random_choose(constants.human_male_name_list)
            else:
                firstname = random_choose(constants.human_female_name_list)
        if self.race == "dwarf":
            if self.sex == "male":
                firstname = f"{random_choose(constants.dwarf_name1_list)}" \
                    f"{random_choose(constants.dwarf_male_name2_list)}"
                surname = f"{random_choose(constants.dwarf_name1_list)}" \
                    f"{random_choose(constants.dwarf_male_name2_list)}son"
            else:
                firstname = f"{random_choose(constants.dwarf_name1_list)}" \
                    f"{random_choose(constants.dwarf_female_name2_list)}"
                surname = f"{random_choose(constants.dwarf_name1_list)}" \
                    f"{random_choose(constants.dwarf_female_name2_list)}sdotr"
        if self.race == "elf":
            surname = random_choose(constants.elf_surname_list)
            if d10() < 6:
                connector = random_choose(constants.elf_name_connector_list)
            else:
                connector = ""
            if self.sex == "male":
                firstname = f"{random_choose(constants.elf_name1_list)}" \
                    f"{connector}" \
                    f"{random_choose(constants.elf_male_name2_list)}"
            else:
                firstname = f"{random_choose(constants.elf_name1_list)}" \
                    f"{connector}" \
                    f"{random_choose(constants.elf_female_name2_list)}"
        if self.race == "halfling":
            surname = random_choose(constants.halfling_surname_list)
            if self.sex == "male":
                firstname = f"{random_choose(constants.halfling_name1_list)}" \
                    f"{random_choose(constants.halfling_male_name2_list)}"
            else:
                firstname = f"{random_choose(constants.halfling_name1_list)}" \
                    f"{random_choose(constants.halfling_female_name2_list)}"

        self.name = f"{firstname} {surname}"

    def roll_age(self):
        """
        Roll the character's age based on race.

        Calculates the character's age based on a random dice roll
        and adjustments specific to their race.
        The age value is stored in the 'age' attribute of the character.
        """
        roll = randint(1, 100)
        additional_weight = (roll - 1) // 5
        if self.race == "human":
            self.age = 16 + additional_weight
        elif self.race == "halfling":
            self.age = 20 + 2 * additional_weight
            if roll > 70:
                self.age += 2
        else:
            self.age = 20 + 5 * additional_weight  # dwarf
            if self.race == "elf":
                self.age += 10

    def roll_star(self):
        """
        Roll the character's star sign.

        Generates the character's star sign based on
        a random dice roll and a predefined mapping.
        The star sign is stored in the 'star' attribute of the character.
        """
        roll = randint(1, 100)
        self.star = mapping_roll(roll, constants.star_mapping)

    def roll_siblings(self):
        """
        Roll the number of character's siblings based on race.

        Generates the number of siblings for the character based on
        a random dice roll and adjustments specific to their race.
        The number of siblings is stored in the 'siblings' attribute
        of the character.
        """
        roll = d10()
        if self.race == "dwarf":
            mapping = constants.siblings_dwarf_mapping
        elif self.race == "elf":
            mapping = constants.siblings_elf_mapping
        else:
            mapping = constants.siblings_human_mapping
        self.siblings = mapping_roll(roll, mapping)
        if self.race == "halfling":
            self.siblings += 1
    
    def roll_birthplace(self):
        """
        Roll the character's birthplace based on race.

        Generates the character's birthplace based on random dice rolls
        and adjustments specific to their race.
        The birthplace is stored in the 'birthplace' attribute
        of the character.
        """
        if self.race == "dwarf":
            if randint(1, 100) > 30:
                self.birthplace = random_choose(
                    constants.dwarf_birthplace_list
                )
        elif self.race == "elf":
            self.birthplace = mapping_roll(
                randint(1, 100), constants.elf_birthplace_dict
            )
        elif self.race == "halfling":
            if randint(1, 100) < 50:
                self.birthplace = constants.halfling_most_common_birthplace
        if self.birthplace is None:
            province = random_choose(list(constants.town_dict.keys()))
            town = mapping_roll(
                randint(1, 100),
                constants.town_dict[province]
            )
            self.birthplace = f"{province}, {town}"