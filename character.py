"""
This module provides character class and generating all stats.
"""
from random import randint
from dataclasses import dataclass
import constants
import professions
from informations import Informations
from myrandom import d10, random_choose, mapping_roll


@dataclass
class CharAttribute:
    """
    Represents an attribute with initial, potential, and final values.

    Parameters:
        initial (int): The initial value of the attribute,
            which depends on race and rolls.
        potential (int): The value of potential attribute growth,
            which depends on profession.
        final (int): The final value of the attribute.

    """

    initial: int
    potential: int
    final: int


class Character(Informations):
    """
    Represents a character.
    Inheritance from base classes:
    Appearance, Informations, Equipment
    and includes skills, ablities,
    main and secondary attributes.

    Attributes:
        Appearance:
        race (str): The race of the character.
        sex (str): The sex of the character.
        eye (str): The eye color of the character.
        hair (str): The hair color of the character.
        weight (int): The weight of the character in kilograms.
        height (int): The height of the character in centimeters.
        special (str): Special characteristics of the character.

        Informations
        profession (str): The profession of the character.
        name (str): The name of the character.
        age (int): The age of the character.
        siblings (int): The number of siblings the character has.
        birthplace (str): The birthplace of the character.
        star (str): The star sign of the character.

        Equipment:
        trappings (list): The trappings of the character.
            Format: [trapping1, trapping2, ...].
        money (int): The money owned by the character in golden corons.
        basic_armor (int):
            Character armor points for basic rules.
        advanced_armor (dict):
            Character armor points for advanced rules.
            The keys represent body parts (head, body, arms, legs),
            and the values represent the armor values for each body part.
        armor_list (list):
            List that contains character armor.
        weapon_list (list):
            List that contains character weapons.

        attributes_main (dict): The main attributes of the character.
            Format: {"attribute_name": attribute_object}.
        attributes_sec (dict): The secondary attributes of the character.
            Format: {"attribute_name": attribute_object}.
        skills (dict): The skills of the character.
            Format: {"skill_name": skill_level}.
        abilities (list): The abilities of the character.
            Format: [ability_name1, ability_name2, ...].


    """

    def __init__(self):
        """
        Initializes a new instance of the Character class.
        """
        super().__init__()
        self.attributes_main = {
            "WW": CharAttribute(0, 0, 0),
            "US": CharAttribute(0, 0, 0),
            "K": CharAttribute(0, 0, 0),
            "Odp": CharAttribute(0, 0, 0),
            "Zr": CharAttribute(0, 0, 0),
            "Int": CharAttribute(0, 0, 0),
            "SW": CharAttribute(0, 0, 0),
            "Ogd": CharAttribute(0, 0, 0),
        }
        self.attributes_sec = {
            "A": CharAttribute(0, 0, 0),
            "Żyw": CharAttribute(0, 0, 0),
            "S": CharAttribute(0, 0, 0),
            "Wt": CharAttribute(0, 0, 0),
            "Sz": CharAttribute(0, 0, 0),
            "Mag": CharAttribute(0, 0, 0),
            "PO": CharAttribute(0, 0, 0),
            "PP": CharAttribute(0, 0, 0),
        }
        self.skills = {}
        self.abilities = []

    def roll_attributes(self):
        """
        Rolls the attributes for the character based on the character's race.

        Returns:
            None

        """
        self.attributes_main = {
            attr: CharAttribute(20 + d10() + d10(), 0, 0)
            for attr in self.attributes_main
        }
        self.attributes_sec["A"].initial = 1
        self.attributes_sec["Sz"].initial = 4

        roll = d10()
        if roll < 4:
            self.attributes_sec["Żyw"].initial = 10
        elif roll < 7:
            self.attributes_sec["Żyw"].initial = 11
        elif roll < 10:
            self.attributes_sec["Żyw"].initial = 12
        else:
            self.attributes_sec["Żyw"].initial = 13

        pp_roll = d10()
        if pp_roll < 5:
            self.attributes_sec["PP"].initial = 2
        else:
            self.attributes_sec["PP"].initial = 3

        if self.race == "halfling":
            self.attributes_main["WW"].initial -= 10
            self.attributes_main["K"].initial -= 10
            self.attributes_main["Odp"].initial -= 10
            self.attributes_main["Ogd"].initial += 10
            self.attributes_main["US"].initial += 10
            self.attributes_main["Zr"].initial += 10
            self.attributes_sec["Żyw"].initial -= 2
            if pp_roll < 8:
                self.attributes_sec["PP"].initial = 2

        if self.race == "dwarf":
            self.attributes_main["WW"].initial += 10
            self.attributes_main["Zr"].initial -= 10
            self.attributes_main["Ogd"].initial -= 10
            self.attributes_main["Odp"].initial += 10
            self.attributes_sec["Żyw"].initial += 1
            self.attributes_sec["Sz"].initial = 3
            if pp_roll < 8:
                self.attributes_sec["PP"].initial -= 1

        if self.race == "elf":
            self.attributes_main["US"].initial += 10
            self.attributes_main["Zr"].initial += 10
            self.attributes_sec["Żyw"].initial -= 1
            self.attributes_sec["PP"].initial -= 1
            self.attributes_sec["Sz"].initial = 5

    def roll_ability(self):
        """
        Rolls ability based on character based on the character's race.

        Raises:
            ValueError: If the race is invalid.

        Returns:
            None

        """
        if self.race == "halfling":
            mapping = constants.halfling_ability_mapping
        elif self.race == "human":
            mapping = constants.human_ability_mapping
        else:
            raise ValueError(f"Wrong race in roll_ability {self.race}")
        return mapping_roll(randint(1, 100), mapping)

    def set_default_skills_and_abilities(self):
        """
        Sets the default skills and abilities for the character
            based on the character's race.

        Returns:
            None

        """
        if self.race == "human":
            skills = constants.starting_human_skills
            ab1 = self.roll_ability()
            ab2 = self.roll_ability()
            while ab1 == ab2:
                ab2 = self.roll_ability()
            abilities = [ab1, ab2]

        if self.race == "halfling":
            skills = constants.starting_halfling_skills
            skills.add(random_choose(
                constants.starting_halfling_skills_optional))
            abilities = constants.starting_halfling_abilities
            abilities.append(self.roll_ability())

        if self.race == "dwarf":
            skills = constants.starting_dwarf_skills
            skills.add(random_choose(constants.starting_dwarf_skills_optional))
            abilities = constants.starting_dwarf_abilities

        if self.race == "elf":
            skills = constants.starting_elf_skills
            abilities = constants.starting_elf_ablities
            abilities.extend(
                [
                    random_choose(constants.starting_elf_ablities_optional1),
                    random_choose(constants.starting_elf_ablities_optional2),
                ]
            )
        self.skills = {skill: "bought" for skill in skills}
        self.abilities = abilities

    def add_skill(self, new_skill) -> bool:
        """
        Adds a new skill to the character's skills
            or increases the level of an existing skill.

        Args:
            new_skill (str): The name of the skill to add or increase.

        Returns:
            bool: True if the skill was successfully added or increased,
                False if the skill is already at the maximum level.

        Raises:
            ValueError: If the value of the skill in `self.skills`
                is not recognized.

        """
        if new_skill in self.skills.keys():
            if self.skills[new_skill] == "bought":
                self.skills[new_skill] = "+10"
            elif self.skills[new_skill] == "+10":
                self.skills[new_skill] = "+20"
            elif self.skills[new_skill] == "+20":
                return False
            else:
                raise ValueError("Wrong value of skill in add_skill function.")
        else:
            self.skills[new_skill] = "bought"
        return True

    def add_ability(self, new_ability) -> bool:
        """
        Adds a new ability to the character's abilities.

        Args:
            new_ability (str): The name of the ability to add.

        Returns:
            bool: True if the ability was successfully added,
                False if character has it.

        """
        if new_ability in self.abilities:
            return False
        self.abilities.append(new_ability)
        return True

    def add_optional_skill(self, new_skills) -> bool:
        """
        Adds an optional skill to the character's skills.

        Args:
            new_skills (list): A list of optional skills to choose from.

        Returns:
            bool: True if an optional skill was successfully added,
                False if no more optional skills are available.

        """
        temp_skills = list()
        for skill in self.skills:
            if skill in new_skills:
                temp_skills.append(skill)
                new_skills.remove(skill)
                if self.skills[skill] == "+20":
                    temp_skills.remove(skill)
        if new_skills == []:
            new_skills = temp_skills
        if new_skills == []:
            return False
        return self.add_skill(random_choose(new_skills))

    def add_optional_ability(self, new_abilities) -> bool:
        """
        Adds an optional ability to the character's abilities.

        Args:
            new_abilities (list): A list of optional abilities to choose from.

        Returns:
            bool: True if an optional ability was successfully added,
                False if no more optional abilities are available.

        """
        for ability in self.abilities:
            if ability in new_abilities:
                new_abilities.remove(ability)
        if new_abilities == []:
            return False
        return self.add_ability(random_choose(new_abilities))

    def update_any_skill(self):
        """
        Updates skill(any) in the character's skills with random choices
            from the corresponding value options.

        The method replaces format skill(any) that matches
            the predefined skills in `constants.any_skills` with random skills
            chosen from the corresponding skill options.
            The number of replacements depends on the current skill value.

        """
        for skill, value in constants.any_skills.items():
            if skill in self.skills:
                if self.skills[skill] == "+20":
                    self.add_skill(random_choose(value))
                    self.add_skill(random_choose(value))
                    self.add_skill(random_choose(value))
                elif self.skills[skill] == "+10":
                    self.add_skill(random_choose(value))
                    self.add_skill(random_choose(value))
                else:
                    self.add_skill(random_choose(value))
                self.skills.pop(skill)

    def update_any_ability(self):
        """
        Updates ability(any) in the character's abilities with
            random choices from the corresponding value options.

        The method replaces format ability(any) that matches
            the predefined abilities in `constants.any_ability` with random
            abilities chosen from the corresponding ability options.

        """
        for ability, values in constants.any_ability.items():
            if ability in self.abilities:
                while True:
                    if self.add_ability(random_choose(values)):
                        self.abilities.remove(ability)
                        break

    def set_starting_profession(self):
        """
        Sets the starting attributes, skills, abilities, trappings
            based on the chosen profession.

        The method initializes the character's attributes, skills,
            abilities, and trappings based on the selected
            profession. It retrieves the attributes, skills, abilities,
            and trappings information from the `professions.professions`
            dictionary and assigns them to the character.

        """
        for atrr in professions.professions[self.profession][
            "attributes_main"
        ]:
            self.attributes_main[atrr].potential = professions.professions[
                self.profession
            ]["attributes_main"][atrr]
        for atrr in professions.professions[self.profession]["attributes_sec"]:
            self.attributes_sec[atrr].potential = professions.professions[
                self.profession
            ]["attributes_sec"][atrr]
        for skill in professions.professions[self.profession]["skills"]:
            self.add_skill(skill)
        for ability in professions.professions[self.profession]["abilities"]:
            self.add_ability(ability)
        for skills in professions.professions[self.profession][
            "optional_skills"
        ]:
            self.add_optional_skill(skills)
        for abilities in professions.professions[self.profession][
            "optional_abilities"
        ]:
            self.add_optional_ability(abilities)
        for trapping in professions.professions[self.profession]["trappings"]:
            self.trappings.append(trapping)
        if "optional_trappings" in professions.professions[self.profession]:
            for trapping in professions.professions[self.profession][
                "optional_trappings"
            ]:
                new_trapping = random_choose(trapping)
                if isinstance(new_trapping, list):
                    self.trappings.extend(new_trapping)
                else:
                    self.trappings.append(new_trapping)

    def update(self):
        """
        Perform updates and modifications to the character.

        This method triggers a series of updates and modifications to
            the character based on their abilities and trappings.
        The following actions are performed in sequence:
        1. Update attributes based on abilities using
            the `update_attr_by_abilities` method.
        2. Set values for attributes "S" and "Wt" using
            the `set_s_wt` method.
        3. Roll random values in trappings using
            the `roll_in_trappings` method.
        4. Extract money from trappings using
            the `take_money_from_trappings` method.
        5. Extract armor from trappings using
            the `take_armor_from_trappings` method.
        5. Extract weapons from trappings using
            the `take_weapon_from_trappings` method.

        """
        self.update_attr_by_abilities()
        self.set_s_wt()
        self.roll_in_trappings()
        self.take_money_from_trappings()
        self.take_armor_from_trappings()
        self.take_weapon_from_trappings()

    def update_attr_by_abilities(self):
        """
        Update character's attributes based on their abilities.

        The method iterates over the character's abilities and checks
        if they have a corresponding attribute modifier in
        the `constants.ability_modify_attr` dictionary.
        If a match is found, the initial values of the corresponding
        attributes in `attributes_main` and `attributes_sec`
        are increased by specific amounts.

        """
        for ability in self.abilities:
            for key, value in constants.ability_modify_attr.items():
                if key == ability:
                    if value in self.attributes_main:
                        self.attributes_main[value].initial += 5
                    if value in self.attributes_sec:
                        self.attributes_sec[value].initial += 1

    def set_s_wt(self):
        """
        Set values for attributes "S" and "Wt" based on other attributes.

        The method calculates the initial and final values for attributes
        "S" and "Wt" based on the initial values of
        attributes "K" and "Odp" respectively.

        """
        self.attributes_sec["S"].initial = \
            self.attributes_main["K"].initial // 10
        self.attributes_sec["Wt"].initial = \
            self.attributes_main["Odp"].initial // 10
        self.attributes_sec["S"].final = self.attributes_main["K"].final // 10
        self.attributes_sec["Wt"].final = \
            self.attributes_main["Odp"].final // 10

    def roll_all(
        self,
        race=None,
        profession=None,
        sex=None,
        name=None,
        height=None,
        weight=None,
        hair=None,
        eye=None,
        special=None,
        siblings=None,
        star=None,
        age=None,
        birthplace=None,
        money=None,
    ):
        """
        Roll all character attributes and generate a complete character.

        Rolls all character attributes including race, profession, sex, name,
        height, weight, hair color, eye color,
        special characteristics, siblings, star sign, age, birthplace,
        attributes, money, skills, abilities, and updates them accordingly.
        You can also set all by yourself.
        This method generates a complete character with all the attributes
        and stores them in the respective attributes of the character.
        """
        if race:
            self.race = race
        else:
            self.roll_race()
        if profession:
            self.profession = profession
        else:
            self.roll_profession()
        if sex:
            self.sex = sex
        else:
            self.roll_sex()
        if name:
            self.name = name
        else:
            self.roll_name()
        if height:
            self.height = height
        else:
            self.roll_height()
        if weight:
            self.weight = weight
        else:
            self.roll_weight()
        if hair:
            self.hair = hair
        else:
            self.roll_hair()
        if eye:
            self.eye = eye
        else:
            self.roll_eye()
        if special:
            self.special = special
        else:
            self.roll_special()
        if siblings:
            self.siblings = siblings
        else:
            self.roll_siblings()
        if star:
            self.star = star
        else:
            self.roll_star()
        if age:
            self.age = age
        else:
            self.roll_age()
        if birthplace:
            self.birthplace = birthplace
        else:
            self.roll_birthplace()
        self.roll_attributes()
        if money:
            self.money = money
        else:
            self.roll_money()
        self.set_default_skills_and_abilities()
        self.set_starting_profession()
        self.update_any_skill()
        self.update_any_ability()
        self.update()
