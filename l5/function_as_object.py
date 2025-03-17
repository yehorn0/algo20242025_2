def get_name_from_input() -> str:
    return input("Enter name: ")


def new_function() -> None:
    print("New Function!")


#name = get_name_from_input()
#print(name)
#print(get_name_from_input.__dir__())
get_name_from_input.new_attribute = 5
get_name_from_input.function = new_function

print(get_name_from_input.__dir__())
print(get_name_from_input.new_attribute)

get_name_from_input.function()
