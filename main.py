from login import login
from result import add_or_update_marks, view_marks

def main():
    print("=== Student Result Management System ===")
    
    # Call the login function
    role = login()

    # Based on role, perform actions
    if role == "admin":
        add_or_update_marks()  # Admin can add or update marks
    elif role == "student":
        view_marks()  # Student can view their marks
    else:
        print("❌ Access denied or invalid user.")

if __name__ == "__main__":
    main()
