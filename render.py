#!/Users/amy/anaconda/bin/python

import pystache
import yaml
import os
import time
from csscompressor import compress

PROJECT_YAML = 'projects.yaml'
NEW_PROJ_NUMBER = 4
RESUME_YALM = 'resume.yaml'
ASSET_DIR = 'assets'
ART_DIR = ASSET_DIR + '/art'
DATA_FILE = lambda f: 'data/' + f
SRC_FILE = lambda f: 'src/' + f

def render():
	projects = from_yaml(PROJECT_YAML)
	data = {
        'assets': ASSET_DIR,
        'month': time.localtime().tm_mon,
        'year': time.localtime().tm_year,
		'projects': projects[:NEW_PROJ_NUMBER],
		'old_projects': projects[NEW_PROJ_NUMBER:],	
		'resume': from_yaml(RESUME_YALM),
		'art': art(),
        'css': css()
	}
	tpl = open(SRC_FILE('homepage.mustache'), 'r').read()
	rendered = pystache.render(tpl, data)
	open('index.html', 'w').write(rendered)

def css():
    return compress(open(SRC_FILE('main.css'), 'r').read())

def from_yaml(file):
	return yaml.load(open(DATA_FILE(file),'r').read())

def art():
	images = filter(lambda f: f != "small" and f[0] != '.', os.listdir(ART_DIR))
	return [ {'image': i} for i in images ]

render()
