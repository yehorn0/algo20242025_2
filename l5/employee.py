class EmployeeSlots:
    __slots__ = ('__name', '__age')

    def __init__(self, name: str, age: int) -> None:
        self.__name: str = name
        self.__age: int = age


class Employee:
    def __init__(self, name: str, age: int) -> None:
        self.__name: str = name
        self.__age: int = age

    def __del__(self):
        print("Deleting Employee")

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: int) -> None:
        if new_age <= 0:
            raise ValueError("Bad Age")

        self.__age = new_age


def main() -> None:
    employee = Employee("Adam", 10)

    print(employee, type(employee))
    # employee.name = "Adam"
    # print(employee.__age)
    print(employee.age)

    try:
        employee.age = -100
    except ValueError:
        print("Bad Age")

    print(employee.age)
    print(employee.__dir__())

    print(employee._Employee__age)
    employee._Employee__age = -100
    print(employee.age)

    employee_slots = EmployeeSlots("Johny", 15)
    # employee_slots.age = 12
    print(employee.__dict__)
    print(employee_slots.__slots__)


def main_with_new() -> None:
    # employee = Employee("Adam", 10)
    adam = Employee.__new__(Employee)
    Employee.__init__(adam, "Adam", 10)


if __name__ == '__main__':
    main_with_new()
