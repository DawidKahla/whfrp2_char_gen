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
        print(field)
    fields["Rasa"] = race_translate(char.race)
    fields["Obecna profesja"] = char.profession
    fields["Wiek"] = char.age
    fields["Kolor oczu"] = char.eye
    fields["Waga"] = char.weight
    fields["Wzrost"] = char.height
    fields["Znak gwiezdny"] = char.star
    fields["Znaki szczególne"] = char.special
    return fields
