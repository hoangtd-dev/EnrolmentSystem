import copy

from ..enums.notification_type_enum import NotificationTypeEnum
from ..enums.role_enum import RoleEnum

from ..entities.subject import Subject
from ..entities.enrolment import Enrolment
from ..base.entities.base_user import BaseUser

from ..core.instants import NUMBER_OF_SUBJECT_ID_LENGTH
from ..core.auth_utils import check_password_valid
from ..core.utils import (
	get_custom_integer_input,
	show_cli_notification,
	format_id
)

class Student(BaseUser):
	def __init__(self, id, name, email, password):
		super().__init__(id, name, email, password, RoleEnum.STUDENT)
		self._enrolment_list = []

	@staticmethod
	def register(id, name, email, password):
		return Student(id, name, email, password)
	
	def get_enrolments(self):
		return copy.deepcopy(self._enrolment_list)
	
	def set_enrolments(self, new_enrolment_list):
		self._enrolment_list = new_enrolment_list

	def show_cli_menu(self, system):
		show_cli_notification(NotificationTypeEnum.INFO, '-------------student menu:--------------')
		
		while True:
			print("1. Enroll in Subject")
			print("2. View Enrollment List")
			print("3. Remove Subject")
			print("4. Change Password")
			print("5. Logout")
			selected_option = get_custom_integer_input('Your choice: ')
			print('-----------------------------')
			self.__handle_option(system, selected_option)
			print('-----------------------------')

			if (selected_option == 5):
				break

	def get_total_marks(self):
		if len(self._enrolment_list) == 0:
			return 0
		return sum([enrolment.get_grade().get_mark() for enrolment in self._enrolment_list]) / len(self._enrolment_list)

	def change_password(self, new_password):
		self._password = new_password
	
	def enrol_subject(self):
		new_subject_id = self.__get_new_subject_id()
		self._enrolment_list.append(Enrolment(Subject(id=new_subject_id, name='name'+new_subject_id)))

	def remove_subject_by_id(self, subject_id):
		new_enrolments = [enrolment for enrolment in self._enrolment_list if enrolment.get_subject().get_id() != subject_id]
		if len(new_enrolments) == len(self._enrolment_list):
			return False
		else:
			self._enrolment_list = new_enrolments
			return True

	def view_enrolment_list(self, enrolments):
		if len(enrolments) == 0:
			show_cli_notification(NotificationTypeEnum.HIGHLIGHT, 'No enrolment found')

		print("\n".join([str(enrolment) for enrolment in enrolments]))

	def __get_new_subject_id(self):
		if len(self._enrolment_list) == 0:
			return format_id(NUMBER_OF_SUBJECT_ID_LENGTH, 1)
		
		next_id = max([int(enrolment.get_subject().get_id()) for enrolment in self._enrolment_list]) + 1
		return format_id(NUMBER_OF_SUBJECT_ID_LENGTH, next_id) 
	
	def __handle_option(self, system, selected_option):
		match selected_option:
			case 1:
				if len(self._enrolment_list) == 4:
					show_cli_notification(NotificationTypeEnum.ERROR, 'You reach maximum subjects in 1 semester')
				else:
					self.enrol_subject()
					show_cli_notification(NotificationTypeEnum.SUCCESS, 'new subject enrolled!')
			case 2:
				self.view_enrolment_list(self._enrolment_list)
			case 3:
				subject_id = input('subject id that you want to remove: ')
				if self.remove_subject_by_id(subject_id):
					show_cli_notification(NotificationTypeEnum.SUCCESS, f'Subject with id {subject_id} is removed')
				else:
					show_cli_notification(NotificationTypeEnum.ERROR, f'Cannot find subject with id {subject_id}')
			case 4:
				while True:
					new_password_input = input('Enter new password:')
					if not check_password_valid(new_password_input):
						show_cli_notification(NotificationTypeEnum.ERROR, 'Password format is incorrect. Please try again.')
						continue

					self.change_password(new_password=new_password_input)
					show_cli_notification(NotificationTypeEnum.SUCCESS, 'Password changed.')
					break
			case 5:
				self.logout()
				system.logout()
				show_cli_notification(NotificationTypeEnum.SUCCESS, 'Logout')
			case _:
				show_cli_notification(NotificationTypeEnum.WARNING, 'Please choose from 1 - 5')

	def __str__(self):
		return f'{super().__str__()} - {self.get_total_marks()}'


	