"""
This module provides functions for working with PDF files using the PyPDF4 library.
"""
import PyPDF4
from character import race_translate


def get_form_fields(file_name) -> dict:
    """
    Returns a dictionary of form field names and their properties.

    :param file_name: The name of the PDF file to extract form fields from.
    :type file_name: str
    :return: A dictionary containing the form fields and their properties.
    :rtype: dict
    :raises ValueError: If the PDF file does not contain any form fields.
    """
    pdf_reader = PyPDF4.PdfFileReader(open(file_name, "rb"))
    if not pdf_reader.getFields():
        raise ValueError("The PDF does not contain the form")
    else:
        return pdf_reader.getFields()


def generate_character_card_pdf_file(input_file_name, output_file_name, fields) -> None:
    """
    Generates a PDF file with filled form fields based on a template file.

    :param input_file_name: The name of the input PDF file with a form.
    :type input_file_name: str
    :param output_file_name: The name of the output PDF file with the filled form fields.
    :type output_file_name: str
    :param fields: A dictionary with the names and values of the form fields to be filled.
    :type fields: dict
    :raises ValueError: If the input PDF file does not contain a form template.
    :return: None
    """
    pdf_reader = PyPDF4.PdfFileReader(open(input_file_name, "rb"))
    pdf_writer = PyPDF4.PdfFileWriter()
    if not pdf_reader.getFields():
        raise ValueError("The PDF does not contain the form")
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
        pdf_writer.updatePageFormFieldValues(pdf_writer.getPage(page), fields)

    with open(output_file_name, "wb") as output_file:
        pdf_writer.write(output_file)


def parse_fields(char, fields) -> dict:
    """
    Parse form fields based on the character's information.

    :param char: Character to update the form fields for.
    :type char: Character
    :param fields: Form fields to update.
    :type fields: dict
    :return: The updated dictionary with the form fields.
    :rtype: dict
    """
    for field in fields:
        fields[field] = ""
    fields["Text1"] = char.name
    fields["Text2"] = race_translate(char.race)
    fields["Text3"] = char.profession.capitalize()
    fields["Text5"] = char.age
    fields["Text6"] = char.eye
    fields["Text7"] = char.hair
    fields["Text8"] = char.star
    fields["Text9"] = char.birthplace
    fields["Text10"] = char.special
    fields["Text11"] = char.sex
    fields["Text12"] = char.weight
    fields["Text13"] = char.height
    fields["Text14"] = char.siblings
    temp_iter = 0
    for attribute in char.attributes_main:
        fields[f"Text{19+temp_iter}"] = char.attributes_main[attribute].initial
        if char.attributes_main[attribute].potential != 0:
            fields[
                f"Text{38+temp_iter}"
            ] = f"+{char.attributes_main[attribute].potential}"
        temp_iter += 1
        if attribute == "Int":
            break
    fields["Text25"] = char.attributes_main["Ogd"].initial
    fields["Text26"] = char.attributes_main["SW"].initial
    if char.attributes_main["Ogd"].potential != 0:
        fields["Text45"] = f"+{char.attributes_main['Ogd'].potential}"
    if char.attributes_main["SW"].potential != 0:
        fields["Text46"] = f"+{char.attributes_main['SW'].potential}"
    temp_iter = 0
    for attribute in char.attributes_sec:
        fields[f"Text{55+temp_iter}"] = char.attributes_sec[attribute].initial
        if char.attributes_sec[attribute].potential != 0:
            fields[
                f"Text{63+temp_iter}"
            ] = f"+{char.attributes_sec[attribute].potential}"
        temp_iter += 1
    return fields
