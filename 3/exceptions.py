def get_int_from_input() -> int:
    while True:
        number_str = input("Enter number: ")

        try:
            number = int(number_str)
        except ValueError:
            print("Bad input (Value error)")
        # except TypeError:
        #     print("Type Error")
        # except:  # Bad decision
        #     print("Bad input. Unknown exception")
        else:
            # print("Good input")
            return number
        # finally:
        #     print("In finally")
#
#
# try:
#     print(x)
# except NameError as name_error:
#     print(f"NameError. {name_error} {name_error.name}")
#
#
# if __name__ == '__main__':
#     some_int = get_int_from_input()
#     print(f"Number from input: {some_int}")

# TypeError
# x = 1 + "123"

#
# x_list = [n for n in range(1, 25) if n % 3 == 0]
#
# idx = get_int_from_input()
# # print(x_list[idx])
# # if 0 <= idx < len(x_list) or 0 > idx >= - len(x_list):
# #     print(x_list[idx])
# # else:
# #     print("Index out of range")
#
# try:
#     print(x_list[idx])
# except IndexError:
#     print("Index out of range")


# KeyError
things_dict = {
    "apple": "fruit",
    "melon": "fruit",
    "strawberry": "fruit",
    "potato": "vegetable"
}

if "tomato" in things_dict:
    type_if = things_dict["tomato"]
else:
    type_if = "default_type"
print(type_if)

try:
    type_ = things_dict["tomato"]
except KeyError:
    print("KeyError")
    type_ = "default_type"

print(type_)

print(things_dict.get("apple", "default_type"))  # <--- "fruit"
print(things_dict.get("tomato", "default_type"))  # <---"default_type"
