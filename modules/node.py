def check():
	return ok.ping('node --version')

def install():
	raise OkException('''Installation must be done manually.
Please visit http://nodejs.org/ for installation instructions.''')

def run(command, module=False):
	if module:
		ok._shell('node_modules/.bin/{}'.format(command))
	else:
		ok._shell('node {}'.format(command))
	return ok
