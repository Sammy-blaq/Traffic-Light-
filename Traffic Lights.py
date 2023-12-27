from tkinter import *
import time

#defines the root screen
trafficLight = Tk()
trafficLight.geometry('300x400+600+200')

#defines my object screen
canvas = Canvas(trafficLight, width=300, height=400, bg='white')
canvas.pack()

canvas.create_rectangle(100, 50, 200, 350, fill='#4eaba1', width=4)

# define functions

while True:
			def green():
				for i in range(10):
					green = canvas.create_oval(100, 50, 200,150, fill='green', width=2)
					trafficLight.update()
					time.sleep(0.50)
					
			def greenBlack():
				for i in range(10):
					green = canvas.create_oval(100, 50, 200,150, fill='black', width=2)
					trafficLight.update()
					time.sleep(0.00001)
					
			def yellow():
				for i in range(10):
					yellow = canvas.create_oval(100, 150, 200,250, fill='yellow', width=2)
					trafficLight.update()
					time.sleep(0.05)
					
			def yellowBlack():
				for i in range(10):
					yellow = canvas.create_oval(100, 150, 200,250, fill='black', width=2)
					trafficLight.update()
					time.sleep(0.00001)
					
			def red():
				for i in range(10):
					red = canvas.create_oval(100, 250, 200,350, fill='red', width=2)
					trafficLight.update()
					time.sleep(0.50)
					
			def redBlack():
				for i in range(10):
					red = canvas.create_oval(100, 250, 200,350, fill='black', width=2)
					trafficLight.update()
					time.sleep(0.0001)

			green()
			greenBlack()
			yellow()
			yellowBlack()
			red()
			redBlack()

trafficLight.mainloop()