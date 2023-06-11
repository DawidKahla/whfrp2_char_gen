from character import Character
from imagefiller import fill_character_card_front, fill_character_card_back

npc = Character()
npc.roll_all()
fill_character_card_front("baseform-1.png", "output1.png", npc)
fill_character_card_back("baseform-2.png", "output2.png", npc)
