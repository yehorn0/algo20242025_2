# list_ = [1, 2, 3, 4, 5, 6, 10, 2, 4, 3, 4, 6, 7, 8, 9]
#
# unique_list: list[int] = []
#
# for elem in list_:  # O(n)
#     for unique_elem in unique_list:  # ~ O(n)
#         if elem == unique_elem:
#             break
#     else:
#         unique_list.append(elem)
#
# print(unique_list)
#
# unique_set: set[int] = set(unique_list)
# print(unique_set)

# example_set = {1}
# example_set.add(True)
# example_set.add(1.0)
# print(example_set) # len = 1 ???

set_A = {1, 2, 3, 4, 8, 10, 1}

# set_2 = set()
# for number in range(11):
#     if number % 2 == 0:
#         set_2.add(number)

set_B = {number for number in range(11) if number % 2 == 0}

set_union_0 = set_A | set_B # set_B | set_A
set_union_1 = set_A.union(set_B)
set_union_2 = set_B.union(set_A)

print(set_union_0, set_union_1, set_union_2)

set_intersection_0 = set_A & set_B
set_intersection_1 = set_A.intersection(set_B)
set_intersection_2 = set_B.intersection(set_A)

print(set_intersection_0, set_intersection_1, set_intersection_2)

set_difference_A_minus_B = set_A - set_B
set_difference_B_minus_A = set_B - set_A
print(set_difference_A_minus_B, set_difference_B_minus_A)
print(set_A.difference(set_B), set_B.difference(set_A))
print(set_union_0 - set_B, set_union_0 - set_A)

set_symmetric_difference_0 = set_A ^ set_B
set_symmetric_difference_1 = set_B ^ set_A
set_symmetric_difference_2 = set_A.symmetric_difference(set_B)
set_symmetric_difference_3 = set_B.symmetric_difference(set_A)
print(set_symmetric_difference_0, set_symmetric_difference_1, set_symmetric_difference_2, set_symmetric_difference_3)

# 0 xor 0 = 0    0 or 0 = 0
# 1 xor 1 = 0    1 or 1 = 1   <-----
# 0 xor 1 = 0    0 or 1 = 1
# 1 xor 0 = 0    1 or 0 = 1

set_small_set = {3, 4}
print(set_small_set.issubset(set_A)) # True
print(set_small_set.issubset(set_B)) # False
print(set_small_set.issuperset(set_A)) # False
print(set_A.issuperset(set_small_set)) # True

new_set = {1, 2, 3, 5}
new_set.add(5)
print(new_set)
new_set.add(4)
print(new_set)
new_set.add(6)
print(new_set)
new_set.remove(5)
print(new_set)
# ERROR KeyError(5)
new_set.remove(5)
print(new_set)
#
