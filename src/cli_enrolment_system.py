from .base.base_system import BaseSystem
from termcolor import colored

from .enums.file_status_enum import FileStatusEnum

class CliEnrolmentSystem(BaseSystem):
	def __init__(self):
		super().__init__()
		self._tab_indent = ' '*4 

	def run(self):
		self.load_data()
		self.__system_menu()

	# MENU SECTION
	def __system_menu(self):
		while self._is_active:
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
			selected_option = input(colored(self._tab_indent + 'Admin System (c/g/p/r/s/x): ', 'blue'))
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
				print(colored('Please input c/g/p/r/s/x only', 'yellow'))

	def __student_menu(self):
		is_loop = True
		while is_loop:
			selected_option = input(colored(self._tab_indent + 'Student System (l/r/x): ', 'blue'))
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
				print(colored('Please input l/r/x only', 'yellow'))

	def __student_course_menu(self):
		is_loop = True
		while is_loop:
			selected_option = input(colored(self._tab_indent * 2 + 'Student Course Menu (c/e/r/s/x): ', 'blue'))
			self.__handle_student_course_menu_option(selected_option)

			if selected_option.lower() == 'x':
				is_loop = False

	def __handle_student_course_menu_option(self, selected_option):
		match selected_option.lower():
			case 'c':
				self.change_password()
			case 'e':
				pass
			case 'r':
				pass
			case 's':
				pass
			case 'x':
				self.logout()
			case _:
				print(colored('Please input c/e/r/s/x only', 'yellow'))
	# END MENU SECTION

	# SAVE AND LOAD DATA SECTION
	def load_data(self):
		file_response = self.read_file()
		if file_response.get_status() == FileStatusEnum.ERROR:
			print(colored(file_response.get_error(), 'red'))
	
	def save_changes(self):
		file_response = self.write_file(self._students)

		if file_response.get_status() == FileStatusEnum.SUCCESS:
			self.load_data()
		else:
			print(colored(file_response.get_error(), 'red'))
	# END SAVE AND LOAD DATA SECTION

	def __handle_register(self):
		print(colored(self._tab_indent + 'Student Sign Up', 'green'))
		while True:
			email = input(self._tab_indent + "Email: ")
			password = input(self._tab_indent + "Password: ")

			if not self.is_password_valid(password) or not self.is_email_valid(email):
				print(colored(self._tab_indent + "Incorrect email or password format", 'red'))
				continue
			else:
				print(colored(self._tab_indent + "email and password formats acceptable", 'yellow'))

			duplicate_name = self.check_duplicate_email(email)
			if duplicate_name:
				print(colored(self._tab_indent + f"Student {duplicate_name} already exists", 'red'))
				continue

			name = input(self._tab_indent + "Name: ")
			self.register_student(name, email, password)
			self.save_changes()
			print(colored(self._tab_indent + f"Enrolling Student {name}", 'yellow'))
			break

	def __handle_login(self):
		print(colored(self._tab_indent + 'Student Sign In', 'green'))
		while True:
			email = input(self._tab_indent + "Email: ")
			password = input(self._tab_indent + "Password: ")

			for student in self._students:
				if student.login(email, password):
					self._active_user = student  
					break

			if self._active_user:
				self.__student_course_menu() 
			else:
				print("Incorrect email or password.")
			break

	def __handle_admin_login(self):
		self._active_user = self._admin

	def change_password(self):
		if self._active_user:
			print(colored(self._tab_indent * 2 + "Updating Password", "yellow"))
			while True:
				new_password = input(self._tab_indent * 2 + "New Password: ")
				if not self.is_password_valid(new_password): 
					print(colored(self._tab_indent * 2 + "Incorrect password", 'red'))
					continue

				while True:
					confirm_password = input(self._tab_indent * 2 + "Confirm Password: ")
					
					if new_password != confirm_password:
						print(colored(self._tab_indent * 2 + "Passwords does not match - try again", 'red'))
						continue
					
					break

				self._active_user.update_password(new_password)
				self.save_changes()
				break