from termcolor import colored

from ..enums.notification_type_enum import NotificationTypeEnum

def format_id(str_len, new_id):
  new_id_str = str(new_id)
  new_id_len = len(new_id_str)

  if new_id_len > str_len:
    return None
 
  return '0' * (str_len - new_id_len) + new_id_str

def show_cli_notification(notification_type, message, is_template_included = True):
	match notification_type:
		case NotificationTypeEnum.Success:
			print(colored(f'{'SUCCESSFUL:' if is_template_included else '' }{message}', 'green'))
		case NotificationTypeEnum.Error:
			print(colored(f'{'ERROR:' if is_template_included else '' }{message}', 'red'))
		case NotificationTypeEnum.Warning:
			print(colored(f'{'WARNING: ' if is_template_included else '' }{message}', 'yellow'))
		case NotificationTypeEnum.Info:
			print(colored(f'{message}', 'blue'))
		case NotificationTypeEnum.Highlight:
			print(colored(f'{message}', None, attrs=["bold"]))		
		case _:
			print(message)