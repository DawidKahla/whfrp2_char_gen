from character import Character
# def execute_ability_modifiers(ability_set, main_attribute_dict, secondary_attribute_dict):
#     if 'Bardzo silny' in ability_set:
#         main_attribute_dict['K'] += 5
#     if 'Błyskotliwość' in ability_set:
#         main_attribute_dict['Int'] += 5
#     if 'Charyzmatyczny' in ability_set:
#         main_attribute_dict['Ogd'] += 5
#     if 'Niezwykle odporny' in ability_set:
#         main_attribute_dict['Odp'] += 5
#     if 'Opanowanie' in ability_set:
#         main_attribute_dict['SW'] += 5
#     if 'Strzelec wyborowy' in ability_set:
#         main_attribute_dict['US'] += 5
#     if 'Szybki refleks' in ability_set:
#         main_attribute_dict['Zr'] += 5
#     if 'Urodzony wojownik' in ability_set:
#         main_attribute_dict['WW'] += 5
#     if 'Bardzo szybki' in ability_set:
#         secondary_attribute_dict['Sz'] += 1
#     if 'Twardziel' in  ability_set:
#         secondary_attribute_dict['Żyw'] += 1

# execute_ability_modifiers(ability_set,main_attribute_dict,secondary_attribute_dict)  
# secondary_attribute_dict['S'] = main_attribute_dict['K']//10
# secondary_attribute_dict['Wt'] = main_attribute_dict['Odp']//10

# print(f"Rasa: {race_translate(race)}")
# print(profession)
# print(main_attribute_dict)
# print(secondary_attribute_dict)
# print(skill_list)
# print(ability_set)
npc = Character()
npc.roll_race()
npc.roll_profession()
npc.roll_attributes()
npc.set_default_skills_and_abilities()
npc.update_attr_by_abilities()
npc.print_character()

