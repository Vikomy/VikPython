import doctest
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, max_speed: float, fuel_level: float):
        """
        Абстрактное транспортное средство

        :param max_speed: Максимальная скорость
        :param fuel_level: Уровень топлива

        >>> v = Vehicle(180, 50)
        """
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительной")
        self.max_speed = max_speed

        if fuel_level < 0:
            raise ValueError("Уровень топлива не может быть отрицательным")
        self.fuel_level = fuel_level

    @abstractmethod
    def move(self, distance: float) -> None:
        """
        Движение транспортного средства

        :param distance: Расстояние движения

        >>> None
        """
        ...

    @abstractmethod
    def refuel(self, amount: float) -> None:
        """
        Заправка транспортного средства

        :param amount: Количество топлива

        >>> None
        """
        ...


class Building(ABC):
    def __init__(self, floors: int, area: float):
        """
        Абстрактное здание

        :param floors: Количество этажей
        :param area: Площадь здания

        >>> b = Building(5, 1200)
        """
        if floors <= 0:
            raise ValueError("Количество этажей должно быть положительным")
        self.floors = floors

        if area <= 0:
            raise ValueError("Площадь должна быть положительной")
        self.area = area

    @abstractmethod
    def open_building(self) -> None:
        """
        Открытие здания

        >>> None
        """
        ...

    @abstractmethod
    def close_building(self) -> None:
        """
        Закрытие здания

        >>> None
        """
        ...


class Device(ABC):
    def __init__(self, power: float, is_on: bool):
        """
        Абстрактное устройство

        :param power: Мощность устройства
        :param is_on: Включено ли устройство

        >>> d = Device(1500, False)
        """
        if power <= 0:
            raise ValueError("Мощность должна быть положительной")
        self.power = power

        if not isinstance(is_on, bool):
            raise TypeError("Состояние должно быть bool")
        self.is_on = is_on

    @abstractmethod
    def turn_on(self) -> None:
        """
        Включение устройства

        >>> None
        """
        ...

    @abstractmethod
    def turn_off(self) -> None:
        """
        Выключение устройства

        >>> None
        """
        ...


if name == "__main__":
    doctest.testmod()