from PyPDF2 import PdfFileReader, PdfFileWriter

with open("example.pdf", 'rb') as infile:

    reader = PdfFileReader(infile)
    writer = PdfFileWriter()
    writer.addPage(reader.getPage(0))

    with open('output.pdf', 'wb') as outfile:
        writer.write(outfile)
