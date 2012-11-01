"""
- Program Name : Jarvis Bot [2.0]
- Program description : An AI chatbot.
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh

"""

""" This source code for Jarvis Bot [2.0] and its accompanied classes was written soley by A.Taylor, and should not be 
distributed or copied without crediting the original author. This source code can be used in whatever projects you wish to use it in.
But i, the original author : A.Taylor. Request that the original credits stay intact.
"""

# Import framework
from os import system
from random import choice

# Import whole Framework module
import os, pyttsx	# Pyttsx is the voice API Jarvis will use.

# Import Time telling modules
from time import gmtime, strftime

# Import Independant Jarvis Classes
import JarvisVoiceAPI, JarvisTopics, JarvisRandomQuestion, JarvisResponseDB, JarvisJokes, JarvisGames

class Jarvis(object) :
	""" This will be the main Jarvis Class """
	REPEAT = 0
	
	def __init__(self, JVersion) :
		# Call the {JarvisVoiceAPI} Class file
		self.JarvisClassVoiceAPI = JarvisVoiceAPI.JarvisVoiceAPI()
	
		# Call the {MiscJarvisAudio} Class
		self.JarvisMiscAudioClass = MiscJarvisAudio()
		
		# Call the {JarvisHelp} Class
		self.sh = JarvisHelp()
		
		# Call the {JarvisResponseDB.JarvisResponse} Class
		self.ResponseDB = JarvisResponseDB.JarvisResponse()
		
		# Call the {JarvisResponseDB.JarvisCommands} Class
		self.ResponseDB_COM = JarvisResponseDB.JarvisCommands()
		
		""" This constructor will create the introduction to Jarvis """
		
		print \
				"""
				Jarvis Bot [V.2.0]
				
		Hi! I'm the friendly AI Bot called Jarvis, that is 
		written in the Python programming language.
				"""
		
	def Jarvis_Intro(self) :
		""" All the option code will be written in this method """
		print "%s%s Hello! I am Jarvis, the AI bot. pleased to meet you, %s . \n" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
		self.JarvisClassVoiceAPI.JarvisIntroVAPI()
		self.JarvisClassVoiceAPI.JarvisQuestionAudio()
		cn = raw_input("%s%s If you would like me to call you by your name. I can, just simply say yes or no : " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT))
		if str(cn.lower()) in JarvisMainVar.JCOMTRUE :
			RU = RenameClass()
			RU.RenUTRUE()
			print "%s%s username changed successfully to %s! " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
			self.JarvisMiscAudioClass.JarvisRNTrue()
			self.Jarvis_Start()
		elif str(cn.lower()) in JarvisMainVar.JCOMFALSE :
			print "%s%s so you're fine with %s . " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
			self.JarvisClassVoiceAPI.JarvisQuestRenUFALSE()
		else :
			self.JarvisClassVoiceAPI.JarvisERROR()
			raw_input("%s%s Input not recognized! " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT))
			system('cls')
			self.Jarvis_Intro()
		
		self.Jarvis_Start()
		
	def Jarvis_Start(self) :
		print "\n"
		print "%s%s Nice to meet you, %s! Don't be shy to ask me a question! \n" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
		# Jarvis VAPI ( Voice API )
		self.JarvisMiscAudioClass.JarvisWelcome()
		self.UserResponse()
	
	def UserResponse(self) :
		# This function is soon going to be transfered to its own independant class file. Because it will be slowing down the main src.
		# User input
		print "%s%s Ask me a question %s, ( I respond to commands like ( Exit, Help ) : " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
		self.JarvisMiscAudioClass.JarvisAskQuestion()
		self.UserInput()
		
	def UserInput(self) :
		# I'll start writing the console commands first, then onto the actual response code.
		UI = raw_input()
		if ((str(UI.lower())) in JarvisMainVar.POSSIBLE_EXIT_COM) :
			print "%s%s I will now shutdown. Goodbye %s . " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
			self.JarvisMiscAudioClass.JarvisExitAudio()
			raw_input()
			exit()
		elif (str(UI.lower()) == self.ResponseDB_COM.Help) :
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
			self.JarvisClassVoiceAPI.JarvisHelpAudio()
			# Go to the help options function
			print "\n"
			self.sh.help()
			
		# Error catching
		elif (UI in JarvisMainVar.ERROR) :
			print "%s%s I don't respond to empty spaces. " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT)
			self.JarvisClassVoiceAPI.JarvisEmpty()
			raw_input()
			self.UserResponse()
		# Misc commands
		elif (JarvisMainVar.JarvisTellTheTime in (str(UI.lower()))) :
			# Call Jarvis time keeping class
			JT = JarvisTimeKeeping()
			JT.JTime()
			# JVAPITIME is the code that calls the Voice API time telling class.
			self.JarvisClassVoiceAPI.JarvisVoiceTellTime()
			print "%s%s The current time is : " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT), JT.JTime()
			self.JarvisNewQuestQuery()
		# Greeting responses
		elif (self.ResponseDB.Greeting_EN in (str(UI.lower()))) :
			while True :
				if UI in JarvisMainVar.REPEAT :
					JarvisMainVar.REPEAT[UI] += 1
					print "%s%s you already said %s %s times." %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, UI, JarvisMainVar.REPEAT)
					self.JarvisNewQuestQuery()
		else :
			print "%s%s Hmm, i didn't recognize that input :( , %s. \n" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
			self.JarvisMiscAudioClass.JarvisInputError()
			self.JarvisQuestError()
			self.UserResponse()

	def JarvisQuestError(self) :
		print "%s%s Try again, %s . But try to be more specific this time. I only have so much processing power!" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
		self.JarvisMiscAudioClass.JarvisTryAgainErr()
		
	def JarvisNewQuestQuery(self) :
		print "%s%s Ask me something else, %s . " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.USER_NAME[0])
		self.JarvisMiscAudioClass.JarvisNewAudioQuery()
		self.UserInput()
		
class JarvisHelp(object) :
	""" Class that will manage Jarvis's help function """
	JF = "Welcome to my help function! I have many assorted options here, feel free to choose them!"
	
	def __init__(self) :
		""" Jarvis's  Help constructor """
		
		# Call the {JarvisVoiceAPI} Class file
		self.JarvisClassVoiceAPI = JarvisVoiceAPI.JarvisVoiceAPI()
	
		# Call the {MiscJarvisAudio} Class
		self.JarvisMiscAudioClass = MiscJarvisAudio()
		
		# Call the {RenameClass} Class
		self.RenJ = RenameClass()
		
	def help(self) :
		print "%s%s %s" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, self.JF)
		self.JarvisClassVoiceAPI.JarvisWelcomeHelpAudio()
		self.JarvisClassVoiceAPI.JarvisHelpUIAudio()
		HelpUI = raw_input("%s%s Enter your choice from the list above. [ Usage : For example to request help on interacting with Jarvis, press 1 ] : " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT))
		# Make the text in the console easier to read
		print "\n"
		# Jarvis help function 
		if (HelpUI == "1") :
			print "%s%s %s%s%s \n"  %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, JarvisMainVar.JD1, JarvisMainVar.JD2, JarvisMainVar.JD3)
			self.JarvisClassVoiceAPI.JarvisHelpDialogue()
			self.help()
		elif (HelpUI == "2") :
			print "%s%s Heh, you will have to try allsorts of hidden keywords. Goodluck!"  %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT)
			self.JarvisClassVoiceAPI.JarvisHiddenCom()
			self.help()
		elif (HelpUI == "3") :
			self.RenJ.RenJTRUE()
			self.help()
		elif (HelpUI == "4") :
			# Call the {Jarvis} Class
			self.RT = Jarvis()
			self.RT.UserResponse()
		else :
			print "%s%s %s wasn't recognized. Please try again." %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT, HelpUI)
			self.JarvisClassVoiceAPI.JarvisHelpERROR()
			self.help()

class RenameClass(object) :
	""" Class to rename Jarvis. """
	
	# This is in a seperate class so that each class can have its own Main functions and methods.
	
	def __init__(self) :
		""" Rename constructor. May need to add something here in the future. """
		
		# Call the {JarvisVoiceAPI} Class file
		self.JarvisClassVoiceAPI = JarvisVoiceAPI.JarvisVoiceAPI()
		
	def RenJTRUE(self) :
		print "%s%s Why would you want to rename me? :( . But, since you requested to rename me, you can :-) . \n" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT)
		# Jarvis speaks out the above message to the user.
		self.JarvisClassVoiceAPI.JarvisRenameAudio()
		# Rename Jarvis class method.
		self.JarvisClassVoiceAPI.BotRenameAudio()
		BOT_RENAME = raw_input("Type the name you would like to rename me to : ")
		JarvisMainVar.BOT_NAME.remove('Jarvis')
		JarvisMainVar.BOT_NAME.append(BOT_RENAME)
		print "%s%s I have successfully been renamed! \n" %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT)
		self.JarvisClassVoiceAPI.BotRenameSuccess()
		
	def RenUTRUE(self) :
		# Rename User class method.
		
		# Jarvis's voice Audio for the below input
		self.JarvisClassVoiceAPI.JarvisQuestRenUTRUE()
		
		un = raw_input("%s%s Type the name that you wish to be called : " %(JarvisMainVar.BOT_NAME[0], JarvisMainVar.MISC_BOT))
		
		JarvisMainVar.USER_NAME.remove("user")
		JarvisMainVar.USER_NAME.append(un)
		
class MiscJarvisAudio(object) :
	"""Class for mutable data types for the JavisVoice API. Hopefully this will keep the new data objects updated when Jarvis Voice API pronounces the user properties """
	# I have put this TTS properties on the main Jarvis file because while it was in the external JarvisVoiceAPI class file it wasn't picking up the changes to the mutable variables.
	
	JarvisMISCVAPI = pyttsx.init("sapi5")
	
	def JarvisGreeting(self) :
		self.JarvisMISCVAPI.say("I'm fine, thanks. %s" %(JarvisMainVar.USER_NAME[0]))
		self.JarvisMISCVAPI.runAndWait()
		
	def JarvisRNTrue(self) :
		self.JarvisMISCVAPI.say("username changed successfully to %s! " %(JarvisMainVar.USER_NAME[0]))
		self.JarvisMISCVAPI.runAndWait()
		
	def JarvisWelcome(self) :
		self.JarvisMISCVAPI.say("Nice to meet you, %s! Don't be shy to ask me a question!" %( JarvisMainVar.USER_NAME[0]))
		self.JarvisMISCVAPI.runAndWait()
		
	def JarvisAskQuestion(self) :
		self.JarvisMISCVAPI.say("Ask me a question %s, I respond to commands like, Exit, or Help." %(JarvisMainVar.USER_NAME[0]))
		self.JarvisMISCVAPI.runAndWait()

	def JarvisNewAudioQuery(self) :
		self.JarvisMISCVAPI.say("Ask me something else, %s . " %(JarvisMainVar.USER_NAME[0]))
		self.JarvisMISCVAPI.runAndWait()
		
	def JarvisInputError(self) :
		self.JarvisMISCVAPI.say("Sorry, i didn't recognize that input ,%s . " %(JarvisMainVar.USER_NAME[0]))
		self.JarvisMISCVAPI.runAndWait()
	
	def JarvisTryAgainErr(self) :
		self.JarvisMISCVAPI.say("Try again, %s . But try to be more specific this time." %(JarvisMainVar.USER_NAME[0]))
		self.JarvisMISCVAPI.say("I only have so much processing power!")
		self.JarvisMISCVAPI.runAndWait()
		
	def JarvisExitAudio(self) :
		self.JarvisMISCVAPI.say("I will now shutdown. Goodbye %s ." %(JarvisMainVar.USER_NAME[0]))
		self.JarvisMISCVAPI.runAndWait()
		
class JarvisTimeKeeping(object) :
	""" Jarvis time telling class """
	
	def JTime(self) :
		return strftime("%a, %d %b %Y %H:%M:%S \n", gmtime())
		
class JarvisMainVar(object) :
	""" Jarvis's variable storage class. All the main variables go into this class. """

	# Repeating Response Catching
	Repeat = {}
	# Jarvis's botname variables
	BOT_NAME = ['Jarvis']
	MISC_BOT = " : "
	
	# Jarvis Voice API Call Class
	
	# Username variable
	# Default name that Jarvis will call the user is {User}
	# But this can be changed because it is assigned a mutable type.
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
	JarvisTellTheTime = "time"
	JarvisTellTheTime1 = "clock"
	
	# Jarvis Dialogue for {JarvisHelp.help()}
	JD1 = "How to correctly interact with me. "
	JD2 = "To interact with me properly, be specific with your inputs for example to ask me a question about how i am, make sure you use the keywords like 'How are you' 'how do you feel Jarvis' "
	JD3 = "As long as you write keywords i will recognize them and reply to you. "
	
	def __str__(self) :
		"Storage class for all the main variables"
		
def main() :
	# Call the main class
	init = Jarvis(JVersion = os.system("title Jarvis Bot [V.2.0] - Beta [1.0] "))
	init.Jarvis_Intro()
	raw_input()
	
# Call the class, and function
if __name__ == "__main__" :
	main()