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
		
	def JarvisHelpAudio(self) :
		self.JarvisVAPI.say("help!")
		self.JarvisVAPI.runAndWait()
		
	def JarvisERROR(self) :
		self.JarvisVAPI.say("Input not recognized! ")
		self.JarvisVAPI.runAndWait()
		
		
		
		

	