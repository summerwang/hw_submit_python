#!/usr/bin/python
# Copyright 2017 Ohio Supercomputer Center
# Summer Wang (xwang@osc.edu)

# This script is used by students to submit assignments into designated submission directory.
# Every use by the student deletes any previous submissions.
# Use: $path
# The size limit of one assignment submitted by each student is %size MB

def st_input():
	import getpass
	import os
	# Set the default values
	# Get the student's user name
	student = getpass.getuser()
	#Get all the input information from student
	print('Hello,', student)

	print('This script will submit your assignment for ***course to OSC.\nNote:\nBefore you run this script, please create one directory which includes all the files you want to submit.\nThe previous submission of the same assignment from you will be replaced by the new submission.')

	#$path_default: the current directory
        path_default = os.getcwd()
	print('Enter the name of assignment and press [ENTER]') 




#def submit_homework():

#return 

if __name__ == '__main__':
        stinput=st_input()
#        submit_homework(stinput)

