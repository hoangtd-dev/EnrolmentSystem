from subject import Subject
from enrolment import Enrolment

class Student:
    def __init__(self, student_id, student_name, password):
        self.student_id = student_id
        self.student_name = student_name
        self.password = password
        self.enrolment_list = []

    def login(self, password):
        return self.password == password

    def logout(self):
        print(f"Student {self.student_name} logged out.")

    def enrol_subject(self):
        if len(self.enrolment_list) >= 4:
            print("Cannot enroll in more than 4 subjects.")
            return "Cannot enroll in more than 4 subjects."

        subject = Subject()  # Automatically generate a new subject with a random ID
        enrolment = Enrolment(subject)
        self.enrolment_list.append(enrolment)

        if len(self.enrolment_list) > 4:
            return "You have enrolled in more than 4 subjects!"

        return f"Enrolled in {subject.subject_name} with ID {subject.subject_id}. Mark: {enrolment.grade.mark}, Grade: {enrolment.grade.grade}"

    def remove_subject(self, subject_id):
        self.enrolment_list = [e for e in self.enrolment_list if e.subject.subject_id != subject_id]
        print(f"Subject with ID {subject_id} removed from enrolments.")
        return f"Subject with ID {subject_id} removed."

    def view_enrolment_list(self):
        if not self.enrolment_list:
            return "No subjects enrolled."
        return "\n".join([f"Subject ID: {e.subject.subject_id}, Name: {e.subject.subject_name}, Mark: {e.grade.mark}, Grade: {e.grade.grade}" for e in self.enrolment_list])

    def change_password(self, new_password):
        self.password = new_password
        return "Password changed successfully."

    def get_total_marks(self):
        return sum(enrolment.grade.mark for enrolment in self.enrolment_list if enrolment.grade)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "student_name": self.student_name,
            "password": self.password,
            "enrolment_list": [enrolment.to_dict() for enrolment in self.enrolment_list]
        }

    @classmethod
    def from_dict(cls, data, subjects):
        student = cls(data["student_id"], data["student_name"], data["password"])
        student.enrolment_list = [Enrolment.from_dict(e, subjects) for e in data["enrolment_list"]]
        return student

    @staticmethod
    def is_password_valid(password):
        return len(password) > 6

    @staticmethod
    def generate_student_id(current_total_student_count):
        return f"S{str(current_total_student_count + 1).zfill(4)}"

    def enrol_subject(self):
        if len(self.enrolment_list) >= 4:
            print("Cannot enroll in more than 4 subjects.")
            return "Cannot enroll in more than 4 subjects."

        subject = Subject()  # Automatically generate a new subject with a random ID
        if subject is None:
            raise ValueError("Failed to create subject for enrolment.")
        
        enrolment = Enrolment(subject)
        self.enrolment_list.append(enrolment)

        if len(self.enrolment_list) > 4:
            return "You have enrolled in more than 4 subjects!"

        return f"Enrolled in {subject.subject_name} with ID {subject.subject_id}. Mark: {enrolment.grade.mark}, Grade: {enrolment.grade.grade}"
