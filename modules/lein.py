def check():
	return ok.ping('lein --version')

def install():
	# @TODO: You CAN install lein automatically, it'll just be messy
	raise utils.OkException('''Installation must be done manually.
Please visit http://leiningen.org/ for installation instructions.''')

def run(command):
	ok.shell('lein {}'.format(command))
	return ok
