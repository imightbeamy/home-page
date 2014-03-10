#!/Users/amy/anaconda/bin/python

import pystache
import yaml
import os
import time

PROJECT_YAML = 'projects.yaml'
RESUME_YALM = 'resume.yaml'
ASSET_DIR = 'assets'
ART_DIR = ASSET_DIR + '/art'
DATA_FILE = lambda f: 'data/' + f

def render():
	data = {
                'assets': ASSET_DIR,
                'month': time.localtime().tm_mon,
                'year': time.localtime().tm_year,
		'projects': from_yaml(PROJECT_YAML),
		'resume': from_yaml(RESUME_YALM),
		'art': art(),
                'css': css()
	}
	tpl = open('homepage.mustache', 'r').read()
	rendered = pystache.render(tpl, data)
	open('index.html', 'w').write(rendered)

def css():
    return open('main.css', 'r').read()

def from_yaml(file):
	return yaml.load(open(DATA_FILE(file),'r').read())

def art():
	images = filter(lambda f: f != "small" and f[0] != '.', os.listdir(ART_DIR))
	return [ {'image': i} for i in images ]

render()
