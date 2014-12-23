'''A convenience module for supporting (b pip freeze)

You may pass in a filename to freeze to. The default is requirements.txt
if no filename is provided.
'''

def check():
	return True  # This is automatically a pip feature

def install():
	pass

def run(filename='requirements.txt'):
	ok.pip('freeze > {}'.format(filename))
