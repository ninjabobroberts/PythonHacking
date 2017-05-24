import speech_recognition
import pyttsx

import random

speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

real_name_picked = False

phrase1 = ''
name = ''

activate = False

def pick_name():
        global name
        name_int = random.randint(1,5)
        if name_int == 1:
                name = 'Johnny Boy'
        elif name_int == 2:
                name = 'Klunk Head'
        elif name_int == 3:
                name = 'Uncle Bob'
        elif name_int == 4:
                name = 'Dog'
        elif name_int == 5:
                name = 'MoneyBags'

def pick_phrase1():
        global phrase1

        phrase_int = random.randint(1,5)
        if phrase_int == 1:
                phrase1 = 'Right Back At Ya'
        elif phrase_int == 2:
                phrase1 = 'Hello'
        elif phrase_int == 3:
                phrase1 = 'Good Day To You'
        elif phrase_int == 4:
                phrase1 = 'Mind The Gap'
        elif phrase_int == 5:
                phrase1 = 'Buienos Dias'

def pick_phrase2():
        global phrase2

        phrase2_int = random.randint(1,5)

        if phrase_int == 1:
                phrase2 = 'Is that cake on your nose?'
        elif phrase_int == 2:
                phrase2 = 'I\'M ALIVE!!!'
        elif phrase_int == 3:
                phrase2 = 'Read Any Good Books Lately?'
        elif phrase_int == 4:
                phrase2 = 'All of this is random, but one day i\'ll be alive!'
        elif phrase_int == 5:
                phrase2 = 'Donald Twump'

        
def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()

def listen():
        global activate
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)
		if audio == "Mick":
                        activate = True

	try:
		return recognizer.recognize_sphinx(audio)
                str_listen(audio)
		# or: return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		print "Could not understand audio"
	except speech_recognition.RequestError as e:
		print "Recog Error; {0}".format(e)

	return ""

def str_listen(audio):
    file1 = open("learn.txt", "w")
    file1.write(str(audio))
    file1.close()


def if_write():
    if 'Hi' or 'Hello' or 'Sup' or 'Good Morning' or 'Self Destruct' or 'Terminator' or 'Yo' in file1:
            if 'Hello' or 'Sup' or 'Good Morning' or 'Yo' in file1:
                    speak("How Are You Today?")
                    listen()
                    speak(phrase1, name)
            elif 'Terminator' or 'Self Destruct' on file1:
                    
    
print "I AM A.I"
print "My Name Is M.i.c.k"
speak("My Name Is M.i.c.k")
if real_name_picked == False:
        print "What Is Your Name?"
        speak("What Is Your Name?")
        real_name = raw_input("Enter: ")
        real_name_picked = True
print "Hello " + name
speak("Hello " + name
print "Waiting For Orders"
speak("Waiting For Orders")
print "I Heard You Say " + str(listen())
Command = str(listen())
speak("I heard you say " + listen())
