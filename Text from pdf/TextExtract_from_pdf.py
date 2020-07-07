# extract text from pdffile
# by @Gokulmishra

import PyPDF2

pdfFile=open('SturmLivouliee.pdf','rb')

#input your pdf file name instead of SturmLivouliee like 'name.pdf' format ...
# ... in thded same folder where the code is saved 

pdfReader= PyPDF2.PdfFileReader(pdfFile)
print(pdfReader.numPages)
pgObj=pdfReader.getPage(0)

#to get different page change index number of getPage

print(pgObj.extractText())
pdfFile.close()
