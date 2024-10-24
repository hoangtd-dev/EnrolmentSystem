from .base.base_system import BaseSystem

from .enums.notification_type_enum import NotificationTypeEnum
from .enums.file_status_enum import FileStatusEnum

from .core.utils import (
	show_cli_notification
)

class CliEnrolmentSystem(BaseSystem):
	def run(self):
		self.load_data()
		self.__system_menu()

	# MENU SECTION
	def __system_menu(self):
		while self._is_active:
			selected_option = input('University System: (A)dmin, (S)tudent, or X: ')
			self.__handle_system_menu_option(selected_option)

	def __handle_system_menu_option(self, selected_option):
			match selected_option.lower():
				case 'a':
					self.__admin_menu()
				case 's':
					self.__student_menu()
				case 'x':
					self.update_active_status(False)
					show_cli_notification(NotificationTypeEnum.Warning, 'Thank You')
				case _:
					show_cli_notification(NotificationTypeEnum.Warning, 'Please input a/s/x only')

	def __admin_menu(self):
		is_loop = True
		while is_loop:
			selected_option = input('Admin System (c/g/p/r/s/x): ')
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
				pass
			case _:
				show_cli_notification(NotificationTypeEnum.Warning, 'Please input c/g/p/r/s/x only')

	def __student_menu(self):
		is_loop = True
		while is_loop:
			selected_option = input('Student System (l/r/x): ')
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
				show_cli_notification(NotificationTypeEnum.Warning, 'Please input l/r/x only')

	def __student_course_menu(self):
		is_loop = True
		while is_loop:
			selected_option = input('Student Course Menu (c/e/r/s/x): ')
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
				show_cli_notification(NotificationTypeEnum.Warning, 'Please input c/e/r/s/x only')
	# END MENU SECTION


	# SAVE AND LOAD DATA SECTION
	def load_data(self):
		file_response = self.read_file()
		if file_response.get_status() == FileStatusEnum.ERROR:
			show_cli_notification(NotificationTypeEnum.Error, file_response.get_error())
	
	def save_changes(self):
		file_response = self.write_file(self._students)

		if file_response.get_status() == FileStatusEnum.SUCCESS:
			self.load_data()
		else:
			show_cli_notification(NotificationTypeEnum.Error, file_response.get_error())
	# END SAVE AND LOAD DATA SECTION

	def __handle_register(self):
		email = input("Email: ")
		password = input("Password: ")

		if not self.is_password_valid(password) or not self.is_email_valid(email):
			print("Incorrect email or password format.")
			return

		if self.is_duplicate_email(email):
			print("This email is already registered.")
			return

		name = input("Name: ")
		self.register_student(name, email, password)
		self.save_changes()
		print("Registration successful.")

	def __handle_login(self):
		email = input("Email: ")
		password = input("Password: ")

		for student in self._students:
			if student.login(email, password):
				print("Login successful!")
				self._active_user = student  
				break

		if self._active_user:
			self.__student_course_menu() 
		else:
			print("Incorrect email or password.")

	def change_password(self):
		if self._active_user:
			while True:
				new_password = input("New Password: ")
				confirm_password = input("Confirm Password: ")
				if new_password != confirm_password:
					print("Passwords do not match - try again.")
					continue
				if not self.is_password_valid(new_password):
					print("Invalid password. Must be at least 8 characters and follow the password policy.")
					continue
				self._active_user.update_password(new_password)
				self.save_changes()
				print("Password updated successfully.")
				break
