from PyPDF2 import PdfReader

with open('Lab Plan 7.pdf','rb') as f:
    # making object reader
    reader = PdfReader(f)
    # print(dir(reader))
    page = reader.pages[1]
    text = page.extract_text()
    print(text)