students = ["Anu", "Bala", "Charan"]
subjects = ["Maths", "Python", "English"]

marks = [
    [85, 90, 78],
    [70, 75, 80],
    [92, 88, 95]
]

print("--- Student Marks Analysis ---")

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)

    print(students[i], "Total:", total, "Average:", round(average, 2))

print("\n--- Subject Averages ---")

for j in range(len(subjects)):
    subject_total = 0

    for i in range(len(students)):
        subject_total += marks[i][j]

    print(subjects[j], "Average:", round(subject_total / len(students), 2))

top_index = 0

for i in range(1, len(students)):
    if sum(marks[i]) > sum(marks[top_index]):
        top_index = i

print("\nTop performer:", students[top_index])