from .base.base_system import BaseSystem

from .enums.notification_type_enum import NotificationTypeEnum

from .core.utils import (
	show_cli_notification
)

class CliEnrolmentSystem(BaseSystem):
	def run(self):
		show_cli_notification(NotificationTypeEnum.Info, 'Enrolment System started!')
		while self._is_active:
			self.__menu()
			selected_option = input('Your selection: ')
			self.__handle_option(selected_option)

	def __menu(self):
		print('University System: (A)dmin, (S)tudent, or X: ')

	def __handle_option(self, selected_option):
			match selected_option.lower():
				case 'a':
					pass
				case 's':
					pass
				case 'x':
					self.update_active_status(False)
				case _:
					show_cli_notification(NotificationTypeEnum.Warning, 'Please input a/s/x only')