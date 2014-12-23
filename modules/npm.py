'''A package manager for Node

Website: https://www.npmjs.com/

Run any regular NPM command.
'''

def check():
	return ok.ping('npm --version')

def install():
	ok.node('--version')  # NPM is bundled with Node, so we can just ping it

def run(command):
	ok.shell('npm {}'.format(command))
	return ok
