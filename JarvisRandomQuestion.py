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
import Jarvis
# Possible inputs for the random question

def Random_quest() :
	Rand_question_ReplyTRUE = ("y", "yeah", "yes", "yep", "sure", "alright", "of course", "go ahead")
	Rand_question_ReplyFALSE = ("n", "no", "you cant", "nope")
	Rand_question = raw_input("%s%s Hey %s i want to ask you a question, but it can be about anything! Can i ? : " %(BOT_NAME[0], BOT_MISC, un))
	if (str(Rand_question.lower())) in Rand_question_ReplyTRUE :
		print "%s%s Ok %s thanks! I will ask you a totally random question! \n" %(BOT_NAME[0], BOT_MISC, un)
		Random_questionINIT()
	elif (str(Rand_question.lower())) in Rand_question_ReplyFALSE :
		print "%s%s Aw, i had a super random question to ask you %s! \n" %(BOT_NAME[0], BOT_MISC, un)
		return Jarvis.UserResponse()
	else :
		"%s%s Erm, i didn't recognize that response! Please try again %s! " %(BOT_NAME[0], BOT_MISC, un)
	
def Random_questionINIT() :
	None
	