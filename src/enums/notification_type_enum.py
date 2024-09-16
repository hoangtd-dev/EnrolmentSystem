from enum import StrEnum

class NotificationTypeEnum(StrEnum):
	Success = 'success'
	Error = 'error',
	Warning = 'warning',
	Info = 'info',
	Highlight = 'highlight'