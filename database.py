import sqlite3

# Function to connect to the SQLite database
def connect():
    return sqlite3.connect('database.db')

# Function to create tables and insert default admin
def create_tables():
    conn = connect()
    cursor = conn.cursor()

    # Create 'users' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            role TEXT
        )
    ''')

    # Create 'marks' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS marks (
            student_id TEXT,
            subject TEXT,
            marks INTEGER,
            PRIMARY KEY(student_id, subject)
        )
    ''')

    cursor.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", 
                   ('admin', 'admin123', 'admin'))

    conn.commit()
    conn.close()

# Run this directly to create tables
if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")


