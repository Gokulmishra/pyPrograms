# extract text from pdffile
import PyPDF2
pdfFile=open('fourier.pdf','rb')
pdfReader= PyPDF2.PdfFileReader(pdfFile)
print(pdfReader.numPages)
pgObj=pdfReader.getPage(0)
print(pgObj.extractText())
pdfFile.close()