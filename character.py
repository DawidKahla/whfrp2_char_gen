import random as rand
import constants

def d10():
    return rand.randint(1,10)

def d100():
    return rand.randint(1,100)

def d1000():
    return rand.randint(1,1000)

def r20_2d10():
    return 20 + d10() + d10() 

def random_choose(list):
    return list[rand.randint(0, len(list)-1)]

def roll_ability(race):
    if race == 'halfling':
        mapping = constants.halfling_ability_mapping
    elif race == 'human':
        mapping = constants.human_ability_mapping
    else:
        raise Exception(f"Wrong race in roll_ability {race}")
    
    keys = mapping.keys()
    roll = d100()
    for key in keys:
        minimum, maximum = key
        if roll >= minimum and roll <= maximum:
            return mapping[key]

def race_translate(race):
    if race == 'human':
        return 'Człowiek'
    elif race == 'halfling':
        return 'Niziołek'
    elif race == 'dwarf':
        return 'Krasnolud'
    elif race == 'elf':
        return 'Elf'
    raise Exception(f"Wrong race in translation {race}")

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
            'WW': 0,
            'US': 0,
            'K': 0,
            'Odp': 0,
            'Zr': 0,
            'Int': 0,
            'SW': 0,
            'Ogd': 0
        }
        self.attributes_sec = {
            'A': 0,
            'Żyw': 0,
            'S': 0,
            'Wt': 0,
            'Sz': 0,
            'Mag': 0,
            'PO': 0,
            'PP': 0,
        }
        self.skills = {}
        self.abilities = {}
    
    def roll_race(self):
        roll = d100()
        if roll == 1:
            output = 'elf'
        elif roll < 6:
            output = 'dwarf'
        elif roll < 11:
            output = 'halfling'
        else: 
            output = 'human'
        self.race = output
    
    def roll_profession(self):
        if self.race == 'elf':
            mapping = constants.elf_profession_mapping
        elif self.race == 'dwarf':
            mapping = constants.dwarf_profession_mapping
        elif self.race == 'halfling':
            mapping = constants.halfling_profession_mapping
        elif self.race == 'human':
            mapping = constants.human_profession_mapping
        else:
            raise Exception(f"Wrong race in roll_profession {self.race}")
        
        keys = mapping.keys()
        roll = d1000()
        for key in keys:
            minimum, maximum = key
            if roll >= minimum and roll <= maximum:
                self.profession = mapping[key]
    
    def roll_attributes(self):
        #self.attributes_main = {attr: r20_2d10() for attr in self.attributes_main}
        # fixed values for tests
        self.attributes_main = {attr: 25 for attr in self.attributes_main}
        self.attributes_sec['A'] = 1
        self.attributes_sec['Sz'] = 4
        
        roll = d10()
        if roll < 4:
            self.attributes_sec['Żyw'] = 10
        elif roll < 7:
            self.attributes_sec['Żyw'] = 11
        elif roll < 10:
            self.attributes_sec['Żyw'] = 12
        else:
            self.attributes_sec['Żyw'] = 13

        pp_roll = d10()
        if pp_roll < 5:
            self.attributes_sec['PP'] = 2
        else:
            self.attributes_sec['PP'] = 3

        if self.race == 'halfling':
            # Czy można to zrobić list comperhension
            self.attributes_main['WW'] -= 10
            self.attributes_main['K'] -= 10
            self.attributes_main['Odp'] -= 10
            self.attributes_main['Ogd'] += 10
            self.attributes_main['US'] += 10
            self.attributes_main['Zr'] += 10
            self.attributes_sec['Żyw'] -= 2
            if pp_roll < 8:
                self.attributes_sec['PP'] = 2
        
        if self.race == 'dwarf':
            self.attributes_main['WW'] += 10
            self.attributes_main['Zr'] -= 10
            self.attributes_main['Ogd'] -= 10
            self.attributes_main['Odp'] += 10
            self.attributes_sec['Żyw'] += 1
            self.attributes_sec['Sz'] = 3
            if pp_roll < 8:
                self.attributes_sec['PP'] -= 1
        
        if self.race == 'elf':
            self.attributes_main['US'] += 10
            self.attributes_main['Zr'] += 10
            self.attributes_sec['Żyw'] -= 1
            self.attributes_sec['PP'] -= 1
            self.attributes_sec['Sz'] = 5

    def set_default_skills_and_abilities(self):
        if self.race == 'human':
            skills = ['Plotkowanie', 'Wiedza(Imperium)', 'Znajomość języka(staroświatowy)']
            ab1 = roll_ability(self.race)
            ab2 = roll_ability(self.race)
            while ab1 == ab2:
                ab2 = roll_ability(self.race)
            abilities = [ab1, ab2]
        
        if self.race == 'halfling':
            skills = ['Plotkowanie', 'Wiedza (niziołki))', 'Znajomość języka (staroświatowy)', 'Znajomość języka( niziołków)', 'Nauka (genealogia/heraldyka)', random_choose(['Rzemiosło (gotowanie)','Rzemiosło (uprawa ziemi)'])]
            abilities = ['Broń specjalna (proca)', 'Odporność na Chaos', 'Widzenie w ciemności', roll_ability(self.race)]

        if self.race == 'dwarf':
            skills = ['Wiedza (krasnoludy)', 'Znajomość języka (khazalid)', 'Znajomość języka (staroświatowy)', random_choose(['Rzemiosło (górnictwo)','Rzemiosło (kamieniarstwo)','Rzemiosło (kowalstwo)'])]
            abilities = ['Krasnoludzki fach', 'Krzepki', 'Odporność na magię', 'Odwaga', 'Widzenie w ciemności', 'Zapiekła nienawiść']

        if self.race == 'elf':
            skills = ['Wiedza (elfy)', 'Znajomość języka (eltharin)', 'Znajomość języka(staroświatowy)']
            abilities = ['Bystry wzrok', 'Widzenie w ciemności', random_choose(['Broń specjalna (długi łuk)','Zmysł magii']), random_choose(['Opanowanie','Błyskotliwość'])]
        
        self.skills = skills
        self.abilities = abilities

    def update(self):
        self.update_attr_by_abilities()
        self.set_S_Wt()


    def update_attr_by_abilities(self):
        # self.attributes_main = {constants.ability_modify_attr[key][0]: constants.ability_modify_attr.values[key][1] + self.attributes_main[constants.ability_modify_attr[key][0]] for key in constants.ability_modify_attr if key in self.abilities}
        # czy można to zapisać prościej? czy takie wykorzystanie try except jest poprawne?
        for ability in self.abilities:
            for key in constants.ability_modify_attr:
                if key == ability:
                    try:
                        self.attributes_main[constants.ability_modify_attr[key]] += 5 
                    except:
                        self.attributes_sec[constants.ability_modify_attr[key]] += 1

    def set_S_Wt(self):
        self.attributes_sec['S'] = self.attributes_main['K']//10
        self.attributes_sec['Wt'] = self.attributes_main['Odp']//10
    
    def roll_sex(self):
        if self.sex == None:
            if d10() < 6:
                self.sex = 'Mężczyzna'
            else:
                self.sex = 'Kobieta'

    def roll_height(self):
        self.height = 100 + d10() + d10()
        if self.sex == 'Mężczyzna':
            self.height += 10
        if self.race == 'dwarf':
            self.height += 30
            if self.sex == 'Mężczyzna':
                self.height += 5
        if self.race == 'human':
            self.height += 50
        if self.race == 'elf':
            self.height += 60   
    
    def roll_weight(self):
        roll = d100()
        if self.race == 'halfling':
            mapping = constants.halfling_weight_mapping
        else:
            mapping = constants.common_weight_mapping
        keys = mapping.keys()
        for key in keys:
            minimum, maximum = key
            if roll >= minimum and roll <= maximum:
                self.weight = mapping[key]
        if self.race == 'elf':
            self.weight -= 5
        if self.race == 'human':
            self.weight += 5
            if roll == 100:
                self.weight = 110

    def roll_hair(self):
        pass

    def roll_eye(self):
        pass

    def roll_special(self):
        pass

    def roll_siblings(self):
        pass

    def roll_star(self):
        pass

    def roll_age(self):
        pass

    def roll_birthplace(self):
        pass

    def roll_name(self):
        pass
    
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
        self.update()

    def print_character(self):
        # print(self.name)
        print(race_translate(self.race))
        # print(self.profession)
        print(self.sex)
        # print(self.age) 
        # print(self.eye) 
        # print(self.hair) 
        # print(self.star) 
        print(f"{self.weight} kg") 
        print(f"{self.height} cm") 
        # print(self.siblings)
        # print(self.birthplace)
        # print(self.special)
        # print(self.skills)
        # print(self.abilities)
        # print(self.attributes_main)
        # print(self.attributes_sec)
        
