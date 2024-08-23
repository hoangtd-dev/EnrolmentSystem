from grade import Grade
import random

class Enrolment:
    def __init__(self, subject):
        self.subject = subject
        self.grade = None
        self.assign_grade()

    def assign_grade(self):
        # Generate a random mark between 25 and 100 and calculate the grade
        mark = random.randint(25, 100)
        self.grade = Grade(mark)

    def to_dict(self):
        return {
            "subject_id": self.subject.subject_id,
            "subject_name": self.subject.subject_name,
            "grade": self.grade.to_dict()
        }

    @classmethod
    def from_dict(cls, data, subjects):
        subject = next((s for s in subjects if s.subject_id == data["subject_id"]), None)
        enrolment = cls(subject)
        enrolment.grade = Grade.from_dict(data["grade"])
        return enrolment
