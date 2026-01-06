python_students = {"Asha", "Ravi", "Kiran"}
data_science_students = {"Ravi", "Meena", "Anil"}

python_students.add("Sita")
data_science_students.remove("Anil")

both_courses = python_students.intersection(data_science_students)
print("Students enrolled in both courses:", both_courses)

only_python = python_students.difference(data_science_students)
print("Students only in Python course:", only_python)

all_students = python_students.union(data_science_students)
print("All students in either course:", all_students)

course_count = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}

for course, count in course_count.items():
    print(f"Course: {course}, Students: {count}")

expected_growth = {course: count * 2 for course, count in course_count.items()}
print("Expected growth:", expected_growth)
