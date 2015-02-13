'''A Java software project management and comprehension tool

Website: http://maven.apache.org/

Run any regular Maven command.
'''

def check():
	return ok.ping('mvn --version')

def install():
	raise utils.OkException('''Installation must be done manually.
Please visit http://maven.apache.org/ for installation instructions.''')

def run(command):
	ok.shell('mvn {}'.format(command))
	return ok
