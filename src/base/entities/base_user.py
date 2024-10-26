class BaseUser:
	def __init__(self, id, name, email, password, role):
		self.__id = id
		self.__name = name
		self.__email = email
		self.__password = password
		self.__role = role

	def get_id(self):
		return self.__id
	
	def get_email(self):
		return self.__email
	
	def get_password(self):
		return self.__password
	
	def get_name(self):
		return self.__name
	
	def update_password(self, new_password):
		self.__password = new_password
		
	def __str__(self):
		return f'id: {self.__id} - name: {self.__name} - role: {self.__role}'
	