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

    def load_subjects(self):
        subjects = {}
        
        if os.path.exists("student.data"):
            try:
                with open("student.data", "r") as f:
                    student_dicts = json.load(f)
                    for student_data in student_dicts:
                        enrolment_list = student_data.get("enrolment_list", [])
                        for enrolment_data in enrolment_list:
                            subject_id = enrolment_data.get("subject_id")
                            subject_name = enrolment_data.get("subject_name")
                            if subject_id and subject_name and subject_id not in subjects:
                                subjects[subject_id] = Subject(subject_id=subject_id, subject_name=subject_name)
                print(f"Loaded {len(subjects)} unique subjects from student data.")
            except json.JSONDecodeError:
                print("Error: student.data is empty or corrupted. Initializing with an empty subject list.")
                return []

        return list(subjects.values())
    
    def load_students(self):
        if os.path.exists("student.data"):
            try:
                with open("student.data", "r") as f:
                    student_dicts = json.load(f)
                    subjects = self.load_subjects()  # Load subjects first
                    self.students = [Student.from_dict(d, subjects) for d in student_dicts]
                    print(f"Loaded {len(self.students)} students from file.")
            except json.JSONDecodeError:
                print("Error: student.data is empty or corrupted. Initializing with an empty student list.")
                self.students = []
        else:
            print("No student data found, creating a new file.")
            self.save_students() 

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

    # def remove_student(self, student_id):
    #     self.students = self.admin.remove_student(self.students, student_id)
    #     self.save_students()

    # def clear_all_students(self):
    #     self.students = self.admin.clear_all_students()
    #     self.save_students()
