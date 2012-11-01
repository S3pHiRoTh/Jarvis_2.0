"""
- Class Name : Jarvis Bot [2.0] [JarvisResponseDB]
- Class description : Data file that stores all the responses.
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh

"""

class JarvisResponse(object) :
	""" Jarvis Greeting responses class """
	
	# English Greeting
	Greeting_EN = "hello"
	Greeting_EN1 = "hi"
	Greeting_EN2 = "howdy"
	# Spanish Greeting
	Greeting_SPA = "hola"
	# German Greeting
	Greeting_GER = "hallo"
	# French Greeting
	Greeting_FRE = "bonjour"
	# Romanian Greeting
	Greeting_RO = "sal"
	# Islamic Greeting
	Greeting_ISL = "salaam"
	
class JarvisExitResponse(object) :
	""" Possible Bye keywords for Jarvis """
		
	# English Goodbye Diag
	Goodbye_EN = "goodbye"
	Goodbye_EN1 = "bye"
	Goodbye_EN2 = "cya"
	# Spanish Goodbye Diag
	Goodbye_SPA = "Adios"
	# French Goodbye Diag
	Goodbye_FRE = "au revoir"
	
	
class JarvisCommands(object) :
	""" Commands for Jarvis """
	
	# Load commands
	Load = "load"
	Load1 = "execute"
	
	# Help commands
	Help = "help"
	
	# Exit Commands
	Exit = "exit"
	Exit1 = "shutdown"
	Exit2 = "quit"
	
class JarvisEasterEggs(object) :
	""" Classified ^-^! """
	
	def EggBatchAlpha(self) :
		Egg = "creator"
	