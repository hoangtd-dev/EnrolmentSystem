import random

class Subject:
    def __init__(self, subject_id=None, subject_name=""):
        if subject_id is None:
            self.subject_id = self.generate_subject_id()
        else:
            self.subject_id = subject_id
        self.subject_name = subject_name

    @staticmethod
    def generate_subject_id():
        # Generate a random 3-digit ID
        return str(random.randint(1, 999)).zfill(3)

    def to_dict(self):
        return {
            "subject_id": self.subject_id,
            "subject_name": self.subject_name
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["subject_id"], data["subject_name"])
