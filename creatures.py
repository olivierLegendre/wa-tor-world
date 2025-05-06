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
    def __init__(self, x: int, y: int, energy=5) -> None:
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


class Creature_List():
    def __init__(self):
        self.c_list = list()
        self.nb_creatures = 0
        
    def add(self, creature):
        self.c_list.append(creature)
        self.nb_creatures += self.nb_creatures + 1
        
    def list(self):
        return self.c_list
    
    def clean(self) -> None:
        """we browse a creature_list to delete every dead creature
            we start from the bottom to avoid modifying the index while we could delete another creature
        """
        creatures_list = self.c_list
        indexes_creature_to_delete = list()
        
        for index_creature in range(len(creatures_list)):
            creature = creatures_list[index_creature]
            if creature.alive is False:
                indexes_creature_to_delete.append(index_creature)
        
        for index_creature_to_delete in indexes_creature_to_delete[::-1]:
            # print(creatures_list[index_creature_to_delete])
            del (creatures_list[index_creature_to_delete])
            
    def creature_in_list(self, position):
        return [creature for creature in self.c_list if creature.x == position[0] and creature.y == position[1]]
        
    def is_fish(self, position):
        creatures = self.creature_in_list(position)
        if len(creatures) == 0:
            print("creature vide")
            return position
        else:
            creature = creatures[0]
            if not isinstance(creature, Fish):
                return False
            else:
                return True

    def is_shark(self, position):
        creatures = self.creature_in_list(position)
        if len(creatures) == 0:
            print("creature vide")
            return position
        else:
            creature = creatures[0]
            if not isinstance(creature, Shark):
                return False
            else:
                return True

def main():
    pass


if __name__ == "__main__":
    main()