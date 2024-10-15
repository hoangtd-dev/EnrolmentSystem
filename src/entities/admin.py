from ..base.entities.base_user import BaseUser

from ..enums.role_enum import RoleEnum

class Admin(BaseUser):
	def __init__(self, id, name, email, password):
		super().__init__(id, name, email, password, RoleEnum.ADMIN)

	def show_cli_menu(self, system):
		pass