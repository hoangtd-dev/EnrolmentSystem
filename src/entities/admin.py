from ..base.entities.base_user import BaseUser

from ..enums.notification_type_enum import NotificationTypeEnum
from ..enums.role_enum import RoleEnum

from ..core.utils import (
	get_custom_integer_input, 
	show_cli_notification
)

class Admin(BaseUser):
	def __init__(self, id, name, email, password):
		super().__init__(id, name, email, password, RoleEnum.Admin)

	def show_cli_menu(self, system):
		show_cli_notification(NotificationTypeEnum.Info, '-------------admin menu:--------------')
		
		while True:
			print('1. View all students')
			print('2. Organize students by grade')
			print('3. categorize students')
			print('4. Remove student by id')
			print('5. Remove all students')
			print('6. Logout')
			selected_option = get_custom_integer_input('Your choice: ')
			print('-----------------------------')
			self.__handle_option(system, selected_option)
			print('-----------------------------')

			if (selected_option == 6):
				break

	def __get_students(self, system):
		return system.get_all_students()

	def view_all_students(self, students):
		if len(students) == 0:
			show_cli_notification(NotificationTypeEnum.Highlight, 'No student found')

		print("\n".join([str(student) for student in students]))

	def organized_students_by_grade(self, students):
		return sorted(students, key=lambda student: student.get_total_marks(), reverse=True)

	def categorize_students(self, students):
		passed_students = []
		failed_students = []
		for student in students:
			if student.get_total_marks() >= 50:
				passed_students.append(student)
			else:
				failed_students.append(student)
		return ( passed_students, failed_students )

	def remove_student_by_id(self, system, student_id):
		return system.remove_student_by_id(student_id)

	def remove_all_students(self, system):
		system.remove_all_students()

	def __handle_option(self, system, selected_option):
		match selected_option:
			case 1:
				students = self.__get_students(system)
				self.view_all_students(students)
			case 2:
				students = self.__get_students(system)
				organized_students = self.organized_students_by_grade(students)
				system.update_students(organized_students)
				show_cli_notification(NotificationTypeEnum.Success, 'students is organized by grade')
			case 3:
				students = self.__get_students(system)
				( passed_students, failed_students ) = self.categorize_students(students)
				show_cli_notification(NotificationTypeEnum.Info, '---Passed students---')
				self.view_all_students(passed_students)
				show_cli_notification(NotificationTypeEnum.Info, '---Failed students---')
				self.view_all_students(failed_students)
			case 4:
				student_id = input('StudentId that you want to remove: ')
				if self.remove_student_by_id(system, student_id):
					show_cli_notification(NotificationTypeEnum.Success, f'Student with id {student_id} is deleted')
				else:
					show_cli_notification(NotificationTypeEnum.Error, f'Cannot find student with id {student_id}')
			case 5:
				self.remove_all_students(system)
				show_cli_notification(NotificationTypeEnum.Success, 'All students are deleted!')
			case 6:
				self.logout()
				system.logout()
				show_cli_notification(NotificationTypeEnum.Success, 'Logout')
			case _:
				show_cli_notification(NotificationTypeEnum.Warning, 'Please choose from 1 - 6')