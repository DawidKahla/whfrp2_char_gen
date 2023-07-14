"""
This module provides character creating functions and interface.

"""
import os
from character import Character
from imagefiller import generate_pdf
from translations import race_translate, sex_translate
from professions import professions


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_random_character(output_file_name):
    new_character = Character()
    new_character.roll_all()
    generate_pdf(output_file_name, new_character)


def create_specified_character(output_file_name):
    print('')
    # char_info: 0 - race, 1 - profession, 2 - sex,
    # 3 - name, 4 - height, 5 - weight, 6 - hair,
    # 7 - eye, 8 - special, 9 - siblings, 10 - star,
    # 11 - age, 12 - birthplace
    char_info = [None for _ in range(12)]
    
    while char_info[0] not in [
        'Człowiek', 'Elf', 'Niziołek', 'Krasnolud', 'Losowe'
    ]:
        clear_screen()
        print('Podaj rasę (człowiek, elf, niziołek, krasnolud, losowe): ')
        char_info[0] = input()
        char_info[0] = char_info[0].capitalize()
    if char_info[0] != 'Losowe':
        char_info[0] = race_translate(char_info[0])

    while char_info[1] not in professions and char_info[1] not in ['losowe']:
        clear_screen()
        print('Podaj profesję (jedna z predefiniowanych lub losowe): ')
        char_info[1] = input()
        if char_info[1] != 'losowe':
            char_info[1] = char_info[1].upper()
    
    while char_info[2] not in ['Kobieta', 'Mężczyzna', 'Losowe']:
        clear_screen()
        print('Podaj płeć (kobieta, mężczyzna, losowe): ')
        char_info[2] = input()
        char_info[2] = char_info[2].capitalize()
    if char_info[2] != 'Losowe':
        char_info[2] = sex_translate(char_info[2])



def interface():
    create_specified_character('')
