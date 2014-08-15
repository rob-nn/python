# Handle It
# Demonstrates handling exceptions

# try/except
try:
	num = float(input("Enter a number: "))
except ValueError:
	print("That was not a number!")


# handle multiple exception types
print()
for value in (None, "Hi!"):
	try:
		print("Attempting to convert", value, "-->", end=" ")
		print(float(value))
	except TypeError:
		print("I can only convert a string or a number!")
	except ValueError:
		print("I can only convert a string of digits!")

# try/except/else
try:
	num = float(input("\nEnter a number: "))
except ValueError:
	print("That was not a number!")
else:
	print("You entered the number", num)
input("\n\nPress the enter key to exit.")
