import tkinter as tk
from tkinter import messagebox, simpledialog
from student import Student
from admin import Admin
from enrolment_system import EnrolmentSystem
class EnrollmentSystemGUI:
    def __init__(self, root, system):
        self.root = root
        self.system = system
        self.current_student = None
        self.root.title("Enrollment System")

        # Login Frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=20, padx=20)

        tk.Label(self.login_frame, text="Enrollment System", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.login_frame, text="Email:").pack(pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(pady=5)

        tk.Label(self.login_frame, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=5)

        self.user_type = tk.StringVar(value="Student")
        tk.Radiobutton(self.login_frame, text="Admin", variable=self.user_type, value="Admin").pack(anchor=tk.CENTER, pady=2)
        tk.Radiobutton(self.login_frame, text="Student", variable=self.user_type, value="Student").pack(anchor=tk.CENTER, pady=2)


        # Create a frame to contain the buttons horizontally
        button_frame = tk.Frame(self.login_frame)
        button_frame.pack(pady=10)

        # Pack the buttons inside the button_frame
        tk.Button(button_frame, text="Login", command=self.login).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Register as Student", command=self.show_registration).pack(side=tk.LEFT, padx=5)

        # Main Menu Frame
        self.main_menu_frame = tk.Frame(root)

        tk.Button(self.main_menu_frame, text="Enroll in Subject", command=self.enroll_student).pack(pady=10)
        tk.Button(self.main_menu_frame, text="View Enrollment List", command=self.view_enrollment_list).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Remove Subject", command=self.remove_subject).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Change Password", command=self.change_password).pack(pady=10)
        tk.Button(self.main_menu_frame, text="Logout", command=self.logout).pack(pady=10)

        # Admin Menu Frame
        self.admin_menu_frame = tk.Frame(root)

        tk.Button(self.admin_menu_frame, text="View All Students", command=self.view_all_students).pack(pady=10)
        tk.Button(self.admin_menu_frame, text="Organize Students by Grade", command=self.organize_students).pack(pady=10)
        tk.Button(self.admin_menu_frame, text="Categorize Students", command=self.categorize_students).pack(pady=10)
        tk.Button(self.admin_menu_frame, text="Remove Student", command=self.remove_student).pack(pady=10)
        tk.Button(self.admin_menu_frame, text="Clear All Students", command=self.clear_all_students).pack(pady=10)
        tk.Button(self.admin_menu_frame, text="Logout", command=self.logout).pack(pady=10)

    def login(self):
        user_type = self.user_type.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if user_type == "Admin":
            admin = self.system.admin
            if admin.login(password):
                self.show_admin_menu()
            else:
                messagebox.showerror("Login Failed", "Invalid admin password")
        else:  # Student login
            student = next((s for s in self.system.students if s.email == username), None)
            if student and student.login(password):
                self.current_student = student
                self.show_main_menu()
            else:
                messagebox.showerror("Login Failed", "Invalid student email or password")

    def logout(self):
        if self.current_student:
            self.current_student.logout()
            self.system.save_students()
            self.current_student = None
        self.system.admin.logout()
        self.show_login_screen()

    def show_login_screen(self):
        self.main_menu_frame.pack_forget()
        self.admin_menu_frame.pack_forget()
        self.login_frame.pack()

    def show_main_menu(self):
        self.login_frame.pack_forget()
        self.main_menu_frame.pack()

    def show_admin_menu(self):
        self.login_frame.pack_forget()
        self.admin_menu_frame.pack()

    def show_registration(self):
        self.login_frame.pack_forget()
        registration_frame = tk.Toplevel(self.root)
        registration_frame.title("Register as Student")

        tk.Label(registration_frame, text="Enter your name:").pack(pady=5)
        name_entry = tk.Entry(registration_frame)
        name_entry.pack(pady=5)

        tk.Label(registration_frame, text="Enter your email:").pack(pady=5)
        email_entry = tk.Entry(registration_frame)
        email_entry.pack(pady=5)

        tk.Label(registration_frame, text="Enter a password:").pack(pady=5)
        password_entry = tk.Entry(registration_frame, show="*")
        password_entry.pack(pady=5)

        def register():
            name = name_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            enrolment_list = []
            student_id = Student.generate_student_id()
            
            try:
                student = Student(student_id, name, email, password, enrolment_list)
                self.system.students.append(student)
                self.system.save_students()  # Save after registering
                messagebox.showinfo("Success", f"Registration successful! Your student ID is {student.student_id}")
                registration_frame.destroy()
                self.show_login_screen()
            except ValueError as e:
                messagebox.showerror("Registration Failed", str(e))

        tk.Button(registration_frame, text="Register", command=register).pack(pady=10)

    def enroll_student(self):
        if self.current_student:
            result = self.current_student.enrol_subject()
            self.system.save_students()  # Save after enrolling
            messagebox.showinfo("Enroll", result)

    def remove_subject(self):
        subject_id = simpledialog.askstring("Remove Subject", "Enter subject ID to remove:")
        if self.current_student:
            result = self.current_student.remove_subject(subject_id)
            self.system.save_students()  # Save after removing subject
            messagebox.showinfo("Remove Subject", result)

    def view_enrollment_list(self):
        if self.current_student:
            enrollment_list = self.current_student.view_enrolment_list()
            messagebox.showinfo("Enrollment List", enrollment_list)

    def change_password(self):
        new_password = simpledialog.askstring("Change Password", "Enter new password:", show="*")
        if self.current_student and new_password:
            try:
                result = self.current_student.change_password(new_password)
                self.system.save_students()  # Save after changing password
                messagebox.showinfo("Change Password", result)
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def view_all_students(self):
        students_list = self.system.admin.view_all_students(self.system.students)
        messagebox.showinfo("All Students", students_list)

    def organize_students(self):
        organized_students = self.system.admin.organize_students_by_grade(self.system.students)
        organized_list = "\n".join([f"Student ID: {s.student_id}, Name: {s.name}, Total Marks: {s.get_total_marks()}" for s in organized_students])
        messagebox.showinfo("Organized Students", organized_list)

    def categorize_students(self):
        categories = self.system.admin.categorize_students(self.system.students)
        pass_list = "\n".join([f"Student ID: {s.student_id}, Name: {s.name}, Total Marks: {s.get_total_marks()}" for s in categories['Pass']])
        fail_list = "\n".join([f"Student ID: {s.student_id}, Name: {s.name}, Total Marks: {s.get_total_marks()}" for s in categories['Fail']])

        messagebox.showinfo("Pass", f"Passed Students:\n{pass_list}" if pass_list else "No students in Pass category.")
        messagebox.showinfo("Fail", f"Failed Students:\n{fail_list}" if fail_list else "No students in Fail category.")

    def remove_student(self):
        student_id = simpledialog.askstring("Remove Student", "Enter student ID to remove:")
        self.system.students = self.system.admin.remove_student(self.system.students, student_id)
        self.system.save_students()  # Save after removing student
        messagebox.showinfo("Success", f"Student with ID {student_id} removed")

    def clear_all_students(self):
        confirm = messagebox.askyesno("Clear All Students", "Are you sure you want to clear all students?")
        if confirm:
            self.system.students = self.system.admin.clear_all_students()
            self.system.save_students()  # Save after clearing all students
            messagebox.showinfo("Success", "All students cleared.")

# Example of initializing the GUI
if __name__ == "__main__":
    admin = Admin("A001", "AdminName", "admin@university.com", "AdminPassword123")
    system = EnrolmentSystem(admin)

    root = tk.Tk()
    app = EnrollmentSystemGUI(root, system)
    root.mainloop()
