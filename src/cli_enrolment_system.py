from .base.base_system import BaseSystem
from termcolor import colored

from .enums.file_status_enum import FileStatusEnum
from .entities.subject import Subject
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
				self.__handle_clear_students()
			case 'g':
				self.__handle_group_students()
			case 'p':
				self.__handle_partition_students()
			case 'r':
				student_id = input(self.__tab_indent + "Remove by ID: ")
				self.__handle_remove_students(student_id)
			case 's':
				self.__handle_show_students()
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
	
	def __handle_clear_students(self):
		print(colored(self.__tab_indent + "Clearing students database", 'yellow'))
		while True:
			userInput = input(colored(self.__tab_indent + "Are you sure you want to clear the database (Y)ES/(N)0: ", 'red'))
			match userInput.lower():
				case 'y':
					self.update_students([])
					self.save_changes() 
					print(colored(self.__tab_indent + "Students data cleared", 'yellow'))
					break
				case 'n':
					break
				case _:
					print(colored(self.__tab_indent + "Invalid input. Please enter 'Y' or 'N' only.", 'red'))

	def __handle_show_students(self):
		print(colored(self.__tab_indent + "Student List", 'yellow'))
		students = self.get_students()
		if students:
			for student in students:
				print(self.__tab_indent + f"{student.get_name()} : : {student.get_id()} --> Email: {student.get_email()}")
		else:
			print(self.__tab_indent * 2 + "< Nothing to display >")
	
	def __handle_group_students(self):
		print(colored(self.__tab_indent + "Grade Grouping", 'yellow'))
		students = self.get_students()
		group_list = {
			'Z': [],
			'P': [],
			'C': [],
			'D': [],
			'HD': []
		}
		if students:
			for student in students:
				avg_grade = student.calculate_average_mark()
				grade_type = Subject.get_classify_grade(avg_grade)
				grade_group = group_list.get(grade_type)

				grade_group.append(f'{student.get_name()} :: {student.get_id()} --> GRADE: {grade_type} - MARK: {avg_grade:.2f}')
		
		if not students:
			print(self.__tab_indent * 2 + "< Nothing to display >")
		else:
			for key in group_list.keys():
				if len(group_list[key]) > 0:
					print(self.__tab_indent + f"{key} ---> [{', '.join(group_list[key])}]")
	
	def __handle_partition_students(self):
		print(colored(self.__tab_indent + "PASS/FAIL Partition", 'yellow'))
		students = self.get_students()
		pass_fail = {"PASS": [], "FAIL": []}

		for student in students:
			avg_grade = student.calculate_average_mark()
			grade_type = Subject.get_classify_grade(avg_grade)
			if avg_grade >= 50:
				pass_fail["PASS"].append((student, grade_type, avg_grade))
			else:
				pass_fail["FAIL"].append((student, grade_type, avg_grade))
		
		for category, student_list in pass_fail.items():
			student_details = [
                f"{student.get_name()} :: {student.get_id()} --> GRADE: {grade_type} - MARK: {avg_grade}"
                for student, grade_type, avg_grade in student_list
            ]
			print(self.__tab_indent + f"{category} --> [{', '.join(student_details)}]")


	def __handle_remove_students(self, student_id):
		students = self.get_students()  # Get the current list of students
		student_remove = next((s for s in students if s.get_id() == student_id), None)
		
		if student_remove:
			updated_students = [s for s in students if s.get_id() != student_id] # Create a new list of students excluding the one to be removed
			self.update_students(updated_students)
			self.save_changes()
		
			print(colored(self.__tab_indent + f"Removing Student {student_id} Account", 'yellow'))
			
		else:
			print(colored(self.__tab_indent + f"Student {student_id} does not exist", 'red'))

        
