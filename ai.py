#Base AI template
#Author: Vhuhwavho Mokoma
import pyttsx3
import speech_recognition as sr

class AI():
    __name = ""
    __skill = []

    def __init__(self,name=None):
        self.engine = pyttsx3.init()
        voice = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voice[1].id)
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if (name is not None):
            self.__name = name
        
        print("Listening...")
        #getting sound from microphone
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value
        sentence = "Hello, my name is" + self.__name
        self.engine.say(sentence)
        self.engine.runAndWait()

    def say(self,sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
    
    def listen(self):
        print("Say something so that I may assist")
        self.engine.say("Say something so that I may assist")
        self.engine.runAndWait()

        with self.m as source:
            audio = self.r.listen(source)
        print("Okay, got it")
        phrase = ""
        try:
            phrase = self.r.recognize_google(audio, show_all=False, language="en-US")
            sentence = "Got it, you said " + phrase
            self.engine.say(sentence)
            self.engine.runAndWait()
        except:
            print("Sorry I didnt catch that")
            self.engine.say("Sorry I didnt catch that")
            self.engine.runAndWait()
        return phrase