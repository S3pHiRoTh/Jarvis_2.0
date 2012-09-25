"""
- Class Name : Jarvis Topics Class
- Class description : Class file that stores the topics that Jarvis will use.
- Language : Python
- Coded by : A.Taylor
- Coder Name : S3pHiRoTh

"""

# Import Nessesary framework
import random

# Import Specific framework
from time import gmtime, strftime

def JarvisTellTime() :
	print strftime("%a, %d %b %Y %H:%M:%S +0000 \n", gmtime())
	return 