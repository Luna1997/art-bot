import cairo
import random
import time 

#Asking for input
curves = int(input("How many curves do you want in the picture?: "))
lines = int(input("How many lines do you want in the picture?: "))
safe = str(input("What do you want it to be called?: "))
 
def make_img():
	with cairo.SVGSurface(safe+".svg", 1920, 1080) as surface:
		#Make the canvas background white
		context = cairo.Context(surface)
		context.scale(1920,1080)
		context.set_source_rgba(1,1,1,1)
		context.rectangle(0,0,1920,1080)
		context.fill()
		context.stroke()
		#Print a bunch of curves		
		for x in range(0,curves):
			context.set_line_width(0.0+random.random()/10)
			context.set_source_rgba(random.random(),random.random(),random.random(),1)
			context.move_to(random.random(),random.random())
			context.curve_to(random.random(),random.random(),random.random(),random.random(),random.random(),random.random())
			context.stroke()
		#Print some nice lines
		for i in range(0,lines):	
			linewidth4 = random.random()/10
			context.set_source_rgba(random.random(),random.random(),random.random(),random.random())
			context.set_line_width(0.0+linewidth4)
			context.move_to(random.random(),random.random())
			context.line_to(random.random(),random.random())
			context.stroke()
		
make_img()
