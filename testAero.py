import fitz  # PyMuPDF
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode
#its better to install PyMuPDF package that fitz


#read text from pdf
def extract_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    extracted_text = ""

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        text = page.get_text()
        extracted_text += text
    pdf_document.close()

    return extracted_text

#read barcodes from pdf
def extract_barcodes_from_pdf(pdf_path):
    images = convert_from_path(pdf_path, 500, poppler_path=r'C:\Users\Public\poppler-0.68.0_x86\poppler-0.68.0\bin')
    barcode_data_list = []

    #i generate image and that read from image barcodes
    for image in images:
        image = image.convert('L')
        barcodes = decode(image)
        for barcode in barcodes:
            barcode_data_list.append(barcode.data.decode('utf-8'))

    return barcode_data_list

pdf_file_path = 'C:/Users/Public/Documents/test_task.pdf'
extracted_text = extract_text_from_pdf(pdf_file_path)
barcode_data_list = extract_barcodes_from_pdf(pdf_file_path)

print(barcode_data_list)
