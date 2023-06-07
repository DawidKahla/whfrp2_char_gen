from character import Character
from imagefiller import fill_character_card_front

npc = Character()
npc.roll_all()
npc.print_character()
fill_character_card_front("baseform-1.png", "output1.png", npc)
