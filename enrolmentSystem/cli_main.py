from enrolment_system import EnrolmentSystem
from admin import Admin

if __name__ == "__main__":
    admin = Admin("A001", "AdminName", "123")
    system = EnrolmentSystem(admin)
    system.login_menu()