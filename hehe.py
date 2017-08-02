# 1.	Create a python program/method that takes any four numbers as arguments and adds them together.

# 2.	Create a python program/method that takes any name as an argument and prints “Yes” if the name has more than 20 characters (tip – you will need to find out the length of the name by using a python method like .length eg. name.length > 20)

# 3.	Create a python program/method that takes a name as an argument and insults you only if your name is “Bob” (tip – you will need an if clause or you can even use a ternary operator if you’re ultra clever)

# 4.	Create a python program/method that takes an array as an argument and finds the lowest number in the array (tip – you will need to find the method in python that finds the lowest number in an array – use Google!)



#1.

def addNumbers(a, b, c, d):
	return a + b + c + d

#2. 

def countdigits(name):
	if len(name) > 20:
		return true
	else:
		return false
		
#3. 
def insult(name):
	if name == "bob":
		return "he sucks"
	else:
		return "cool
		
		
def insult(name):
	name == "bob" ? "he sucks" : null
		
		
# 4.
def minArrayFinder(array):
	return min(array)
