"""
This module provides Equipment class.
"""
from random import randint
from myrandom import d10, random_choose
import constants

class Equipment:
    """
    Represents the classified equipment of the character.

    Atrributes:
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
    
    def __init__(self) -> None:
        """
        Initializes a new instance of the Equipment class.
        """
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

    def roll_money(self):
        """
        Roll the character's starting money.

        Generates the starting money for the character
        based on random dice rolls.
        The money is stored in the 'money' attribute of the character.
        """
        self.money = d10() + d10()

    def roll_in_trappings(self):
        """
        Roll random values in trappings.

        The method iterates over the trappings list and replaces
        specific patterns with rolled values. The patterns include
        "1k10/2", "2k10", "3k10", and "6k10" representing dice rolls.
        The rolled values are inserted into the trappings list.

        """
        for idx, trapping in enumerate(
            self.trappings
        ):
            self.trappings[idx] = trapping.replace(
                "1k10/2", f"{randint(1, 5)}")
            self.trappings[idx] = self.trappings[idx].replace(
                "2k10", f"{d10()+d10()}"
            )
            self.trappings[idx] = self.trappings[idx].replace(
                "3k10", f"{d10()+d10()+d10()}"
            )
            self.trappings[idx] = self.trappings[idx].replace(
                "6k10", f"{d10() + d10() + d10() + d10() + d10() + d10()}",
            )
            self.trappings[idx] = self.trappings[idx].replace(
                "1k10", f"{d10()}"
            )

    def take_money_from_trappings(self):
        """
        Extract money from trappings.

        The method checks the trappings list for entries
        containing the string " zk" (e.g., "10 zk"). If a matching
        entry is found, the corresponding amount is removed from
        the trappings list and added to the character's money.
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
        If a trapping contains the keyword 'pancerz', it checks for the
        type of armor and assigns it accordingly.
        The function also updates the character's advanced_armor dictionary
        based on the armor details.

        Raises:
            ValueError: If an unrecognized type of armor is found
                in the trappings.

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
        If trapping contain weapon it's removed from trappings
        and asigned to weapon_list.
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
                            self.trappings.append(
                                "proch i amunicja na 10 strzałów"
                                )
                        else:
                            self.trappings.append("10 strzał")
                    if "bełt" in trapping:
                        self.trappings.append("10 bełtów")
        for trapping in trappings_to_remove:
            self.trappings.remove(trapping)
