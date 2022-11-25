1) install pytesseract

   installation guide
     * Download tesseract exe from https://github.com/UB-Mannheim/tesseract/wiki.
     * Install this exe in C:\Program Files (x86)\Tesseract-OCR
     * Open virtual machine command prompt in windows
     * Run pip install pytesseract


2) Run pip install googletrans

     * if anyone get error from this try this,  pip install googletrans==3.1.0a0

3) make sure the TESSDATA_PREFIX environment variable is set to the parent directory of your "tessdata" directory

   TESSDATA_PREFIX = "C:\Program Files\Tesseract-OCR\tessdata"

  * if you need more language to translate download the tessdata from here-  https://github.com/tesseract-ocr/tessdata
    (you can download the specific one or everything if you need)


4) finally, please make sure your input file in same dictionary and enjoy ...
