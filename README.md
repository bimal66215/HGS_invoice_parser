# HGS_invoice_parser

The Output is saved as 'output.xlsx' and the project directory itself. For this project, you will have to install the Tesseract using the installer in the below link:

<a href="https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.1.0.20220510.exe" target="_blank">32 Bit</a>

<a href="https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.1.0.20220510.exe" target="_blank">64 Bit</a>

The path for the tesseract.exe need to noted down while installing the Tesseract for the below code in the program:

```diff

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
```

"C:\Program Files\Tesseract-OCR\tesseract" is the default path

