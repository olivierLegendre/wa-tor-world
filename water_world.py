import random
import copy
import creatures


class Water_World():
    def __init__(self) -> None:
        """ create an empty world
        """
        self.world_size_x = int
        self.world_size_y = int
        self.sea_map = list()
        self.fishes_list = list()
        self.shark_list = list()
        # 0 for water
        # 1 for fish
        # 2 for shark
        self.const_water = 0
        self.const_fish = 1
        self.const_shark = 2
        # self.chronos = 0
        # self.world_iteration = list()
        self.chronos_to_fish_birth = 3
        self.chronos_to_shark_birth = 3
        self.starting_shark_energy = 3
    
    def init_water_world(self, nb_fish: int, nb_shark: int, x_size: int, y_size:int) -> None:
        """Populate the world

        Args:
            nb_fish (int): Fish number at the initialization
            nb_shark (int): Shark number at the initialization
            x_size (int): widht of the map
            y_size (int): height of the map
        """
        self.world_size_x = x_size
        self.world_size_y = y_size
        self.nb_fish_init = nb_fish
        self.nb_shark_init = nb_shark
        self.sea_map = [[0 for i in range(x_size)] for j in range(y_size)]
        self.populate_with_fish()
        self.populate_with_shark()
        self.set_rules()
        
    def set_rules(self, chronos_to_fish_birth=3,chronos_to_shark_birth=5, starting_shark_energy=3, mode=1) -> None:
        """Setting some constant

        Args:
            chronos_to_fish_birth (int, optional): _description_. Defaults to 3.
            chronos_to_shark_birth (int, optional): _description_. Defaults to 5.
            starting_shark_energy (int, optional): _description_. Defaults to 3.
            mode (int, optional): _description_. Defaults to 1.
        """
        self.chronos_to_fish_birth = chronos_to_fish_birth
        self.chronos_to_shark_birth = chronos_to_shark_birth
        self.starting_shark_energy = starting_shark_energy
        self.mode = mode

    def populate_with_fish(self) -> None:
        """populate the sea map and fishes_list
        """
        x = random.randrange(0, self.world_size_x)
        y = random.randrange(0, self.world_size_y)
        nb_fish = 0
        while nb_fish < self.nb_fish_init:
            if self.sea_map[x][y] == self.const_water:
                self.create_new_fish(x, y)
                nb_fish += 1
            x = random.randrange(0, self.world_size_x)
            y = random.randrange(0, self.world_size_y)
            
    def create_new_fish(self, x: int, y: int) -> None:
        """create a fish 
            add it to sea map at postion (x, y)
            add it to fishes_list     
        Args:
            x (int): _description_
            y (int): _description_
        """
        fish = creatures.Fish(x, y, 0)
        self.fishes_list.append(fish)
        self.sea_map[x][y] = self.const_fish
                
    def populate_with_shark(self)-> None:
        """populate the sea map and sharks_list
        """
        x = random.randrange(0, self.world_size_x)
        y = random.randrange(0, self.world_size_y)
        nb_shark = 0
        while nb_shark < self.nb_shark_init:
            if self.sea_map[x][y] == self.const_water:
                self.create_new_shark(x, y)
                nb_shark += 1
            x = random.randrange(0, self.world_size_x)
            y = random.randrange(0, self.world_size_y)
            
    def create_new_shark(self, x: int, y: int) -> None:
        """ create a shark 
            add it to sea map at postion (x, y)
            add it to sharks_list
        Args:
            x (int): _description_
            y (int): _description_
        """
        shark = dict()
        shark = creatures.Shark(x, y, 0, self.starting_shark_energy)
        self.shark_list.append(shark)
        self.sea_map[x][y] = self.const_shark
        

class World_History():
    def __init__(self):
        """init a sea map history 
            containing a dict with sea_map (sea_world.sea_map)
        """
        self.sea_map_history = dict()
        self.generations = 0
        
    def add_sea_map_to_history(self, sea_map: list) -> None:
        """
        Add a sea_map to the history
        Args:
            sea_map (sea_word.sea_map): _description_
        """
        self.sea_map_history[self.generations] = sea_map
        
    def get_generation(self, generation: int) -> list:
        """Return the sea_map from the generation

        Args:
            generation (int): _description_

        Returns:
            list: a sea_map
        """
        return self.sea_map_history[generation]


def main():
    pass


if __name__ == "__main__":
    main()