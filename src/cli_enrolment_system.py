from .base.base_system import BaseSystem

from .enums.notification_type_enum import NotificationTypeEnum

from .core.utils import (
	show_cli_notification
)

class CliEnrolmentSystem(BaseSystem):
	def run(self):
		self.__system_menu()

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
					show_cli_notification(NotificationTypeEnum.Warning, 'Thank You', is_template_included=False)
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
				pass
			case 'r':
				pass
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
				pass
			case 'e':
				pass
			case 'r':
				pass
			case 's':
				pass
			case 'x':
				pass
			case _:
				show_cli_notification(NotificationTypeEnum.Warning, 'Please input c/e/r/s/x only')

