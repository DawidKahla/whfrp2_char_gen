from character import Character
import imagefiller

if __name__ == "__main__":
    npc = Character()
    npc.roll_all()
    npc.print_character()
    imagefiller.generate_pdf("output.pdf", npc)
