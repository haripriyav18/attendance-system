import csv
from datetime import datetime

def add_student():
    try:
        name = input("Enter student name: ")
        with open("students.txt", "a") as file:
            file.write(name + "\n")
        print("Student added successfully!")
    except Exception as e:
        print("Error:", e)

def mark_attendance():
    try:
        present = []
        with open("students.txt", "r") as file:
            students = file.readlines()

        for s in students:
            status = input(f"Is {s.strip()} present? (y/n): ")
            present.append([s.strip(), "Present" if status.lower() == "y" else "Absent"])

        with open("attendance.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", datetime.now().date()])
            writer.writerows(present)
        print("Attendance marked successfully!")
    except FileNotFoundError:
        print("No students file found. Add students first!")
    except Exception as e:
        print("Error:", e)

def view_report():
    try:
        with open("attendance.csv", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No attendance data found!")

while True:
    print("\n1. Add Student\n2. Mark Attendance\n3. View Attendance Report\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_report()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
