# import PyPDF2
# # we have specified rb, which means its read binary format
# # since the the pdf file is not the normal one
# f = open("Working_Business_Proposal.pdf", "rb")

# pdf_reader = PyPDF2.PdfFileReader(f)
# pdf_reader.numPages

for i in range(15):
    for j in range (i):
        print(j)
    print()