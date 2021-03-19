import pyttsx3
import PyPDF2

#a pdf reader in python
book = open('Thesis 1.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()


for num in range(9,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)

    speaker.runAndWait()