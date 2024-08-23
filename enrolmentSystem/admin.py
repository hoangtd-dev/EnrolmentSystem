from user import User
from student import Student

class Admin(User):
    def __init__(self, admin_id, name, email, password):
        super().__init__(name, email, password)  # Initialize the base User class
        self.admin_id = admin_id

    def view_all_students(self, students):
        return "\n".join([f"Student ID: {s.student_id}, Name: {s.name}, Total Marks: {s.get_total_marks()}" for s in students])

    def organize_students_by_grade(self, students):
        # Sort students by their total marks in descending order
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
        # Remove the student with the specified ID
        students = [student for student in students if student.student_id != student_id]
        return students

    def clear_all_students(self):
        # Clear the entire list of students
        return []
