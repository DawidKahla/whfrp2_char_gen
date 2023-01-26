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
        