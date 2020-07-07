import win32com.client
import sys

#one has to install above packges to run the following program

b=True
s=win32com.client.Dispatch("SAPI.SpVoice")

while b:
	print("Enter the word or sentence \n")
	s.Speak("Enter the word or sentence ")
	p=input()
	s.Speak(p)
	print("Do you want to continue  y/n ")
	p=input()
	if p=='n':
		b=False
print("Good-Bye, see you soon")
s.Speak("Good-Bye, see you soon")
#for instance try this:- namaskaar, aaap kai sa hain,  aur bataa o, lockdown mei kaya kar ra ha ho?