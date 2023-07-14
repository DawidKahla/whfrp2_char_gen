"""
This module provides character creating functions and interface.

"""
from character import Character
from imagefiller import generate_pdf
import curses


def create_random_character(output_file_name):
    new_character = Character()
    new_character.roll_all()
    generate_pdf(output_file_name, new_character)


def create_specified_character(output_file_name, stdscr):
    stdscr.clear()
    stdscr.addstr('')
    stdscr.refresh()
    stdscr.getch()


def interface(stdscr):
    create_specified_character('', stdscr)
