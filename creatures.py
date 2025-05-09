class Creature():

    def __init__(self, coordinate: tuple[int]):
        """Initializer of Creature object

        Args:
            coordinate (tuple[int]): coordinate of the creature (x-axis, y-axis)
        """
        self.coordinate = coordinate
        self.age = 0

class Fish(Creature):

    __CONST_FISH_MATURITY = 3

    def __init__(self, coordinate: tuple[int]):
        """Initializer of Fish object

        Args:
            coordinate (tuple[int]): coordinate of the creature (x-axis, y-axis)
        """
        super().__init__(coordinate)

    @property
    def get_const_fish_maturity(self) -> int:
        """Get the fish maturity
        Returns:
            int: fish maturity
        """
        return self.__CONST_FISH_MATURITY
    
    def __repr__(self) -> str:
        """Return a string that represents this object

        Returns:
            str: Return an string representation of the Fish object
        """
        attrs = ', '.join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"

class Shark(Creature):

    __CONST_SHARK_MATURITY = 7
    __CONST_SHARK_INITIAL_ENERGY = 5

    def __init__(self, coordinate: tuple[int]):
        """Initializer of Fish object

        Args:
            coordinate (tuple[int]): coordinate of the creature (x-axis, y-axis)
        """
        super().__init__(coordinate)
        energy = self.__CONST_SHARK_INITIAL_ENERGY

    @property
    def get_const_shark_maturity(self) -> int:
        """Get the shark maturity
        Returns:
            int: shark maturity
        """
        return self.__CONST_SHARK_MATURITY

    @property
    def get_const_shark_initial_energy(self) -> int:
        """Get the shark energy
        Returns:
            int: shark energy
        """
        return self.__CONST_SHARK_INITIAL_ENERGY

    def __repr__(self) -> str:
        """Return a string that represents this object

        Returns:
            str: Return an string representation of the Shark object
        """
        attrs = ', '.join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"
