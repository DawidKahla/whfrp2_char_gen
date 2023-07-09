class Equipment:
    def __init__(self) -> None:
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