'''GNU Make

Website: http://www.gnu.org/software/make/

Run any regular Make command. You can also omit the command, which is the
same as simply running (b make).
'''

def check():
	return ok.ping('make --version')

def install():
	raise utils.OkException('''Installation must be done manually.
Please visit http://www.gnu.org/software/make/ for installation instructions.''')

def run(command=None):
	ok.shell('make{}'.format('' if command is None else " " + command))
	return ok
