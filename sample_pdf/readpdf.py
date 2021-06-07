import fitz
from PIL import Image
import PyPDF2 as pypdf
from pdf2image import convert_from_path


# doesn't work
def pymupdf():
    # doc = fitz.open("./River_Flows_In_You.pdf")
    doc = fitz.open("./不是因為天氣晴朗才愛你.pdf")

    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:
                print("RGB")
                img1 = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                img1.show()
            else:
                print("cmyk")
                
            pix = None


# doesn't work
def pypdf2():
    # doc = pypdf.PdfFileReader(open("./River_Flows_In_You.pdf", 'rb'))
    doc = pypdf.PdfFileReader(open("./不是因為天氣晴朗才愛你.pdf", 'rb'))
    page0 = doc.getPage(0)
    xObject = page0['/Resources']['/XObject'].getObject()
    print(xObject)

    for obj in xObject:
        if xObject[obj]['/Subtype'] == '/Image':
            size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            data = xObject[obj].getData()
            if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                mode = "RGB"
            else:
                mode = "P"

            if xObject[obj]['/Filter'] == '/FlateDecode':
                img = Image.frombytes(mode, size, data)
                print("FLATE")
                print(obj[1:])
                img.show()
                # img.save(obj[1:] + ".png")
            elif xObject[obj]['/Filter'] == '/DCTDecode':
                # img = open(obj[1:] + ".jpg", "wb")
                img = Image.fromBytes(mode, size, data)
                # img.write(data)
                print("DCT")
                print(obj[1:])
                img.show()
                # img.close()
            elif xObject[obj]['/Filter'] == '/JPXDecode':
                # img = open(obj[1:] + ".jp2", "wb")
                # img.write(data)
                # img.close()
                print("JPX")
                img = Image.frombytes(mode, size, data)
                print(obj[1:])
                img.show()

def pdf2image():
    pages = convert_from_path('./River_Flows_In_You.pdf', 500)
    # pages[0].show()
    print(type(pages[0]))
    img = Image.open('../1.png')
    print(type(img))

if __name__ == "__main__":
    # pymupdf()
    # pypdf2()
    pdf2image()
