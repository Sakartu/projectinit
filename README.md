projectinit
===========

This is a little tool that can be used to initialize projects for a given programming language in the current working directory.

Configuration
=============

There is very little configuration required:

- First of all, make sure projectinit.py is in your PATH somewhere
- Create a .templates directory in your homedirectory
- Fill the .templates directory with templates. Each subdirectory of .templates is considered a template for a different programming language. For instance, if you have .templates/python and .templates/latex you can create projects in two languages, python and LaTeX. 
- Fill each of the subdirectories of .templates with the desired content. For instance, in python, provide a runnable main.py with some content, a README file and some of your favorite packages (don't forget __init__.py files!)
- Whenever you want to create a new project of a given language, create a directory for the project somewhere on the filesystem, cd into that directory and type "projectinit.py <language>" to setup the project. projectinit.py will copy all the necessary files from the .templates directory to your working directory. So, if I want to start a python project called "foobar", the following commands will do the trick:

> $ mkdir foobar  
> $ cd foobar  
> $ projectinit python  

Extra options
=============
projectinit provides the following extra options:

git init
--------

projectinit can create a new git repository for you after it has setup the template. Just add the -g option.

Different template directory
----------------------------

If you don't like the default template directory location, you can either symlink another dir on your fs as ~/.templates or you can change the TEMPLATE_HOME configuration parameter in projectinit.py

