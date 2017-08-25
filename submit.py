#!/usr/bin/python
# Copyright 2017 Ohio Supercomputer Center
# Summer Wang (xwang@osc.edu)

import sys
import os
import getpass
from pwd import getpwuid
from os import stat
from stat import *

def pi_input():
	# Set the default values
	#path_default is the default directory where the homework submission direcotry will be created
	#??Question: $path_default: home directory or current directory
	path_default = os.getcwd()
	#size_default is the default size limit of one homework submitted by each student, in MB (megabyte)
	size_default = '1000'
	#reply_default is no, which means only student receives email notification after his/her homework has been submitted
	reply_default = 'n'
	#Get the professor name
	professor = getpass.getuser()

	# Get all the input information from professor 
	print('Hello,', professor)

	print('Enter the absolute path where the submission direcotry of your assignments will be created.\nIt is suggested that the path points to the directory owned by you with right permissions.\nThe submission direcotry will be created within', path_default, 'if you simply press [ENTER]: ')
	path_pi = input('>>>')
	if path_pi == "":
		path_pi = path_default

	while not os.path.exists(path_pi):
		print('The path is not valid.\nEnter the absolute path where the submission direcotry will be created.\nThe submission direcotry will be created within', path_default, 'if you simply press [ENTER].\nEnter \'quit\' if you want to exit the program ')
		path_pi = input('>>>')
		if path_pi == "":
                	path_pi = path_default
		if path_pi == 'quit':
			print('You entered \'quit\' and will quit the program ...')
			sys.exit(11)
	
	owner_path_pi = getpwuid(stat(path_pi).st_uid).pw_name
	if owner_path_pi != professor: 
		print ('The directory %s is not owned by you.\nYou may have restricted permissions to create directries there. Please double check.\nEnter \'yes\' if you want to continue. Otherwise you will exit the program' %path_pi)
		answer = input('>>>')
		if answer != 'yes':
			print('You entered %s and will quit the program ...' %answer)
			sys.exit(12)
	
	print ('*****************************************************')
	print ('*** The submission directory of your assignments will be created under %s' % path_pi) 
	print ('*****************************************************')

	print('Enter the course number and press [ENTER]:')
	course_input = input('>>>')
	if course_input == "":
		print('Course number is empty. Exit.')
		sys.exit(21)
	course = course_input.upper()


	print('Enter the name of assignment and press [ENTER]: ')
	assign_input = input('>>>')
	if assign_input == "":
                print('Assignment name is empty. Exit.')
                sys.exit(31)
	assignment = assign_input.lower()

	path_pic = path_pi
	path_pic += '/Submissions/'
	path_pic += course
	path_pic +='/'
	path_pic += assignment
	destination = ''.join(path_pic)
	while os.path.exists(destination):
		print('%s exists.\nPlease provide a different assignment name or delete the current directory. Enter \'quit\' if you want to quit the program.' % destination)
		assign_input = input('>>>')
		if assign_input == "":
			print('Assignment name is empty. Exit.')
			sys.exit(31)
		if assign_input == 'quit':
			print('You entered \'quit\' and will quit the program ...')
			sys.exit(41)
		
		assignment = assign_input.lower()
		
		path_pic = path_pi
		path_pic += '/Submissions/'
		path_pic += course
		path_pic +='/'
		path_pic += assignment
		destination = ''.join(path_pic)	
			
	print ('*****************************************************')
	print ('*** You will create directory for Course %s, Assignment %s' % (course_input, assign_input))
	print ('*****************************************************')


	print('Enter the size limit of one assignment submitted by each student, in MB (megabyte). Integer only.\nThe size limit of one homework submitted by each student is', size_default, 'MB if you simply press [ENTER]: ')
	size = input('>>>')
	if size == "":
		size = size_default 
	while not size.isdigit():
		print ('Not Valid input.\nEnter the size limit of one assignment submitted by each student, in MB (megabyte). Integer only.\nFor example, for 1000 MB, enter 1000 and press [Enter].\nEnter \'quit\' if you want to exit the program ')
		size = input('>>>')
		if  size == 'quit':
			print('You entered \'quit\' and will quit the program ...')
			sys.exit(51)

	print ('*****************************************************')
	print ('*** The size limit of your assignment %s is %s MB' % (assign_input, size))
	print ('*****************************************************')



	print('The student will receive an email notification after he/she submits the homework.\nDo you want to get email notification, too [y/n]?')
	reply_email = input('>>>')
	if reply_email == "":
		reply_email = reply_default
	print ('*****************************************************')
	if reply_email == 'y':
		print('*** An email notification will be sent to both the student and your email after his/her homework has been submitted.')
	else:
		print('*** An email notification will be sent to the student after his/her homework has been submitted.')
	print ('*****************************************************')

	return path_pi, course, assignment, size, reply_email
	#return destination

def create_directory(input):
	professor = getpass.getuser()
	path_pi = input[0]
	head = path_pi
	while head != '/':
		owner_head = getpwuid(stat(head).st_uid).pw_name
		if owner_head is professor:
			os.chmod(head, os.stat(head).st_mode | S_IXGRP)
		head = os.path.split(head)[0]
		tail = os.path.split(head)[1]

	path_pi += '/Submissions/'
	submission_d = ''.join(path_pi)
	if not os.path.exists(submission_d):
		os.makedirs(submission_d)
		os.chmod(submission_d, 0o710)
	submission_d += input[1]
	submission_d +='/'
	course_d = ''.join(submission_d)
	if not os.path.exists(course_d):
		os.makedirs(course_d)
		os.chmod(course_d, 0o710)
	course_d += input[2]
	destination = ''.join(course_d)
	
	os.makedirs(destination)
	os.chmod(destination, 0o730)

	if os.path.exists(destination):
		print('')
		print('%s is created successfully.\nYour students can submit assignment to%s.'% (destination, destination))
		print('')

	else:
		print('')
		print('%s is not created.\nPlease check error message or contact oschelp@osc.edu for assistance. Exit' %destination)
		print('')
		sys.exit(101)


def create_submit(input):




if __name__=='__main__':
	profinput = pi_input()
	create_directory(profinput)
	create_submit(profinput)
