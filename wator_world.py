import creatures
import random
import termcolor
from termcolor import colored, cprint

#region Class
class WatorWorld():
    world_map = []
    school_of_fish = []
    school_of_shark = []

    nb_fish = 0
    nb_shark = 0

    birth_fish = 0
    birth_shark = 0

    dead_fish = 0
    dead_shark = 0

    #region Constantes
    __CONST_WATER = 0
    __CONST_FISH = 1
    __CONST_SHARK = 2


    #marge de déplacement pour les créatures
    __RANGE_MOVEMENT = 3

    def __init__(self, dim_map_x, dim_map_y, number_of_fish, number_of_shark, CONST_FISH_MATURITY=3, CONST_SHARK_MATURITY=7,  CONST_SHARK_INITIAL_ENERGY=5):
        """Initializer of WatorWorld object

        Args:
            dim_map_x (_type_): world dimension x-axis
            dim_map_y (_type_): world dimension y-axis
            number_of_fish (_type_): number of fishes on the world map at the beginning
            number_of_shark (_type_): number of sharks on the world map at the beginning
        """ 
        self.__dim_map_x = dim_map_x
        self.__dim_map_y = dim_map_y
        self.nb_fish = number_of_fish
        self.nb_shark = number_of_shark
        self.__CONST_FISH_MATURITY = CONST_FISH_MATURITY
        self.__CONST_SHARK_MATURITY = CONST_SHARK_MATURITY
        self.__CONST_SHARK_INITIAL_ENERGY = CONST_SHARK_INITIAL_ENERGY

        self.__initialization(number_of_fish, number_of_shark)
    
    def __initialization(self, number_of_fish: int, number_of_shark: int) -> None:
        """Initialize world map at the dimension x-axis & y-axis with water and populate the world of creatures

        Args:
            number_of_fish (int): number of fish on world map at the beginning
            number_of_shark (int): number of shark on world map at the beginning
        """
        self.initialize_world_map()
        if number_of_fish + number_of_shark <= self.__dim_map_x * self.__dim_map_y - self.__RANGE_MOVEMENT:
            self.add_creatures_to_world_map(number_of_fish, number_of_shark)
        else:
            print("Trop de créature pour la world map")

    def initialize_world_map(self) -> None:
        """Initialize world map at the dimension x-axis & y-axis with water
        """
        self.world_map = [[self.__CONST_WATER for _ in range(self.__dim_map_x)] for _ in range(self.__dim_map_y)]


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
        #contiendra toutes les coordonnées dispo de la map
        #contient tuple index x et index y
        list_temp = []
        for index_x, list in enumerate(self.world_map):
            for index_y, _ in enumerate(list):
                if self.world_map[index_x][index_y] == self.__CONST_WATER:
                    list_temp.append((index_x, index_y))

        # coordonnée aléatoire qui part de 0 jusqu'à la fin de la list_temp.
        # retire à l'index le contenu
        for _ in range(number_of_fish):
            self.add_fish(list_temp.pop(random.randint(0, len(list_temp)-1)))
            
    def add_fish(self, position: tuple) -> bool:
        """Adding one fish

        Args:
            position (tuple): coordinate of the fish

        Returns:
            bool: successfully added
        """
        fish = creatures.Fish(position)
        if self.world_map[position[0]][position[1]] == self.__CONST_WATER:
            self.set_param_to_position(self.__CONST_FISH, position)
            self.school_of_fish.append(fish)
            return True
        return False

    def add_sharks(self, number_of_shark: int) -> None:
        """Adding all the shark

        Args:
            number_of_shark (int): number of shark to add to the world map
        """
        #position = tuple of coordinates (x,y)
        # for _ in range(number_of_shark):
        #     x = random.randint(0, self.__dim_map_x -1)
        #     y = random.randint(0, self.__dim_map_y -1)
        #     position = (x,y)
        #     if self.is_position_free(position):
        #         self.add_shark(position)
        
        list_temp = []
        #contiendra toutes les coordonnées dispo de la map
        #contient tuple index x et index y
        for index_x, list in enumerate(self.world_map):
            for index_y, _ in enumerate(list):
                if self.world_map[index_x][index_y] == self.__CONST_WATER:
                    list_temp.append((index_x,index_y))

        # coordonnée aléatoire qui part de 0 jusqu'à la fin de la list_temp.
        # retire à l'index le contenu
        for _ in range(number_of_shark):
            self.add_shark(list_temp.pop(random.randint(0,len(list_temp)-1)))

    def add_shark(self, position: tuple) -> bool:
        """Adding one shark

        Args:
            position (tuple): coordinate of the shark

        Returns:
            bool: successfully added
        """
        shark = creatures.Shark(position,self.__CONST_SHARK_INITIAL_ENERGY)
        if self.world_map[position[0]][position[1]] == self.__CONST_WATER:
            self.set_param_to_position(self.__CONST_SHARK,position)
            self.school_of_shark.append(shark)
            return True
        return False
    
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
        for shark in self.school_of_shark:
            self.move_shark(shark)

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
        if not prey_list == []:
            prey_position = self.choice_of_prey(prey_list)
        else:
            #random() move: north, east, west, south
            # coordenate_x = random.randint(0,1)
            # coordenate_y = (0 if coordenate_x == 1 else 1)
            # random_coordinate = (coordenate_x, coordenate_y)
            list_prey_position = self.check_presence_water(shark)
            prey_position = list_prey_position[random.randint(0,len(list_prey_position)-1)]
        #print(f"shark:coordinate={shark.coordinate} : decision_position= {prey_position}")
        #Move to prey
        current_position = shark.coordinate
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
        return shark.energy > 0

    def check_presence_prey(self, shark: creatures.Shark) -> list[tuple]:
        """Check if there is available prey

        Args:
            shark (creatures.Shark): the shark that will hunt

        Returns:
            list[tuple]: list of each prey coordinate
        """
        prey_list = []

        #Create var to check prey presence
        check_preysence_north = (shark.coordinate[0], (shark.coordinate[1]-1) % (self.__dim_map_y))
        check_preysence_south = (shark.coordinate[0], (shark.coordinate[1]+1) % (self.__dim_map_y))
        check_preysence_east = ((shark.coordinate[0]+1) % (self.__dim_map_x), shark.coordinate[1])
        check_preysence_west = ((shark.coordinate[0]-1) % (self.__dim_map_x), shark.coordinate[1])

        if self.world_map[check_preysence_north[0]][check_preysence_north[1]] == self.__CONST_FISH:
            prey_list.append(check_preysence_north)
        if self.world_map[check_preysence_south[0]][check_preysence_south[1]] == self.__CONST_FISH:
            prey_list.append(check_preysence_south)
        if self.world_map[check_preysence_east[0]][check_preysence_south[1]] == self.__CONST_FISH:
            prey_list.append(check_preysence_east)
        if self.world_map[check_preysence_west[0]][check_preysence_west[1]] == self.__CONST_FISH:
            prey_list.append(check_preysence_west)

        #print(f"prey_list= {prey_list}")
        return prey_list
    
    def choice_of_prey(self, prey_list: list[tuple]) -> tuple:
        """Choose one prey to hunt

        Args:
            prey_list (list[tuple]): list of each prey coordinate

        Returns:
            tuple: coordinate of one prey
        """
        return prey_list[random.randint(0, len(prey_list)-1)]

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
        self.kill_fish(prey_position,shark)
        #Update school_of_shark
        shark.coordinate = prey_position
        shark.energy -= 1
        #Create baby shark if the shark is mature
        if self.is_shark_mature(shark):
            self.make_baby_shark(current_position)
    
    def kill_fish(self, prey_position: tuple[int], shark: creatures.Shark) -> creatures.Fish:
        """Delete the fish in the fish list

        Args:
            prey_position (tuple[int]): the fish coordinate

        Returns:
            bool: index of the fish to kill
        """
        index = None
        for i, fish in enumerate(self.school_of_fish):
            if fish.coordinate == prey_position:
                index = i
        if index is not None:
            fish_killed = self.school_of_fish.pop(index)   
            if fish_killed:
                shark.energy = self.__CONST_SHARK_INITIAL_ENERGY
                self.dead_fish += 1
                
            return fish_killed

    def kill_shark(self, shark_position: tuple[int]) -> bool:
        """Delete the shark in the shark list if not enough energy

        Args:
            shark_position (tuple[int]): the shark coordinate

        Returns:
            bool: condition if the shark is delete
        """
        #update list
        for i, shark in enumerate(self.school_of_shark):
            if shark.coordinate == shark_position:
                index = i
        self.school_of_shark.pop(index)
        #update world map
        self.set_param_to_position(self.__CONST_SHARK, shark_position)
        
    def move_shark_to_position(self, current_position: tuple[int], prey_position: tuple[int]) -> None:
        """Shark's movement on a position

        Args:
            current_position (tuple[int]): the shark coordinate
            prey_position (tuple[int]): the prey coordinate
        """
        #update shark futur position
        self.set_param_to_position(self.__CONST_SHARK, prey_position)
        #update shark past position
        self.set_param_to_position(self.__CONST_WATER, current_position)

    def set_param_to_position(self, param: int, position: tuple[int]) -> None:
        """Update coordinate of the world map position

        Args:
            param (int): symbol of the creature or water
            position (tuple[int]): coordinate to update
        """
        self.world_map[position[0]][position[1]] = param

    def iterate(self):
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
        self.school_of_shark.append(creatures.Shark(current_position, self.__CONST_SHARK_INITIAL_ENERGY))
        #Update world map coordinate
        self.set_param_to_position(self.__CONST_SHARK, current_position)

    def is_shark_mature(self, shark: creatures.Shark) -> bool:
        """Verify if the shark is mature to create baby

        Args:
            shark (creatures.Shark): the shark to check

        Returns:
            bool: condition if the shark is mature
        """
        return shark.age % self.__CONST_SHARK_MATURITY == 0 if not shark.age == 0 else False

    def move_fishes(self):
        """Move all the fishes one by one
        """
        #loop on each fish object of self.school_of_fish

        for fish in self.school_of_fish:
            self.move_fish(fish)
    
    def check_presence_water(self, creature:creatures.Creature) -> list[tuple]:
        water_list = []
        check_preysence_north = (creature.coordinate[0], (creature.coordinate[1]-1) % (self.__dim_map_y))
        check_preysence_south = (creature.coordinate[0], (creature.coordinate[1]+1) % (self.__dim_map_y))
        check_preysence_east = ((creature.coordinate[0]+1) % (self.__dim_map_x), creature.coordinate[1])
        check_preysence_west = ((creature.coordinate[0]-1) % (self.__dim_map_x), creature.coordinate[1])

        if self.world_map[check_preysence_north[0]][check_preysence_north[1]] == self.__CONST_WATER:
            water_list.append(check_preysence_north)
        if self.world_map[check_preysence_south[0]][check_preysence_south[1]] == self.__CONST_WATER:
            water_list.append(check_preysence_south)
        if self.world_map[check_preysence_east[0]][check_preysence_south[1]] == self.__CONST_WATER:
            water_list.append(check_preysence_east)
        if self.world_map[check_preysence_west[0]][check_preysence_west[1]] == self.__CONST_WATER:
            water_list.append(check_preysence_west)
        return water_list

    def choice_of_destination(self, water_list:list[tuple]) -> tuple:
        return water_list[random.randint(0, len(water_list)-1)]

    def move_fish(self, fish: creatures.Fish) -> bool:
        """Movement of a fish

        Args:
            fish (creatures.Fish): the fish that will move

        Returns:
            bool: condition if fish move
        """
        #Verify water availability
        water_list = []
        water_list = self.check_presence_water(fish)
        if water_list:
            #Choice water position
            water_position = self.choice_of_destination(water_list)
            #print(f"fish:coordinate={fish.coordinate} : water_position= {water_position}")

            #Move to water coordinate
            current_position = fish.coordinate
            self.move_to_destination(fish, current_position, water_position)

    def move_to_destination(self, fish: creatures.Fish, current_position: tuple, water_position: tuple) -> None:
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
        fish.coordinate = water_position

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
        self.set_param_to_position(self.__CONST_FISH, water_position)
        #update fish past position
        self.set_param_to_position(self.__CONST_WATER, current_position)  

    def make_baby_fish(self, current_position: tuple[int])-> None:
        """Create a new fish on wator world

        Args:
            current_position (tuple[int]): position of the new fish
        """
        #Create new fish and add to the list school_of_fish
        self.school_of_fish.append(creatures.Fish(current_position))
        #Update world map coordinate
        self.set_param_to_position(self.__CONST_FISH, current_position)


    def is_fish_mature(self, fish: creatures.Fish) -> bool:
        """Verify if the fish is mature to create baby

        Args:
            fish (creatures.Fish): the fish to check

        Returns:
            bool: condition if the fish is mature
        """
        return fish.age % self.__CONST_FISH_MATURITY == 0 if not fish.age == 0 else False

    def display_affichage(self, __CONST_WATER, __CONST_FISH, __CONST_SHARK):
        __CONST_WATER = termcolor.colored("~", "blue")
        __CONST_FISH = termcolor.colored("1", "white")
        __CONST_SHARK = termcolor.colored("2", "red")

def main():
    my_world_map = WatorWorld(20,20,20, 3)
    for i in my_world_map.world_map :
        for j in i :
            print(f"{j}", end =" ")
        print()

    print()

    #nb d'iteration
    for _ in range(5):  
        my_world_map.iterate()
        for i in my_world_map.world_map:
            for j in i:
                print(f"{j}", end=" ")
            print()
        print()

if __name__ == "__main__":
    main()
