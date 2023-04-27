import openai
import speech_recognition as sr
import threading
import pyttsx3
import time
from queue import Queue

# Set your OpenAI API key
api_key = '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'

# Set the API key for the OpenAI library
openai.api_key = api_key

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)

# Define function to generate response from GPT-3
def generate_response(prompt, response_queue):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response_queue.put(completions.choices[0].text.strip())

# Define function to print chat messages with delay
def print_chat(chat):
    for word in chat:
        time.sleep(0.055)
        print(word, end="", flush=True)
    print()

# Setup speech recognition and chat loop
r = sr.Recognizer()

# Create a queue to communicate the response between threads
response_queue = Queue()

# Update the chat loop function to handle multiple recognition results
def chat_loop():
    print("-----------------------Chat is ready-----------------------")
    while True:
        print("Me:", end=" ", flush=True)
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, show_all=True)
            if text:
                # Extract the transcript from the first alternative in the list
                if 'alternative' in text:
                    text_result = text['alternative'][0]['transcript']
                else:
                    text_result = text[0]['transcript']
                if "stop" in text_result:
                    print("ENDING CHAT COMMUNICATION")
                    break

                # Generate response from GPT-3 in a separate thread
                t1 = threading.Thread(target=generate_response, args=(text_result, response_queue))
                t1.start()
                t1.join()
                gpt3_response = response_queue.get()

                print("ChatGPT:", end=" ")
                print_chat(gpt3_response)

                # Speak the response using text-to-speech engine
                engine.say(gpt3_response)
                engine.runAndWait()
                print("--------------------------------------------")
            else:
                print("No speech recognized")
        except sr.UnknownValueError:
            print("Sorry could not recognize your voice")

if __name__ == "__main__":
    chat_loop()
