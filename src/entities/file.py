from ..enums.file_status_enum import FileStatusEnum

class FileStatus:
	def __init__(self, status, error_msg = ''):
		self._status = status
		self._error_msg = error_msg

	def get_status(self):
		return self._status

	def get_error(self):
		return self._error_msg

class FileResponse(FileStatus):
	def __init__(self, status, data_response, error_msg = ''):
		super().__init__(status, error_msg)
		self._data_response = data_response

	def value(self):
		return self._data_response if self._status == FileStatusEnum.SUCCESS else self._error_msg
