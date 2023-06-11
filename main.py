"""
Main Program

This program generates a character for the Warhammer Fantasy Roleplay (WHFRP).
It generates a character sheet in PDF format.

Usage:
    python main.py

Arguments:
    None

Output:
    The program generates a PDF file named "output.pdf" with the character sheet.
    Also generates PNG files which it was composed from ("output1.png", "output2.png").

Note:
    Make sure to have the necessary dependencies installed, such as Python 3.
    Required packages in file: "requirements.txt".

Author:
    Dawid Kahla
"""
from character import Character
import imagefiller

if __name__ == "__main__":
    npc = Character()
    npc.roll_all()
    npc.print_character()
    imagefiller.generate_pdf("output.pdf", npc)
