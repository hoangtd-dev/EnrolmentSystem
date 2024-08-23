import json
import os
from student import Student
from subject import Subject

class EnrolmentSystem:
    def __init__(self, admin):
        self.admin = admin
        self.students = []
        self.subjects = []  # Start with an empty list of subjects
        self.load_students()

    def load_students(self):
        if os.path.exists("student.data"):
            with open("student.data", "r") as f:
                student_dicts = json.load(f)
                self.students = [Student.from_dict(d, self.subjects) for d in student_dicts]
                print(f"Loaded {len(self.students)} students from file.")
        else:
            print("No student data found, creating a new file.")
            self.save_students()  # Create an empty student.data file

    def save_students(self):
        with open("student.data", "w") as f:
            json.dump([student.to_dict() for student in self.students], f, indent=4)
        print("Student data saved.")

    def add_subject(self, subject_id, subject_name):
        subject = Subject(subject_id=subject_id, subject_name=subject_name)
        self.subjects.append(subject)
        print(f"Added subject {subject_name} with ID {subject_id}.")

    def get_subject_by_id(self, subject_id):
        return next((subject for subject in self.subjects if subject.subject_id == subject_id), None)

    def remove_student(self, student_id):
        self.students = self.admin.remove_student(self.students, student_id)
        self.save_students()

    def clear_all_students(self):
        self.students = self.admin.clear_all_students()
        self.save_students()
