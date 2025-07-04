import sqlite3

# Admin Function: Add or update marks
def add_or_update_marks():
    print("\n=== Add or Update Marks (Admin Only) ===")
    student_id = input("Enter Student ID: ")
    subject = input("Enter Subject: ")
    marks = input("Enter Marks: ")

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR REPLACE INTO marks (student_id, subject, marks)
        VALUES (?, ?, ?)
    ''', (student_id, subject, marks))

    conn.commit()
    conn.close()

    print(f"\n✅ Marks for {student_id} saved successfully!\n")

# Student Function: View marks
def view_marks():
    print("\n=== View Marks (Student) ===")
    student_id = input("Enter your Student ID: ")

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT subject, marks FROM marks WHERE student_id = ?", (student_id,))
    results = cursor.fetchall()

    conn.close()

    if results:
        print(f"\n📄 Marks for Student ID: {student_id}")
        print("----------------------------------")
        for subject, mark in results:
            print(f"{subject}: {mark}")
        print("----------------------------------\n")
    else:
        print("\n No marks found for this student ID.\n")

# Optional testing block
if __name__ == "__main__":
    add_or_update_marks()
