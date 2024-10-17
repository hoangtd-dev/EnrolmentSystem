from .base.base_system import BaseSystem

from .enums.notification_type_enum import NotificationTypeEnum

from .core.utils import (
	show_cli_notification
)

class CliEnrolmentSystem(BaseSystem):
	def run(self):
		while self._is_active:
			selected_option = self.__menu()
			self.__handle_option(selected_option)


	def __menu(self):
		return input('University System: (A)dmin, (S)tudent, or X: ')

	def __handle_option(self, selected_option):
			match selected_option.lower():
				case 'a':
					self._active_user = self._admin
					self._active_user.show_cli_menu(self)
				case 's':
					self.__student_authentication_menu()
				case 'x':
					self.update_active_status(False)
				case _:
					show_cli_notification(NotificationTypeEnum.Warning, 'Please input a/s/x only')

	def __student_authentication_menu(self):
		print('student authentication menu...')