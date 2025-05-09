import creatures

#region Class
class WatorWorld():
    world_map = []
    school_of_fish = []
    school_of_shark = []

    #region Constantes
    __CONST_WATER = 0
    __CONST_FISH = 1
    __CONST_SHARK = 2

    __CONST_FISH_MATURITY = 3
    __CONST_SHARK_MATURITY = 7
    __CONST_SHARK_INITIAL_ENERGY = 5

    def __init__(self, dim_map_x, dim_map_y, number_of_fish, number_of_shark):
        """Initializer of WatorWorld object

        Args:
            dim_map_x (_type_): world dimension x-axis
            dim_map_y (_type_): world dimension y-axis
            number_of_fish (_type_): number of fishes on the world map at the beginning
            number_of_shark (_type_): number of sharks on the world map at the beginning
        """ 
        self.__dim_map_x = dim_map_x
        self.__dim_map_y = dim_map_y

        self.__initialization(number_of_fish, number_of_shark)
    
    def __initialization(self, number_of_fish: int, number_of_shark: int) -> None:
        """Initialize world map at the dimension x-axis & y-axis with water and populate the world of creatures

        Args:
            number_of_fish (int): number of fish on world map at the beginning
            number_of_shark (int): number of shark on world map at the beginning
        """
        self.initialize_world_map()
        self.add_creatures_to_world_map(number_of_fish, number_of_shark)

    def initialize_world_map(self) -> None:
        """Initialize world map at the dimension x-axis & y-axis with water
        """
        self.world_map = [[self.__CONST_WATER for _ in range(self.__dim_map_x)]for _ in range(self.__dim_map_y)]
        for i in self.world_map :
            for j in i :
                print(f"{j}", end =" ")
            print()

    def add_creatures_to_world_map(self, number_of_fish: int, number_of_shark: int) -> None:
        """Populate world map of creatures

        Args:
            number_of_fish (int): number of fish on world map at the beginning
            number_of_shark (int): number of shark on world map at the beginning
        """
        self.add_fishes(number_of_fish)
        self.add_sharks(number_of_shark)

    def add_fishes(self, number_of_fish: int) -> None:
        """Adding all the fish 

        Args:
            number_of_fish (int): number of fish to add to the world map
        """
        #position = tuple of coordinates (x,y)
        position = ()
        if self.is_position_free(position):
            self.add_fish(position)
        
        pass

    def add_fish(self, position: tuple) -> bool:
        """Adding one fish

        Args:
            position (tuple): coordinate of the fish

        Returns:
            bool: successfully added
        """
        x, y = position
        if self.world_map[y][x] == self.__CONST_WATER:
            self.world_map[y][x] == self.__CONST_FISH
            self.school_of_fish.append(position)
            return True
        return False   
        
        #update school_of_fish
        #update world map

    def add_sharks(self, number_of_shark: int) -> None:
        """Adding all the shark

        Args:
            number_of_shark (int): number of shark to add to the world map
        """
        #position = tuple of coordinates (x,y)
        position = ()
        if self.is_position_free(position):
            self.add_shark(position)
        pass

    def add_shark(self, position: tuple) -> bool:
        """Adding one shark

        Args:
            position (tuple): coordinate of the shark

        Returns:
            bool: successfully added
        """
        self.school_of_shark
        #update school_of_fish
        #update world map
        pass
    
    def is_position_free(self, position: tuple) -> bool:
        """Check whether the position is free

        Args:
            position (tuple): coordinate on the world map

        Returns:
            bool: condition if position is free or not
        """
        x, y = position
        return self.world_map[y][x] == self.__CONST_WATER
    #condition position is free or not

    def move_sharks(self) -> None:
        """Move all the sharks one by one
        """
        #loop on each shark object of self.school_of_shark
        self.move_shark(self, shark)

    def move_shark(self, shark: creatures.Shark) -> bool:
        """Movement of a shark

        Args:
            shark (creatures.Shark): the shark that will move

        Returns:
            bool: condition if shark move
        """
        #Verify prey availability
        prey_list = self.check_presence_prey(shark)
        #Choice prey if prey_list not null else random() move
        if not prey_list:
            prey_position = self.choice_of_prey(prey_list)
        else:
            #random() move: north, east, west, south
            random_coordinate = ()
            prey_position = random_coordinate
        #Move to prey
        #current_position = shark position
        self.move_to_prey(shark, current_position, prey_position)
        
        #Verify energy shark
        if not self.is_shark_still_alive(shark):
            self.kill_shark

    def is_shark_still_alive(self, shark) -> bool:
        """Vérify if the shark have enough energy

        Args:
            shark (_type_): _description_

        Returns:
            bool: _description_
        """
        return shark.energy >= 0

    def check_presence_prey(self, shark) -> list[tuple]:
        """Check if there is available prey

        Args:
            shark (creatures.Shark): the shark that will hunt

        Returns:
            list[tuple]: list of each prey coordinate
        """
        prey_list = []
        return prey_list
    
    def choice_of_prey(self, prey_list: list[tuple]) -> tuple:
        """Choose one prey to hunt

        Args:
            prey_list (list[tuple]): list of each prey coordinate

        Returns:
            tuple: coordinate of one prey
        """
        #random on one prey to hunt
        pass

    def move_to_prey(self, shark: creatures.Shark, current_position: tuple, prey_position: tuple) -> bool:
        """Shark's movement on its prey

        Args:
            shark (creatures.Shark): the shark that will move
            current_position (tuple): the shark coordinate
            prey_position (tuple): the prey coordinate

        Returns:
            bool: condition if the shark move
        """
        #Shark movement on the world map
        self.move_shark_to_position(current_position, prey_position)
        #Delete the prey
        self.kill_fish(prey_position)
        #Update school_of_shark
        pass
        #Create baby shark if the shark is mature
        if self.is_shark_mature(shark):
            self.make_baby_shark(current_position)
        #Verify shark energy
        self.kill_shark(prey_position)
    
    def kill_fish(self, prey_position: tuple[int]) -> int:
        """Delete the fish in the fish list

        Args:
            prey_position (tuple[int]): the fish coordinate

        Returns:
            bool: index of the fish to kill
        """
        index = [i for i, fish in enumerate(self.school_of_fish) if fish.position == prey_position]
        return self.school_of_fish(index)

    def kill_shark(self, shark_position: tuple[int]) -> bool:
        """Delete the shark in the shark list if not enough energy

        Args:
            shark_position (tuple[int]): the shark coordinate

        Returns:
            bool: condition if the shark is delete
        """
        #update list
        #update world map
        pass
        
    def move_shark_to_position(self, current_position: tuple[int], prey_position: tuple[int]) -> None:
        """Shark's movement on a position

        Args:
            current_position (tuple[int]): the shark coordinate
            prey_position (tuple[int]): the prey coordinate
        """
        #update shark futur position
        #update shark past position
        pass

    def set_param_to_position(self, param: int, position: tuple[int]) -> None:
        """Update coordinate of the world map position

        Args:
            param (int): symbol of the creature or water
            position (tuple[int]): coordinate to update
        """
        self.world_map[position[0]][position[1]] = param

    def __iterate(self):
        """Execute one cycle of the world
        """
        self.move_sharks()
        self.move_fishes()
    
    def make_baby_shark(self, current_position: tuple[int]):
        """Create a new shark on wator world

        Args:
            current_position (tuple[int]): position of the new shark
        """
        #Create new shark and add to the list school_of_shark
        self.school_of_shark.append(creatures.Shark(current_position))
        #Update world map coordinate
        self.set_param_to_position(self.__CONST_CREATURE_TYPE_SHARK, current_position)

    def is_shark_mature(self, shark: creatures.Shark) -> bool:
        """Verify if the shark is mature to create baby

        Args:
            shark (creatures.Shark): the shark to check

        Returns:
            bool: condition if the shark is mature
        """
        return shark.age % self.__CONST_SHARK_MATURITY == 0

    def move_fishes(self):
        """Move all the fishes one by one
        """
        #loop on each fish object of self.school_of_fish
        self.move_fish(self, fish)

    def move_fish(self, fish: creatures.Fish) -> bool:
        """Movement of a fish

        Args:
            fish (creatures.Fish): the fish that will move

        Returns:
            bool: condition if fish move
        """
        #Verify water availability
        water_list = self.check_presence_water(fish)
        #Choice water position
        water_position = self.choice_of_water(water_list)
        #Move to water coordinate
        #current_position = water coordinate position
        self.move_to_water(fish, current_position, water_position)

    def move_to_water(self, fish: creatures.Fish, current_position: tuple, water_position: tuple) -> None:
        """Fish's movement on its water coordinate

        Args:
            fish (creatures.Shark): the fish that will move
            current_position (tuple): the fish coordinate
            water_position (tuple): the water coordinate

        Returns:
            bool: condition if the shark move
        """
        #Fish movement on the world map
        self.move_fish_to_position(current_position, water_position)
        #Update school_of_fish
        pass
        #Create baby fish if the fish is mature
        if self.is_fish_mature(fish):
            self.make_baby_fish(current_position)

    def move_fish_to_position(self, current_position: tuple[int], water_position: tuple[int]) -> None:
        """Fish's movement on a position

        Args:
            current_position (tuple[int]): the fish coordinate
            water_position (tuple[int]): the water coordinate
        """
        #update fish futur position
        #update fish past position
        pass

    def make_baby_fish(self, current_position: tuple[int]):
        """Create a new fish on wator world

        Args:
            current_position (tuple[int]): position of the new fish
        """
        #Create new fish and add to the list school_of_fish
        self.school_of_fish.append(creatures.Fish(current_position))
        #Update world map coordinate
        self.set_param_to_position(self.__CONST_CREATURE_TYPE_FISH, current_position)

    def is_fish_mature(self, fish: creatures.Fish) -> bool:
        """Verify if the fish is mature to create baby

        Args:
            fish (creatures.Fish): the fish to check

        Returns:
            bool: condition if the fish is mature
        """
        return fish.age % self.__CONST_SHARK_MATURITY == 0
    
    #Display Waterworld_map
world = WatorWorld(10,10,5,0)

