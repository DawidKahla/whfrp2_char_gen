"""
This module provides Appearance class.
"""
from random import randint
from myrandom import d10, random_choose
import constants

class Appearance:
    """
    Represents a set of characteristics of a character's appearance

    Atrributes:
        race (str): The race of the character.
        sex (str): The sex of the character.
        eye (str): The eye color of the character.
        hair (str): The hair color of the character.
        weight (int): The weight of the character in kilograms.
        height (int): The height of the character in centimeters.
        special (str): Special characteristics of the character.

    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Appearance class.
        """
        self.race = None
        self.sex = None
        self.eye = None
        self.hair = None
        self.weight = None
        self.height = None
        self.special = None
    

    def roll_sex(self):
        """
        Roll the character's sex if it is not already set.

        Randomly determines the sex of the character based on a dice roll.
        If the sex is already set, no action is taken.
        """
        if self.sex is None:
            if d10() < 6:
                self.sex = "male"
            else:
                self.sex = "female"

    def roll_height(self):
        """
        Roll the character's height based on race and sex.

        Calculates the character's height based on random dice rolls
        and adjustments specific to their race and sex.
        The height value is stored in the 'height' attribute of the character.
        """
        self.height = 100 + d10() + d10()
        if self.sex == "male":
            self.height += 10
        if self.race == "dwarf":
            self.height += 30
            if self.sex == "male":
                self.height += 5
        if self.race == "human":
            self.height += 50
        if self.race == "elf":
            self.height += 60

    def roll_weight(self):
        """
        Roll the character's weight based on race.

        Calculates the character's weight based on a random dice roll
        and adjustments specific to their race.
        The weight value is stored in the 'weight' attribute of the character.
        """
        roll = randint(1, 100)
        if self.race == "halfling":
            mapping = constants.halfling_weight_mapping
        else:
            mapping = constants.common_weight_mapping
        self.weight = mapping_roll(roll, mapping)
        if self.race == "elf":
            self.weight -= 5
        if self.race == "human":
            self.weight += 5
            if roll == 100:
                self.weight = 110

    def roll_hair(self):
        """
        Roll the character's hair color based on race.

        Randomly selects the character's hair color from a predefined
        list of hair colors specific to their race.
        The selected hair color is stored in the 'hair'
        attribute of the character.
        """
        if self.race == "human":
            hair_list = constants.human_hair_list
        if self.race == "dwarf":
            hair_list = constants.dwarf_hair_list
        if self.race == "halfling":
            hair_list = constants.halfling_hair_list
        if self.race == "elf":
            hair_list = constants.elf_hair_list
        self.hair = hair_list[d10() - 1]

    def roll_eye(self):
        """
        Roll the character's eye color based on race.

        Randomly selects the character's eye color from a predefined
        list of eye colors specific to their race.
        The selected eye color is stored
        in the 'eye' attribute of the character.
        """
        if self.race == "human":
            eye_list = constants.human_eye_list
        if self.race == "dwarf":
            eye_list = constants.dwarf_eye_list
        if self.race == "halfling":
            eye_list = constants.halfling_eye_list
        if self.race == "elf":
            eye_list = constants.elf_eye_list
        self.eye = eye_list[d10() - 1]

    def roll_special(self):
        """
        Roll the character's special characteristic.

        Generates a random value for the character's special characteristic
        based on a dice roll and a predefined mapping.
        The value is stored in the 'special' attribute of the character.
        """
        roll = randint(1, 100)
        self.special = mapping_roll(roll, constants.special_mapping)
