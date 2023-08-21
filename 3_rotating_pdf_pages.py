
import PyPDF2 as p

with open('rotating.pdf','rb') as inputFile:
    # creating pdf reader and writer object
    pdf = p.PdfReader(inputFile)
    writer = p.PdfWriter()
    print("Rotating pages:")
    for i in range(0,len(pdf.pages)):
        page = pdf.pages[i]
        page.rotate(90)
        writer.add_page(page)
with open('rotated_PDF.pdf','wb') as outputFile:
    writer.write(outputFile)
    print("pages rotate successfully:")