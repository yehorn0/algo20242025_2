from typing import Protocol, TypeVar, NoReturn
from l9.entity import Entity


T = TypeVar('T', bound=Entity)


class StorageProto(Protocol[T]):
    def insert(self, element: T) -> None | NoReturn:
        ...

    def find(self, key: str) -> T | NoReturn:
        ...

    def update(self, element: T) -> None | NoReturn:
        ...
