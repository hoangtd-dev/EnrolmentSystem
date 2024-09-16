from .base.base_system import BaseSystem

from .enums.notification_type_enum import NotificationTypeEnum

from .core.utils import (
	get_custom_integer_input, 
	show_cli_notification
)
from .core.auth_utils import (
	check_email_valid, 
	check_password_valid
)

class CliEnrolmentSystem(BaseSystem):
	def run(self):
		show_cli_notification(NotificationTypeEnum.Info, 'Enrolment System started!')
		while self._is_active:
			self.__menu()
			selected_option = get_custom_integer_input('Your selection: ')
			self.__handle_option(selected_option)

	def __menu(self):
		print('1. Login')
		print('2. Register')
		print('3. Quit')

	def __handle_option(self, selected_option):
			match selected_option:
				case 1:
					self.__handle_login()
				case 2:
					print('Register processing')
				case 3:
					print('Enrolment system stopped!')
					self.update_active_status(False)
				case _:
					show_cli_notification(NotificationTypeEnum.Warning, 'Please input 1 or 2 only')

	def __handle_login(self):
		while True:
			email_input = input('Input email: ')
			password_input = input('Input password: ')

			if not check_email_valid(email_input) or not check_password_valid(password_input):
					show_cli_notification(NotificationTypeEnum.Error, 'Email or password format is incorrect. Please try again.')
					continue

			if self.login(email=email_input, password=password_input):
					self._active_user.show_cli_menu(self)
					break
			else:
					show_cli_notification(NotificationTypeEnum.Error, 'Username/password is not matching. Please try again.')
