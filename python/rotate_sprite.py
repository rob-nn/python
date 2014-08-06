# Read key
# Demonstrates reading the keyboard

from livewires import games


games.init(screen_width = 640, screen_height = 480, fps = 50)

class Ship(games.Sprite):

	""" A moving ship. """
	def update(self):
		""" Move ship based on keys pressed. """
		if games.keyboard.is_pressed(games.K_RIGHT):
			self.angle += 1
		if games.keyboard.is_pressed(games.K_LEFT):
			self.angle -= 1
		
		if games.keyboard.is_pressed(games.K_1):
			self.angle = 0
		if games.keyboard.is_pressed(games.K_2):
			self.angle = 90
		if games.keyboard.is_pressed(games.K_3):
			self.angle = 180
		if games.keyboard.is_pressed(games.K_4):
			self.angle = 270


def main():
	nebula_image = games.load_image("nebula.jpg")
	games.screen.background = nebula_image

	ship_image = games.load_image("ship.png")
	the_ship = Ship(image = ship_image, 
			x = games.screen.width/2, 
			y = games.screen.height/2)
	games.screen.add(the_ship)
	
	games.screen.mainloop()

main()

