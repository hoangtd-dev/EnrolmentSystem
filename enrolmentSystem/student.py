from user import User
from subject import Subject
from enrolment import Enrolment
import json
import os

class Student(User):
    student_counter = 0  # To keep track of the last generated student ID

    def __init__(self, student_id, name, email, password, enrolment_list):
        super().__init__(name, email, password)
          # Initialize the base User class
        if student_id:
            self.student_id = student_id
        else:
            self.student_id = self.generate_student_id()
        
        if enrolment_list:
            self.enrolment_list = enrolment_list
        else:
            self.enrolment_list = []


    @classmethod
    def generate_student_id(cls):
        # Check if the student.data file exists
        if os.path.exists("student.data"):
            with open("student.data", "r") as f:
                try:
                    # Load the existing students
                    student_dicts = json.load(f)
                    # Find the highest student ID
                    existing_ids = [int(student["student_id"]) for student in student_dicts if student["student_id"].isdigit()]
                    if existing_ids:
                        cls.student_counter = max(existing_ids)
                except json.JSONDecodeError:
                    print("Error: student.data is empty or corrupted. Initializing with default student counter.")
                    cls.student_counter = 0
        else:
            print("No student data found, starting student ID generation from 000001.")

        # Increment the student counter to generate the next ID
        cls.student_counter += 1
        return str(cls.student_counter).zfill(6)

    def enrol_subject(self):
        if len(self.enrolment_list) >= 4:
            return "Cannot enroll in more than 4 subjects."

        # Automatically generate a new subject with a random ID
        subject = Subject()
        if subject is None:
            raise ValueError("Failed to create subject for enrolment.")
        
        enrolment = Enrolment(subject)
        self.enrolment_list.append(enrolment)

        return f"Enrolled in {subject.subject_name} with ID {subject.subject_id}. Mark: {enrolment.grade.mark}, Grade: {enrolment.grade.grade}"

    def remove_subject(self, subject_id):
        self.enrolment_list = [e for e in self.enrolment_list if e.subject.subject_id != subject_id]
        return f"Subject with ID {subject_id} removed."

    def view_enrolment_list(self):
        if not self.enrolment_list:
            return "No subjects enrolled."
        return "\n".join([f"Subject ID: {e.subject.subject_id}, Name: {e.subject.subject_name}, Mark: {e.grade.mark}, Grade: {e.grade.grade}" for e in self.enrolment_list])

    def change_password(self, new_password):
        if not self.is_password_valid(new_password):
            raise ValueError("Invalid password. Password must start with an uppercase letter, have at least 5 letters, and be followed by 3 or more digits.")
        self.password = new_password
        return "Password changed successfully."

    def get_total_marks(self):
        return sum(enrolment.grade.mark for enrolment in self.enrolment_list if enrolment.grade)
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "student_name": self.name,
            "email": self.email,
            "password": self.password,
            "enrolment_list": [enrolment.to_dict() for enrolment in self.enrolment_list]  # Convert each enrolment to dict
        }

    @classmethod
    def from_dict(cls, data, subjects):
    # Correctly initializing the Student instance with the expected arguments
        student = cls(
            data["student_id"],
            data["student_name"],
            data["email"],
            data["password"],
            []  # Initialize with an empty enrolment list
        )

        # If there's an enrolment list, handle it accordingly
        if "enrolment_list" in data:
            student.enrolment_list = [Enrolment.from_dict(e, subjects) for e in data.get("enrolment_list", [])]

        return student