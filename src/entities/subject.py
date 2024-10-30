from ..enums.grade_type_enum import GradeTypeEnum

class Subject:
    def __init__(self, id, mark, grade=None):
        self.__id = id
        self.__mark = mark
        self.__grade = grade if grade else self.get_classify_grade(mark)

    def get_id(self):
        return self.__id

    def get_mark(self):
        return self.__mark

    def get_grade(self):
        return self.__grade

    @staticmethod
    def get_classify_grade(mark):
        """Classifies the grade type based on the mark."""
        if mark >= 85:
            return GradeTypeEnum.HIGH_DISTINCTION
        elif mark >= 75:
            return GradeTypeEnum.DISTINCTION
        elif mark >= 65:
            return GradeTypeEnum.CREDIT
        elif mark >= 50:
            return GradeTypeEnum.PASS
        else:
            return GradeTypeEnum.FAIL

    def to_dict(self):
        return {
            "id": self.__id,
            "mark": self.__mark,
			"type": self.__grade
        }