from termcolor import colored

from ..enums.notification_type_enum import NotificationTypeEnum

def show_cli_notification(notification_type, message):
	match notification_type:
		case NotificationTypeEnum.Success:
			print(colored(f'SUCCESSFUL: {message}', 'green'))
		case NotificationTypeEnum.Error:
			print(colored(f'ERROR: {message}', 'red'))
		case NotificationTypeEnum.Warning:
			print(colored(f'WARNING: {message}', 'yellow'))
		case NotificationTypeEnum.Info:
			print(colored(f'{message}', 'blue'))
		case NotificationTypeEnum.Highlight:
			print(colored(f'{message}', None, attrs=["bold"]))		
		case _:
			print(message)

def show_gui_notification(type, title, message):
	pass

def get_custom_integer_input(prompt):
	while True:
		try:
			value = int(input(prompt))
			return value
		except ValueError:
			show_cli_notification(NotificationTypeEnum.Error, "Invalid input. Please enter an integer.")

def get_custom_float_input(prompt):
	while True:
		try:
			value = float(input(prompt))
			return value
		except ValueError:
			show_cli_notification(NotificationTypeEnum.Error, "Invalid input. Please enter an float.")