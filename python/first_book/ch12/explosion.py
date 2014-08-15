# Explosion
# Demonstrates creating an animation

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

nebula_image = games.load_image("nebula.jpg", transparent = 0)
games.screen.background = nebula_image

explosion_files = ["explosion1.png",
		"explosion2.png",
		"explosion3.png",
		"explosion4.png",
		"explosion5.png",
		"explosion6.png",
		"explosion7.png",
		"explosion8.png",
		"explosion9.png"]

explosion = games.Animation(images = explosion_files,
		x = games.screen.width/2,
		y = games.screen.height/2,
		n_repeats = 0,
		repeat_interval = 5)

games.screen.add(explosion)


games.screen.mainloop()
