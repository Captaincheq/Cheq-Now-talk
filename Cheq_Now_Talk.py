import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sqlacodegen

listener = sr.Recognizer()
#giving Cheq permision to say something
engine = pyttsx3.init()
#To change the voice next 2 lines
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):   
    engine.say(text)
    engine.runAndWait()

#command for Cheq to listen to me
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening....')
            voice = listener.listen(source)
            #can use bing
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa',  '')
                print(command)
                # talk(command)

    except:
        pass
    return command

#Add more commands on elif statements below to expand your alexa.
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song) 
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        #print(time)
        talk('Current time is ' + time)
    
    elif 'how to' in command:
        person = command.replace('how to', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'relationship' in command:
        relation = command.replace('relationship', '')
        info = sqlacodegen.codegen(relation, 3)
        talk(info)


    else:
        talk('Please say that again , I didnt hear you clearly')


while True:
    run_alexa()