class Creature():

    def __init__(self, coordinate: tuple[int]):
        """Initializer of Creature object

        Args:
            coordinate (tuple[int]): coordinate of the creature (x-axis, y-axis)
        """
        self.coordinate = coordinate
        self.age = 0

class Fish(Creature):

    def __init__(self, coordinate: tuple[int]):
        """Initializer of Fish object

        Args:
            coordinate (tuple[int]): coordinate of the creature (x-axis, y-axis)
        """
        super().__init__(coordinate)
    
    def __repr__(self) -> str:
        """Return a string that represents this object

        Returns:
            str: Return an string representation of the Fish object
        """
        attrs = ', '.join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"

class Shark(Creature):

    def __init__(self, coordinate: tuple[int], initial_energy):
        """Initializer of Fish object

        Args:
            coordinate (tuple[int]): coordinate of the creature (x-axis, y-axis)
        """
        super().__init__(coordinate)
        self.shark_energy = initial_energy

    def __repr__(self) -> str:
        """Return a string that represents this object

        Returns:
            str: Return an string representation of the Shark object
        """
        attrs = ', '.join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"
