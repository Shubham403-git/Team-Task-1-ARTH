      import os
      import pyttsx3
      import wikipedia
      import datetime
      import time
      import webbrowser
      from datetime import date
      import speech_recognition as sr
      #pyttsx3.speak("Welcome to my text  based chatbot named Dora")
      pyttsx3.speak("Tell me your requirments:")
      while True:     
          r = sr.Recognizer() 
          with sr.Microphone() as source:
              r.energy_threshold = 4000
              r.adjust_for_ambient_noise(source, duration = 3)
              print('we are listening...')
              audio=r.listen(source)
              print('speech done...')

          try:
              #pyttsx3.speak("You said " + r.recognize_google(audio))
              p = r.recognize_google(audio)
          except sr.UnknownValueError:
                  pyttsx3.speak('Sorry, I did not get that')
                  continue

          except sr.RequestError.with_traceback:
                  pyttsx3.speak('Sorry, my service is down')
          if (('do not' in p )or ('do nothing' in p) or ("don't" in p) or ('never' in p)):
              pyttsx3.speak('ok as your wish')
              print('ok as your wish')
              continue
          elif ("exit" in p) or ("quit" in p) or ("terminate" in p) or ("end" in p):
              print("Thanks, see yoy again.")
              pyttsx3.speak("Thanks, see yoy again.")
              break
