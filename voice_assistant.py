import speech_recognition as sr
import wikipedia
import pyttsx3


#starting the text to speach engine
engine=pyttsx3.init()

#starting the speechrecognition library
recognizer=sr.Recognizer()

with sr.Microphone() as source:
    #clear background noise
    print('Clearing background noise... Please Wait')
    recognizer.adjust_for_ambient_noise(source,duration=1)

    #waiting for speech message
    print("Wating for your message")
    recordedaudio=recognizer.lesten(source)
    print('Done recording')

#printing message

try:
    print('Printing your message...Please wait')
    text=recognizer.recognize_google(recordedaudio,language='en-US')
    print('Your Message: {}', format(text))

except Exception as ex:
    print(ex)

#Input Data
    wikiserach=wikipedia.summary(text)
    engine.say(wikiserach)

    
