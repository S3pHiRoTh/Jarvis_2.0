"""
- Class Name : Jarvis Random question class file
- Class description : Thos class file calls the questions that jarvis may ask the user.
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh

"""
# Import framework
import random
from random import choice
# Possible inputs for the random question

class JarvisRandomQuestion(object) :
	""" Class for Jarvis to ask the user random questions. """
	def Random_quest(self) :
		Rand_question_ReplyTRUE = ("y", "yeah", "yes", "yep", "sure", "alright", "of course", "go ahead")
		Rand_question_ReplyFALSE = ("n", "no", "you cant", "nope")
		Rand_question = raw_input("Hey i want to ask you a question, but it can be about anything! Can i ? : ")
		if (str(Rand_question.lower())) in Rand_question_ReplyTRUE :
			print "%s%s Ok thanks, %s! I will ask you a totally random question! \n" %(Jarvis.JarvisMainVar.BOT_NAME[0], Jarvis.JarvisMainVar.MISC_BOT, Jarvis.JarvisMainVar.USER_NAME[0])
		elif (str(Rand_question.lower())) in Rand_question_ReplyFALSE :
			print "%s%s Aw, i had a super random question to ask you %s! \n" %(Jarvis.JarvisMainVar.BOT_NAME[0], Jarvis.JarvisMainVar.MISC_BOT, Jarvis.JarvisMainVar.USER_NAME[0])
			return Jarvis.UserResponse()
		else :
			"%s%s Erm, i didn't recognize that response! Please try again %s! " %(Jarvis.JarvisMainVar.BOT_NAME[0], Jarvis.JarvisMainVar.MISC_BOT, Jarvis.JarvisMainVar.USER_NAME[0])
		
	
