from PyPDF2 import PdfMerger

def merge_pdfs(pdf1, pdf2, output_file):
    merger = PdfMerger()
    merger.append(pdf1)
    merger.append(pdf2)
    merger.write(output_file)
    merger.close()


pdf1 = "file1.pdf"
pdf2 = "file2.pdf"
output_file = "merged_file.pdf"

merge_pdfs(pdf1, pdf2, output_file)
print("PDFs merged successfully!")
