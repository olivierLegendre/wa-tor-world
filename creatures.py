class Creature():
    def __init__(self, x: int, y: int) -> None:
        """
        Generique creature
        Args:
            x (int): X position on water_word map
            y (int): Y_description_X position on water_word map
            age (int, optional): creatures start their life at 0.
        """
        self.x = x
        self.y = y
        self.age = 0
        self.alive = True


class Fish(Creature):
    def __init__(self, x: int, y: int) -> None:
        """
        A fish is a creature
        Args:
            x (int): X position on water_word map
            y (int): Y_description_X position on water_word map
            age (int, optional): creatures start their life at 0. every 3 year the fish reproduce
        """
        Creature.__init__(self, x, y)


class Shark(Creature):
    def __init__(self, x: int, y: int, energy=3) -> None:
        """
        A fish is a creature
        Args:
            x (int): X position on water_word map
            y (int): Y_description_X position on water_word map
            age (int, optional): creatures start their life at 0. every 3 year the fish reproduce
            energy (int, optinal): if a shark energy goes down to 0, it dies
        """
        Creature.__init__(self, x, y)
        self.energy = energy


def main():
    pass


if __name__ == "__main__":
    main()