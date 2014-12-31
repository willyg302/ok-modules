'''Go SDK for Google App Engine

Website: https://cloud.google.com/appengine/docs/go/

Run any regular App Engine Go SDK command.
'''

def check():
	return ok.ping('goapp version')

def install():
	raise utils.OkException('''Installation must be done manually.
Please visit https://cloud.google.com/appengine/docs/go/
for installation instructions.''')

def run(command):
	ok.shell('goapp {}'.format(command))
	return ok
