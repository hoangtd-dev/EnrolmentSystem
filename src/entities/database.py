import json
import os
from ..entities.file import FileResponse, FileStatus
from ..enums.file_status_enum import FileStatusEnum

class Database:
	def __init__(self):
		self.__path = os.getcwd() + '/data/students.data'
		
	def read_file(self):
		if not os.path.exists(self.__path) or os.stat(self.__path).st_size == 0:
			return FileResponse(FileStatusEnum.SUCCESS, [])

		try:
			with open(self.__path, 'r') as file:
				return FileResponse(FileStatusEnum.SUCCESS, json.load(file))
		except IOError as error:
			return FileResponse(FileStatusEnum.ERROR, data_response=None, error_msg=str(error.strerror))
		except TypeError as error:
			return FileResponse(FileStatusEnum.ERROR, data_response=None, error_msg=str(error))
		except ValueError as error:
			return FileResponse(FileStatusEnum.ERROR, data_response=None, error_msg=str(error))

	def write_file(self, data):
		try:
			with open(self.__path, 'w+') as file:
				json.dump([item.to_dict() for item in data], file, indent=4)
				return FileStatus(FileStatusEnum.SUCCESS)
		except IOError as e:
			return FileStatus(FileStatusEnum.ERROR, str(e.strerror))
		except TypeError as e:
			return FileStatus(FileStatusEnum.ERROR, e)