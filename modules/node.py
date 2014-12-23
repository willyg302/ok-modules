'''Evented I/O for V8 JavaScript

Website: http://nodejs.org/

Run any regular Node command. You may also run a locally installed Node
module, for example Gulp, by passing (b module=True).
'''

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
