def check():
	return ok.ping('node --version')

def install():
	raise utils.OkException('''Installation must be done manually.
Please visit http://nodejs.org/ for installation instructions.''')

def run(command, module=False):
	if module:
		ok.shell('node_modules/.bin/{}'.format(command))
	else:
		ok.shell('node {}'.format(command))
	return ok
