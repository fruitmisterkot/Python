class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """ Инициализация экземпляра класса книги """
        self.name = name
        self.author = author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        """Возвращает название книги"""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Устанавливает название книги"""
        self._name = new_name

    @property
    def author(self) -> str:
        """Возвращает автора книги"""
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        """Устанавливает автора книги"""
        self._author = new_author


class PaperBook(Book):
    """ Класс бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        """ Инициализация экземпляра класса бумажные книги"""
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages ={self._pages!r})"

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, pages) -> None:
        """Проверка присвоения значения свойству pages"""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages


class AudioBook(Book):
    """ Класс аудио книга"""
    def __init__(self, name: str, author: str, duration: float):
        """ Инициализация экземпляра класса аудио книги"""
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    @property
    def duration(self) -> float:
        """Возвращает продолжительность книги"""
        return self._duration

    @duration.setter
    def duration(self, duration) -> None:
        """Проверка присвоения значения свойству duration"""
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом")
        self._duration = duration

