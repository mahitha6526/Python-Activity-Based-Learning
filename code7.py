email = input("Enter student email: ").strip()
student_id = input("Enter student identifier (e.g. 24CSE001): ").strip().upper()

email_parts = email.split("@")

valid_email = (
    len(email_parts) == 2
    and len(email_parts[0]) > 0
    and "." in email_parts[1]
    and not email_parts[1].startswith(".")
    and not email_parts[1].endswith(".")
)

valid_id = (
    len(student_id) == 8
    and student_id[:2].isdigit()
    and student_id[2:5].isalpha()
    and student_id[5:].isdigit()
)

print("Email:", "Valid" if valid_email else "Invalid")
print("Student ID:", "Valid" if valid_id else "Invalid")