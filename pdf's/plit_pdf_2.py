from PyPDF2 import PdfFileWriter, PdfFileReader
import glob
import sys
 
pdfs = glob.glob("*.pdf")

for pdf in pdfs:
 
    inputpdf = PdfFileReader(open(pdf, "rb"))

    if inputpdf.isEncrypted:
        inputpdf.decrypt('')
        
    for i in range(inputpdf.numPages // 2):
            
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i * 2))
    
        if i * 2 + 1 <  inputpdf.numPages:
            output.addPage(inputpdf.getPage(i * 2 + 1))
    
        newname = pdf[:7] + "-" + str(i) + ".pdf"
    
        outputStream = open(newname, "wb")
        output.write(outputStream)
        outputStream.close()
