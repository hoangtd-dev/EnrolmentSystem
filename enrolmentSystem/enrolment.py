import random
from grade import Grade  # Import the Grade class
from subject import Subject

class Enrolment:
    def __init__(self, subject):
        if subject is None:
            raise ValueError("Subject cannot be None")
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
            "grade": self.grade.to_dict() if self.grade else None
        }

    @classmethod
    def from_dict(cls, data, subjects):
        subject = next((s for s in subjects if s.subject_id == data["subject_id"]), None)
        if subject is None:
            # Handle missing subject: create a placeholder or skip the enrolment
            print(f"Warning: Subject with ID {data['subject_id']} not found. Creating placeholder subject.")
            subject = Subject(subject_id=data["subject_id"], subject_name="Unknown Subject")
        
        enrolment = cls(subject)
        enrolment.grade = Grade.from_dict(data["grade"]) if data["grade"] else None
        return enrolment
