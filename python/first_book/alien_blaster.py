# Allien Blaster
# Demonstrates object interaction

class Player(object):
	""" A player in a shooter game. """
	def blast(self, enemy):
		print("The player blasts an enemy.\n")
		enemy.die()

class Alien(object):
	"""An alien in a shooter game."""
	def die(self):
		print("The alien gasps and says. 'Oh, this is it. Thisis the big one.\n"\
			"yes, it's getting dark now. Tem my 1.6 million larvae that I loved them...\n"\
			"Good-bye, cruel universe.'")	
# main
print("\t\tDeath of an Alien\n")

hero = Player()
invader= Alien()
hero.blast(invader)

input("\n\nPress enter key to exit.")
