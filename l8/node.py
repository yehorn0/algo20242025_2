from typing import Optional, Generic, TypeVar


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.__data: T = data
        self.__next: Optional["Node"] = None

    @property
    def data(self) -> T:
        return self.__data

    @data.setter
    def data(self, data: T):
        self.__data = data

    @property
    def next(self) -> Optional["Node"]:
        return self.__next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.__next = next_

    def __repr__(self) -> str:
        return f"Node({self.__data})"


if __name__ == '__main__':
    node = Node[int](1)
    print(node.data)
    print(node)
