'''The Cross-platform Toolkit

Website: http://haxe.org/

Run any regular Haxe command.
'''

def check():
	return ok.ping('haxe -version')

def install():
	raise utils.OkException('''Installation must be done manually.
Please visit http://haxe.org/ for installation instructions.''')

def run(command):
	ok.shell('haxe {}'.format(command))
	return ok
