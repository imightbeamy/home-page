#!/usr/bin/python

import pystache
import yaml
import os
import time
from csscompressor import compress

PROJECT_YAML = 'projects.yaml'
RESUME_YALM = 'resume.yaml'
ASSET_DIR = 'assets'
ART_DIR = ASSET_DIR + '/art'
DATA_FILE = lambda f: 'data/' + f
SRC_FILE = lambda f: 'src/' + f

PAGES = ['index', 'projects']

def render():
    projects = from_yaml(PROJECT_YAML)
    data = {
        'assets': ASSET_DIR,
        'month': time.localtime().tm_mon,
        'year': time.localtime().tm_year,
        'projects': [p for p in projects if p.get('featured', False)],
        'all_projects': projects,
        'resume': from_yaml(RESUME_YALM),
        'art': art(),
        'css': css()
    }
    for page_file in PAGES:
        tpl = open(SRC_FILE(page_file + '.mustache'), 'r').read()
        rendered = pystache.render(tpl, data)
        open(page_file + '.html', 'w').write(rendered)

def css():
    return compress(open(SRC_FILE('main.css'), 'r').read())

def from_yaml(file):
    return yaml.load(open(DATA_FILE(file),'r').read())

def art():
    images = filter(lambda f: f != "small" and f[0] != '.', os.listdir(ART_DIR))
    return [ {'image': i} for i in images ]

render()
