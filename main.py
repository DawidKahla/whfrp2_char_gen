import random as rand

def d10():
    return rand.randint(1,10)

def d100():
    return rand.randint(1,100)

def r20_2d10():
    return 20 + d10() + d10() 

def roll_random_ability(race, roll):
    common_mapping = {
        (1,4): 'Bardzo silny',
        (5,9): 'Bardzo szybki',
        (10,13): 'Błyskotliwość',
        (14,18): 'Bystry wzrok',
    }
    halfling_mapping = common_mapping | {
        (19,23): 'Charyzmatyczny',
        (24,28): 'Czuły słuch',
        (29,34): 'Geniusz arytmetyczny',
        (35,39): 'Krzepki',
        (40,44): 'Naśladowca',
        (45,49): 'Niezwykle odporny',
        (50,53): 'Oburęczność',
        (54,58): 'Odporność na choroby',
        (59,62): 'Odporność na magię',
        (63,64): 'Odporność na trucizny',
        (65,68): 'Odporność psychiczna',
        (69,73): 'Opanowanie',
        (74,78): 'Strzelec wyborowy',
        (79,82): 'Szczęście',
        (83,87): 'Szósty zmysł',
        (88,92): 'Szybki refleks',
        (93,96): 'Twardziel',
        (97,100): 'Urodzony wojownik'
    }
    human_mapping = common_mapping | {
        (19,22): 'Charyzmatyczny',
        (23,27): 'Czuły słuch',
        (28,31): 'Geniusz arytmetyczny',
        (32,35): 'Krzepki',
        (36,40): 'Naśladowca',
        (41,44): 'Niezwykle odporny',
        (45,49): 'Oburęczność',
        (50,53): 'Odporność na choroby',
        (54,57): 'Odporność na magię',
        (58,61): 'Odporność na trucizny',
        (62,66): 'Odporność psychiczna',
        (67,71): 'Opanowanie',
        (72,75): 'Strzelec wyborowy',
        (76,79): 'Szczęście',
        (80,83): 'Szósty zmysł',
        (84,87): 'Szybki refleks',
        (88,91): 'Twardziel',
        (92,95): 'Urodzony wojownik',
        (96,100): 'Widzenie w ciemności'
    }
    if race == 'halfling':
        keys = halfling_mapping.keys()
    elif race == 'human':
        keys = human_mapping.keys()
    else:
        raise Exception("Wrong race in roll_random_ability")

    for key in keys:
        minimum, maximum = key
        if roll >= minimum and roll <= maximum:
            if race == 'halfling':
                return halfling_mapping[key]
            else:
                return human_mapping[key]

def execute_ability_modifiers(ability_set, main_attribute_dict, secondary_attribute_dict):
    if 'Bardzo silny' in ability_set:
        main_attribute_dict['K'] += 5
    if 'Błyskotliwość' in ability_set:
        main_attribute_dict['Int'] += 5
    if 'Charyzmatyczny' in ability_set:
        main_attribute_dict['Ogd'] += 5
    if 'Niezwykle odporny' in ability_set:
        main_attribute_dict['Odp'] += 5
    if 'Opanowanie' in ability_set:
        main_attribute_dict['SW'] += 5
    if 'Strzelec wyborowy' in ability_set:
        main_attribute_dict['US'] += 5
    if 'Szybki refleks' in ability_set:
        main_attribute_dict['Zr'] += 5
    if 'Urodzony wojownik' in ability_set:
        main_attribute_dict['WW'] += 5
    if 'Bardzo szybki' in ability_set:
        secondary_attribute_dict['Sz'] += 1
    if 'Twardziel' in  ability_set:
        secondary_attribute_dict['Żyw'] += 1

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
race = race.lower()
if race != 'elf' and race != 'dwarf' and race != 'human' and race != 'halfling':
    print('Wyjątek: nie podano właściwej rasy!')
    exit()

main_attribute_list = ['WW', 'US', 'K', 'Odp', 'Zr', 'Int', 'SW', 'Ogd']
main_attribute_dict = {}
secondary_attribute_dict = {}
skill_list = []
ability_set = set()

main_attribute_dict = {attr: r20_2d10() for attr in main_attribute_list}

secondary_attribute_dict['A'] = 1
zyw_roll = d10()
if zyw_roll < 4:
    secondary_attribute_dict['Żyw'] = 10
elif zyw_roll < 7:
    secondary_attribute_dict['Żyw'] = 11
elif zyw_roll < 10:
    secondary_attribute_dict['Żyw'] = 12
else:
    secondary_attribute_dict['Żyw'] = 13
secondary_attribute_dict['Sz'] = 4
secondary_attribute_dict['Mag'] = 0
secondary_attribute_dict['PO'] = 0
pp_roll = d10()
if pp_roll < 5:
    secondary_attribute_dict['PP'] = 2
else:
    secondary_attribute_dict['PP'] = 3

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
        main_attribute_dict['WW'] -= 10
        main_attribute_dict['US'] += 10
        main_attribute_dict['K'] -= 10
        main_attribute_dict['Odp'] -=10
        main_attribute_dict['Zr'] += 10
        main_attribute_dict['Ogd'] += 10 
        secondary_attribute_dict['Żyw'] -= 2
        if pp_roll < 8:
            secondary_attribute_dict['PP'] = 2

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
        main_attribute_dict['US'] += 10
        main_attribute_dict['Zr'] += 10
        secondary_attribute_dict['Żyw'] -= 1
        secondary_attribute_dict['Sz'] = 5
        secondary_attribute_dict['PP'] -= 1

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
        main_attribute_dict['WW'] += 10
        main_attribute_dict['Odp'] +=10
        main_attribute_dict['Zr'] -= 10
        main_attribute_dict['Ogd'] -= 10 
        secondary_attribute_dict['Żyw'] += 2
        secondary_attribute_dict['Sz'] = 3
        if pp_roll < 8:
            secondary_attribute_dict['PP'] -= 1

execute_ability_modifiers(ability_set,main_attribute_dict,secondary_attribute_dict)  
secondary_attribute_dict['S'] = main_attribute_dict['K']//10
secondary_attribute_dict['Wt'] = main_attribute_dict['Odp']//10

print(f"Rasa: {race_translate(race)}")
print(main_attribute_dict)
print(secondary_attribute_dict)
print(skill_list)
print(ability_set)
