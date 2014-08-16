def say_hello():
	import pdb; pdb.set_trace()
	name = raw_input('Say your name, broo: ')
	print("Hello World %s"%name)
	bro(name)


def bro(name):
	print('Hi Broo, %s'%name)


if __name__=="__main__":
	say_hello()
