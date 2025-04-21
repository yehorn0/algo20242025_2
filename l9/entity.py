from typing import NoReturn


class Entity:
    def __init__(self, key: str, timestamp: int, temperature: float) -> None:
        self.__key = key
        self.__timestamp = timestamp
        self.__temperature = temperature

    @property
    def key(self) -> str:
        return self.__key

    @property
    def timestamp(self) -> int:
        return self.__timestamp

    @property
    def temperature(self) -> float:
        return self.__temperature

    def update(self, other: "Entity") -> None | NoReturn:
        if not isinstance(other, Entity):
            raise ValueError("Other is not entity class")
        if self.__key != other.key:
            raise ValueError("Keys don't match")

        self.__timestamp = other.timestamp
        self.__temperature = other.temperature
        return None

    def __repr__(self) -> str:
        return f"<Entity[{self.key}, {self.timestamp}, {self.temperature}]>"
