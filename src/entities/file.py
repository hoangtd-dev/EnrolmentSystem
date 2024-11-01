from ..enums.file_status_enum import FileStatusEnum

class FileStatus:
	def __init__(self, status, error_msg = ''):
		self.__status = status
		self.__error_msg = error_msg

	def get_status(self):
		return self.__status

	def get_error(self):
		return self.__error_msg

class FileResponse(FileStatus):
	def __init__(self, status, data_response, error_msg = ''):
		super().__init__(status, error_msg)
		self.__data_response = data_response

	def value(self):
		return self.__data_response if self.get_status() == FileStatusEnum.SUCCESS else self.get_error()
