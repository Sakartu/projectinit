#!/usr/bin/env python3

import sys
import os
import shutil
import optparse
import subprocess
from glob import glob

TEMPLATE_HOME = '~/.templates'
init_git = False
wanted = ''

def main():
	args = parse_args()
	if len(args) < 1:
		usage()
	
	wanted = args[0]

	templatedir = os.path.expanduser(TEMPLATE_HOME)
	targetdir = ''
	template = ''
	if os.path.isdir(templatedir):
		for t in os.listdir(templatedir):
			if t == wanted:
				template = os.path.join(templatedir, t)
				targetdir = os.path.abspath('.')
	else: 
		print('Template directory {0} did not exist, exitting'.format(TEMPLATE_HOME))

	if len(template) > 0: 
		print('Setting up a {0} project...'.format(wanted))
		sourcedir = os.path.abspath(os.path.join(templatedir, template))
		for dirpath, dirname, filenames in os.walk(sourcedir):
			#first create dirs if they aren't available
			reldir = remove_dir(dirpath, sourcedir)
			newdir = os.path.join(targetdir, reldir)
			os.makedirs(newdir, exist_ok=True)
			#now we have directories, let's copy files
			for f in filenames:
				shutil.copy(os.path.join(dirpath, f), newdir)
	else:
		print('No template available for {0}!'.format(wanted))
	
	if init_git:
		#we have to call 'git init' in the target dir
		git = ['git', 'init', targetdir]
		subprocess.call(git)

def remove_dir(fullpath, remove):
	if fullpath.startswith(remove):
		result = fullpath[len(remove):]
		while result.startswith(os.path.sep):
			result = result[1:]
		return result
	else:
		return fullpath

def parse_args():
	global init_git
	parser = optparse.OptionParser()
	parser.add_option('-g', '--git', action='store_true', dest="init_git") #to initialize a git repo after initting the project
	(options, args) = parser.parse_args()
	init_git = options.init_git
	return args

def usage():
	print('This tool will setup a project for a given language in the current directory')
	print('Usage: {0} <project language>'.format(sys.argv[0]))
	if os.path.isdir(os.path.expanduser(TEMPLATE_HOME)):
		print('Possible languages:')
		for template in os.listdir(os.path.expanduser(TEMPLATE_HOME)):
			print('\t{0}'.format(template))
	sys.exit(0)
	

if __name__ == '__main__':
	sys.argv.append('python')
	sys.argv.append('-g')
	main()