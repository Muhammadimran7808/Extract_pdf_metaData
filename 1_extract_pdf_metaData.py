from PyPDF2 import PdfReader

#  if pdf file in the same directory, just store the name of file in path variable. Otherwise give complete path
path = "Lab Plan 7.pdf"

# opning pdf file

with open(path,'rb') as f:

    # creating an object of PdfFileReader() class
    pdfObj = PdfReader(f)

    # creating A variabe to store information of pdf file
    information = pdfObj.metadata
    # print(information)
    for key,value in information.items():    #unpack the tuple
        print(key ," : ", value)

    number_of_pages = len(pdfObj.pages)
    print(number_of_pages)