import creatures
import random
import termcolor
from termcolor import colored, cprint
import time

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

    def __init__(self, dim_map_x, dim_map_y, number_of_fish, number_of_shark, CONST_FISH_MATURITY=3, CONST_SHARK_MATURITY=10,  CONST_SHARK_INITIAL_ENERGY=5):
        """Initializer of WatorWorld object

        Args:
            dim_map_x (_type_): world dimension x-axis
            dim_map_y (_type_): world dimension y-axis
            number_of_fish (_type_): number of fishes on the world map at the beginning
            number_of_shark (_type_): number of sharks on the world map at the beginning
            CONST_FISH_MATURITY (int, optional): maturity of the fish. Defaults to 3.
            CONST_SHARK_MATURITY (int, optional): maturity of the shark. Defaults to 10.
            CONST_SHARK_INITIAL_ENERGY (int, optional): initial energy of the shark. Defaults to 5.
        """
        self.__dim_map_x = dim_map_x
        self.__dim_map_y = dim_map_y
        self.nb_fish = number_of_fish
        self.nb_shark = number_of_shark
        self.CONST_FISH_MATURITY = CONST_FISH_MATURITY
        self.CONST_SHARK_MATURITY = CONST_SHARK_MATURITY
        self.CONST_SHARK_INITIAL_ENERGY = CONST_SHARK_INITIAL_ENERGY

        self.__initialization(number_of_fish, number_of_shark)

#######
#region init_world_map
#######

    def __initialization(self, number_of_fish: int, number_of_shark: int) -> None:
        """Initialize world map at the dimension x-axis & y-axis with water and populate the world of creatures

        Args:
            number_of_fish (int): number of fish to add to the world map at the beginning
            number_of_shark (int): number of shark to add to the world map at the beginning
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
            number_of_fish (int): number of fish to add to the world map at the beginning
            number_of_shark (int): number of shark to add to the world map at the beginning
        """
        self.add_fishes(number_of_fish)
        self.add_sharks(number_of_shark)

    def add_fishes(self, number_of_fish: int) -> None:
        """Adding all the fish 

        Args:
            number_of_fish (int): number of fish to add to the world map
        """
        #list_temp = all coordinate of water (tuple[int,int])
        list_temp = []
        for index_x, list in enumerate(self.world_map):
            for index_y, _ in enumerate(list):
                if self.world_map[index_x][index_y] == self.__CONST_WATER:
                    list_temp.append((index_x, index_y))
        #choose one coordinate for the fish
        for _ in range(number_of_fish):
            self.add_fish(list_temp.pop(random.randint(0, len(list_temp)-1)))
            
    def add_fish(self, position: tuple[int,int]) -> bool:
        """Adding one fish on the world map and school of fish list

        Args:
            position (tuple[int,int]): coordinate of the fish

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
        #list_temp = all coordinate of water (tuple[int,int])     
        list_temp = []
        for index_x, list in enumerate(self.world_map):
            for index_y, _ in enumerate(list):
                if self.world_map[index_x][index_y] == self.__CONST_WATER:
                    list_temp.append((index_x,index_y))

        #choose one coordinate for the fish
        for _ in range(number_of_shark):
            self.add_shark(list_temp.pop(random.randint(0,len(list_temp)-1)))

    def add_shark(self, position: tuple[int,int]) -> bool:
        """Adding one shark on the world map and school of fish list

        Args:
            position (tuple[int,int]): coordinate of the shark

        Returns:
            bool: successfully added
        """
        shark = creatures.Shark(position,self.CONST_SHARK_INITIAL_ENERGY)
        if self.world_map[position[0]][position[1]] == self.__CONST_WATER:
            self.set_param_to_position(self.__CONST_SHARK,position)
            self.school_of_shark.append(shark)
            return True
        return False
    
    def is_position_free(self, position: tuple[int,int]) -> bool:
        """Check whether the position is free

        Args:
            position (tuple[int,int]): coordinate on the world map

        Returns:
            bool: condition if position is free or not
        """
        x, y = position
        return self.world_map[y][x] == self.__CONST_WATER

#region shark
    def move_sharks(self) -> None:
        """Move all the sharks one by one
        """
        #loop on each shark object of self.school_of_shark
        for shark in self.school_of_shark[::-1]:
            self.move_shark(shark)

    def move_shark(self, shark: creatures.Shark) -> None:
        """Movement of a shark

        Args:
            shark (creatures.Shark): the shark that will move
        """
        #Verify destinations availability
        destinations_available_list = self.check_destinations_available(shark)
        if not destinations_available_list == []:
            #Choice destination if available
            destination_position = self.choice_of_destination(destinations_available_list)
            #Move to destination
            current_position = shark.coordinate
            self.move_to_destination(shark, current_position, destination_position)
            #Verify energy shark
            if not self.is_shark_still_alive(shark):
                self.kill_shark(shark.coordinate)
        #No destinations available
        else:
            shark.energy = shark.energy - 1
            shark.age = shark.age + 1
            if not self.is_shark_still_alive(shark):
                self.kill_shark(shark.coordinate)

    def is_shark_still_alive(self, shark: creatures.Shark) -> bool:
        """Vérify if the shark have enough energy

        Args:
            shark (_type_): _description_

        Returns:
            bool: condition if the shark have more than 0 energy
        """
        return shark.energy > 0

    def kill_shark(self, shark_position: tuple[int,int]) -> None:
        """Kill the shark in the shark list if not enough energy

        Args:
            shark_position (tuple[int,int]): the shark coordinate
        """
        #update list
        index = None
        for i, shark in enumerate(self.school_of_shark):
            if shark.coordinate == shark_position:
                index = i 
        self.school_of_shark.pop(index)
        #update world map
        self.set_param_to_position(self.__CONST_WATER, shark_position)
        self.nb_shark = self.nb_shark - 1
        self.dead_shark = self.dead_shark + 1

#region fish
    def move_fishes(self):
        """Move all the fishes one by one
        """
        #loop on each fish object of self.school_of_fish
        for fish in self.school_of_fish[::-1]:
            self.move_fish(fish)
    
    def move_fish(self, fish: creatures.Fish) -> bool:
        """Movement of a fish

        Args:
            fish (creatures.Fish): the fish that will move
        """
        #Verify water availability
        water_list = []
        water_list = self.check_destinations_available(fish)
        if water_list:
            #Choice water position
            water_position = self.choice_of_destination(water_list)
            #Move to water coordinate
            current_position = fish.coordinate
            self.move_to_destination(fish, current_position, water_position)
        else:
            fish.age = fish.age + 1

    def kill_fish(self, prey_position: tuple[int,int], shark: creatures.Shark) -> None:
        """Kill the fish in the fish list

        Args:
            prey_position (tuple[int,int]): the fish coordinate
            shark (creatures.Shark): use for update shark energy
        """
        index = None
        for i, fish in enumerate(self.school_of_fish):
            if fish.coordinate == prey_position:
                index = i
        if index is not None:
            fish_killed = self.school_of_fish.pop(index)  
            if fish_killed:
                shark.energy = self.CONST_SHARK_INITIAL_ENERGY
                self.dead_fish = self.dead_fish + 1
                self.nb_fish = self.nb_fish - 1

                
#region creature
    def move_to_destination(self, creature: creatures.Creature, current_position: tuple[int,int], futur_position: tuple[int,int]) -> None:
        """Creature's movement on her futur coordinate

        Args:
            creature (creatures.Creature): type of the creature
            current_position (tuple[int,int]): the creature coordinate
            futur_position (tuple[int,int]): the futur coordinate
        """
        if isinstance(creature, creatures.Shark):
            creature.energy = creature.energy - 1
        #creature movement on the world map
        self.update_world_map_position(current_position, futur_position, creature)
        #Kill the prey if destination is a fish
        self.kill_fish(futur_position,creature)
        #Update creature
        creature.coordinate = futur_position
        creature.age = creature.age + 1
        #Create baby if the creature is mature
        if self.is_creature_mature(creature):
            self.make_baby_creature(current_position, creature) 

    def update_world_map_position(self, current_position: tuple[int,int], destination_position: tuple[int,int], creature: creatures.Creature) -> None:
        """Update creature position on world map

        Args:
            current_position (tuple[int,int]): current position of the creature
            destination_position (tuple[int,int]): futur position of the creature
            creature (creatures.Creature): creature to check type
        """
        if isinstance(creature, creatures.Fish):
            creature_const = self.__CONST_FISH
        elif isinstance(creature, creatures.Shark):
            creature_const = self.__CONST_SHARK

        #update creature futur position        
        self.set_param_to_position(creature_const, destination_position)
        #update creature past position
        self.set_param_to_position(self.__CONST_WATER, current_position) 

    def choice_of_destination(self, destination_list: tuple[int,int]) -> tuple:
        """Choose one destination

        Args:
            destination_list (tuple[int,int]): list of each coordinate available

        Returns:
            tuple: coordinate of one destination
        """
        return destination_list[random.randint(0, len(destination_list)-1)]

    def check_destinations_available(self, creature: creatures.Creature) -> list[tuple[int, int]]:
        """Check if there is available destination

        Args:
            creature (creatures.Creature): creature to check type

        Returns:
            list[tuple[int, int]]: list of each coordinate available
        """
        destinations_list = []
        if isinstance(creature, creatures.Shark):

            #Create var to check prey presence
            check_preysence_west = (creature.coordinate[0], (creature.coordinate[1]-1) % (self.__dim_map_y))
            check_preysence_east = (creature.coordinate[0], (creature.coordinate[1]+1) % (self.__dim_map_y))
            check_preysence_south = ((creature.coordinate[0]+1) % (self.__dim_map_x), creature.coordinate[1])
            check_preysence_north = ((creature.coordinate[0]-1) % (self.__dim_map_x), creature.coordinate[1])
                
            if self.world_map[check_preysence_north[0]][check_preysence_north[1]] == self.__CONST_FISH:
                destinations_list.append(check_preysence_north)
            if self.world_map[check_preysence_south[0]][check_preysence_south[1]] == self.__CONST_FISH:
                destinations_list.append(check_preysence_south)
            if self.world_map[check_preysence_east[0]][check_preysence_east[1]] == self.__CONST_FISH:
                destinations_list.append(check_preysence_east)
            if self.world_map[check_preysence_west[0]][check_preysence_west[1]] == self.__CONST_FISH:
                destinations_list.append(check_preysence_west)
        
        if not destinations_list == []:
            return destinations_list
        else:
            return self.check_presence_water(creature)

    def check_presence_water(self, creature:creatures.Creature) -> list[tuple[int,int]]:
        """Check if there is available destination

        Args:
            creature (creatures.Creature): creature to check type

        Returns:
            list[tuple[int, int]]: list of each coordinate available of water
        """
        destinations_list = []
        #Create var to check prey presence
        check_preysence_west = (creature.coordinate[0], (creature.coordinate[1]-1) % (self.__dim_map_y))
        check_preysence_east = (creature.coordinate[0], (creature.coordinate[1]+1) % (self.__dim_map_y))
        check_preysence_south = ((creature.coordinate[0]+1) % (self.__dim_map_x), creature.coordinate[1])
        check_preysence_north = ((creature.coordinate[0]-1) % (self.__dim_map_x), creature.coordinate[1])

        if self.world_map[check_preysence_north[0]][check_preysence_north[1]] == self.__CONST_WATER:
            destinations_list.append(check_preysence_north)
        if self.world_map[check_preysence_south[0]][check_preysence_south[1]] == self.__CONST_WATER:
            destinations_list.append(check_preysence_south)
        if self.world_map[check_preysence_east[0]][check_preysence_east[1]] == self.__CONST_WATER:
            destinations_list.append(check_preysence_east)
        if self.world_map[check_preysence_west[0]][check_preysence_west[1]] == self.__CONST_WATER:
            destinations_list.append(check_preysence_west)
        return destinations_list

    def make_baby_creature(self, current_position: tuple[int,int], creature_dad: creatures.Creature) -> None:
        """Create a new creature on wator world

        Args:
            current_position (tuple[int,int]): position of the new creature
            creature_dad (creatures.Creature): creature to check type
        """
        #if creature is Fish
        if isinstance(creature_dad, creatures.Fish):
            #Create new fish and add to the list school_of_fish
            self.school_of_fish.append(creatures.Fish(current_position))
            #Update world map coordinate
            self.set_param_to_position(self.__CONST_FISH, current_position)
            self.nb_fish = self.nb_fish + 1
            self.birth_fish = self.birth_fish + 1
        #if creature is Shark
        elif isinstance(creature_dad, creatures.Shark):
            #Create new shark and add to the list school_of_shark
            self.school_of_shark.append(creatures.Shark(current_position, self.CONST_SHARK_INITIAL_ENERGY))
            #Update world map coordinate
            self.set_param_to_position(self.__CONST_SHARK, current_position)
            self.nb_shark = self.nb_shark + 1
            self.birth_shark = self.birth_shark + 1

    def is_creature_mature(self, creature: creatures.Creature) -> bool:
        """Verify if the creature is mature

        Args:
            creature (creatures.Creature): the creature to check type

        Returns:
            bool: condition if the creature is mature
        """
        if isinstance(creature, creatures.Fish):
            creature_const = self.CONST_FISH_MATURITY
        elif isinstance(creature, creatures.Shark):
            creature_const = self.CONST_SHARK_MATURITY
        return creature.age % creature_const == 0 if not creature.age == 0 else False

#region display
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

    def display(self):
        print(f"   🐠   Nombre:{self.nb_fish:<5}| Naissance: {self.birth_fish:<5}| Mort: {self.dead_fish}")
        print(f"   🦈   Nombre:{self.nb_shark:<5}| Naissance: {self.birth_shark:<5}| Mort: {self.dead_shark}")
        print()

        for i in self.world_map:
            for j in i:
                if j == self.__CONST_WATER:
                    print(termcolor.colored("~", "blue"),end=" ")
                elif j == self.__CONST_FISH:
                    print("🐠",end=" ")
                elif j == self.__CONST_SHARK:
                    print("🦈",end=" ")
            print()
        print()
            
def main():
    my_world_map = WatorWorld(40, 40, 100, 50, 2, 15, 7)
    #my_world_map.display()
    chronon_circle = 0
    print()
    print(f"Chronon = {chronon_circle}")
    print()

    while True :
        my_world_map.iterate()
        chronon_circle += 1
        print(f"Chronon = {chronon_circle}")
        print()
        my_world_map.display()
        print("=" * 120)
        time.sleep(0.5)

if __name__ == "__main__":
        main()