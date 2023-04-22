import PyPDF2


def get_form_fields(file_name):
    pdf_reader = PyPDF2.PdfReader(open(file_name, "rb"))
    if not pdf_reader.get_fields():
        raise Exception("Plik PDF nie zawiera formularza")
    else:
        return pdf_reader.get_fields()


def form_generate(input_file_name, output_file_name, fields):
    pdf_reader = PyPDF2.PdfReader(open(input_file_name, "rb"))
    pdf_writer = PyPDF2.PdfWriter()
    if not pdf_reader.get_fields():
        raise Exception("Plik PDF nie zawiera formularza")

    for page in range(pdf_reader.numPages):
        pdf_writer.add_page(pdf_reader.pages[page])
        pdf_writer.update_page_form_field_values(pdf_writer.pages[page], fields)

    # Zapisz zmieniony plik PDF
    output_file = open(output_file_name, "wb")
    pdf_writer.write(output_file)
    output_file.close()
