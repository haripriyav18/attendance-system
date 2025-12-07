import csv
import os

# Create a folder to store attendance files
if not os.path.exists("data"):
    os.makedirs("data")

filename = "data/attendance.csv"

# Add students
students = {}
n = int(input("Enter number of students: "))
for i in range(n):
    sid = input("Enter student ID: ")
    name = input("Enter student name: ")
    students[sid] = name

# Mark attendance
attendance = {}
print("\nMark attendance (y for Present / n for Absent):")
for sid, name in students.items():
    status = input(f"{name} (ID: {sid}): ")
    attendance[sid] = "Present" if status.lower() == 'y' else "Absent"

# Save attendance to CSV
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Student ID", "Name", "Attendance"])
    for sid in students:
        writer.writerow([sid, students[sid], attendance[sid]])

print(f"\n✅ Attendance saved successfully in {filename}")

# Optional: Show attendance summary
print("\nAttendance Summary:")
for sid in students:
    print(f"{students[sid]}: {attendance[sid]}")
