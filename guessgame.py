import random

class guissingame():
	global guess
	guess = input("guess the number between 1-10:\n")

	def __init__(self):
		self.rand_choise = random.randint(0,10)		#rand_choise save the random integer

	# Method for resetting random number
	def reset_random(self):
		print("Resseting random number!!")
		self.rand_choise = random.randint(0,10)

	def userguess(self):
		
		if guess == self.rand_choise:
			print("you are right!!")
		else:
			print("sorry!! try again!!")
			print("number is: {}".format(self.rand_choise))


g = guissingame()
g.userguess()
g.reset_random()