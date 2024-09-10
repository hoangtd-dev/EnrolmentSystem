from setup import get_default_system_args
from src.cli_enrolment_system import CliEnrolmentSystem
from src.gui_enrolment_system import GuiEnrolmentSystem
from src.enums.system_mode import SystemModeEnum

def initialize():
	mode = get_default_system_args()

	if mode == SystemModeEnum.GUI:
		GuiEnrolmentSystem().run()
	else:
		CliEnrolmentSystem().run()

if __name__ == '__main__':
	initialize()