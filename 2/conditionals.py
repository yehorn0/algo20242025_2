import time


def is_less_than_with_sleep(x: int, y: int) -> bool:
    print("In sleep function")
    time.sleep(2)
    print("Out sleep function")

    # condition ? value1 : value2 - C/C++/js
    # value1 if condition else value2
    # return True if x < y else False
    # if x < y:
    #     return True
    # else:
    #     return False
    return x < y

#
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
#
#
# # >, <, <=, >=, ==, !=, !(), .. is, in
# if x > y:
#     print("x is greater than y")
# elif is_less_than_with_sleep(x, y):
#     print("x is less than y")
# else:
#     print("x equals than y")

# A,B
# !(A and B) = !A or !B
# !(A or !B) = !A and B


# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print(f"{id(a)}, {id(b)}")
#
# list1 = [1, 2, 3] # Mutable !
# list2 = [1, 2, 3]
# print(list1 == list2)  # True
# print(list1 is list2)  # False
# print(f"{id(list1)}, {id(list2)}")

# score = int(input("Enter your score: "))
#
# if 90 <= score:  # !(SCORE >= 90) <> SCORE < 90
#     print("A")
# elif 80 <= score:
#     print("B")
# elif 70 <= score:
#     print("C")
# elif 60 <= score:
#     print("D")
# else:
#     print("F")


def is_divisible_by(x: int, y: int) -> bool:
    print(f"Checking if number {x} is divisible by {y}")
    return x % y == 0


# if is_divisible_by(10, 5) or is_divisible_by(5, 2) or is_divisible_by(6, 10):
#     print("True")
# else:
#     print("False")
#
# if is_divisible_by(10, 3) and unnamed_function(5, 2) and is_divisible_by(6, 10):
#     print("True")
# else:
#     print("False")

#
# if any([is_divisible_by(10, 5), is_divisible_by(5, 2), is_divisible_by(6, 10)]):
#     print("True")
# else:
#     print("False")
#
#
# if all([is_divisible_by(10, 5), is_divisible_by(5, 2), is_divisible_by(6, 10)]):
#     print("True")
# else:
#     print("False")


"""
switch (variable):
    case 1:
        ....
        break
    case 2:
        ....
    case 3:
        ...
        break
    default:
        ...
"""
name = input("Enter your name: ")

match name:
    case "Adam" | "Peter" | "Simon":
        print("NF-12")
    # case "Peter":
    #     print("NF-12")
    # case "Simon":
    #     print("NF-12")
    case "Anna":
        print("NF-13")
    case "John":
        print("NF-14")
    case _:
        print("Invalid input")
