"""
This module provides character class and generating all stats.
"""
import random as rand
from dataclasses import dataclass
import constants
import professions


def random_choose(list):
    """
    Roll one random element of list.

    :param list: List to roll element from.
    :type list: list
    :return: One element of list.
    :rtype: not defined
    """
    return list[rand.randint(0, len(list) - 1)]


def mapping_roll(roll, mapping):
    """
    Get value from mapping depends on input roll.

    :param roll: Number in mapping keys.
    :type roll: int
    :param mapping: Containing 2 numbers tuples as keys and strings as values.
    :type mapping: dict
    :return: Value from mapping
    :r type: str
    :raises ValueError: If roll not in mapping keys.
    """
    for key in mapping.keys():
        minimum, maximum = key
        if roll >= minimum and roll <= maximum:
            return mapping[key]
    raise ValueError(f"Roll: ({roll}) not in mapping: ({mapping})")


@dataclass
class attribute:
    """
    Represents attribute with initial, potential and final values.

    :param initial: The initial value of the attribute, depends on race and rolls.
    :type initial: int
    :param potential: The value of potential attribute growth, depends on profession.
    :type potential: int
    :param final: The final value of attribute.
    :type final: int
    """

    initial: int
    potential: int
    final: int


class Character(object):
    def __init__(self):
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

    def roll_race(self):
        roll = rand.randint(1, 100)
        if roll == 1:
            output = "elf"
        elif roll < 6:
            output = "dwarf"
        elif roll < 11:
            output = "halfling"
        else:
            output = "human"
        self.race = output

    def roll_profession(self):
        if self.race == "elf":
            mapping = constants.elf_profession_mapping
        elif self.race == "dwarf":
            mapping = constants.dwarf_profession_mapping
        elif self.race == "halfling":
            mapping = constants.halfling_profession_mapping
        elif self.race == "human":
            mapping = constants.human_profession_mapping
        else:
            raise Exception(f"Wrong race in roll_profession {self.race}")

        roll = rand.randint(1, 1000)
        # self.profession = mapping_roll(roll, mapping)
        self.profession = "CYRKOWIEC"

    def roll_attributes(self):
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
        if self.race == "halfling":
            mapping = constants.halfling_ability_mapping
        elif self.race == "human":
            mapping = constants.human_ability_mapping
        else:
            raise ValueError(f"Wrong race in roll_ability {self.race}")
        return mapping_roll(rand.randint(1, 100), mapping)

    def set_default_skills_and_abilities(self):
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
            abilities.extend(self.roll_ability())

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

    def add_skill(self, new_skill):
        if new_skill in self.skills.keys():
            if self.skills[new_skill] == "bought":
                self.skills[new_skill] = "+10"
            elif self.skills[new_skill] == "+10":
                self.skills[new_skill] = "+20"
            elif self.skills[new_skill] == "+20":
                return False  # skill is maxed out
            else:
                raise ValueError("Wrong value of skill in add_skill function.")
        else:
            self.skills[new_skill] = "bought"
        return True

    def add_ability(self, new_ability):
        if new_ability in self.abilities:
            return False
        self.abilities.append(new_ability)
        return True

    def add_optional_skill(self, new_skills):
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

    def add_optional_ability(self, new_abilities):
        for ability in self.abilities:
            if ability in new_abilities:
                new_abilities.remove(ability)
        if new_abilities == []:
            return False
        return self.add_ability(random_choose(new_abilities))

    def update_any_skill(self):
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
        for ability, values in constants.any_ability.items():
            if ability in self.abilities:
                while True:
                    if self.add_ability(random_choose(values)):
                        self.abilities.remove(ability)
                        break

    def set_starting_profession(self):
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

    def update(self):
        self.update_attr_by_abilities()
        self.set_S_Wt()

    def update_attr_by_abilities(self):
        for ability in self.abilities:
            for key, value in constants.ability_modify_attr.items():
                if key == ability:
                    if value in self.attributes_main.keys():
                        self.attributes_main[value].initial += 5
                    if value in self.attributes_sec.keys():
                        self.attributes_sec[value].initial += 1

    def set_S_Wt(self):
        self.attributes_sec["S"].initial = self.attributes_main["K"].initial // 10
        self.attributes_sec["Wt"].initial = self.attributes_main["Odp"].initial // 10
        self.attributes_sec["S"].final = self.attributes_main["K"].final // 10
        self.attributes_sec["Wt"].final = self.attributes_main["Odp"].final // 10

    def roll_sex(self):
        if self.sex == None:
            if rand.randint(1, 10) < 6:
                self.sex = "male"
            else:
                self.sex = "female"

    def roll_height(self):
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
        roll = rand.randint(1, 100)
        self.special = mapping_roll(roll, constants.special_mapping)

    def roll_siblings(self):
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
        roll = rand.randint(1, 100)
        self.star = mapping_roll(roll, constants.star_mapping)

    def roll_age(self):
        roll = rand.randint(1, 100)
        x = (roll - 1) // 5
        if self.race == "human":
            self.age = 16 + x
        elif self.race == "halfling":
            self.age = 20 + 2 * x
            if roll > 70:
                self.age += 2
        else:
            self.age = 20 + 5 * x  # dwarf
            if self.race == "elf":
                self.age += 10

    def roll_birthplace(self):
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
        self.money = rand.randint(1, 10) + rand.randint(1, 10)

    def roll_all(self):
        self.roll_race()
        self.roll_profession()
        self.roll_sex()
        self.roll_name()
        self.roll_height()
        self.roll_weight()
        self.roll_hair()
        self.roll_eye()
        self.roll_special()
        self.roll_siblings()
        self.roll_star()
        self.roll_age()
        self.roll_birthplace()
        self.roll_attributes()
        self.roll_money()
        self.set_default_skills_and_abilities()
        self.set_starting_profession()
        self.update_any_skill()
        self.update_any_ability()
        self.update()

    def print_character(self):
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
