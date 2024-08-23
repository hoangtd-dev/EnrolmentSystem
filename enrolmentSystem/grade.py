class Grade:
    def __init__(self, mark):
        self.mark = mark
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark < 50:
            return 'Z'
        elif 50 <= self.mark < 65:
            return 'P'
        elif 65 <= self.mark < 75:
            return 'C'
        elif 75 <= self.mark < 85:
            return 'D'
        else:
            return 'HD'

    def is_pass(self):
        return self.mark >= 50

    def to_dict(self):
        return {
            "mark": self.mark,
            "grade": self.grade
        }

    @classmethod
    def from_dict(cls, data):
        grade = cls(data["mark"])
        grade.grade = data["grade"]
        return grade
