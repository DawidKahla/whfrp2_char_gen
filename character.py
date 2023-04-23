import random as rand
import constants
import professions
from dataclasses import dataclass


def d10():
    return rand.randint(1, 10)


def d100():
    return rand.randint(1, 100)


def d1000():
    return rand.randint(1, 1000)


def r20_2d10():
    return 20 + d10() + d10()


def random_choose(list):
    return list[rand.randint(0, len(list) - 1)]


def mapping_roll(roll, mapping):
    for key in mapping.keys():
        minimum, maximum = key
        if roll >= minimum and roll <= maximum:
            return mapping[key]


def race_translate(race):
    mapping = {
        "human": "Człowiek",
        "halfling": "Niziołek",
        "dwarf": "Krasnolud",
        "elf": "Elf",
    }
    if race not in mapping:
        raise Exception(f"Wrong race in translation: {race}")
    return mapping[race]


@dataclass
class atrribute:
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
        self.xp = None
        self.attributes_main = {
            "WW": atrribute(0, 0, 0),
            "US": atrribute(0, 0, 0),
            "K": atrribute(0, 0, 0),
            "Odp": atrribute(0, 0, 0),
            "Zr": atrribute(0, 0, 0),
            "Int": atrribute(0, 0, 0),
            "SW": atrribute(0, 0, 0),
            "Ogd": atrribute(0, 0, 0),
        }
        self.attributes_sec = {
            "A": atrribute(0, 0, 0),
            "Żyw": atrribute(0, 0, 0),
            "S": atrribute(0, 0, 0),
            "Wt": atrribute(0, 0, 0),
            "Sz": atrribute(0, 0, 0),
            "Mag": atrribute(0, 0, 0),
            "PO": atrribute(0, 0, 0),
            "PP": atrribute(0, 0, 0),
        }
        self.skills = {}
        self.abilities = []
        self.trappings = []

    def roll_race(self):
        roll = d100()
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

        roll = d1000()
        self.profession = mapping_roll(roll, mapping)

    def roll_attributes(self):
        self.attributes_main = {
            attr: atrribute(r20_2d10(), 0, 0) for attr in self.attributes_main
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
        if self.race == "halfling":
            mapping = constants.halfling_ability_mapping
        elif self.race == "human":
            mapping = constants.human_ability_mapping
        else:
            raise Exception(f"Wrong race in roll_ability {self.race}")
        return mapping_roll(d100(), mapping)

    def set_default_skills_and_abilities(self):
        if self.race == "human":
            skills = {
                "plotkowanie",
                "wiedza (Imperium)",
                "znajomość języka (staroświatowy)",
            }

            ab1 = self.roll_ability()
            ab2 = self.roll_ability()
            while ab1 == ab2:
                ab2 = self.roll_ability()
            abilities = [ab1, ab2]

        if self.race == "halfling":
            skills = [
                "plotkowanie",
                "wiedza (niziołki)",
                "znajomość języka (staroświatowy)",
                "znajomość języka (niziołków)",
                "nauka (genealogia/heraldyka)",
                random_choose(["rzemiosło (gotowanie)", "rzemiosło (uprawa ziemi)"]),
            ]
            abilities = [
                "broń specjalna (proca)",
                "odporność na Chaos",
                "widzenie w ciemności",
                self.roll_ability(),
            ]

        if self.race == "dwarf":
            skills = [
                "wiedza (krasnoludy)",
                "znajomość języka (khazalid)",
                "znajomość języka (staroświatowy)",
                random_choose(
                    [
                        "rzemiosło (górnictwo)",
                        "rzemiosło (kamieniarstwo)",
                        "rzemiosło (kowalstwo)",
                    ]
                ),
            ]
            abilities = [
                "krasnoludzki fach",
                "krzepki",
                "odporność na magię",
                "odwaga",
                "widzenie w ciemności",
                "zapiekła nienawiść",
            ]

        if self.race == "elf":
            skills = [
                "wiedza (elfy)",
                "znajomość języka (eltharin)",
                "znajomość języka (staroświatowy)",
            ]
            abilities = [
                "bystry wzrok",
                "widzenie w ciemności",
                random_choose(["broń specjalna (długi łuk)", "zmysł magii"]),
                random_choose(["opanowanie", "błyskotliwość"]),
            ]

        self.skills = {skill: "Wykupione" for skill in skills}
        self.abilities = abilities

    def add_skill(self, new_skill):
        if new_skill in self.skills.keys():
            if self.skills[new_skill] == "Wykupione":
                self.skills[new_skill] = "+10"
            elif self.skills[new_skill] == "+10":
                self.skills[new_skill] = "+20"
            elif self.skills[new_skill] == "+20":
                return False  # skill is maxed out
            else:
                raise Exception("Wrong value of skill in add_skill function.")
        else:
            self.skills[new_skill] = "Wykupione"
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
        for skill in constants.any_skills.keys():
            if skill in self.skills:
                if self.skills[skill] == "+20":
                    self.add_skill(random_choose(constants.any_skills[skill]))
                    self.add_skill(random_choose(constants.any_skills[skill]))
                    self.add_skill(random_choose(constants.any_skills[skill]))
                elif self.skills[skill] == "+10":
                    self.add_skill(random_choose(constants.any_skills[skill]))
                    self.add_skill(random_choose(constants.any_skills[skill]))
                else:
                    self.add_skill(random_choose(constants.any_skills[skill]))
                self.skills.pop(skill)

    def update_any_ability(self):
        for ability in constants.any_ability.keys():
            if ability in self.abilities:
                while True:
                    if self.add_ability(random_choose(constants.any_ability[ability])):
                        self.abilities.remove(ability)
                        break

    def set_starting_profession(self):
        for atrr in professions.professions[self.profession]["atrributes_main"]:
            self.attributes_main[atrr].potential = professions.professions[
                self.profession
            ]["atrributes_main"][atrr]
        for atrr in professions.professions[self.profession]["atrributes_sec"]:
            self.attributes_sec[atrr].potential = professions.professions[
                self.profession
            ]["atrributes_sec"][atrr]
        for skill in professions.professions[self.profession]["skills"]:
            self.add_skill(skill)  # return False here doesn't have effect
        for ability in professions.professions[self.profession]["abilities"]:
            self.add_ability(ability)  # return False here doesn't have effect
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
            for key in constants.ability_modify_attr:
                if key == ability:
                    if (
                        constants.ability_modify_attr[key]
                        in self.attributes_main.keys()
                    ):
                        self.attributes_main[
                            constants.ability_modify_attr[key]
                        ].initial += 5
                    if constants.ability_modify_attr[key] in self.attributes_sec.keys():
                        self.attributes_sec[
                            constants.ability_modify_attr[key]
                        ].initial += 1

    def set_S_Wt(self):
        self.attributes_sec["S"].initial = self.attributes_main["K"].initial // 10
        self.attributes_sec["Wt"].initial = self.attributes_main["Odp"].initial // 10
        self.attributes_sec["S"].final = self.attributes_main["K"].final // 10
        self.attributes_sec["Wt"].final = self.attributes_main["Odp"].final // 10

    def roll_sex(self):
        if self.sex == None:
            if d10() < 6:
                self.sex = "Mężczyzna"
            else:
                self.sex = "Kobieta"

    def roll_height(self):
        self.height = 100 + d10() + d10()
        if self.sex == "Mężczyzna":
            self.height += 10
        if self.race == "dwarf":
            self.height += 30
            if self.sex == "Mężczyzna":
                self.height += 5
        if self.race == "human":
            self.height += 50
        if self.race == "elf":
            self.height += 60

    def roll_weight(self):
        roll = d100()
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
        self.hair = hair_list[d10() - 1]

    def roll_eye(self):
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
        roll = d100()
        for key in constants.special_mapping.keys():
            minimum, maximum = key
            if roll >= minimum and roll <= maximum:
                self.special = constants.special_mapping[key]

    def roll_siblings(self):
        roll = d10()
        if self.race == "dwarf":
            mapping = constants.siblings_dwarf_mapping
        elif self.race == "elf":
            mapping = constants.siblings_elf_mapping
        else:
            mapping = constants.siblings_human_mapping
        for key in mapping:
            minimum, maximum = key
            if roll >= minimum and roll <= maximum:
                self.siblings = mapping[key]
        if self.race == "halfling":
            self.siblings += 1

    def roll_star(self):
        roll = d100()
        for key in constants.star_mapping.keys():
            minimum, maximum = key
            if roll >= minimum and roll <= maximum:
                self.star = constants.star_mapping[key]

    def roll_age(self):
        roll = d100()
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
            if d100() > 30:
                self.birthplace = random_choose(constants.dwarf_birthplace_list)
        elif self.race == "elf":
            self.birthplace = mapping_roll(d100(), constants.elf_birthplace_dict)
        elif self.race == "halfling":
            if d100() < 50:
                self.birthplace = "Kraina Zgromadzenia"
        if self.birthplace == None:
            province = random_choose(list(constants.town_dict.keys()))
            town = mapping_roll(d100(), constants.town_dict[province])
            self.birthplace = f"{province}, {town}"

    def roll_name(self):
        if self.race == "human":
            surname = random_choose(constants.human_surname_list)
            if self.sex == "Mężczyzna":
                firstname = random_choose(constants.human_male_name_list)
            else:
                firstname = random_choose(constants.human_female_name_list)
        if self.race == "dwarf":
            if self.sex == "Mężczyzna":
                firstname = f"{random_choose(constants.dwarf_name1_list)}{random_choose(constants.dwarf_male_name2_list)}"
                surname = f"{random_choose(constants.dwarf_name1_list)}{random_choose(constants.dwarf_male_name2_list)}son"
            else:
                firstname = f"{random_choose(constants.dwarf_name1_list)}{random_choose(constants.dwarf_female_name2_list)}"
                surname = f"{random_choose(constants.dwarf_name1_list)}{random_choose(constants.dwarf_female_name2_list)}sdotr"
        if self.race == "elf":
            surname = random_choose(constants.elf_surname_list)
            if d10() < 6:
                connector = random_choose(constants.elf_name_connector_list)
            else:
                connector = ""
            if self.sex == "Mężczyzna":
                firstname = f"{random_choose(constants.elf_name1_list)}{connector}{random_choose(constants.elf_male_name2_list)}"
            else:
                firstname = f"{random_choose(constants.elf_name1_list)}{connector}{random_choose(constants.elf_female_name2_list)}"
        if self.race == "halfling":
            surname = random_choose(constants.halfling_surname_list)
            if self.sex == "Mężczyzna":
                firstname = f"{random_choose(constants.halfling_name1_list)}{random_choose(constants.halfling_male_name2_list)}"
            else:
                firstname = f"{random_choose(constants.halfling_name1_list)}{random_choose(constants.halfling_female_name2_list)}"

        self.name = f"{firstname} {surname}"

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
        self.set_default_skills_and_abilities()
        self.set_starting_profession()
        self.update_any_skill()
        self.update_any_ability()
        self.update()

    def print_character(self):
        print(f"Imię i nazwisko/przydomek: {self.name}")
        print(f"Rasa: {race_translate(self.race)}")
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
        print(d10() + d10())
