import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr
# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    audio_text = r.listen(source)
    if (audio_text):
        print("audio taken please wait")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    print("Text: " + r.recognize_google(audio_text, language="en-IN"))
    t = (r.recognize_google(audio_text,language="en-IN"))
    with open("text.txt", "a", encoding='utf-8') as file_object:
        # Append 'hello' at the end of file
        file_object.write(t)
    file_object.close()
    try:
        # using google speech recognition
        print(type(t))
    except:
        print("Sorry, I did not get that")
print("done execution")
