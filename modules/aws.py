'''The AWS Command Line Interface (CLI)

Website: http://aws.amazon.com/cli/

Run any regular AWS CLI command.
'''

def check():
	return ok.ping('aws --version')

def install():
	raise utils.OkException('''Installation must be done manually.
Please visit http://aws.amazon.com/cli/ for installation instructions.''')

def run(command):
	ok.shell('aws {}'.format(command))
	return ok
