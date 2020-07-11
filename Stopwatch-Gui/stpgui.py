import tkinter as tk
import tkinter.font as Tkfont
from datetime import datetime

def run():
	current_time = datetime.now()
	diff =current_time-start_time
	txt_var.set('%d.%02d'%(diff.seconds,diff.microseconds//10000))
	
#run timer again

	if running: #time lapse
		root.after(20,run) #to reschedule after 20ms,refresh display
		
def start():
	global running
	global start_time
	
	if not running:
		running =True
		start_time=datetime.now()

		root.after(10,run)

def stop():
	global running

	running=False
	
def reset():
	
	global start_time
	start_time=datetime.now()

	if not running:
		txt_var.set('0.00')
running=False
start_time=None

root =tk.Tk()
root.geometry("500x200")#width Xheight
root.title("Stopwatch")

txt_var=tk.StringVar()
txt_var.set('0.00')

#from tkinter import font,tk #fonts=list(font.families())
fontstyle=Tkfont.Font(family = "Lucida Grande",size=50)
tk.Label(root,textvariable=txt_var,font=fontstyle).pack()

tk.Button(root,text= "Start",command=start).pack(fill='x')
tk.Button(root,text= "Stop",command=stop).pack(fill='x')
tk.Button(root,text= "Reset",command=reset).pack(fill='x')

root.mainloop()

		 