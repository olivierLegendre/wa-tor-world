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
        # self.fishes_list = list()
        self.fishes_list = creatures.Creature_List()
        # self.sharks_list = list()
        self.sharks_list = creatures.Creature_List()
        # 0 for water
        # 1 for fish
        # 2 for shark
        self.const_water = 0
        self.const_fish = 1
        self.const_shark = 2
        self.chronos_to_fish_birth = 3
        self.chronos_to_shark_birth = 7
        self.starting_shark_energy = 5
    
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
        self.set_rules()
        self.world_size_x = x_size
        self.world_size_y = y_size
        self.nb_fish_init = nb_fish
        self.nb_shark_init = nb_shark
        self.sea_map = [[0 for i in range(x_size)] for j in range(y_size)]
        self.populate_with_fish()
        self.populate_with_shark()
        
    def set_rules(self, chronos_to_fish_birth=3, chronos_to_shark_birth=7, starting_shark_energy=5, mode=1) -> None:
        """Setting some constant

        Args:
            chronos_to_fish_birth (int, optional): _description_. Defaults to 3.
            chronos_to_shark_birth (int, optional): _description_. Defaults to 7.
            starting_shark_energy (int, optional): _description_. Defaults to 5.
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
        self.fishes_list.add(fish)
        self.sea_map[x][y] = self.const_fish
                
    def populate_with_shark(self) -> None:
        """populate the sea map and sharks_list
        """
        x = random.randrange(0, self.world_size_x)
        y = random.randrange(0, self.world_size_y)
        nb_shark = 0
        while nb_shark < self.nb_shark_init:
            if self.sea_map[x][y] == self.const_water:
                self.create_new_shark(x, y, self.starting_shark_energy)
                nb_shark += 1
            x = random.randrange(0, self.world_size_x)
            y = random.randrange(0, self.world_size_y)
            
    def create_new_shark(self, x: int, y: int, energy:int) -> None:
        """ create a shark 
            add it to sea map at postion (x, y)
            add it to sharks_list
        Args:
            x (int): _description_
            y (int): _description_
        """
        shark = dict()
        shark = creatures.Shark(x, y, energy)
        self.sharks_list.list().append(shark)
        self.sea_map[x][y] = self.const_shark
        
    def pass_one_iteration(self) -> None:
        """ method use to make the world evolve one chronos
            we make all the fishes move
            we make all the sharks move
            we clean the dead creatures from sharks_list and fishes_list
        """
        self.fishes_move()
        self.sharks_move()
        self.clean_dead_creatures()

    def fishes_move(self) -> None:
        """ we move every fish on fishes_list
            movement is possible if there is a free space nearby
            every chronos_to_fish_birth chronos, a fish give birth to another fish
        """
        fishes_list = self.fishes_list
        for fish in fishes_list.list():
            fish.age = fish.age + 1
            current_position = tuple()
            current_position = fish.x, fish.y
            futur_position = self.random_move(current_position)
            move_ok = self.is_move_possible(futur_position, "fish")
            if move_ok: 
                #if fish give birth
                self.move_fish(fish, current_position, futur_position)
                # print(f"age : {fish.age}")
                if fish.age % self.chronos_to_fish_birth == 0:
                    if fish.age != 0:
                        # print("reproduction : ")
                        # print(f"age du poisson : {fish.age}")
                        # print(f" time to sex : {fish.age % self.chronos_to_fish_birth == 0}")
                        self.create_new_fish(current_position[0], current_position[1])
                        # self.create_new_fish(self.futur_iteration_sea_map, current_position[0], current_position[1])

    def move_fish(self, fish: object, current_position : tuple, futur_position: tuple) -> None:
        """We move a single fish
        Args:
            fish (object): a fish object
            current_position (tuple):   x y
            futur_position (tuple): x y
        """
        self.sea_map[futur_position[0]][futur_position[1]] = self.const_fish
        self.sea_map[current_position[0]][current_position[1]] = self.const_water
        fish.x, fish.y = futur_position
        
    def sharks_move(self):
        """we move every fish on fishes_list
            movement is possible if there is a free space nearby
            if there is a fish nearby, it is prioritized
            every chronos_to_shark_birth chronos, a shark give birth to another shark
            if a shark reach 0 energy, he dies from hunger
        """
        sharks_list = self.sharks_list
        for shark in sharks_list.list():
            # shark["age"] += shark["age"]
            # print(f"shark energy {shark.energy}")
            shark.age = shark.age + 1
            shark.energy = shark.energy - 1
            # current_position = shark["position"]
            current_position = tuple()
            current_position = shark.x, shark.y
            futur_position = tuple()
            move_ok = False
            if self.get_prey_positions(current_position):
                if self.select_prey_to_kill():
                    prey_position = self.prey
                    self.hunt_prey(shark, current_position, prey_position)
                    # self.kill_fish_by_position(self.prey)
                    futur_position = prey_position
                    move_ok = True
                # print("time to eat !!")
            else:
                # print(f"current position {current_position}")
                futur_position = self.random_move(current_position)
                move_ok = self.is_move_possible(futur_position, "shark")
                
            # print(f"future position : {futur_position}")
            # print(f"future position state: {self.sea_map[futur_position[0]][futur_position[1]]}")
            
            # print(f"je suis avant move ok {move_ok}")
            
            if move_ok: 
                #if shark give birth
                # print(f"age : {shark.age}")
                self.move_shark(shark, current_position, futur_position)
                
                if shark.age % self.chronos_to_shark_birth == 0:
                    if shark.age != 0:
                        # print("reproduction : ")
                        # print(f"age du requin : {shark.age}")
                        # print(f" time to sex : {shark.age % self.chronos_to_shark_birth == 0}")
                        self.create_new_shark(current_position[0], current_position[1], self.starting_shark_energy)
                        
            if shark.energy < 1:
                print("je suis mort")
                self.kill_shark_from_hunger(shark, futur_position)
            else:
                # print("toujours vivant")
                pass
                
    def move_shark(self, shark: object, current_position: tuple, futur_position: tuple) -> None:
        """we move a single shark

        Args:
            shark (object): shark object
            current_position (tuple): x y 
            futur_position (tuple): x y 
        """
        self.sea_map[futur_position[0]][futur_position[1]] = self.const_shark
        self.sea_map[current_position[0]][current_position[1]] = self.const_water
        shark.x, shark.y = futur_position
        
    def hunt_prey(self, shark: object, current_position: tuple, prey_position: tuple) -> None:
        """a shark move to the space of a fish
            the shark reagains it's energy
            the fish is killed
        Args:
            shark (object): shark object
            current_position (tuple): x y
            prey_position (tuple): x y
        """
        self.sea_map[prey_position[0]][prey_position[1]] = self.const_shark
        self.sea_map[current_position[0]][current_position[1]] = self.const_water
        shark.x, shark.y = prey_position
        shark.energy = self.starting_shark_energy
        self.kill_fish_by_position(prey_position)
        
    def kill_fish_by_position(self, position: tuple) -> None:
        """we modify the killed fish by putting fish.alive to False
            clean_dead_creatures() will take care of it
        Args:
            position (tuple): x y
        """
        fishes_list = self.fishes_list
        dead_fish_list = [fish for fish in fishes_list.list() if fish.x == position[0] and fish.y == position[1]]
        dead_fish = dead_fish_list[0]
        dead_fish.alive = False
        
    def kill_shark_from_hunger(self, shark: object, position: tuple) -> None:
        """the shark dis from hunger
            shark.alive is put to false
            clean_dead_creatures() will take care of it
        Args:
            shark (object): shark object
            position (tuple): x y
        """
        shark.alive = False
        self.sea_map[position[0]][position[1]] = self.const_water
        
    def random_move(self, position: tuple) -> None:
        """move a creature in a random direction
            for now, the mode is 1 meaning the direction is choosen as follows
             1: up 2: right 3: down 4: left
             the world is a tor, so going up all the way actually make you reappear in the bottom, etc
        Args:
            position (tuple): x y 

        Returns:
            new_position (tuple): the position the creature will try to move to
        """
        # mode = 1 cross : 1 up 2 right 3 down 4 left
        # mode 2 diagonal : as the numerical keyboard
        new_position = tuple()
        x = self.world_size_x
        y = self.world_size_y
        if self.mode == 1:
            direction = random.randrange(1, 4)
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
    
    def get_prey_positions(self, position: tuple) -> bool:
        """ look around a shark in all 4 directions to spot a fish (a 1)

        Args:
            position (tuple): the shark position

        Returns:
            bool: return True if they are preys
        """
        #check up,down, left, right
        # up, down, left, right = int
        x = self.world_size_x
        y = self.world_size_y
        
        if position[0] != 0:
            up = (position[0] - 1, position[1])
        else:
            up = (x - 1, position[1])

        if position[1] != y - 1:
            left = (position[0], position[1] + 1)
        else:
            left = (position[0], 0)

        if position[0] != x - 1:
            down = (position[0] + 1, position[1])
        else:
            down = (0, position[1])

        if position[1] != 0:
            right = (position[0], position[1] - 1)
        else:
            right = (position[0], y - 1)
            
        positions_to_check = list([up, down, left, right])
        prey_positions = list()
        
        for position in positions_to_check:
            if self.sea_map[position[0]][position[1]] == self.const_fish:
                prey_positions.append(position)
        self.prey_positions = prey_positions
        return True if len(prey_positions) > 0 else False
    
    def select_prey_to_kill(self) -> None:
        """select a prey at random if there is multiple fishes around the shark

        Returns:
            none
        """
        if len(self.prey_positions) > 0:
            index_to_select = random.randrange(0, len(self.prey_positions))
            self.prey = self.prey_positions[index_to_select]
            return True
        else:
            print('error no prey around')
            return False
    
    def is_move_possible(self, position: tuple, animal_type: str) -> bool:
        """check is the destination of a move is valid
            for a fish only water is valid (0)
            for a shark, both water (0) and fish (1) are valid
        Args:
            position (tuple): x y, position of the creature
            animal_type (str): "fish" or "shark"

        Returns:
            bool: _description_
        """
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

    def clean_dead_creatures(self) -> None:
        """we browse a creature_list to delete every dead creature
            we start from the bottom to avoid modifying the index while we could delete another creature
        """
        self.fishes_list.clean()
        self.sharks_list.clean()
        
        # fishes_list = self.fishes_list
        # indexes_fish_to_delete = list()
        
        # for index_fish in range(len(fishes_list)):
        #     fish = fishes_list[index_fish]
        #     if fish.alive is False:
        #         indexes_fish_to_delete.append(index_fish)
        
        # for index_fish_to_delete in indexes_fish_to_delete[::-1]:
        #     del (fishes_list[index_fish_to_delete])
            
        # sharks_list = self.sharks_list
        # indexes_shark_to_delete = list()
        # for index_shark in range(len(sharks_list)):
        #     shark = sharks_list[index_shark]
        #     if shark.alive is False:
        #         indexes_shark_to_delete.append(index_shark)
                
        # for index_shark_to_delete in indexes_shark_to_delete[::-1]:
        #     del (sharks_list[index_shark_to_delete])
        

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
        self.sea_map_history[self.generations] = current_map
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