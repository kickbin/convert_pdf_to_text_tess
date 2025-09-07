# sudo apt install tesseract-ocr fonts-noto-cjk fonts-noto-cjk-extra fonts-wqy-zenhei tesseract-ocr-chi-sim -y
# sudo fc-cache -f -v
# export TESSDATA_PREFIX="/usr/share/tesseract-ocr/5/tessdata"
# download chi_sim.traineddata and place into /usr/share/tesseract-ocr/5/tessdata
# chmod 644 to /usr/share/tesseract-ocr/5/tessdata/chi_sim.traineddata
# pip install python-poppler pytesseract PyMuPDF 
import pytesseract
from PIL import Image
import fitz
import os

pdf_path = 'target.pdf'
pdf_doc = fitz.open(pdf_path)

# set png save dir
os.chdir('/usr/username/Downloads/pngs')
extracted_pages = []
for pn in range(len(pdf_doc)):
    page = pdf_doc.load_page(pn)
    png = page.get_pixmap()
    # save png with a filename
    filename = f'pg_{pn}.png'
    png.save(filename)
    img = Image.open(filename)
    extracted_text = pytesseract.image_to_string(img, lang='chi_sim')
    extracted_pages.append(extracted_text)
