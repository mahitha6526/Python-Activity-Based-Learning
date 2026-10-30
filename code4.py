subjects = ["English", "Maths", "Python"]
marks = []
pass_mark = 35
grace_limit = 3
grace_used = False

for subject in subjects:
    mark = float(input("Enter marks in " + subject + " (0-100): "))

    while mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        mark = float(input("Re-enter marks in " + subject + ": "))

    marks.append(mark)

final_marks = marks.copy()

for i in range(len(final_marks)):
    gap = pass_mark - final_marks[i]

    if final_marks[i] < pass_mark and gap <= grace_limit and not grace_used:
        final_marks[i] = min(pass_mark, final_marks[i] + grace_limit)
        grace_used = True

for i in range(len(subjects)):
    print(subjects[i], "Original:", marks[i], "Final:", final_marks[i])

if all(mark >= pass_mark for mark in final_marks):
    print("Result: PASS")
else:
    print("Result: FAIL")