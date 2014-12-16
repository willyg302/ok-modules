def check():
	return ok.ping('make --version')

def install():
	raise utils.OkException('''Installation must be done manually.
Please visit http://www.gnu.org/software/make/ for installation instructions.''')

def run(command=None):
	ok.shell('make{}'.format('' if command is None else " " + command))
	return ok
