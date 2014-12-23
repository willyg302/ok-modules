'''A package manager for the web

Website: http://bower.io/

Run any regular Bower command. You may also specify a (b root) directory to
run Bower from, in case your bower.json lives elsewhere.
'''

def check():
	return ok.ping('bower --version')

def install():
	ok.npm('install -g bower')

def run(command, root='.'):
	with ok.root(root):
		ok.shell('bower {}'.format(command))
	return ok
