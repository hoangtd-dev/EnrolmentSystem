from .base.base_system import BaseSystem
from termcolor import colored

from .enums.file_status_enum import FileStatusEnum
import random

class CliEnrolmentSystem(BaseSystem):
	def __init__(self):
		super().__init__()
		self.__tab_indent = ' '*4 

	def run(self):
		self.load_data()
		self.__system_menu()

	# MENU SECTION
	def __system_menu(self):
		while self.is_active():
			selected_option = input(colored('University System: (A)dmin, (S)tudent, or X: ', 'blue'))
			self.__handle_system_menu_option(selected_option)

	def __handle_system_menu_option(self, selected_option):
			match selected_option.lower():
				case 'a':
					self.__handle_admin_login()
					self.__admin_menu()
				case 's':
					self.__student_menu()
				case 'x':
					self.update_active_status(False)
					print(colored('Thank You', 'yellow'))
				case _:
					print(colored('Please input a/s/x only', 'yellow'))

	def __admin_menu(self):
		is_loop = True
		while is_loop:
			selected_option = input(colored(self.__tab_indent + 'Admin System (c/g/p/r/s/x): ', 'blue'))
			self.__handle_admin_menu_option(selected_option)

			if selected_option.lower() == 'x':
				is_loop = False

	def __handle_admin_menu_option(self, selected_option):
		match selected_option.lower():
			case 'c':
				pass
			case 'g':
				pass
			case 'p':
				pass
			case 'r':
				pass
			case 's':
				pass
			case 'x':
				self.logout()
			case _:
				print(colored(self.__tab_indent + 'Please input c/g/p/r/s/x only', 'yellow'))

	def __student_menu(self):
		is_loop = True
		while is_loop:
			selected_option = input(colored(self.__tab_indent + 'Student System (l/r/x): ', 'blue'))
			self.__handle_student_menu_option(selected_option)

			if selected_option.lower() == 'x':
				is_loop = False

	def __handle_student_menu_option(self, selected_option):
		match selected_option.lower():
			case 'l':
				self.__handle_login()
			case 'r':
				self.__handle_register()
			case 'x':
				pass
			case _:
				print(colored(self.__tab_indent + 'Please input l/r/x only', 'yellow'))
    
	def __student_course_menu(self):
		is_loop = True
		while is_loop:
			selected_option = input(colored(self.__tab_indent + 'Subject System (c/e/r/s/x): ', 'blue'))
			self.__handle_subject_menu_option(selected_option)
			
			if selected_option.lower() == 'x':
				is_loop = False

	def __handle_subject_menu_option(self, selected_option):
		match selected_option.lower():
			case 'e':
				self.__handle_enrolment()
			case 'r':
				self.__handle_remove_subject()
			case 's':
				self.__show_enrolled_subjects()
			case 'c':
				self.change_password()
			case 'x':
				self.logout()
			case _:
				print(colored(self.__tab_indent + 'Please input c/e/r/s/x only', 'yellow'))

	# END MENU SECTION

	# SAVE AND LOAD DATA SECTION
	def load_data(self):
		file_response = self.read_file()
		if file_response.get_status() == FileStatusEnum.ERROR:
			print(colored('Cannot load data from database', 'red'))
	
	def save_changes(self):
		file_response = self.write_file(self.get_students())

		if file_response.get_status() == FileStatusEnum.SUCCESS:
			self.load_data()
		else:
			print(colored('Cannot save data in database', 'red'))
	# END SAVE AND LOAD DATA SECTION

	def __handle_register(self):
		print(colored(self.__tab_indent + 'Student Sign Up', 'green'))
		while True:
			email = input(self.__tab_indent + "Email: ")
			password = input(self.__tab_indent + "Password: ")

			if not self.is_password_valid(password) or not self.is_email_valid(email):
				print(colored(self.__tab_indent + "Incorrect email or password format", 'red'))
				continue
			else:
				print(colored(self.__tab_indent + "email and password formats acceptable", 'yellow'))

			duplicate_name = self.check_duplicate_email(email)
			if duplicate_name:
				print(colored(self.__tab_indent + f"Student {duplicate_name} already exists", 'red'))
				break

			name = input(self.__tab_indent + "Name: ")
			self.register_student(name, email, password)
			self.save_changes()
			print(colored(self.__tab_indent + f"Enrolling Student {name}", 'yellow'))
			break

	def __handle_login(self):
		print(colored(self.__tab_indent + 'Student Sign In', 'green'))
		while True:
			email = input(self.__tab_indent + "Email: ")
			password = input(self.__tab_indent + "Password: ")
			
			if not self.is_password_valid(password) or not self.is_email_valid(email):
				print(colored(self.__tab_indent + "Incorrect email or password format", 'red'))
				continue
			else:
				print(colored(self.__tab_indent + "email and password formats acceptable", 'yellow'))

			students = self.get_students()
			for student in students:
				if student.login(email, password):
					self.update_active_user(student)  
					break

			if self.get_active_user():
				self.__student_course_menu() 
			else:
				print(colored(self.__tab_indent + "Student does not exist", 'red'))
			break

	def __handle_admin_login(self):
		self.update_active_user(self.get_admin())

	def change_password(self):
		active_user = self.get_active_user()

		if active_user:
			print(colored(self.__tab_indent * 2 + "Updating Password", "yellow"))
			while True:
				new_password = input(self.__tab_indent * 2 + "New Password: ")
				if not self.is_password_valid(new_password): 
					print(colored(self.__tab_indent * 2 + "Incorrect password", 'red'))
					continue

				while True:
					confirm_password = input(self.__tab_indent * 2 + "Confirm Password: ")
					
					if new_password != confirm_password:
						print(colored(self.__tab_indent * 2 + "Passwords does not match - try again", 'red'))
						continue
					
					break

				active_user.update_password(new_password)
				self.save_changes()
				break

	def __handle_enrolment(self):
		try:

			# Enroll the student in the subject, using the subject ID 
			active_user = self.get_active_user()
			subject_id = active_user.enrol_subject()
			self.save_changes()

			# Count how many subjects the student is enrolled in
			current_enrolment_count = len(active_user.get_enrolled_subjects())

			# Display the success message with the subject ID and current enrollment status
			print(colored(self.__tab_indent + f"Enrolling in Subject-{subject_id}", 'yellow'))
			print(colored(self.__tab_indent + f"You are now enrolled in {current_enrolment_count} out of 4 subjects", 'yellow'))

		except ValueError as e:
			print(colored(self.__tab_indent + str(e), 'red'))

	def __handle_remove_subject(self):
		subject_id = input(self.__tab_indent + "Remove subject by ID: ")
  		
    	# Check if the subject_id is a valid number
		if not subject_id.isdigit():
			print(colored(self.__tab_indent + "Invalid input. Please enter a valid subject ID number.", 'red'))
			return

		active_user = self.get_active_user()
		if active_user.remove_subject(subject_id):
			print(colored(self.__tab_indent + f"Dropping Subject-{subject_id}", 'yellow'))
			print(colored(self.__tab_indent + f"You are now enrolled in {len(active_user.get_enrolled_subjects())} out of 4 subjects", 'yellow'))
			self.save_changes()
		else:
			print(colored(self.__tab_indent + "Input subject ID not found", 'red'))

	def __show_enrolled_subjects(self):
		active_user = self.get_active_user()
		enrolled_subjects = active_user.get_enrolled_subjects()
		
		# Show the number of subjects
		subject_count = len(enrolled_subjects)
		print(colored(self.__tab_indent + f"Showing {subject_count} subjects", 'yellow'))

		if enrolled_subjects:
			# Display each enrolled subject with its mark and grade
			for enrolled_subject in enrolled_subjects:
				print(self.__tab_indent + f"[ Subject::{enrolled_subject.get_id()} -- mark = {enrolled_subject.get_mark()} -- grade = {enrolled_subject.get_grade()} ]")