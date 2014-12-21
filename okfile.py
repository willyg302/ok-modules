import os
import json


project = 'ok Modules'

def install():
	pass

def default():
	'''Rebuild the registry'''
	with open('registry.json', 'w') as f:
		json.dump(sorted(os.listdir('modules')), f)
