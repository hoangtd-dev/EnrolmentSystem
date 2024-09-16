from setup import get_default_system_args

from src.enums.system_mode_enum import SystemModeEnum

from src.cli_enrolment_system import CliEnrolmentSystem
from src.gui_enrolment_system import GuiEnrolmentSystem

def initialize():
	mode = get_default_system_args()

	if mode == SystemModeEnum.Gui:
		GuiEnrolmentSystem().run()
	else:
		CliEnrolmentSystem().run()

if __name__ == '__main__':
	initialize()