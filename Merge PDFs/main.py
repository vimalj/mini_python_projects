from PyPDF2 import PdfMerger


def by_appending():
    merger = PdfMerger()
    f1 = open("testPDF1.pdf", "rb")
    merger.append(f1)
    merger.append("testPDF2.pdf")

    merger.write("mergedPDF.pdf")

def by_inserting():
    merger = PdfMerger()
    merger.append("testPDF2.pdf")
    merger.merge(0, "testPDF1.pdf")
    merger.write("mergedPDF.pdf")

    print("pdfs have been merged: please check folder")

if __name__ == "__main__":
    by_appending()
    by_inserting()
