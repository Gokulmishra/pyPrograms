import speech_recognition as sr
import webbrowser as wb
import pyaudio
import datetime
import os

import win32com.client
import sys
s=win32com.client.Dispatch("SAPI.SpVoice")
 
r2=sr.Recognizer()
r3=sr.Recognizer()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        s.Speak("Good Morning!")

    elif hour>=12 and hour<18:
        s.Speak("Good Afternoon!")  

    else:
        s.Speak("Good Evening!") 

    s.Speak("I am G Neutrino Sir. Please tell me how may I help you")
with sr.Microphone() as source:
	print("Speech recognition")
	print("Please wait. Calibrating microphone...")  
      # listen for 5 seconds and create the ambient noise energy level
	r3.adjust_for_ambient_noise(source, duration=5)
	wishMe()
	print("Speak Now")
	audio=r3.listen(source)

if 'hi ' in r3.recognize_google(audio):
	r2=sr.Recognizer()
	url='https://www.youtube.com/results?search_query='
#https://www.google.com/search?q=
	with sr.Microphone() as source:
		r2.adjust_for_ambient_noise(source, duration=5)
		print('Search your query')
		s.Speak('Search your query')
		audio=r2.listen(source)

		try:
			text=r2.recognize_google(audio)
			print(text)
			wb.get().open_new(url+text)

		except sr.UnknownValueError:
			print('error')

		except sr.RequestError as e:
			print('failed'.format(e))
elif 'play music' in r3.recognize_google(audio):
            music_dir = ''
	#in music_dir= put address of your song within '' for eg: i have a folder named song in d drive so D:\\Song
            songs = os.listdir(music_dir)
            print(songs)   
            os.startfile(os.path.join(music_dir, songs[0]))

#speech_recognition.RequestError: recognition connection failed: [Errno 11001] getaddrinfo failed