import csv
import os
from datetime import datetime

# Ensure data folder exists
if not os.path.exists("data"):
    os.makedirs("data")

students_file = "data/students.txt"
attendance_file = "data/attendance.csv"

def add_student():
    name = input("Enter student name: ")
    with open(students_file, "a") as file:
        file.write(name + "\n")
    print("Student added successfully!")

def mark_attendance():
    if not os.path.exists(students_file):
        print("No students file found. Add students first!")
        return

    with open(students_file, "r") as file:
        students = [s.strip() for s in file.readlines()]

    today = str(datetime.now().date())
    today_attendance = []

    for s in students:
        status = input(f"Is {s} present? (y/n): ")
        today_attendance.append([today, s, "Present" if status.lower() == "y" else "Absent"])

    # Read old attendance
    all_attendance = []
    if os.path.exists(attendance_file):
        with open(attendance_file, "r") as file:
            all_attendance = list(csv.reader(file))

        # Remove old entries for today if they exist
        all_attendance = [row for row in all_attendance if row[0] != today]

    # Write updated attendance
    with open(attendance_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Student", "Attendance"])
        writer.writerows(all_attendance)
        writer.writerows(today_attendance)

    print("Attendance marked successfully!")

def view_report():
    if not os.path.exists(attendance_file):
        print("No attendance data found!")
        return
    with open(attendance_file, "r") as file:
        print(file.read())

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
