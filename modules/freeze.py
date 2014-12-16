def check():
	return True  # This is automatically a pip feature

def install():
	pass

def run(filename='requirements.txt'):
	ok.pip('freeze > {}'.format(filename))
