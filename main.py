"""
Main Program

This program generates a character for the Warhammer Fantasy Roleplay (WHFRP).
It generates a character sheet in PDF format.

Usage:
    python main.py
    or /main.dist/main.exe

Arguments:
    None

Output:
    The program generates a PDF file named "output.pdf"
        with the character sheet.
    Also generates PNG files which it was composed from
        ("output1.png", "output2.png").

Note:
    to create with nuitka:
    python -m nuitka --standalone --include-data-dir=imgs=imgs
        --include-data-dir=fonts=fonts main.py

Author:
    Dawid Kahla
"""
from interface import interface


def main():
    """
    Opens UI.
    """
    interface()


if __name__ == "__main__":
    main()
