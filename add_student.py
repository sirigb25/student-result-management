import sqlite3

def add_student():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # List of students to add (username, password, role)
    students = [
        ('siri123', 'siri@123', 'student'),
        ('poorna', 'poorna@123', 'student')
    ]

    # Insert each student if not already present
    for student in students:
        cursor.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", student)

    # Save and close connection
    conn.commit()
    conn.close()

    print("✅ Student users 'siri123' and 'poorna' added successfully!")

if __name__ == "__main__":
    add_student()
