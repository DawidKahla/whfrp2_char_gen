from character import Character
import pdfform_client

npc = Character()
npc.roll_all()
# npc.print_character()
fields = pdfform_client.get_form_fields("baseform.pdf")
fields = pdfform_client.parse_fields(npc, fields)
pdfform_client.generate_character_card_pdf_file(
    "baseform.pdf", "outputfile.pdf", fields
)
