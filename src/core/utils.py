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
		case NotificationTypeEnum.Success:
			print(colored(message, 'green'))
		case NotificationTypeEnum.Error:
			print(colored(message, 'red'))
		case NotificationTypeEnum.Warning:
			print(colored(message, 'yellow'))
		case NotificationTypeEnum.Info:
			print(colored(message, 'blue'))
		case NotificationTypeEnum.Highlight:
			print(colored(message, None, attrs=["bold"]))		
		case _:
			print(message)