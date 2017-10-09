#initialise stats
import time

remaining_points = 20
name = ""
intelligence = 0
strength = 0
health = 100
def say(input):
	print(input)
	time.sleep(1)
def intro():
	print("Welcome to Shitty RPG!")
	print("================================================")

def assignPoints(skill):
	#import global variables
	global remaining_points
	#take input from user for given skill
	points = int(input("set your " + skill + ": "))
	#check there are enough remaining points
	if points > remaining_points:
		points = remaining_points
		say("You don't have enough points, you'll get what you're given. you think this is a fucking game?!")
	remaining_points = remaining_points - points
	say ("you have set your " + skill + " to " + str(points))
	say("you have " + str(remaining_points) + " points left")
	return points
	
def setStats():
	#import global variables
	global remaining_points
	global intelligence
	global strength
	#assign points
	say("Let's get started; lets create your character!")
	intelligence = assignPoints('intelligence')
	strength = assignPoints('strength')
	#exit function
	say ("You're ready for your adventure!")
	
def introMission():
	
	global intelligence
	global strength
	global health
	say("===============================================")
	say("Room One")
	say("===============================================")
	say("You wake in a dark and cold room. Your memory of how you came to be here is hazy.")
	say("A small frail figure hobbles toward you through the gloom. As he gets closer his weak, geriatric form becomes apparent, but you notice the glint of a fierce intelligence in his eyes.")
	say("There is a door behind him, as you move toward it the man blocks your path.")
	say("'I'm afraid you cannot leave this place just yet, young man' says the figure.")
	say("Fuck this shit, you think.")
	say("")
	say("DECISION!!!")
	say("")
	say("Type strike to hit the man with your fist. He looks like a weak, mewing fool.")
	say("Or type charm to try and outwit the old man. Dude's probably got dementia anyway, right?")
	action = input("Choose!: ")
	if action == "strike":
		say("you struck")
		
		
	elif action == "charm":
		say("you charmed")
	else:
		say("That's not valid, dickhead")
	

intro()
setStats()
introMission()