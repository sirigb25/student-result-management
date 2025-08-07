 Student Result Management System

A mini project in Python using SQLite based on the V-Model.

Login Credentials

| Username | Password  | Role     |
|----------|-----------|----------|
| admin    | admin123  | admin    |
| siri123  | siri@123  | student  |
| poorna   | poorna@123| student  |
| rahul01  | rahul@123 | student  |

 File Overview

| File           | Description                                |
|----------------|--------------------------------------------|
| `database.py`  | Creates `users` and `marks` tables         |
| `login.py`     | Handles login authentication               |
| `result.py`    | Admin adds/updates marks, students view    |
| `main.py`      | Project entry point                        |
| `add_student.py` | Add new students to the database         |

 How to Run

1. Run `database.py` to create the database and default admin  
2. Run `add_student.py` to add students (optional)  
3. Run `main.py` to use the application  
