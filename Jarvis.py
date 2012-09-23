"""
- Program Name : Jarvis Bot [2.0]
- Program description : An AI chatbot.
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh

"""

# Any framework that needs importing goes here.
from os import system
from random import choice

# Import whole Framework module
import os

# Import Independant Jarvis classes 
import JarvisTopics, JarvisRandomQuestion

# Global Variable
# Jarvis's botname variable
BOT_NAME = ['Jarvis']
MISC_BOT = " : "

def intro() :
	# Global variables
	global un
	
	print \
	"""
				Jarvis Bot [V.2.0]
				
		Hi! I'm the friendly AI Bot called Jarvis, that is 
		written in the Python programming language.
		
		
		
	"""
	# User Variables
	un = raw_input("%s%s User, please type your Name : " %(BOT_NAME[0], MISC_BOT))
	Jarvis_Start()
	
def Jarvis_Start() :
	print "\n"
	print "%s%s Hi i'm Jarvis, Nice to meet you, %s! Don't be shy to ask me a question! \n" %(BOT_NAME[0], MISC_BOT, un)
	
	UserResponse()
	
def UserResponse() :
	# This functions global variables
	None
	# User input
	UI = raw_input("%s%s Ask me a question ( I respond to commands like ( Exit, Help ) : " %(BOT_NAME[0], MISC_BOT))
	# I'll start writing the console commands first, then onto the actual response code.
	if (str(UI.lower())) == "exit" or "quit" or "leave" or "bye" or "cya" :
		print "%s%s I will now shutdown. Goodbye %s . " %(BOT_NAME[0], MISC_BOT, un)
		raw_input()
		exit()	
	elif (str(UI.lower()) == "help") :
		print \
		"""
		Welcome to the help menu. Below is the list
		on what help options Jarvis has. To select an option
		simply enter the number that it's allocated to.
			
		1 - How to interact with Jarvis
		2 - Hidden commands
		3 - Want to rename Jarvis? You can!
		4 - Return to asking Jarvis a question
		"""
			
		# Go to the help options function
		print "\n"
		help()
	else :
		print "%s%s Hmm, i didn't recognize that input :( . Can you try again? \n" %(BOT_NAME[0], MISC_BOT)
		UserResponse()

def help() :
	HelpUI = raw_input("Enter your choice from the list above. [ Usage : For example to request help on interacting with Jarvis, press 1 ] : ")
	# Make the text in the console easier to read
	print "\n"
	# Jarvis help function 
	if (HelpUI == "1") :
		print "How to correct interact with Jarvis : To interact with Jarvis properly, be specific with your inputs for example to ask Jarvis a question about how he is, make sure you use the keywords like 'How are you' 'how do you feel Jarvis?'. As long as you write keywords jarvis will recognize them and reply to you"
	elif (HelpUI == "2") :
		print "Heh, you will have to try allsorts of hidden keywords. Goodluck!"
	elif (HelpUI == "3") :
		print "Why would you want to rename Jarvis? :( . But, since you requested to rename Jarvis, you can :-) . \n"
		RenameJarvis()
		
def RenameJarvis() :
	# Rename Jarvis function
	BOT_RENAME = raw_input("Type the name you would like to rename Jarvis to : ")
	BOT_NAME.remove('Jarvis')
	BOT_NAME.append(BOT_RENAME)
	print "%s%s I have successfully been renamed! \n" %(BOT_NAME[0], MISC_BOT)
	UserResponse()
	
def Init() :
	# Add a function name here, to load it easily ;-) .
	intro()
	
# Initialize code
Init()

# Keep the CUI open
raw_input()