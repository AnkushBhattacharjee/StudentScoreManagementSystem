import sqlite3

# Connect to database (creates one if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    marks INTEGER NOT NULL
)
''')

conn.commit()
conn.close()
print("✅ Database and table created successfully!")

import sqlite3
import pandas as pd

# Function to add a new student record
def add_student(name, subject, marks):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, subject, marks) VALUES (?, ?, ?)", (name, subject, marks))
    conn.commit()
    conn.close()
    print(f"✅ Added student: {name}, Subject: {subject}, Marks: {marks}")

# Function to view all students
def view_students():
    conn = sqlite3.connect('students.db')
    df = pd.read_sql_query("SELECT * FROM students", conn)
    conn.close()
    print("\n📊 All Students:")
    print(df if not df.empty else "No records found.")

# Function to delete any student
def delete_student():
    name = input("Enter student name to delete: ")
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    conn.commit()
    print(f"🗑️ Deleted student record for: {name}")


# Simple menu system
def main():
    while True:
        print("\n🎓 Student Score Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))
            add_student(name, subject, marks)
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice, try again!")

if __name__ == "__main__":
    main()

