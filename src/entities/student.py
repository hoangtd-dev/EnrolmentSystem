from ..base.entities.base_user import BaseUser
class Student(BaseUser):
	def __init__(self, id, name, email, password, role):
		super().__init__(id, name, email, password, role)
		self._enrolment_list = []

	def show_cli_menu(self, system):
		print(f'Welcome, {self._name}')

	def get_enrolments(self):
		pass
	
	def set_enrolments(self, new_enrolment_list):
		self._enrolment_list = new_enrolment_list

	def get_total_marks(self):
		pass

	def change_password(self, new_password):
		self._password = new_password
	
	def enrol_subject(self, subject):
		# Check whether exceed 4 subject __is_number_of_subject_exceed()
		# Create new "enrolment" object with new subject
		# Add to enrolment list
		pass

	def remove_subject(self, subject_id):
		pass

	def view_enrolment_list(self):
		pass

	def get_total_marks(self):
		return 0;

	def __is_number_of_subject_exceed():
		pass

	@staticmethod
	def register(id, name, email, password):
		# return new student
		pass

	