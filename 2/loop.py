i = 0

# while condition:
#     body


# while i < 5:
#     print(f"In loop: {i}")
#
#     i += 1
#
#
# i = 0
# while True:
#     print(f"In loop: {i}")
#
#     i += 1
#
#     if i >= 5:
#         break

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]

# chunk_len = 3
#
# while chunk := data[i:i+chunk_len]:
#     print(chunk)
#     i += chunk_len
#

#
# print(data[1:5:2]) # start(default=0):end(len(list)):step(default=1)
# print(data[:5])
# print(data[3:])
# print(data[1::3])
#
# print(data[::-1])
# print(data[5:7:-1]) # []
# print(data[7:5:-1]) # []
#
# students = ["Adam", "Peter", "Bart", "John"]
# # for counter in range(len(students)):
# #     print(students[counter])
#
# # for student in students:
# #     print(student)
#
# for idx, student in enumerate(students):
#     print(idx, student)

students = [
    {"name": "Adam", "group": "nf-12", "average": 10.},
    {"name": "Peter", "group": "nf-12", "average": 12.},
    {"name": "Simon", "group": "nf-12", "average": 14.},
    {"name": "John", "group": "nf-11", "average": 20.},
    {"name": "Anna", "group": "nf-13", "average": 30.},
]
#
# for student in students:
#     print(student["name"], student["group"], student["average"])

students_dict = {}
for student in students:
    students_dict[student["name"]] = {
        "group": student["group"],
        "average": student["average"],
    }

# for student in students_dict:
#     print(student, students_dict[student])

for student_key, student_value in students_dict.items():
    print(student_key, student_value)
