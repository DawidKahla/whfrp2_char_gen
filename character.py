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
        self.attributes = {
            'WW': [0,0,0],
            'US': [0,0,0],
            'K': [0,0,0],
            'Odp': [0,0,0],
            'Zr': [0,0,0],
            'Int': [0,0,0],
            'SW': [0,0,0],
            'Ogd': [0,0,0],
            'A': [0,0,0],
            'Żyw': [0,0,0],
            'S': [0,0,0],
            'Wt': [0,0,0],
            'Sz': [0,0,0],
            'Mag': [0,0,0],
            'PO': [0,0,0],
            'PP': [0,0,0],
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
            raise Exception("Wrong race in roll_profession")
        
        keys = mapping.keys()
        roll = d1000()
        for key in keys:
            minimum, maximum = key
            if roll >= minimum and roll <= maximum:
                self.profession = mapping[key]

    def print_character(self):
        print(self.race)
        print(self.profession)