import math


class Device:
    """Базовый класс Оборудование"""
    def __init__(self, name: str, _type: str, volume: float , substance: str):
        """ Инициализация экземпляра класса оборудование """
        self.name = name
        self._type = type
        self._volume = volume
        self.substance = substance

    def __str__(self) -> str:
        return f"Оборудование {self.name} типа {self._type} с веществом {self.substance} и объемом {self.volume}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, type={self._type!r}, volume={self._volume!r}, substance={self.substance!r})"


    @property
    def volume(self) -> float:
        """Возвращает объем устройства. Инкапсуляция используется, так как необходима проверка введенных пользователем данных"""
        return self.volume

    @volume.setter
    def volume(self, volume) -> None:
        """Проверка присвоения значения свойству volume"""
        if not isinstance(volume, float):
            raise TypeError("Объем оборудования должен быть типа float")
        if volume <= 0:
            raise ValueError("Объем оборудования долже быть положительным числом")
        self._volume = volume

    @property
    def type(self) -> float:
        """Возвращает тип устройства. Инкапсуляция используется, так как необходима проверка введенных пользователем данных"""
        return self.type

    @type.setter
    def type(self, _type) -> None:
        """Проверка присвоения значения свойству type"""
        if not isinstance(type, ("pipeline", "reservoir", "separator", "pump")):
            raise TypeError("Объем оборудования должен быть типа float")
        self._type = type

    def get_type_of_hazardous_substance(self, substance: str) -> int:
        """Функция устанавливает тип опасного вещества по его названию"""
        pass

    def get_volume_of_substance(self)->float:
        """Определяет объем вещества в оборудовании заданного объема"""

class Pipeline(Device):
    """Класс Трубопровод"""
    def __init__(self, name: str,  _type: str, volume: float, substance: str, length: float, diameter: float):
        """ Инициализация экземпляра класса Трубопровод"""
        super().__init__(name, _type, volume, substance)
        self.length = length
        self.diameter = diameter

    def __repr__(self) -> str:
        """Перегрузка магического метода __repr__.Появились новые атрибуты length и diametr"""
        return f"{self.__class__.__name__}(name={self.name!r}, type={self._type!r}, volume={self._volume!r}, substance={self.substance!r}, length={self.length!r}, diameter={self.diameter!r})"

    def get_volume_of_substance(self)->float:
        """Определяет объем вещества в трубопроводе"""
        volume = self.length * self.diameter / 2 * self.diameter / 2 * math.pi
        return volume

class Reservoir(Device):
    """Класс Резервуар"""
    def __init__(self,  name: str, _type: str, volume: float, substance: str, coefficient_filling: float):
        """ Инициализация экземпляра класса Резервуар"""
        super().__init__(name, _type, volume, substance)
        self.coefficient_filling = coefficient_filling

    def __repr__(self) -> str:
        """Перегрузка магического метода __repr__.Появился новый атрибут coefficient_filling"""
        return f"{self.__class__.__name__}(name={self.name!r}, type={self._type!r}, volume={self.volume!r}, substance={self.substance!r}, coefficient_filling={self.coefficient_filling!r})"

    def get_volume_of_substance(self)->float:
        """Определяет объем вещества в резервуаре"""
        volume = self.volume * self.coefficient_filling
        return volume

