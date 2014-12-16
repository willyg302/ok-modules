def check():
	return ok.ping('npm --version')

def install():
	raise OkException('''Installation must be done manually.
Please visit http://nodejs.org/ for installation instructions.''')

def run(command):
	ok._shell('npm {}'.format(command))
	return ok
