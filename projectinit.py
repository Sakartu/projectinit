#!/usr/bin/env python3

'''
projectinit is a small utility that can be used to setup
a project from a given project template in the current
working directory.

for more information, see the accompanied README.md file

'''
import sys
import os
import optparse
import subprocess
import projectinit_util as util

TEMPLATE_HOME = '~/.templates'
options = None
wanted = ''

usage = 'This tool will setup a project for a given language in the current directory\n' 
usage += 'Usage: {0} <project language>\n'.format(sys.argv[0]) 
if os.path.isdir(os.path.expanduser(TEMPLATE_HOME)):
	usage += 'Possible languages:\n'
	for template in os.listdir(os.path.expanduser(TEMPLATE_HOME)):
		usage += '\t{0}\n'.format(template)

def main():
	args = parse_args()
	if len(args) < 1:
		print(usage)
		sys.exit(0)
	
	wanted = args[0]

	templatedir = os.path.expanduser(TEMPLATE_HOME)
	(targetdir, template) = util.find_template(templatedir, wanted)

	if len(template) > 0: 
		print('Setting up a {0} project...'.format(wanted))
		util.setup_project(template, templatedir, targetdir)
	else:
		print('No template available for {0}!'.format(wanted))
		sys.exit(-1)
	
	if options.init_git:
		#we have to call 'git init' in the target dir
		git = ['git', 'init', targetdir]
		subprocess.call(git)
	elif options.init_mercurial: #we can only have one VCS
		#we have to call 'hg init' in the target dir
		hg = ['hg', 'init', targetdir]
		subprocess.call(hg)

def parse_args():
	global options
	parser = optparse.OptionParser(usage)
	parser.add_option('-g', '--git', action='store_true', dest="init_git", help="setup git after setting up the project") #to initialize a git repo after initting the project
	parser.add_option('-m', '--mercurial', action='store_true', dest="init_mercurial", help="setup mercurial after setting up the project") #to initialize a mercurial repo after initting the project

	(options, args) = parser.parse_args()

	return args

if __name__ == '__main__':
	main()
