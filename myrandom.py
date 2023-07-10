"""
This module contains functions related to randomness
such as dice roll, choosing random element from list
and get value from specified dictionary base on roll.
"""
from random import randint

def d10():
    """
    Represent a projection of a ten-sided dice.

    Returns:
        Random number from 1 to 10.
    """
    return randint(1, 10)


def random_choose(some_list):
    """
    Rolls a random element from a list.

    Parameters:
        some_list (list): The list to roll an element from.

    Returns:
        The randomly selected element from the list.
    """
    return some_list[randint(0, len(some_list) - 1)]


def mapping_roll(roll, mapping) -> str:
    """
    Get a value from a mapping based on the input roll.

    Parameters:
        roll (int): The number corresponding to a key in the mapping.
        mapping (dict): A dictionary containing 2-number tuples
            as keys and strings as values.

    Returns:
        The value associated with the input roll in the mapping.

    Raises:
        ValueError: If the roll is not present in the keys of the mapping.
    """
    for key in mapping.keys():
        minimum, maximum = key
        if minimum <= roll <= maximum:
            return mapping[key]
    raise ValueError(f"Roll: ({roll}) not in mapping: ({mapping})")
