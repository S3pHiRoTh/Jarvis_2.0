"""
- Class Name : Jarvis Bot [2.0] (TTS API Class)
- Class description : (TTS class to store audio responses)
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh

"""

# Import Voice API Framework
import pyttsx

# Import time telling module
from time import gmtime, strftime

# Import Jarvis File to so we can havw a reference to the variables
import Jarvis

class JarvisVoiceAPI(object) :
	""" Class that stores Jarvis audio responses. """
	JarvisVAPI = pyttsx.init("sapi5")
		
	def JarvisIntroVAPI(self) :
		self.JarvisVAPI.say("Hello! I am Jarvis. The AI bot. Please to meet you, %s ." %(Jarvis.JarvisMainVar.USER_NAME[0]))
		self.JarvisVAPI.runAndWait()
	
	def JarvisQuestionAudio(self) :
		self.JarvisVAPI.say("If you would like me to call you by your name. I can. Just simply say yes or no.")
		self.JarvisVAPI.runAndWait()
		
	def JarvisQuestRenUTRUE(self) :
		self.JarvisVAPI.say("Type the name that you wish to be called.")
		self.JarvisVAPI.runAndWait()
		
	def JarvisQuestRenUFALSE(self) :
		self.JarvisVAPI.say("so you're fine with %s . " %(Jarvis.JarvisMainVar.USER_NAME[0]))
		self.JarvisVAPI.runAndWait()
		
	def JarvisVoiceTellTime(self) :
		self.JarvisVAPI.say(strftime("The current time is %a, %d %b %Y %H:%M:%S \n", gmtime()))
		self.JarvisVAPI.runAndWait()
		
	def JarvisWelcomeHelpAudio(self) :
		self.JarvisVAPI.say("%s" %(Jarvis.JarvisHelp.JF))
		self.JarvisVAPI.runAndWait()
		
	def JarvisHelpUIAudio(self) :
		self.JarvisVAPI.say("Enter your choice from the list above.")
		self.JarvisVAPI.say("Usage. For example to request help on interacting with Jarvis, press 1 . ")
		self.JarvisVAPI.runAndWait()
		
	def JarvisHelpDialogue(self) :
		self.JarvisVAPI.say("%s" %(Jarvis.JarvisMainVar.JD1))
		self.JarvisVAPI.say("%s" %(Jarvis.JarvisMainVar.JD2))
		self.JarvisVAPI.say("%s" %(Jarvis.JarvisMainVar.JD3))
		self.JarvisVAPI.runAndWait()
		
	def JarvisHiddenCom(self) :
		self.JarvisVAPI.say("Heh, you will have to try allsorts of hidden keywords. Goodluck!")
		self.JarvisVAPI.runAndWait()
		
	def JarvisRenameAudio(self) :
		self.JarvisVAPI.say("Why would you want to rename me?")
		self.JarvisVAPI.say("But, since you requested to rename me, you can!")
		self.JarvisVAPI.runAndWait()
		
	def BotRenameAudio(self) :
		self.JarvisVAPI.say("Type the name you would like to rename me to. ")
		self.JarvisVAPI.runAndWait()
	
	def BotRenameSuccess(self) :
		self.JarvisVAPI.say("I have successfully been renamed!")
		self.JarvisVAPI.say("But i'm not so sure that i like my new name!")
		self.JarvisVAPI.runAndWait()
		
	def JarvisHelpAudio(self) :
		self.JarvisVAPI.say("Welcome to the help menu.")
		self.JarvisVAPI.say("To select an option simply enter the number that it's allocated to.")
		self.JarvisVAPI.runAndWait()
		
	def JarvisERROR(self) :
		self.JarvisVAPI.say("Input not recognized! ")
		self.JarvisVAPI.runAndWait()
		
	def JarvisHelpERROR(self) :
		self.JarvisVAPI.say("Hey, i did not find that requested help function in my database.")
		self.JarvisVAPI.say("Can you try again for me? Make sure the number you chose is valid.")
		self.JarvisVAPI.say("Thank you!")
		self.JarvisVAPI.runAndWait()
		
	def JarvisEmpty(self) :
		self.JarvisVAPI.say("I don't respond to empty spaces.")
		self.JarvisVAPI.runAndWait()
		
		
		
		
		

	