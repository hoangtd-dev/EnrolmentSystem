from argparse import ArgumentParser

from src.enums.system_mode_enum import SystemModeEnum

def get_default_system_args():
	parser = ArgumentParser(
		description="Script that provide application mode"
	)

	parser.add_argument(
		'-m' ,"--mode", 
		type=SystemModeEnum, 
		default=SystemModeEnum.Gui,
		help="using 2 options: cli or gui"
	)
	
	result = parser.parse_args()
	return (result.mode)