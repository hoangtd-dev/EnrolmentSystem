from enrolment_system import EnrolmentSystem
from admin import Admin

def login_menu(system):
    while True:
        print("\nWelcome to the Enrollment System")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_login(system)
        elif choice == "2":
            student_login(system)
        elif choice == "3":
            print("Exiting the system.")
            system.save_students()  # Save data before exiting
            break
        else:
            print("Invalid choice. Please try again.")

def admin_login(system):
    password = input("Enter Admin Password: ")
    if system.admin.login(password):
        print(f"Welcome, {system.admin.admin_name}!")
        admin_menu(system)
    else:
        print("Invalid password. Please try again.")

def student_login(system):
    student_id = input("Enter Student ID: ")
    password = input("Enter Password: ")
    student = next((s for s in system.students if s.student_id == student_id), None)
    if student and student.login(password):
        print(f"Welcome, {student.student_name}!")
        student_menu(system, student)
    else:
        print("Invalid ID or password. Please try again.")

def admin_menu(system):
    while True:
        print("\nAdmin Menu")
        print("1. View All Students")
        print("2. Organize Students by Grade")
        print("3. Categorize Students (Pass/Fail)")
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
        print("\nStudent Menu")
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
            remove_subject(system, student)
        elif choice == "4":
            change_student_password(system, student)
        elif choice == "5":
            print("Logging out.")
            break
        else:
            print("Invalid choice. Please try again.")

def organize_students(system):
    organized_students = system.admin.organize_students_by_grade(system.students)
    organized_list = "\n".join([f"Student ID: {s.student_id}, Name: {s.student_name}, Total Marks: {s.get_total_marks()}" for s in organized_students])
    print(organized_list)

def categorize_students(system):
    categories = system.admin.categorize_students(system.students)
    pass_list = "\n".join([f"Student ID: {s.student_id}, Name: {s.student_name}, Total Marks: {s.get_total_marks()}" for s in categories['Pass']])
    fail_list = "\n".join([f"Student ID: {s.student_id}, Name: {s.student_name}, Total Marks: {s.get_total_marks()}" for s in categories['Fail']])

    print("Passed Students:\n" + pass_list if pass_list else "No students in Pass category.")
    print("Failed Students:\n" + fail_list if fail_list else "No students in Fail category.")

def remove_student(system):
    student_id = input("Enter student ID to remove: ")
    system.students = system.admin.remove_student(system.students, student_id)
    system.save_students()  # Save after removing student
    print(f"Student with ID {student_id} removed.")

def clear_all_students(system):
    confirm = input("Are you sure you want to clear all students? (y/n): ")
    if confirm.lower() == 'y':
        system.students = system.admin.clear_all_students()
        system.save_students()  # Save after clearing all students
        print("All students cleared.")

def remove_subject(system, student):
    subject_id = input("Enter subject ID to remove: ")
    result = student.remove_subject(subject_id)
    system.save_students()  # Save after removing subject
    print(result)

def change_student_password(system, student):
    new_password = input("Enter new password: ")
    result = student.change_password(new_password)
    system.save_students()  # Save after changing password
    print(result)

if __name__ == "__main__":
    # Initialize the EnrolmentSystem with an admin instance
    admin = Admin("A001", "AdminName", "admin_password")
    system = EnrolmentSystem(admin)

    # Start the CLI
    login_menu(system)
