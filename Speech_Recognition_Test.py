        # -*- coding: utf-8 -*-
"""
Speech Recognition

V1.0.1

Created on Thu Aug 26 15:46:11 2021

@author: ARMAG
"""

# Important library
import pyttsx3
import pyaudio
import pydub

import speech_recognition as sr

#print("1")
def listening():
#Defining the recognizer to start recognizing words from microphone
    listener = sr.Recognizer()
#Setting the model to catch phrases from the microphone not an audiofile
    with sr.Microphone() as source:        
# Setting a threshold for energy to make the model stop dectating when there's nothing said
        listener.dynamic_energy_threshold = False
        listener.adjust_for_ambient_noise(source)
        listener.energy_threshold = 400
        #Start listening
        #print("2")
        audio = listener.listen(source)
        #print("3")
        try:
        #Using google's online speech recognition model
            phrase = listener.recognize_google(audio)
            #print("4")
            print(phrase)
            return phrase
        except sr.UnknownValueError:
                print('I couldn\'t catch the phrase')
                return 'fail'
        except sr.RequestError:
                print('Connection Error')
                return 'fail'           

