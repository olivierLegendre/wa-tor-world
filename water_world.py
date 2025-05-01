import random
import copy as cp
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
        try:
            if nb_fish + nb_fish > (x_size * y_size) / 2:
                print("too many creatures at initialization")
                raise ValueError('Too many creatures')
        except ValueError:
            print(ValueError)
            exit()
        self.world_size_x = x_size
        self.world_size_y = y_size
        self.nb_fish_init = nb_fish
        self.nb_shark_init = nb_shark
        self.sea_map = [[0 for i in range(x_size)] for j in range(y_size)]
        self.populate_with_fish()
        self.populate_with_shark()
        self.set_rules()
        
    def set_rules(self, chronos_to_fish_birth=3, chronos_to_shark_birth=5, starting_shark_energy=3, mode=1) -> None:
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
        fish = creatures.Fish(x, y)
        self.fishes_list.append(fish)
        self.sea_map[x][y] = self.const_fish
                
    def populate_with_shark(self) -> None:
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
        shark = creatures.Shark(x, y, self.starting_shark_energy)
        self.shark_list.append(shark)
        self.sea_map[x][y] = self.const_shark
        
    def pass_one_iteration(self):
        # self.futur_sea_map = self.sea_map.copy()
        # print(f"avant : {self.sea_map}")
        self.fishes_move()
        # print(f"apres : {self.sea_map}")
        self.sharks_move()
        self.clean_dead_creatures()

    def fishes_move(self):
        # my_fishes = copy.copy(self.futur_iteration_sea_map.fishes_list)
        fishes_list = self.fishes_list
        for fish in fishes_list:
            # fish["age"] += fish["age"]
            fish.age = fish.age + 1
            # current_position = fish["position"]
            current_position = tuple()
            current_position = fish.x, fish.y
            # print(f"current position {current_position}")
            futur_position = self.random_move(current_position)
            # print(f"future position : {futur_position}")
            move_ok = self.is_move_possible(futur_position, "fish")
            if move_ok: 
                #if fish give birth
                self.move_fish(fish, current_position, futur_position)
                print(f"age : {fish.age}")
                if fish.age % self.chronos_to_fish_birth == 0:
                    if fish.age != 0:
                        print("reproduction : ")
                        print(f"age du poisson : {fish.age}")
                        print(f" time to sex : {fish.age % self.chronos_to_fish_birth == 0}")
                        self.create_new_fish(current_position[0], current_position[1])
                        # self.create_new_fish(self.futur_iteration_sea_map, current_position[0], current_position[1])
            
                
    def move_fish(self, fish, current_position, futur_position):
        
        # self.futur_iteration_sea_map.sea_world[futur_position[0]][futur_position[1]] = self.futur_iteration_sea_map.const_fish
        # self.futur_iteration_sea_map.sea_world[current_position[0]][current_position[1]] = self.futur_iteration_sea_map.const_water
        self.sea_map[futur_position[0]][futur_position[1]] = self.const_fish
        # print(f"a effacer :{current_position}")
        # print(self.sea_map[current_position[0]][current_position[1]])
        self.sea_map[current_position[0]][current_position[1]] = self.const_water
        # print(self.sea_map[current_position[0]][current_position[1]])
        fish.x, fish.y = futur_position
        # print(fish.x, fish.y)
        
    def random_move(self, position):
        # mode = 1 cross : 1 up 2 right 3 down 4 left
        # mode 2 diagonal : as the numerical keyboard
        new_position = tuple()
        x = self.world_size_x
        y = self.world_size_y
        # print(f"position initiale :{position}")
        if self.mode == 1:
            direction = random.randrange(1, 4)
            # print(f"direction {direction}")
        match direction:
            case 1:
                if position[0] != 0:
                    new_position = (position[0] - 1, position[1])
                else:
                    new_position = (x - 1, position[1])
            case 2:
                if position[1] != y - 1:
                    new_position = (position[0], position[1] + 1)
                else:
                    new_position = (position[0], 0)
            case 3:
                if position[0] != x - 1:
                    new_position = (position[0] + 1, position[1])
                else:
                    new_position = (0, position[1])
            case 4:
                if position[1] != 0:
                    new_position = (position[0], position[1] - 1)
                else:
                    new_position = (position[0], y - 1)
        # print(f"position finale :{new_position}")
        return new_position
    
    def is_move_possible(self, position, animal_type) -> bool:
        legal_destination = list()
        if animal_type == "fish":
            legal_destination.append(0)
        if animal_type == "shark":
            legal_destination.append(0)
            legal_destination.append(1)
        if self.sea_map[position[0]][position[1]] not in legal_destination:
            return False
        else:
            return True

    def clean_dead_creatures(self):
        pass
        

class World_History():
    def __init__(self):
        """init a sea map history 
            containing a dict with sea_map (sea_world.sea_map)
        """
        self.sea_map_history = dict()
        self.generations = 0
        
    def add_sea_map_to_history(self, sea_world: object) -> None:
        """
        Add a sea_map to the history
        Args:
            sea_world ( obj water_world) : sea_world to get sea_map
        """
        #copy to avoid rewriting the same list
        original_map = sea_world.sea_map
        current_map = original_map.copy()
        # current_map = sea_world.sea_map.copy()
        print(f" insertion dans la generation {self.generations} la carte : {current_map}")
        print(f"juste avant insertion: {self.sea_map_history}")
        self.sea_map_history[self.generations] = current_map
        print(f"juste apres insertion: {self.sea_map_history}")
        self.generations += 1
        
    def get_generation(self, generation: int) -> list:
        """Return the sea_map from the generation

        Args:
            generation (int): _description_

        Returns:
            list: a sea_map
        """
        return self.sea_map_history[generation]


def main():
    water_world = Water_World()
    water_world.init_water_world(2, 1, 4, 4)
    sea_map_history = World_History()
    sea_map_history.add_sea_map_to_history(water_world)


if __name__ == "__main__":
    main()