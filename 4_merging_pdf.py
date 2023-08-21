from PyPDF2 import PdfReader,PdfWriter
path = ['Lab Plan 7.pdf','rotated_PDF.pdf']

# create writer object
writer = PdfWriter()

for i in path:
    # create pdf object
    pdf = PdfReader(i,'rb')
    for pg in range(0,len(pdf.pages)):
        writer.add_page(pdf.pages[pg])

with open('Merged_PDF.pdf','wb') as out:
    writer.write(out)

print("Pdf merge susscifully ")