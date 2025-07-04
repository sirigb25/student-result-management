import sqlite3

def login():
    print("\n=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    conn.close()

    if result:
        role = result[0]
        print(f"\nLogin successful! Logged in as {role}.\n")
        return role
    else:
        print("\nLogin failed. Invalid username or password.\n")
        return None
if __name__ == "__main__":
    login()