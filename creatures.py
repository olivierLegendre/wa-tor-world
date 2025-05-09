class Creature():
    
    def __init__(self, coordinate: tuple[int]):
        """Initializer of Creatures object

        Args:
            coordinate (tuple[int]): coordinate of the creature
        """
        self.coordinate = coordinate

class Fish(Creature):

    __CONST_FISH_MATURITY = 3

    def __init__(self, coordinate):
        super().__init__(coordinate)

    @property
    def fish_maturity(self) -> int:
        """Get the fish maturity

        Returns:
            int: fish maturity
        """
        return self.__CONST_FISH_MATURITY
    
    @fish_maturity.setter
    def fish_maturity(self, fish_maturity: int) -> None:
        """Set the fish maturity

        Args:
            fish_maturity (int): fish maturity
        """
        self.__CONST_FISH_MATURITY = fish_maturity
    
    def __repr__(self):
        attrs = ', '.join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"

class Shark(Creature):

    __CONST_SHARK_MATURITY = 7

    def __init__(self, coordinate):
        super().__init__(coordinate)
