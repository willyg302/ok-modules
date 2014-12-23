'''The Elixir build tool

Website: http://elixir-lang.org/docs/stable/mix/

Run any regular Mix command.
'''

def check():
	return ok.ping('mix --version')

def install():
	# @TODO: You CAN install Elixir automatically (see below), it'll just be messy
	raise utils.OkException('''Installation must be done manually.
Please visit http://elixir-lang.org/ for installation instructions.''')

def run(command):
	ok.shell('mix {}'.format(command))
	return ok


"""
def install_erlang_deps_ubuntu():
	'''Ubuntu: Install Erlang dependencies'''
	deps = [
		'build-essential',
		'libncurses5-dev',
		'openssl',
		'libssl-dev',
		'fop',
		'xsltproc',
		'unixodbc-dev'
	]
	strap.run('apt-get install {}'.format(' '.join(deps)))

def install_erlang_ubuntu():
	'''Ubuntu: Install Erlang'''
	with strap.root('/usr/bin'):
		strap.run([
			'wget http://erlang.org/download/otp_src_17.1.tar.gz',
			'tar -xzvf otp_src_17.1.tar.gz'
		])
		with strap.root('otp_src_17.1'):
			strap.run('./configure').make().make('install')

def install_elixir_ubuntu():
	'''Ubuntu: Install Elixir'''
	with strap.root('/usr/bin'):
		strap.run('git clone https://github.com/elixir-lang/elixir')
		with strap.root('elixir'):
			strap.run('git checkout v1.0.0').make().make('install')
"""
