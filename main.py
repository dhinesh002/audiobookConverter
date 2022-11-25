from PIL import Image
import pytesseract
import PyPDF3
import pyttsx3
import pdfplumber
from googletrans import Translator


translator = Translator()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

TESSDATA_PREFIX = "C:\Program Files\Tesseract-OCR\tessdata"


need = int(input('Pdf to Audiobook --> press 1 , image to Audiobook --> press 2 : '))


def pdf_to_audio():
    file = input('enter pdf file name (example:file.pdf) : ')
    audiobook_name = input('enter output file name (without extension) : ')
    book = open(file, 'rb')
    pdfreader = PyPDF3.PdfFileReader(book)
    pages = pdfreader.numPages
    finaltext = ""

    with pdfplumber.open(file) as pdf:
        for i in range(0, pages):
            page = pdf.pages[i]
            text = page.extract_text()
            finaltext += text

    translations = translator.translate(finaltext, dest='en')
    finaltexts = translations.text

    engine = pyttsx3.init()
    engine.save_to_file(finaltexts, f'{audiobook_name}.mp3')
    engine.runAndWait()

    print(f'{audiobook_name}.mp3 successfully created')


def img_to_audio(x):
    image_file = input('enter image file name (example:file.png or file.jpg) : ')
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image, lang=x)

    translations = translator.translate(text, dest='en')
    finalTexts = translations.text

    audiobook_name = input('enter output file name (without extension) : ')
    engine = pyttsx3.init()
    engine.save_to_file(finalTexts, f'{audiobook_name}.mp3')
    engine.runAndWait()

    print(f'{audiobook_name}.mp3 successfully created')


if need == 1:
    pdf_to_audio()


if need == 2:
    dic = {'tamil': 'tam', 'hindi': 'hin', 'english': 'eng', 'malayalam': 'mal', 'telugu': 'tel'}
    languages = ['tamil', 'hindi', 'telugu', 'malayalam', 'english']
    file_language = input('enter file language(enter 1 to show supported languages ) ').lower()
    if file_language == str(1):
        for i in languages:
            print(i)
        file_language = input('enter file language(enter 1 to show supported languages ) ').lower()
    new = ''
    for lan in languages:
        if file_language == lan:
            f_languages = dic[lan]
            new += f_languages
            print(f_languages)
            print(new)
    img_to_audio(new)

