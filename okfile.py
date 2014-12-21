import os
import json


project = 'ok Modules'

def install():
	pass

def default():
	'''Rebuild the registry'''
	with open('registry.json', 'w') as f:
		json.dump(sorted([m[:-3] for m in os.listdir('modules')]), f)
