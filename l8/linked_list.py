"""
+ 1. append() -> add to the end
2. remove() -> remove firstelement with data T; if doesn't exist than raises ValueError
+ 3. __len__ -> length
+ 4. __getitem__ -> list[idx] -> raises IndexError if no idx
+ 5. __setitems__ ...
+ 6. __str__, __repr__: Node(1) -> Node(2) -> Node(3) .....
7.
"""
from l8.node import Node
from typing import Generic, TypeVar, Optional, NoReturn, Iterable, Iterator


T = TypeVar("T")


class LinkedList(Generic[T]):
    def __init__(self, iterable: Optional[Iterable[T]] = None) -> None:
        self.__head: Optional[Node[T]] = None
        self.__len: int = 0

        for t in iterable or []:
            self.append(t)

    def append(self, item: T) -> None:
        self.__len += 1
        if not self.__head:
            self.__head = Node[T](item)
            return

        current: Node[T] = self.__head

        while current.next:
            current = current.next

        current.next = Node[T](item)

    def remove(self, item: T) -> None | NoReturn:
        if not self.__head:
            raise ValueError(f"list.remove(x): {item} not in list")

        if self.__head.data == item:
            self.__head = self.__head.next
            self.__len -= 1
            return

        current: Node[T] = self.__head
        while current.next and current.next.data != item:
            current = current.next

        if not current.next:
            raise ValueError(f"list.remove(x): {item} not in list")

        self.__len -= 1
        current.next = current.next.next

    def __repr__(self) -> str:
        ret_val: str = f"LL(length {self.__len}): "
        current: Node[T] = self.__head

        while current:
            ret_val += f"{repr(current)} => "
            current = current.next

        ret_val += "None"

        return ret_val

    def __len__(self) -> int:
        # len_: int = 0
        # current: Node[T] = self.__head
        #
        # while current:
        #     len_ += 1
        #     current = current.next
        #
        # return len_
        return self.__len

    def __getitem__(self, idx: int) -> T | NoReturn:
        current_idx: int = 0
        current: Node[T] = self.__head

        while current:
            if current_idx == idx:
                return current.data
            current_idx += 1
            current = current.next

        raise IndexError("list index out of range")

    def __setitem__(self, idx: int, item: T) -> None | NoReturn:
        current_idx: int = 0
        current: Node[T] = self.__head

        while current:
            if current_idx == idx:
                current.data = item
                return
            current_idx += 1
            current = current.next

        raise IndexError("list index out of range")

    def __iter__(self) -> Iterator[T]:
        current: Node[T] = self.__head

        while current:
            yield current.data
            current = current.next

    # ============================================================================================== #
    # ======================================== LAB 8 =============================================== #
    # ============================================================================================== #
    def reverse(self) -> "LinkedList[T]":
        ...
    # ============================================================================================== #
    # ============================================================================================== #
    # ============================================================================================== #


if __name__ == "__main__":
    ll = LinkedList[int]()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(-1)

    print(ll)
    ll.remove(1)
    print(ll)
    try:
        ll.remove(100)
    except ValueError:
        pass

    print(ll)
    linked_list = LinkedList([1, 2, 3, 4, 5])
    print(linked_list)

    for data in linked_list:
        print(data)

    # print(ll)
    # print(len(ll))
    #
    # print(ll[0])
    # try:
    #     print(ll[100])
    # except IndexError as ie:
    #     print(ie)
    #
    # ll[1] = 123
    # print(ll)
    # try:
    #     ll[100] = 12
    # except IndexError as ie:
    #     print(ie)
