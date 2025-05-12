from abc import ABC, abstractmethod
# import creatures_abstract as creature


class WaterworldAbstract(ABC):

    const_fish_maturity = 3
    const_shark_maturity = 7
    const_water_symbol = 0
    const_fish_symbol = 1
    const_shark_symbol = 2
    const_energy_shark = 5

    @abstractmethod
    def __init__(self, world_dim_x: int, world_dim_y: int, nb_fish: int, nb_shark: int):
        pass

    @abstractmethod
    def move_shark(self, shark: object) -> None:
        pass

    @abstractmethod
    def move_to_prey(self, shark: object, current_position: tuple, prey_position: tuple)-> None:
        pass

    @abstractmethod
    def move_shark_to_position(self, current_position: tuple, futur_position: tuple)-> None:
        pass

    @abstractmethod
    def kill_fish(self, prey_position: tuple):
        pass

    @abstractmethod
    def make_baby_shark(self, current_position: tuple):
        pass
    
    @property
    @abstractmethod
    def is_shark_mature(self, shark: object) -> bool :
        pass

    @abstractmethod
    def set_param_to_position(self, param: str, position: tuple):
        pass

    @abstractmethod
    def kill_shark(self):
        pass



