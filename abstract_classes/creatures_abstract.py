from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def __init__(self):
        pass


class Fish(Creature):
    def __init__(self):
        pass


class Shark(Creature):
    def __init__(self):
        pass
