"""
This module provides character class and generating all stats.
"""
import random as rand
from dataclasses import dataclass
import constants
import professions


def random_choose(some_list):
    """
    Rolls a random element from a list.

    Parameters:
        some_list (list): The list to roll an element from.

    Returns:
        The randomly selected element from the list.
    """
    return some_list[rand.randint(0, len(some_list) - 1)]


def mapping_roll(roll, mapping) -> str:
    """
    Get a value from a mapping based on the input roll.

    Parameters:
        roll (int): The number corresponding to a key in the mapping.
        mapping (dict): A dictionary containing 2-number tuples as keys and strings as values.

    Returns:
        The value associated with the input roll in the mapping.

    Raises:
        ValueError: If the roll is not present in the keys of the mapping.
    """
    for key in mapping.keys():
        minimum, maximum = key
        if roll >= minimum and roll <= maximum:
            return mapping[key]
    raise ValueError(f"Roll: ({roll}) not in mapping: ({mapping})")


@dataclass
class attribute:
    """
    Represents an attribute with initial, potential, and final values.

    Parameters:
        initial (int): The initial value of the attribute, which depends on race and rolls.
        potential (int): The value of potential attribute growth, which depends on profession.
        final (int): The final value of the attribute.

    """

    initial: int
    potential: int
    final: int


class Character(object):
    """
    Represents a character.

    Attributes:
        race (str): The race of the character.
        profession (str): The profession of the character.
        sex (str): The sex of the character.
        name (str): The name of the character.
        age (int): The age of the character.
        eye (str): The eye color of the character.
        hair (str): The hair color of the character.
        star (str): The star sign of the character.
        weight (int): The weight of the character in kilograms.
        height (int): The height of the character in centimeters.
        siblings (int): The number of siblings the character has.
        birthplace (str): The birthplace of the character.
        special (str): Special characteristics of the character.
        attributes_main (dict): The main attributes of the character.
            Format: {"attribute_name": attribute_object}.
        attributes_sec (dict): The secondary attributes of the character.
            Format: {"attribute_name": attribute_object}.
        skills (dict): The skills of the character.
            Format: {"skill_name": skill_level}.
        abilities (list): The abilities of the character.
            Format: [ability_name1, ability_name2, ...].
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


    """

    def __init__(self):
        """
        Initializes a new instance of the Character class.
        """
        self.race = None
        self.profession = None
        self.sex = None
        self.name = None
        self.age = None
        self.eye = None
        self.hair = None
        self.star = None
        self.weight = None
        self.height = None
        self.siblings = None
        self.birthplace = None
        self.special = None
        self.attributes_main = {
            "WW": attribute(0, 0, 0),
            "US": attribute(0, 0, 0),
            "K": attribute(0, 0, 0),
            "Odp": attribute(0, 0, 0),
            "Zr": attribute(0, 0, 0),
            "Int": attribute(0, 0, 0),
            "SW": attribute(0, 0, 0),
            "Ogd": attribute(0, 0, 0),
        }
        self.attributes_sec = {
            "A": attribute(0, 0, 0),
            "Żyw": attribute(0, 0, 0),
            "S": attribute(0, 0, 0),
            "Wt": attribute(0, 0, 0),
            "Sz": attribute(0, 0, 0),
            "Mag": attribute(0, 0, 0),
            "PO": attribute(0, 0, 0),
            "PP": attribute(0, 0, 0),
        }
        self.skills = {}
        self.abilities = []
        self.trappings = []
        self.money = None
        self.basic_armor = None
        self.advanced_armor = {
            "head": 0,
            "body": 0,
            "arms": 0,
            "legs": 0,
        }
        self.armor_list = []
        self.weapon_list = []

    def roll_race(self):
        """
        Rolls the race for the character.

        Returns:
            None

        """
        roll = rand.randint(1, 100)
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

        roll = rand.randint(1, 1000)
        self.profession = mapping_roll(roll, mapping)

    def roll_attributes(self):
        """
        Rolls the attributes for the character based on the character's race.

        Returns:
            None

        """
        self.attributes_main = {
            attr: attribute(20 + rand.randint(1, 10) + rand.randint(1, 10), 0, 0)
            for attr in self.attributes_main
        }
        self.attributes_sec["A"].initial = 1
        self.attributes_sec["Sz"].initial = 4

        roll = rand.randint(1, 10)
        if roll < 4:
            self.attributes_sec["Żyw"].initial = 10
        elif roll < 7:
            self.attributes_sec["Żyw"].initial = 11
        elif roll < 10:
            self.attributes_sec["Żyw"].initial = 12
        else:
            self.attributes_sec["Żyw"].initial = 13

        pp_roll = rand.randint(1, 10)
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
        return mapping_roll(rand.randint(1, 100), mapping)

    def set_default_skills_and_abilities(self):
        """
        Sets the default skills and abilities for the character based on the character's race.

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
            skills.add(random_choose(constants.starting_halfling_skills_optional))
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
        Adds a new skill to the character's skills or increases the level of an existing skill.

        Args:
            new_skill (str): The name of the skill to add or increase.

        Returns:
            bool: True if the skill was successfully added or increased, False if the skill is already at the maximum level.

        Raises:
            ValueError: If the value of the skill in `self.skills` is not recognized.

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
            bool: True if the ability was successfully added, False if character has it.

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
            bool: True if an optional skill was successfully added, False if no more optional skills are available.

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
            bool: True if an optional ability was successfully added, False if no more optional abilities are available.

        """
        for ability in self.abilities:
            if ability in new_abilities:
                new_abilities.remove(ability)
        if new_abilities == []:
            return False
        return self.add_ability(random_choose(new_abilities))

    def update_any_skill(self):
        """
        Updates skill(any) in the character's skills with random choices from the corresponding value options.

        The method replaces format skill(any) that matches the predefined skills in `constants.any_skills` with random skills
        chosen from the corresponding skill options. The number of replacements depends on the current skill value.

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
        Updates ability(any) in the character's abilities with random choices from the corresponding value options.

        The method replaces format ability(any) that matches the predefined abilities in `constants.any_ability` with random
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
        Sets the starting attributes, skills, abilities, trappings based on the chosen profession.

        The method initializes the character's attributes, skills, abilities, and trappings based on the selected
        profession. It retrieves the attributes, skills, abilities, and trappings information from the
        `professions.professions` dictionary and assigns them to the character.

        """
        for atrr in professions.professions[self.profession]["attributes_main"]:
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
        for skills in professions.professions[self.profession]["optional_skills"]:
            self.add_optional_skill(skills)
        for abilities in professions.professions[self.profession]["optional_abilities"]:
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

        This method triggers a series of updates and modifications to the character based on their abilities and trappings.
        The following actions are performed in sequence:
        1. Update attributes based on abilities using the `update_attr_by_abilities` method.
        2. Set values for attributes "S" and "Wt" using the `set_S_Wt` method.
        3. Roll random values in trappings using the `roll_in_trappings` method.
        4. Extract money from trappings using the `take_money_from_trappings` method.
        5. Extract armor from trappings using the `take_armor_from_trappings` method.
        5. Extract weapons from trappings using the `take_weapon_from_trappings` method.

        """
        self.update_attr_by_abilities()
        self.set_S_Wt()
        self.roll_in_trappings()
        self.take_money_from_trappings()
        self.take_armor_from_trappings()
        self.take_weapon_from_trappings()

    def update_attr_by_abilities(self):
        """
        Update character's attributes based on their abilities.

        The method iterates over the character's abilities and checks if they have a corresponding attribute modifier in
        the `constants.ability_modify_attr` dictionary. If a match is found, the initial values of the corresponding
        attributes in `attributes_main` and `attributes_sec` are increased by specific amounts.

        """
        for ability in self.abilities:
            for key, value in constants.ability_modify_attr.items():
                if key == ability:
                    if value in self.attributes_main.keys():
                        self.attributes_main[value].initial += 5
                    if value in self.attributes_sec.keys():
                        self.attributes_sec[value].initial += 1

    def set_S_Wt(self):
        """
        Set values for attributes "S" and "Wt" based on other attributes.

        The method calculates the initial and final values for attributes "S" and "Wt" based on the initial values of
        attributes "K" and "Odp" respectively.

        """
        self.attributes_sec["S"].initial = self.attributes_main["K"].initial // 10
        self.attributes_sec["Wt"].initial = self.attributes_main["Odp"].initial // 10
        self.attributes_sec["S"].final = self.attributes_main["K"].final // 10
        self.attributes_sec["Wt"].final = self.attributes_main["Odp"].final // 10

    def roll_in_trappings(self):
        """
        Roll random values in trappings.

        The method iterates over the trappings list and replaces specific patterns with rolled values. The
        patterns include "1k10/2", "2k10", "3k10", and "6k10" representing dice rolls. The rolled values are inserted
        into the trappings list.

        """
        for idx, trapping in enumerate(self.trappings):
            self.trappings[idx] = trapping.replace("1k10/2", f"{rand.randint(1, 5)}")
            self.trappings[idx] = self.trappings[idx].replace(
                "2k10", f"{rand.randint(1, 10)+rand.randint(1, 10)}"
            )
            self.trappings[idx] = self.trappings[idx].replace(
                "3k10", f"{rand.randint(1, 10)+rand.randint(1, 10)+rand.randint(1, 10)}"
            )
            self.trappings[idx] = self.trappings[idx].replace(
                "6k10",
                f"{rand.randint(1, 10) + rand.randint(1, 10) + rand.randint(1, 10) + rand.randint(1, 10) + rand.randint(1, 10) + rand.randint(1, 10)}",
            )
            self.trappings[idx] = self.trappings[idx].replace(
                "1k10", f"{rand.randint(1, 10)}"
            )

    def take_money_from_trappings(self):
        """
        Extract money from trappings.

        The method checks the trappings list for entries containing the string " zk" (e.g., "10 zk"). If a matching
        entry is found, the corresponding amount is removed from the trappings list and added to the character's money.
        Cap at "999 zk".

        """
        for trapping in self.trappings:
            if " zk" in trapping and len(trapping) < 7:
                additional_money = int(trapping.replace(" zk", ""))
                self.trappings.remove(trapping)
                self.money += additional_money

    def take_armor_from_trappings(self):
        """
        Extracts armor from trappings and assigns it.

        The function iterates over the trappings list of the character.
        If a trapping contains the keyword 'pancerz', it checks for the type of armor and assigns it accordingly.
        The function also updates the character's advanced_armor dictionary based on the armor details.

        Raises:
            ValueError: If an unrecognized type of armor is found in the trappings.

        """
        for trapping in self.trappings:
            if "pancerz" in trapping:
                if "lekki pancerz" in trapping:
                    self.basic_armor = 1
                elif "średni pancerz" in trapping:
                    self.basic_armor = 3
                else:
                    raise ValueError("Unrecognized type of armor: {trapping}.")
                for armor_name, armor_detail in constants.armors.items():
                    if armor_name in trapping:
                        if "głowa" in armor_detail[0]:
                            self.advanced_armor["head"] += armor_detail[1]
                        if "korpus" in armor_detail[0]:
                            self.advanced_armor["body"] += armor_detail[1]
                        if "nogi" in armor_detail[0]:
                            self.advanced_armor["legs"] += armor_detail[1]
                        if "ręce" in armor_detail[0]:
                            self.advanced_armor["arms"] += armor_detail[1]
                        self.armor_list.append(armor_name)
                self.trappings.remove(trapping)

    def take_weapon_from_trappings(self):
        """
        Extracts weapons from trappings and assigns it.

        The function iterates over the trappings list of the character.
        If trapping contain weapon it's removed from trappings and asigned to weapon_list.
        """
        trappings_to_remove = []
        for trapping in self.trappings:
            for weapon_name, weapon_detail in constants.weapons.items():
                if weapon_name in trapping:
                    if weapon_name == "łuk":
                        if (
                            "długi łuk" in trapping
                            or "elfi łuk" in trapping
                            or "kislevski łuk konny"
                        ):
                            continue
                    if weapon_name == "topór":
                        if "dwuręczny topór" in trapping:
                            continue
                    if weapon_name == "broń jednoręczna":
                        self.weapon_list.append(
                            random_choose(constants.onehand_random_weapon)
                        )
                    else:
                        self.weapon_list.append(weapon_name)
                    trappings_to_remove.append(trapping)
                    if "strzał" in trapping:
                        if weapon_detail[1] == "palna":
                            self.trappings.append("proch i amunicja na 10 strzałów")
                        else:
                            self.trappings.append("10 strzał")
                    if "bełt" in trapping:
                        self.trappings.append("10 bełtów")
        for trapping in trappings_to_remove:
            self.trappings.remove(trapping)

    def roll_sex(self):
        """
        Roll the character's sex if it is not already set.

        Randomly determines the sex of the character based on a dice roll.
        If the sex is already set, no action is taken.
        """
        if self.sex is None:
            if rand.randint(1, 10) < 6:
                self.sex = "male"
            else:
                self.sex = "female"

    def roll_height(self):
        """
        Roll the character's height based on race and sex.

        Calculates the character's height based on random dice rolls and adjustments specific to their race and sex.
        The height value is stored in the 'height' attribute of the character.
        """
        self.height = 100 + rand.randint(1, 10) + rand.randint(1, 10)
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

        Calculates the character's weight based on a random dice roll and adjustments specific to their race.
        The weight value is stored in the 'weight' attribute of the character.
        """
        roll = rand.randint(1, 100)
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

        Randomly selects the character's hair color from a predefined list of hair colors specific to their race.
        The selected hair color is stored in the 'hair' attribute of the character.
        """
        if self.race == "human":
            hair_list = constants.human_hair_list
        if self.race == "dwarf":
            hair_list = constants.dwarf_hair_list
        if self.race == "halfling":
            hair_list = constants.halfling_hair_list
        if self.race == "elf":
            hair_list = constants.elf_hair_list
        self.hair = hair_list[rand.randint(1, 10) - 1]

    def roll_eye(self):
        """
        Roll the character's eye color based on race.

        Randomly selects the character's eye color from a predefined list of eye colors specific to their race.
        The selected eye color is stored in the 'eye' attribute of the character.
        """
        if self.race == "human":
            eye_list = constants.human_eye_list
        if self.race == "dwarf":
            eye_list = constants.dwarf_eye_list
        if self.race == "halfling":
            eye_list = constants.halfling_eye_list
        if self.race == "elf":
            eye_list = constants.elf_eye_list
        self.eye = eye_list[rand.randint(1, 10) - 1]

    def roll_special(self):
        """
        Roll the character's special characteristic.

        Generates a random value for the character's special characteristic based on a dice roll and a predefined mapping.
        The value is stored in the 'special' attribute of the character.
        """
        roll = rand.randint(1, 100)
        self.special = mapping_roll(roll, constants.special_mapping)

    def roll_siblings(self):
        """
        Roll the number of character's siblings based on race.

        Generates the number of siblings for the character based on a random dice roll and adjustments specific to their race.
        The number of siblings is stored in the 'siblings' attribute of the character.
        """
        roll = rand.randint(1, 10)
        if self.race == "dwarf":
            mapping = constants.siblings_dwarf_mapping
        elif self.race == "elf":
            mapping = constants.siblings_elf_mapping
        else:
            mapping = constants.siblings_human_mapping
        self.siblings = mapping_roll(roll, mapping)
        if self.race == "halfling":
            self.siblings += 1

    def roll_star(self):
        """
        Roll the character's star sign.

        Generates the character's star sign based on a random dice roll and a predefined mapping.
        The star sign is stored in the 'star' attribute of the character.
        """
        roll = rand.randint(1, 100)
        self.star = mapping_roll(roll, constants.star_mapping)

    def roll_age(self):
        """
        Roll the character's age based on race.

        Calculates the character's age based on a random dice roll and adjustments specific to their race.
        The age value is stored in the 'age' attribute of the character.
        """
        roll = rand.randint(1, 100)
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

    def roll_birthplace(self):
        """
        Roll the character's birthplace based on race.

        Generates the character's birthplace based on random dice rolls and adjustments specific to their race.
        The birthplace is stored in the 'birthplace' attribute of the character.
        """
        if self.race == "dwarf":
            if rand.randint(1, 100) > 30:
                self.birthplace = random_choose(constants.dwarf_birthplace_list)
        elif self.race == "elf":
            self.birthplace = mapping_roll(
                rand.randint(1, 100), constants.elf_birthplace_dict
            )
        elif self.race == "halfling":
            if rand.randint(1, 100) < 50:
                self.birthplace = constants.halfling_most_common_birthplace
        if self.birthplace is None:
            province = random_choose(list(constants.town_dict.keys()))
            town = mapping_roll(rand.randint(1, 100), constants.town_dict[province])
            self.birthplace = f"{province}, {town}"

    def roll_name(self):
        """
        Roll the character's name based on race and sex.

        Generates the character's name based on random selections from predefined name lists specific to their race and sex.
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
                firstname = f"{random_choose(constants.dwarf_name1_list)}{random_choose(constants.dwarf_male_name2_list)}"
                surname = f"{random_choose(constants.dwarf_name1_list)}{random_choose(constants.dwarf_male_name2_list)}son"
            else:
                firstname = f"{random_choose(constants.dwarf_name1_list)}{random_choose(constants.dwarf_female_name2_list)}"
                surname = f"{random_choose(constants.dwarf_name1_list)}{random_choose(constants.dwarf_female_name2_list)}sdotr"
        if self.race == "elf":
            surname = random_choose(constants.elf_surname_list)
            if rand.randint(1, 10) < 6:
                connector = random_choose(constants.elf_name_connector_list)
            else:
                connector = ""
            if self.sex == "male":
                firstname = f"{random_choose(constants.elf_name1_list)}{connector}{random_choose(constants.elf_male_name2_list)}"
            else:
                firstname = f"{random_choose(constants.elf_name1_list)}{connector}{random_choose(constants.elf_female_name2_list)}"
        if self.race == "halfling":
            surname = random_choose(constants.halfling_surname_list)
            if self.sex == "male":
                firstname = f"{random_choose(constants.halfling_name1_list)}{random_choose(constants.halfling_male_name2_list)}"
            else:
                firstname = f"{random_choose(constants.halfling_name1_list)}{random_choose(constants.halfling_female_name2_list)}"

        self.name = f"{firstname} {surname}"

    def roll_money(self):
        """
        Roll the character's starting money.

        Generates the starting money for the character based on random dice rolls.
        The money is stored in the 'money' attribute of the character.
        """
        self.money = rand.randint(1, 10) + rand.randint(1, 10)

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

        Rolls all character attributes including race, profession, sex, name, height, weight, hair color, eye color,
        special characteristics, siblings, star sign, age, birthplace, attributes, money, skills, abilities, and updates them accordingly.
        You can also set all by yourself.
        This method generates a complete character with all the attributes and stores them in the respective attributes of the character.
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

    def print_character(self):
        """
        Print the character's attributes.

        Prints all the character's attributes including name, race, profession, sex, age, eye color, hair color,
        star sign, weight, height, number of siblings, birthplace, special characteristics, skills, abilities, main attributes,
        secondary attributes, trappings, and starting money.
        """
        print(f"Imię i nazwisko/przydomek: {self.name}")
        print(f"Rasa: {self.race}")
        print(f"Profesja: {self.profession}")
        print(f"Płeć: {self.sex}")
        print(f"Wiek: {self.age}")
        print(f"Kolor oczu: {self.eye}")
        print(f"Kolor włosów: {self.hair}")
        print(f"Znak gwiezdny: {self.star}")
        print(f"Masa: {self.weight} kg")
        print(f"Wzrost: {self.height} cm")
        print(f"Ilość rodzeństwa: {self.siblings}")
        print(f"Miejsce urodzenia: {self.birthplace}")
        print(f"Znaki szczególne: {self.special}")
        print(self.skills)
        print(self.abilities)
        print(self.attributes_main)
        print(self.attributes_sec)
        print(self.trappings)
        print(f"{self.money} zk")
