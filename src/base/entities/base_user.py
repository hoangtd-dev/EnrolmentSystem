from abc import abstractmethod

class BaseUser:
	def __init__(self, id, name, email, password, role):
		self._id = id
		self._name = name
		self._email = email
		self._password = password
		self._role = role
		self._is_login = False

	@abstractmethod
	def show_cli_menu(system): raise NotImplementedError		

	def get_id(self):
		return self._id

	def is_login(self):
		return self._is_login
	
	def login(self, email, password):
		if self._email == email and self._password == password:
			self._is_login = True
			return True
		return False
		
	def logout(self):
		self._is_login = False

	def __str__(self):
		return f'name: {self._name} - role: {self._role}'
	
