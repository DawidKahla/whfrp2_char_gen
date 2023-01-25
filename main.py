import random as rand

def d10():
    return rand.randint(1,10)

def d100():
    return rand.randint(1,100)

def d1000():
    return rand.randint(1,1000)

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
    human_mapping = {
        (1,16): 'Akolita',
        (17,28): 'Aptekarz',
        (29,32): 'Bagiennik',
        (33,44): 'Bajarz',
        (45,48): 'Balsamista',
        (49,64): 'Banita',
        (65,68): 'Berserker z Norski',
        (69,80): 'Błędny rycerz',
        (81,88): 'Były więzień',
        (89,92): 'Cenobita',
        (93,104): 'Chłop',
        (105,112): 'Ciura obozowa',
        (113,128): 'Cyrkowiec',
        (129,140): 'Cyrulik',
        (141,144): 'Czekista',
        (145,148): 'Doker',
        (149,160): 'Dyletant',
        (161,164): 'Fanatyk',
        (165,180): 'Flisak',
        (181,184): 'Gazeciarz',
        (185,192): 'Giermek',
        (193,204): 'Gladiator',
        (205,212): 'Górnik',
        (213,220): 'Grabarz',
        (221,224): 'Grabieżca',
        (225,236): 'Guślarz',
        (237,244): 'Handlarz końmi',
        (245,256): 'Hiena cmentarna',
        (257,260): 'Kadet',
        (261,276): 'Kanciarz',
        (277,284): 'Kartograf',
        (285,288): 'Koczownik',
        (289,300): 'Kominiarz',
        (301,304): 'Korsarz',
        (305,312): 'Kozak kislevski',
        (313,320): 'Latarnik',
        (321,332): 'Leśnik',
        (333,344): 'Łowca',
        (345,356): 'Łowca nagród',
        (357,368): 'Mieszczanin',
        (369,372): 'Mytnik',
        (373,388): 'Najemnik',
        (389,392): 'Niewolnik',
        (393,404): 'Ochotnik',
        (405,420): 'Ochroniarz',
        (421,432): 'Oprych',
        (433,444): 'Pachołek',
        (445,448): 'Pasterz z Carcasonne',
        (449,456): 'Paź',
        (457,468): 'Pielgrzym',
        (469,476): 'Pielgrzym Graala',
        (477,480): 'Pirat rzeczny',
        (481,492): 'Podżegacz',
        (493,500): 'Poganiacz bydła',
        (501,508): 'Poganiacz mułów',
        (509,516): 'Pogranicznik',
        (517,520): 'Pokutnik',
        (521,528): 'Porywacz zwłok',
        (529,536): 'Poskramiacz niedźwiedzi',
        (537,544): 'Posłaniec',
        (545,548): 'Prawnik',
        (549,556): 'Przemytnik',
        (557,564): 'Przepatrywacz',
        (565,572): 'Przewoźnik',
        (573,576): 'Pustelnik',
        (577,580): 'Rogaty łowca',
        (581,592): 'Rolnik',
        (593,596): 'Rozjemca',
        (597,608): 'Rybak',
        (609,624): 'Rzemieślnik',
        (625,636): 'Rzezimieszek',
        (637,640): 'Skald',
        (641,652): 'Skarbnik',
        (653,664): 'Skryba',
        (665,672): 'Sługa',
        (673,684): 'Strażnik',
        (685,700): 'Strażnik dróg',
        (701,708): 'Strażnik kanałów',
        (709,716): 'Strażnik rzeczny',
        (717,720): 'Strażnik świątynny',
        (721,724): 'Strażnik tuneli',
        (725,732): 'Strażnik więzienny',
        (733,736): 'Streltsi',
        (737,740): 'Strzygański mistyk',
        (741,760): 'Szczurołap',
        (761,772): 'Szeptucha',
        (773,776): 'Szermierz estalijski',
        (777,792): 'Szlachcic',
        (793,796): 'Szperacz',
        (797,808): 'Szuler',
        (809,816): 'Śmieciarz',
        (817,824): 'Uczennica lodowej wiedźmy',
        (825,840): 'Uczeń czarodzieja',
        (841,848): 'Uczeń guślarza',
        (849,856): 'Węglarz',
        (857,864): 'Wielorybnik',
        (865,872): 'Włóczykij',
        (873,876): 'Woj',
        (877,888): 'Woźnica',
        (889,896): 'Wróżbita',
        (897,904): 'Zakapturzony',
        (905,916): 'Zarządca',
        (917,924): 'Zbieracz łajna',
        (925,940): 'Złodziej',
        (941,948): 'Żabiarka',
        (949,960): 'Żak',
        (961,972): 'Żeglarz',
        (973,984): 'Żołnierz',
        (985,1000): 'Żołnierz okrętowy'
    }

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
race = 'dwarf'
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
secondary_attribute_dict['S'] = 0
secondary_attribute_dict['Wt'] = 0
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
