import random as rand

def d10():
    return rand.randint(1,10)

def d100():
    return rand.randint(1,100)

def r20_2d10():
    return 20 + d10() + d10() 

def roll_random_ability(race, roll):
    if race == 'halfling':
        match roll:
            case 1 | 2 | 3 | 4:
                return 'Bardzo silny'
            case 5 | 6 | 7 | 8 | 9:
                return 'Bardzo szybki' 
            case 10 | 11 | 12 | 13:
                return 'Błyskotliwość'
            case 14 | 15 | 16 | 17 | 18:
                return 'Bystry wzrok'
            case 19 | 20 | 21 | 22 | 23:
                return 'Charyzmatyczny'
            case 24 | 25 | 26 | 27 | 28:
                return 'Czuły słuch'
            case 29 | 30 | 31 | 32 | 33 | 34:
                return 'Geniusz arytmetyczny'
            case 35 | 36 | 37 | 38 | 39:
                return 'Krzepki'
            case 40 | 41 | 42 | 43 | 44:
                return 'Naśladowca'
            case 45 | 46 | 47 | 48 | 49:
                return 'Niezwykle odporny'
            case 50 | 51 | 52 | 53:
                return 'Oburęczność'
            case 54 | 55 | 56 | 57 | 58:
                return 'Odporność na choroby'
            case 59 | 60 | 61 | 62:
                return 'Odporność na magię'
            case 63 | 64:
                return 'Odporność na trucizny'
            case 65 | 66 | 67 | 68:
                return 'Odporność psychiczna'
            case 69 | 70 | 71 | 72 | 73:
                return 'Opanowanie'
            case 74 | 75 | 76 | 77 | 78:
                return 'Strzelec wyborowy'
            case 79 | 80 | 81 | 82:
                return 'Szczęście'
            case 83 | 84 | 85 | 86 | 87:
                return 'Szósty zmysł'
            case 88 | 89 | 90 | 91 | 92:
                return 'Szybki refleks'
            case 93 | 94 | 95 | 96:
                return 'Twardziel'
            case 97 | 98 | 99 | 100:
                return 'Urodzony wojownik'
    else:
        match roll:
            case 1 | 2 | 3 | 4:
                return 'Bardzo silny'
            case 5 | 6 | 7 | 8 | 9:
                return 'Błyskotliwość'
            case 10 | 11 | 12 | 13:
                return 'Błyskotliwość'
            case 14 | 15 | 16 | 17 | 18:
                return 'Bystry wzrok'
            case 19 | 20 | 21 | 22:
                return 'Charyzmatyczny'
            case 23 | 24 | 25 | 26 | 27:
                return 'Czuły słuch'
            case 28 | 29 | 30 | 31:
                return 'Geniusz arytmetyczny'
            case 32 | 33 | 34 | 35:
                return 'Krzepki'
            case 36 | 37 | 38 | 39 | 40:
                return 'Naśladowca'
            case 41 | 42 | 43 | 44:
                return 'Niezwykle odporny'
            case 45 | 46 | 47 | 48 | 49:
                return 'Oburęczność'
            case 50 | 51 | 52 | 53:
                return 'Odporność na choroby'
            case 54 | 55 | 56 | 57:
                return 'Odporność na magię'
            case 58 | 59 | 60 | 61:
                return 'Odporność na trucizny'
            case 62 | 63 | 64 | 65 | 66:
                return 'Odporność psychiczna'
            case 67 | 68 | 69 | 70 | 71:
                return 'Opanowanie'
            case 72 | 73 | 74 | 75:
                return 'Strzelec wyborowy'
            case 76 | 77 | 78 | 79:
                return 'Szczęście'
            case 80 | 81 | 82 | 83:
                return 'Szósty zmysł'
            case 84 | 85 | 86 | 87:
                return 'Szybki refleks'
            case 88 | 89 | 90 | 91:
                return 'Twardziel'
            case 92 | 93 | 94 | 95:
                return 'Urodzony wojownik'
            case 96 | 97 | 98 | 99 | 100:
                return 'Widzenie w ciemności'

def execute_ability_modifiers(ability_set, main_atribute_dict, secondary_atribute_dict):
    if 'Bardzo silny' in ability_set:
        main_atribute_dict['K'] += 5
    if 'Błyskotliwość' in ability_set:
        main_atribute_dict['Int'] += 5
    if 'Charyzmatyczny' in ability_set:
        main_atribute_dict['Ogd'] += 5
    if 'Niezwykle odporny' in ability_set:
        main_atribute_dict['Odp'] += 5
    if 'Opanowanie' in ability_set:
        main_atribute_dict['SW'] += 5
    if 'Strzelec wyborowy' in ability_set:
        main_atribute_dict['US'] += 5
    if 'Szybki refleks' in ability_set:
        main_atribute_dict['Zr'] += 5
    if 'Urodzony wojownik' in ability_set:
        main_atribute_dict['WW'] += 5
    if 'Bardzo szybki' in ability_set:
        secondary_atribute_dict['Sz'] += 1
    if 'Twardziel' in  ability_set:
        secondary_atribute_dict['Żyw'] += 1

def roll_random_profession(race, roll):
    profession = 'None'
    if race == 'human':
        match roll:
            case 1 | 2:
                profession = 'Akolita'
            case 3 | 4:
                profession = 'Banita'
            case 5:
                profession = 'Berserker z Norski'
            # ...
    return profession

def random_race(roll):
    if roll == 1:
        return 'elf'
    elif roll < 6:
        return 'dwarf'
    elif roll < 11:
        return 'halfling'
    else:
        return 'human'

def race_translate(race):
    if race == 'human':
        return 'człowiek'
    elif race == 'halfling':
        return 'niziołek'
    elif race == 'dwarf':
        return 'krasnolud'
    elif race == 'elf':
        return race
    else:
        return 'Wyjątek: Problem z rasą'

race = random_race(d100())
race.lower()
if race != 'elf' and race != 'dwarf' and race != 'human' and race != 'halfling':
    print('Wyjątek: nie podano właściwej rasy!')
    exit()

main_atribute_list = ['WW', 'US', 'K', 'Odp', 'Zr', 'Int', 'SW', 'Ogd']
main_atribute_dict = {}
secondary_atribute_dict = {}
skill_list = []
ability_set = set()

# czy to można zapisać list comperhense?
for atribute in main_atribute_list:
    main_atribute_dict[atribute] = r20_2d10()

secondary_atribute_dict['A'] = 1
Zyw_roll = d10()
if Zyw_roll < 4:
    secondary_atribute_dict['Żyw'] = 10
elif Zyw_roll < 7:
    secondary_atribute_dict['Żyw'] = 11
elif Zyw_roll < 10:
    secondary_atribute_dict['Żyw'] = 12
else:
    secondary_atribute_dict['Żyw'] = 13
secondary_atribute_dict['Sz'] = 4
secondary_atribute_dict['Mag'] = 0
secondary_atribute_dict['PO'] = 0
PP_roll = d10()
if PP_roll < 5:
    secondary_atribute_dict['PP'] = 2
else:
    secondary_atribute_dict['PP'] = 3

match race:
    case 'human':
        skill_list.extend(['Plotkowanie', 'Wiedza(Imperium)', 'Znajomość języka(staroświatowy)'])
        while len(ability_set) < 2:
            ability_set.update({roll_random_ability(race,d100())})

    case 'halfling':
        skill_list.extend(['Plotkowanie', 'Wiedza (niziołki))', 'Znajomość języka (staroświatowy)', 'Znajomość języka( niziołków)', 'Nauka (genealogia/heraldyka)'])
        if d10() < 6:
            skill_list.append('Rzemiosło (gotowanie)')
        else:
            skill_list.append('Rzemiosło (uprawa ziemi)')
        ability_set.update({'Broń specjalna (proca)'}, {'Odporność na Chaos'}, {'Widzenie w ciemności'}, {roll_random_ability(race,d100())})
        main_atribute_dict['WW'] -= 10
        main_atribute_dict['US'] += 10
        main_atribute_dict['K'] -= 10
        main_atribute_dict['Odp'] -=10
        main_atribute_dict['Zr'] += 10
        main_atribute_dict['Ogd'] += 10 
        secondary_atribute_dict['Żyw'] -= 2
        if PP_roll < 8:
            secondary_atribute_dict['PP'] = 2

    case 'elf':
        skill_list.extend(['Wiedza (elfy)', 'Znajomość języka (eltharin)', 'Znajomość języka(staroświatowy)'])
        ability_set.update({'Bystry wzrok'}, {'Widzenie w ciemności'})
        if d10() < 6:
            ability_set.update({'Broń specjalna (długi łuk)'})
        else:
            ability_set.update({'Zmysł magii'})
        if d10() < 6:
            ability_set.update({'Opanowanie'})
        else:
            ability_set.update({'Błyskotliwość'})
        main_atribute_dict['US'] += 10
        main_atribute_dict['Zr'] += 10
        secondary_atribute_dict['Żyw'] -= 1
        secondary_atribute_dict['Sz'] = 5
        secondary_atribute_dict['PP'] -= 1

    case 'dwarf':
        skill_list.extend(['Wiedza (krasnoludy)', 'Znajomość języka (khazalid)', 'Znajomość języka (staroświatowy)'])
        a = rand.randint(1,3)
        if a == 1:
            skill_list.append('Rzemiosło (górnictwo)')
        elif a == 2:
            skill_list.append('Rzemiosło (kamieniarstwo)')
        else:
            skill_list.append('Rzemiosło (kowalstwo)')
        ability_set.update({'Krasnoludzki fach'}, {'Krzepki'}, {'Odporność na magię'}, {'Odwaga'}, {'Widzenie w ciemności'}, {'Zapiekła nienawiść'})
        main_atribute_dict['WW'] += 10
        main_atribute_dict['Odp'] +=10
        main_atribute_dict['Zr'] -= 10
        main_atribute_dict['Ogd'] -= 10 
        secondary_atribute_dict['Żyw'] += 2
        secondary_atribute_dict['Sz'] = 3
        if PP_roll < 8:
            secondary_atribute_dict['PP'] -= 1

execute_ability_modifiers(ability_set,main_atribute_dict,secondary_atribute_dict)  
secondary_atribute_dict['S'] = main_atribute_dict['K']//10
secondary_atribute_dict['Wt'] = main_atribute_dict['Odp']//10

print(f"Rasa: {race_translate(race)}")
print(main_atribute_dict)
print(secondary_atribute_dict)
print(skill_list)
print(ability_set)
