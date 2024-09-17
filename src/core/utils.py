from termcolor import colored

from ..enums.notification_type_enum import NotificationTypeEnum

def format_id(str_len, new_id):
  new_id_str = str(new_id)
  new_id_len = len(new_id_str)

  if new_id_len > str_len:
    return None
 
  return '0' * (str_len - new_id_len) + new_id_str

def show_cli_notification(notification_type, message):
	match notification_type:
		case NotificationTypeEnum.SUCCESS:
			print(colored(f'SUCCESSFUL: {message}', 'green'))
		case NotificationTypeEnum.ERROR:
			print(colored(f'ERROR: {message}', 'red'))
		case NotificationTypeEnum.WARNING:
			print(colored(f'WARNING: {message}', 'yellow'))
		case NotificationTypeEnum.INFO:
			print(colored(f'{message}', 'blue'))
		case NotificationTypeEnum.HIGHLIGHT:
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
			show_cli_notification(NotificationTypeEnum.ERROR, "Invalid input. Please enter an integer.")

def get_custom_float_input(prompt):
	while True:
		try:
			value = float(input(prompt))
			return value
		except ValueError:
			show_cli_notification(NotificationTypeEnum.ERROR, "Invalid input. Please enter an float.")