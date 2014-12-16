import os
import shutil
import tempfile
import urllib

def check():
	return ok.ping('pip --version')

def install():
	with ok_directory():  # This has to be done relative to ok.py
		tmpdir = None
		try:
			# Create a temporary working directory
			tmpdir = tempfile.mkdtemp()
			get_pip = os.path.join(tmpdir, 'get-pip.py')

			# Download get-pip.py and run it
			urllib.urlretrieve('https://bootstrap.pypa.io/get-pip.py', get_pip)
			ok._shell('python {}'.format(get_pip))
		finally:
			# Clean up our temporary working directory
			if tmpdir:
				shutil.rmtree(tmpdir, ignore_errors=True)

def run(command):
	ok._shell('pip {}'.format(command))
	return ok
