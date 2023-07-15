"""
This module provides character creating functions and interface.

"""
import os
from character import Character
from imagefiller import generate_pdf
from translations import race_translate, sex_translate
from professions import professions
from myrandom import d10


def clear_screen():
    """
    Clears the console screen.

    Returns:
        None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def wait_for_input():
    """
    Waits for user input to continue.

    Returns:
        None
    """
    input("Naciśnij Enter, aby kontynuować...")


def specify_file_path():
    """
    Prompts the user to specify the file path for the character card.

    Returns:
        str: File path for the character card.
    """
    print("Podaj nazwę docelowego pliku karty postaci.")
    print("Zostanie on utworzony w podkatalogu imgs.")
    print("W przypadku powielenia nazwy plik zostanie nadpisany.")
    print("Ewentualnie napisywany plik nie może być otwarty.")
    user_input = input("Nazwa pliku: ")
    return f"imgs\\{user_input}"


def progress_bar(progress):
    """
    Displays a progress bar based on the given progress value.

    Args:
        progress (float): Progress value between 0 and 1.

    Returns:
        None
    """
    bar_length = 20
    filled_length = int(round(bar_length * progress))
    bar_pro = '=' * filled_length + '-' * (bar_length - filled_length)
    percentage = round(progress * 100, 2)
    print(f'[{bar_pro}] {percentage}%')


def input_number(message):
    """
    Prompts the user to input a number.

    Args:
        message (str): Prompt message.

    Returns:
        int: User input as an integer.
    """
    while True:
        user_input = input(message)
        clear_screen()
        if user_input == 'losowe':
            return user_input
        try:
            int(user_input)
        except ValueError:
            print(f"Nieprawidłowa wartość ({user_input}), "
                  f"podaj liczbę całkowitą.")
            continue
        if int(user_input) < 1:
            print(f"Nieprawidłowa wartość ({user_input}), "
                  f"podaj liczbę dodatnią.")
            continue
        else:
            return int(user_input)


def create_random_character(output_file_name):
    """
    Generates a random character and creates a PDF character card.

    Args:
        output_file_name (str): File name for the generated character card.

    Returns:
        None
    """
    new_character = Character()
    new_character.roll_all()
    generate_pdf(output_file_name, new_character)


def create_multiple_random_characters():
    """
    Generates multiple random characters and creates PDF character cards.

    Returns:
        None
    """
    clear_screen()
    print('Wybrano opcję automatycznej generacji kart postaci.')
    output_file_path = specify_file_path()
    clear_screen()
    cards = input_number('Podaj liczbę kart do wygenerowania: ')
    if cards == 'losowe':
        cards = d10()
    if cards > 1000:
        print('Podano zbyt dużą liczbę kart do generacji.')
        print('Maksymalna liczba generowanych kart: 1000.')
        print('Zredukowano liczbę generowanych kart do 10.')
        wait_for_input()
        cards = 10
    for idx in range(cards):
        clear_screen()
        print(f'Generuje karty postaci ({cards})...')
        progress_bar(idx/int(cards))
        create_random_character(f'{output_file_path}_{idx+1}.pdf')
    clear_screen()
    print(f'Wygenerowano karty postaci ({cards}).')
    print(f'Są zapisane w postaci: {output_file_path}_numer.pdf.')
    wait_for_input()


def create_specified_character():
    """
    Allows the user to specify character attributes manually
    and generate a character card.

    Returns:
        None
    """
    clear_screen()
    print('Wybrano opcję własnoręcznej specyfikacji części atrybutów.')
    wait_for_input()
    clear_screen()
    output_file_path = specify_file_path()
    # char_info: 0 - race, 1 - profession, 2 - sex,
    # 3 - name, 4 - height, 5 - weight, 6 - hair,
    # 7 - eye, 8 - special, 9 - siblings, 10 - star,
    # 11 - age, 12 - birthplace
    char_info = [None for _ in range(13)]

    while char_info[0] not in [
        'Człowiek', 'Elf', 'Niziołek', 'Krasnolud', 'Losowe'
    ]:
        clear_screen()
        char_info[0] = input('Podaj rasę (człowiek, elf,'
                             ' niziołek, krasnolud, losowe): \n')
        char_info[0] = char_info[0].capitalize()

    while char_info[1] not in professions and char_info[1] not in ['losowe']:
        clear_screen()
        char_info[1] = input('Podaj profesję (jedna z predefiniowanych'
                             ' lub losowe): \n')
        if char_info[1] != 'losowe':
            char_info[1] = char_info[1].upper()

    while char_info[2] not in ['Kobieta', 'Mężczyzna', 'Losowe']:
        clear_screen()
        char_info[2] = input('Podaj płeć (kobieta, mężczyzna, losowe): \n')
        char_info[2] = char_info[2].capitalize()

    clear_screen()
    char_info[3] = input('Podaj imię postaci (dowolne lub losowe): \n')
    clear_screen()
    char_info[4] = input_number('Podaj wzrost postaci w cm'
                                ' (liczba lub losowe): \n')
    clear_screen()
    char_info[5] = input_number('Podaj masę postaci w kg'
                                ' (liczba lub losowe): \n')
    clear_screen()
    char_info[6] = input('Podaj kolor włosów (dowolne lub losowe): \n')
    clear_screen()
    char_info[7] = input('Podaj kolor oczu (dowolne lub losowe): \n')
    clear_screen()
    char_info[8] = input('Podaj znaki szczególne (dowolne lub losowe): \n')
    clear_screen()
    char_info[9] = input_number('Podaj liczbę rodzeństwa'
                                ' (liczba lub losowe): \n')
    clear_screen()
    char_info[10] = input('Podaj znak gwiezdny (dowolne lub losowe): \n')
    clear_screen()
    char_info[11] = input_number('Podaj wiek w latach (liczba lub losowe): \n')
    clear_screen()
    char_info[12] = input('Podaj miejsce urodzenia (dowolne lub losowe): \n')
    for idx in [4, 5, 9, 11]:
        if char_info[idx] != 'losowe':
            if char_info[idx] > 1000000:
                char_info[idx] = '>1000000'
    for idx in [6, 7]:
        if len(char_info[idx]) > 15:
            char_info[idx] = f"{char_info[idx][:12]}..."
    for idx in [10]:
        if len(char_info[idx]) > 18:
            char_info[idx] = f"{char_info[idx][:16]}..."
    for idx in [3, 8, 12]:
        if len(char_info[idx]) > 33:
            char_info[idx] = f"{char_info[idx][:33]}..."
    att_names = ['Rasa', 'Profesja', 'Płeć', 'Imię', 'Wzrost',
                 'Waga', 'Włosy', 'Oczy', 'Znaki szczególne',
                 'Rodzeństwo', 'Znak gwiezdny', 'Wiek', 'Miejsce urodzenia']
    clear_screen()
    for idx, value in enumerate(char_info):
        print(f"{att_names[idx]}: {value}")
    proceed = None
    while proceed not in ['tak', 'nie']:
        proceed = input('Czy zatwierdzasz powyższe dane? (tak/nie): ')

    if proceed == 'nie':
        clear_screen()
        print('Zrezygnowano z generacji kart postaci na podstawie '
              'wprowadzonych danych.')
        wait_for_input()
        return

    if char_info[2] != 'Losowe':
        char_info[2] = sex_translate(char_info[2])
    if char_info[0] != 'Losowe':
        char_info[0] = race_translate(char_info[0])
    for idx, value in enumerate(char_info):
        if value == 'losowe' or value == 'Losowe':
            char_info[idx] = None

    new_character = Character()
    new_character.roll_all(*char_info)
    print("Rozpoczynam generację karty postaci.")
    generate_pdf(f"{output_file_path}.pdf", new_character)
    clear_screen()
    print(f"Wygenerowana karta postaci jest zapisana w {output_file_path}.pdf")
    wait_for_input()


def interface():
    """
    Main interface for the character card generator.

    Allows the user to choose between generating
    a specified number of random character cards,
    creating a character card with manually specified
    attributes, or exiting the application.

    Returns:
        None
    """
    clear_screen()
    print('Witaj w generatorze kart postaci do Warhammer Fantasy Roleplay 2!')
    wait_for_input()
    user_input = None
    while True:
        while user_input not in ['1', '2', '3']:
            clear_screen()
            print('Możesz wygenerować określoną liczbę losowych '
                  'kart postaci (1),')
            print('samodzielnie wprowadzić wybrane elementy pojedynczej '
                  'kart i resztę wylosować (2).')
            print('lub zakończyć działanie aplikacji (3).')
            user_input = input('Wybierz opcję (1, 2 lub 3): ')
        if user_input == '1':
            create_multiple_random_characters()
        if user_input == '2':
            create_specified_character()
        if user_input == '3':
            return
        user_input = None
