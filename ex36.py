def start():
	print ("You are in a big house, do you wish to go the right wing or left wing?")
	answer = input("> ")
	if answer == 'left':
		left_wing()
	elif answer == 'right':
		right_wing()

def left_wing():
	print("Welcome to the left wing, where all the peasants come together")
	print("do you wish to stay in this room or run away?")
	decision = input("> ")
	if decision == 'stay':
			peasant_quarters()
	elif decision == 'run':
			print("Welp, congrats the master has seen you and the dogs have been released.... you die")

def peasant_quarters():
	print("Are you ready?")

def right_wing():
	print("Welcome to the right wing, all of your dreams MIGHT come true")
	print("do you wish to stay here or go explore your other rooms?")
	answer = input("> ")
	if answer == 'stay':
		print("A schandeleer has just fallen on you, way to go you scardy cat")  
	elif answer == 'explore':
		print("""You have three doors from which to pick?
			A. Powder Room 
			B. Jewls Room 
			C. Wigs Room""")
		print("Which one will you choose to enter?")
		room = input("> ")
		if room == 'a':
			Powder_Room()
		elif room == 'b':
			Jewls_Room()
		elif room == 'c':
			Wigs_Room()


def Powder_Room():
	Print("Welcome to the powder room, where we can make you as pretty as a button.")
	print("Do you wish to try your luck out with these boxes? One of them can bring you greate pleasure, but they other can bring you greate dispear")
	print("""which do you choose?
		A. Gold Box
		B. Silver Box""")

def Jewls_Room():
	print("Welcome to the Jewls Room, come in take a look, you can keep whatever you wish... Just be careful with what you wish for")
	print("""Look at those two boxes, you can keep whatever is in one of those boxes, Which one will you take along in your travels?
		A. Box A
		B. Box B""")

def Wigs_Room():
	print("""Welcome to the Wigs Room, come try on a wig on. We have a vast selection, pick right or you might end up with a hairdo to die for
		1. Pink Wig
		2. White Wig
		3. Red Wig""")
	print("Which one do you choose")
	wig = input("> ")
	if wig == '1':
		Pink_Wig()
	elif wig == '2':
		White_Wig()
	elif wig == '3':
		Red_Wig()

def Pink_Wig():
	print("I hope you enjoy the lice that will haunt you for a million years")

def White_Wig():
	print("Way to go, with age comes experience. You can rule the world now")

def Red_Wig():
	print("""Did you know that we got the wig to be this red by downing it in the blood of plague infected children
		.....it was nice knowing you""")

start()