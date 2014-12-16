import os
import contextlib
import platform


def check():
	return ok.ping('virtualenv --version')

def install():
	ok.pip('install virtualenv')

@contextlib.contextmanager
def run(path):
	try:
		path = utils.normalize_path(path)

		# Check if our virtual environment is already created, and create if not
		ok.log('Checking virtual environment')
		if not os.path.isdir(path):
			ok.log('Creating virtual environment at {}...'.format(os.path.basename(path)))
			ok.shell('virtualenv {}'.format(path), force_global=True)

		ok._env = utils.normalize_path('{}/{}'.format(path, 'Scripts' if platform.system() == 'Windows' else 'bin'))
		yield
	finally:
		ok._env = None
