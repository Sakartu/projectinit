import os
import shutil

def remove_dir_prefix(fullpath, prefix):
	'''
	if fullpath starts with prefix, remove the prefix and any 
	remaning leading path separators
	'''
	if fullpath.startswith(prefix):
		result = fullpath[len(prefix):]
		while result.startswith(os.path.sep):
			result = result[1:]
		return result
	else:
		return fullpath

def find_template(templatedir, wanted):
	'''
	A method to locate a wanted template in the templatedir
	'''

	targetdir = ''
	template = ''

	if os.path.isdir(templatedir):
		for t in os.listdir(templatedir):
			if t == wanted:
				template = os.path.join(templatedir, t)
				targetdir = os.path.abspath('.')
	else: 
		print('Template directory {0} did not exist, exitting'.format(TEMPLATE_HOME))

	return (targetdir, template)

def setup_project(template, templatedir, targetdir):
	sourcedir = os.path.abspath(os.path.join(templatedir, template))
	for dirpath, dirname, filenames in os.walk(sourcedir):
		#first create dirs if they aren't available
		reldir = remove_dir_prefix(dirpath, sourcedir)
		newdir = os.path.join(targetdir, reldir)
		os.makedirs(newdir, exist_ok=True)
		#now we have directories, let's copy files
		for f in filenames:
			shutil.copy(os.path.join(dirpath, f), newdir)
