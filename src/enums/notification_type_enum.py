from enum import StrEnum

class NotificationTypeEnum(StrEnum):
	SUCCESS = 'success'
	ERROR = 'error',
	WARNING = 'warning',
	INFO = 'info',
	HIGHLIGHT = 'highlight'

