from enum import Enum

class LifeSituationName(Enum):
    NAME1 = 'name1'
    NAME2 = 'name2'


class ServiceType(Enum):
    AMENITY = 'Услуга'
    FUNCTION = 'Функция'
    SERVICE = 'Сервис'


class ServiceStatus(Enum):
    IN_QUEUE = 'В очереди на исследование'


class ClientChoice(Enum):
    INTERNAL = 'Внутренний'
    EXTERNAL = 'Внешний'


class DigitalFormatChoice(Enum):
    DIGITAL = 'Цифровой'
    NON_DIGITAL = 'Не цифровой'
