if __name__ == "__main__":
    class Employee:
        """Базовый класс сотрудника."""

        def __init__(self, name: str, salary: float):
            """
            Создать объект сотрудника.

            :param name: Имя сотрудника.
            :param salary: Зарплата сотрудника.
            """
            self.name = name
            self.salary = salary

        def __str__(self) -> str:
            """
            Вернуть строковое представление объекта для пользователя.

            :return: Строка с основной информацией о сотруднике.
            """
            return f"Сотрудник: {self.name}, зарплата: {self.salary}"

        def __repr__(self) -> str:
            """
            Вернуть строковое представление объекта для разработчика.

            :return: Строка с названием класса и параметрами объекта.
            """
            return f"{self.__class__.__name__}(name={self.name!r}, salary={self.salary!r})"

        def work(self) -> str:
            """
            Описать выполнение работы сотрудником.

            :return: Сообщение о работе сотрудника.
            """
            return f"{self.name} выполняет свою работу."

        def take_break(self) -> str:
            """
            Описать перерыв сотрудника.

            :return: Сообщение о перерыве сотрудника.
            """
            return f"{self.name} на перерыве."


    class Manager(Employee):
        """Дочерний класс менеджера."""

        def __init__(self, name: str, salary: float, department: str):
            """
            Создать объект менеджера.

            :param name: Имя менеджера.
            :param salary: Зарплата менеджера.
            :param department: Отдел менеджера.
            """
            super().__init__(name, salary)
            self.department = department

        def __str__(self) -> str:
            """
            Вернуть строковое представление менеджера для пользователя.

            :return: Строка с основной информацией о менеджере.
            """
            return (
                f"Менеджер: {self.name}, зарплата: {self.salary}, "
                f"отдел: {self.department}"
            )

        def __repr__(self) -> str:
            """
            Вернуть строковое представление менеджера для разработчика.

            :return: Строка с названием класса и параметрами объекта.
            """
            return (
                f"{self.__class__.__name__}(name={self.name!r}, "
                f"salary={self.salary!r}, department={self.department!r})"
            )

        def work(self) -> str:
            """
            Описать выполнение работы менеджером.

            Метод перегружен, потому что менеджер не только работает,
            но и управляет сотрудниками отдела.

            :return: Сообщение о работе менеджера.
            """
            return f"{self.name} управляет отделом {self.department}."

        # Метод take_break() унаследован без изменений.
    pass
