#password generator

import string
from random import *
length = int(input('How many characters do you want your password to be? \n'))
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(length))
print (password)

