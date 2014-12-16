def check():
	return ok.ping('bower --version')

def install():
	ok.npm('install -g bower')

def run(command, root='.'):
	with ok.root(root):
		ok.shell('bower {}'.format(command))
	return ok
