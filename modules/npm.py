def check():
	return ok.ping('npm --version')

def install():
	raise utils.OkException('''Installation must be done manually.
Please visit http://nodejs.org/ for installation instructions.''')

def run(command):
	ok.shell('npm {}'.format(command))
	return ok
