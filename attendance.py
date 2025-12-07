import csv
from datetime import datetime
import os

def mark_attendance():
    try:
        if not os.path.exists("students.txt"):
            print("No students file found. Add students first!")
            return

        present = []
        with open("students.txt", "r") as file:
            students = file.readlines()

        today = str(datetime.now().date())

        # Read previous dates to avoid duplicate date entries
        if os.path.exists("attendance.csv"):
            with open("attendance.csv", "r") as file:
                lines = file.readlines()
                if any(today in line for line in lines):
                    print(f"Attendance for {today} has already been marked!")
                    return

        for s in students:
            status = input(f"Is {s.strip()} present? (y/n): ")
            present.append([s.strip(), "Present" if status.lower() == "y" else "Absent"])

        with open("attendance.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", today])
            writer.writerows(present)

        print("Attendance marked successfully!")

    except Exception as e:
        print("Error:", e)
