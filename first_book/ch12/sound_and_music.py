# Sound and Music
# Demonstrates playing sound and music files

from livewires import games


games.init(screen_width = 640, screen_height = 480, fps = 50)

# load a sound file
missile_sound = games.load_sound("missile.wav")

# load music file

games.music.load("theme.mid")

choice = None

while choice != "0":
	print(
		"""
		Sound a Music

		0 - Quit
		1 - Play missile sound
		2 - Loop missile sound
		3 - Stop missile Sound
		4 - Play them music
		5 - Loop them music 
		6 - Stop them music
		"""
		)


	choice = str(input("Choice: "))
	print()

	# exit
	if choice =="0":
		print("Good-bye.")

	# play missile sound
	elif choice == "1":
		missile_sound.play()
	elif choice == "2":
		loop = int(input("Loop how many extra times? (-1 = forever): "))
		missile_sound.play(loop)
		print("Looping missile sound.")
	# stop missile sound
	elif choice == "3":
		missile_sound.stop()
		print("Stopping missile sound.")
	# play them music
	elif choice == "4":
		games.music.play()
		print("Playing them music.")

	# loop theme music
	elif choice == "5":
		loop = int(input("Loop how many extra times? (-1 = forever): "))
		games.music.play(loop)
		print("Looping them music.")
	# stop them music
	elif choice == "6":
		games.music.stop()
		print("Stopping them music.")

	#some unknown choice
	else:
		print("\nSorry, bout", choice, "isn't a valide choice.")

input("\n\nPree the enter key to exit.")		
