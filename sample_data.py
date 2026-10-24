
import csv
from pathlib import Path

# Sample student data for Git and GitHub practice
students = [
    {"student_id": "ST001", "name": "Abebe Bekele", "department": "Software Engineering", "year": 3},
    {"student_id": "ST002", "name": "Hana Alemu", "department": "Computer Science", "year": 2},
    {"student_id": "ST003", "name": "Dawit Kebede", "department": "Information Systems", "year": 4},
]

# Save the CSV file in the project directory
output_file = Path(__file__).resolve().parent.parent / "sample_data.csv"

with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["student_id", "name", "department", "year"]
    )
    writer.writeheader()
    writer.writerows(students)

print(f"Sample data saved to: {output_file}")
