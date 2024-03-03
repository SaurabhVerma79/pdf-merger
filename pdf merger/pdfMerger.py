import PyPDF2
pdfMerge=PyPDF2.PdfMerger()
pdfiles=["1.pdf","2.pdf"]
for filename in pdfiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        pdfMerge.append(pdfReader)
pdfFile.close()
pdfMerge.write('merged.pdf')