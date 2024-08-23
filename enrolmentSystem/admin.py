from student import Student
import random

class Admin:
    def __init__(self, admin_id, admin_name, password):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.password = password
        self.is_logged_in = False

    def login(self, password):
        if self.password == password:
            self.is_logged_in = True
            print(f"Admin {self.admin_name} logged in successfully.")
            return True
        else:
            print("Invalid admin password.")
            return False

    def logout(self):
        self.is_logged_in = False
        print(f"Admin {self.admin_name} logged out.")

    def view_all_students(self, students):
        return "\n".join([f"Student ID: {s.student_id}, Name: {s.student_name}, Total Marks: {s.get_total_marks()}" for s in students])

    def organize_students_by_grade(self, students):
        # Sort students by their total marks, using the get_total_marks() method directly
        organized_students = sorted(students, key=lambda s: s.get_total_marks(), reverse=True)
        return organized_students

    def categorize_students(self, students):
        categories = {'Pass': [], 'Fail': []}
        for student in students:
            # Check if any subject has a mark less than 50
            has_failed = any(enrolment.grade.mark < 50 for enrolment in student.enrolment_list if enrolment.grade)
            
            if has_failed:
                categories['Fail'].append(student)
            else:
                categories['Pass'].append(student)
        return categories
    
    def remove_student(self, students, student_id):
        students = [student for student in students if student.student_id != student_id]
        return students

    def clear_all_students(self):
        return []
