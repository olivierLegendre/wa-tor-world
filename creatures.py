class Creature():
    
    def __init__(self, coordinate: tuple[int]):
        """Initializer of Creature object

        Args:
            coordinate (tuple[int]): coordinate of the creature (x-axis, y-axis)
        """
        # à voir si besoin de privé ou protected
        self.coordinate = coordinate

class Fish(Creature):

    __CONST_FISH_MATURITY = 3

    def __init__(self, coordinate: tuple[int]):
        """Initializer of Fish object

        Args:
            coordinate (tuple[int]): coordinate of the creature (x-axis, y-axis)
        """
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
        """Return a string that represents this object

        Returns:
            str: Return an string representation of the Fish object
        """
        attrs = ', '.join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"

class Shark(Creature):

    __CONST_SHARK_MATURITY = 7
    __CONST_SHARK_ENERGY = 5

    def __init__(self, coordinate: tuple[int]):
        """Initializer of Fish object

        Args:
            coordinate (tuple[int]): coordinate of the creature (x-axis, y-axis)
        """
        super().__init__(coordinate)

    @property
    def shark_maturity(self) -> int:
        """Get the shark maturity

        Returns:
            int: shark maturity
        """
        return self.__CONST_FISH_MATURITY
    
    @shark_maturity.setter
    def shark_maturity(self, shark_maturity: int) -> None:
        """Set the shark maturity

        Args:
            shark_maturity (int): shark maturity
        """
        self.__CONST_FISH_MATURITY = shark_maturity
    
    @property
    def shark_energy(self) -> int:
        """Get the shark energy

        Returns:
            int: shark energy
        """
        return self.__CONST_FISH_ENERGY
    
    @shark_energy.setter
    def shark_energy(self, shark_energy: int) -> None:
        """Set the shark energy

        Args:
            shark_energy (int): shark energy
        """
        self.__CONST_FISH_ENERGY = shark_energy
    

    def __repr__(self) -> str:
        """Return a string that represents this object

        Returns:
            str: Return an string representation of the Shark object
        """
        attrs = ', '.join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"
