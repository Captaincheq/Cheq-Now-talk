import pyttsx3
import PyPDF2

#a pdf reader in python
book = open('The Journey My Life.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()

for num in range(2, pages):
    page = pdfReader.getPage(2)
    text = page.extractText()
    speaker.say(text)

    speaker.runAndWait()