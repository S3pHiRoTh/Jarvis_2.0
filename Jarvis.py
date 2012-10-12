"""
- Program Name : Jarvis Bot [2.0]
- Program description : An AI chatbot.
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh

"""

# Import framework
from os import system
from random import choice

# Import whole Framework module
import os, sqlite3 # Sqlite3 will be used later to create the Jarvis response Database.

# Import Time telling modules
from time import gmtime, strftime

# Import Independant Jarvis Classes
None 	# None at the moment. They will be added later

class Jarvis(object) :
	""" This will be the main Jarvis Class """
	def __init__(self) :
		""" This constructor will create the introduction to Jarvis """
		print \
				"""
				Jarvis Bot [V.2.0]
				
		Hi! I'm the friendly AI Bot called Jarvis, that is 
		written in the Python programming language.
				"""
		
		self.Jarvis_Intro()
		
	def Jarvis_Intro(self) :
		""" All the option code will be written in this method """
		
		print "%s%s Hello! I am Jarvis, the AI bot. pleased to meet you, %s . \n" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
		cn = raw_input("%s%s If you would like me to call you by your name. I can, just simply say yes or no : " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT))
		if str(cn.lower()) in JarvisMainVar.JCOMTRUE :
			RU = RenameClass()
			RU.RenUTRUE()
			print "%s%s username changed successfully to %s! " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
			self.Jarvis_Start()
		elif str(cn.lower()) in JarvisMainVar.JCOMFALSE :
			print "%s%s so you're fine with %s . " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
		else :
			raw_input("%s%s Input not recognized! " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT))
			system('cls')
			self.Jarvis_Intro()
		
		self.Jarvis_Start()
		
	def Jarvis_Start(self) :
		print "\n"
		print "%s%s Hi i'm Jarvis, Nice to meet you, %s! Don't be shy to ask me a question! \n" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
	
		self.UserResponse()
	
	def UserResponse(self) :
		# This function is soon going to be transfered to its own independant class file. Because it will be slowing down the main src.
		# User input
		UI = raw_input("%s%s Ask me a question %s, ( I respond to commands like ( Exit, Help ) : " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0]))
		# I'll start writing the console commands first, then onto the actual response code.
		if (str(UI.lower())) in JarvisMainVar.POSSIBLE_EXIT_COM :
			print "%s%s I will now shutdown. Goodbye %s . " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
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
			sh = JarvisHelp()
			sh.help()
			
		# Error catching
		elif UI in JarvisMainVar.ERROR :
			print "%s%s I don't respond to empty spaces. " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT)
			self.UserResponse()
		elif (str(UI.lower())) in JarvisMainVar.JarvisTellTheTime :
			# Call Jarvis time keeping class
			JT = JarvisTimeKeeping()
			JT.JTime()
			print "%s%s The current time is : " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT), JT.JTime()
			self.UserResponse()
		else :
			print "%s%s Hmm, i didn't recognize that input :( . Can you try again? \n" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
			self.UserResponse()
		
class JarvisHelp(object) :
	""" Class that will manage Jarvis's help function """
	JF = "Welcome to my help function! I have many assorted options here, feel free to choose them!"
	
	def __init__(self) :
		""" Jarvis's  Help constructor """
		print "%s%s %s" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, self.JF)
		
	def help(self) :
		HelpUI = raw_input("Enter your choice from the list above. [ Usage : For example to request help on interacting with Jarvis, press 1 ] : ")
		# Make the text in the console easier to read
		print "\n"
		# Jarvis help function 
		if (HelpUI == "1") :
			print \
			"""%s%s How to correctly interact with me.
				To interact with me properly, be specific with your inputs for example to ask me a question about how i am, make sure you use the keywords like 'How are you' 'how do you feel Jarvis?'. 
				As long as you write keywords i will recognize them and reply to you \n
			""" % (JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT)
			self.help()
		elif (HelpUI == "2") :
			print "%s%s Heh, you will have to try allsorts of hidden keywords. Goodluck!"  %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT)
		elif (HelpUI == "3") :
			RenJ = RenameJarvis()
			RenJ.RenJTRUE()
		elif (HelpUI == "4") :
			ref = Jarvis()
			ref.UserResponse()
		else :
			print "%s%s %s wasn't recognized. Please try again." %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, HelpUI)
			self.help()

class RenameClass(object) :
	""" Class to rename Jarvis. """
	
	# This is in a seperate class so that each class can have its own Main functions and methods.
	def __init__(self) :
		print "%s%s Why would you want to rename me? :( . But, since you requested to rename me, you can :-) . \n" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT)
		self.RenJTRUE()
		
	def RenJTRUE(self) :
		# Rename Jarvis class method.
		BOT_RENAME = raw_input("Type the name you would like to rename Jarvis to : ")
		JarvisMainVar.BOT_NAME.remove('Jarvis')
		JarvisMainVar.BOT_NAME.append(BOT_RENAME)
		print "%s%s I have successfully been renamed! \n" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT)
	
	def RenUTRUE(self) :
		# Rename User class method.
		
		un = raw_input("%s%s Type the name that you wish to be called : " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT))
		JarvisMainVar.USER_NAME.remove("user")
		JarvisMainVar.USER_NAME.append(un)

class JarvisTimeKeeping(object) :
	""" Jarvis time telling class """
	
	def JTime(self) :
		print strftime("%a, %d %b %Y %H:%M:%S \n", gmtime())
		
class JarvisMainVar(object) :
	""" Jarvis's variable storage class. All the main variables go into this class. """

	# Jarvis's botname variables
	BOT_NAME = ['Jarvis']
	MISC_BOT = " : "
	
	# Username variable
	USER_NAME = ['user']
	
	# Error catching for UserResponse() Function
	ERROR = " "
	
	# Possible bot replies [Still in beta mode]
	# Bot TRUE/FALSE replies
	# {POSSIBLE_EXIT_COM = Exit response for function UserResponse() }
	# {JCOMTRUE = True commands for intro() }
	# {JCOMFALSE = False commands for intro() }
	# {JarvisTellTheTime = Function for telling the time }
	
	POSSIBLE_EXIT_COM = ['exit', 'leave', 'cya', 'bye']
	JCOMTRUE = ("y", "yes", "yes please", "yep", "change my name", "name change", "yeah", "ye")
	JCOMFALSE = ("n", "no", "im not bothered", "no thanks", "nope", "user is fine")
	JarvisTellTheTime = ( "time", "whats the current time", "tell the time", "whats the time?" )
	
	def __str__(self) :
		"Storage class for all the main variables"
		
# Call the main class
def main() :
	init = Jarvis()
	raw_input()
	
# Call the class, and function
main()