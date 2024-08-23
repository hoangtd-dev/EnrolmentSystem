from enrolment_system import EnrolmentSystem
from student import Student
from admin import Admin

def register_student(system):
    print("\n--- Student Registration ---")
    name = input("Enter your name: ")
    email = input("Enter your email (must end with @university.com): ")
    password = input("Enter your password (must start with an uppercase letter, contain at least 5 letters, and end with 3+ digits): ")
    enrolment_list = []


    try:
        student = Student(Student.generate_student_id(), name, email, password, enrolment_list)
        system.students.append(student)
        system.save_students()  # Save the new student to the data file
        print(f"Registration successful! Your student ID is {student.student_id}")
    except ValueError as e:
        print(f"Registration failed: {e}")

def main_menu(system):
    while True:
        print("\n--- Main Menu ---")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Register as Student")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_login(system)
        elif choice == "2":
            student_login(system)
        elif choice == "3":
            register_student(system)
        elif choice == "4":
            print("Exiting the system.")
            system.save_students()  # Ensure data is saved before exiting
            break
        else:
            print("Invalid choice. Please try again.")

def admin_login(system):
    password = input("Enter Admin Password: ")
    if system.admin.login(password):
        print(f"Welcome, {system.admin.name}!")
        admin_menu(system)
    else:
        print("Invalid password.")

def student_login(system):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    student = next((s for s in system.students if s.email == email), None)
    if student and student.login(password):
        print(f"Welcome, {student.name}!")
        student_menu(system, student)
    else:
        print("Invalid email or password.")

def admin_menu(system):
    while True:
        print("\n--- Admin Menu ---")
        print("1. View All Students")
        print("2. Organize Students by Grade")
        print("3. Categorize Students")
        print("4. Remove Student")
        print("5. Clear All Students")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(system.admin.view_all_students(system.students))
        elif choice == "2":
            organize_students(system)
        elif choice == "3":
            categorize_students(system)
        elif choice == "4":
            remove_student(system)
        elif choice == "5":
            clear_all_students(system)
        elif choice == "6":
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again.")

def student_menu(system, student):
    while True:
        print("\n--- Student Menu ---")
        print("1. Enroll in Subject")
        print("2. View Enrollment List")
        print("3. Remove Subject")
        print("4. Change Password")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            result = student.enrol_subject()
            print(result)
        elif choice == "2":
            print(student.view_enrolment_list())
        elif choice == "3":
            subject_id = input("Enter subject ID to remove: ")
            print(student.remove_subject(subject_id))
        elif choice == "4":
            new_password = input("Enter new password: ")
            try:
                print(student.change_password(new_password))
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "5":
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again.")

def organize_students(system):
    organized_students = system.admin.organize_students_by_grade(system.students)
    for student in organized_students:
        print(f"Student ID: {student.student_id}, Name: {student.name}, Total Marks: {student.get_total_marks()}")

def categorize_students(system):
    categories = system.admin.categorize_students(system.students)
    print("Passed Students:")
    for student in categories['Pass']:
        print(f"Student ID: {student.student_id}, Name: {student.name}")
    
    print("Failed Students:")
    for student in categories['Fail']:
        print(f"Student ID: {student.student_id}, Name: {student.name}")

def remove_student(system):
    student_id = input("Enter student ID to remove: ")
    system.students = system.admin.remove_student(system.students, student_id)
    system.save_students()
    print(f"Student with ID {student_id} has been removed.")

def clear_all_students(system):
    confirm = input("Are you sure you want to clear all students? (y/n): ")
    if confirm.lower() == 'y':
        system.students = system.admin.clear_all_students()
        system.save_students()
        print("All students have been cleared.")

if __name__ == "__main__":
    admin = Admin("A001", "AdminName", "admin@university.com", "AdminPassword123")
    system = EnrolmentSystem(admin)
    main_menu(system)
