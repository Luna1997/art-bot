import cairo
import random
import time 

seed = random.randint(0,1001)
random.seed(seed)
#Title generator
s_nouns = ["Nissen","Julemanden","Slagteren","Bibliotekaren","Den undertrykte","Den mindregjordte","Den transkønnede","Den lesbiske","Vejviseren","Rotten","Musen","Anarkisten","Kommunisten"]
p_nouns = ["malerne","politibetjentene","buschauførrene","nisserne","bigfoots","aliensne","gespensterne","pungrotterne","hundene","kattene","vennerne","gutterne","de fremmedgjordte","de mindregjordte","de homoseksuelle","de lesbiske","de transkønnede","kapitalisterne","proletariatet","arbejderne"]
s_verbs = ["æder","slår","kysser","spiser", "sparker", "giver en kage til", "truer", "sees med", "kreere", "hacker", "konfigurer", "ser til", "klumser", "meower", "flygter fra", "automatiserer", "eksploderer"]
#p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["for at skabe en revolution","for at ødelægge pandoras æske","for at skabe kommunisme","for at få sine ønsker opfyldt", "for at få nye venner","for at få en kæreste","for at rede verden.","for at lave en kage.", "uden nogen grund.", "fordi himlen er sort.", "for en sygdom.", "for at akkumulere mere viden."]
title = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)

#Removes unwanted characters from the title
replacexwith = "(',.)"
safe = str(title)
for char in replacexwith:
	safe = safe.replace(char,"")
space = " "
for char in space:
	safe = safe.replace(char,"_")

def make_img():
	with cairo.SVGSurface(safe+"_"+str(seed)+".svg", 1920, 1080) as surface:
		#Make the canvas background white
		context = cairo.Context(surface)
		context.scale(1920,1080)
		context.set_source_rgba(1,1,1,1)
		context.rectangle(0,0,1920,1080)
		context.fill()
		context.stroke()
		#Print a bunch of curves
		for y in range(0,random.randint(0,7)):
		    context.set_line_width(0.0+random.random()/10)
		    context.set_source_rgba(random.random(),random.random(),random.random(),1)
		    context.move_to(random.random(),random.random())
		    context.curve_to(random.random(),random.random(),random.random(),random.random(),random.random(),random.random())
		    context.stroke()
		#Print some nice lines
		for x in range(0,random.randint(1,6)):
		    linewidth4 = random.random()/10
		    context.set_source_rgba(random.random(),random.random(),random.random(),random.random())
		    context.set_line_width(0.0+linewidth4)
		    context.move_to(random.random(),random.random())
		    context.line_to(random.random(),random.random())
		    context.stroke()
		time.sleep(0.05)
		
make_img()
