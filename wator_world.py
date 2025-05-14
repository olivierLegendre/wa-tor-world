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
        self.CONST_FISH_MATURITY = CONST_FISH_MATURITY
        self.CONST_SHARK_MATURITY = CONST_SHARK_MATURITY
        self.CONST_SHARK_INITIAL_ENERGY = CONST_SHARK_INITIAL_ENERGY

        self.__initialization(number_of_fish, number_of_shark)

#region init_world_map

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
            
    def add_fish(self, position: tuple[int,int]) -> bool:
        """Adding one fish

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

    def add_shark(self, position: tuple[int,int]) -> bool:
        """Adding one shark

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
        destinations_available_list = self.check_destinations_available(shark)
        if not destinations_available_list == []:
            #Choice destination if available
            destination_position = self.choice_of_destination(destinations_available_list)
            #Move to destination
            current_position = shark.coordinate
            self.move_to_prey(shark, current_position, destination_position)
            #Verify energy shark
            if not self.is_shark_still_alive(shark):
                self.kill_shark(shark.coordinate)
        else:
            for i, shark_in_world_map in enumerate(self.school_of_shark):
                if shark_in_world_map.coordinate == shark.coordinate:
                    shark_in_world_map.energy = shark_in_world_map.energy - 1
                    shark_in_world_map.age = shark_in_world_map.age + 1
            if not self.is_shark_still_alive(shark):
                self.kill_shark(shark.coordinate)

    def move_to_prey(self, shark: creatures.Shark, current_position: tuple[int,int], destination_position: tuple[int,int]) -> bool:
        """Shark's movement on its prey

        Args:
            shark (creatures.Shark): the shark that will move
            current_position (tuple[int,int]): the shark current coordinate
            destination_position (tuple[int,int]): the futur coordinate of the shark

        Returns:
            bool: condition if the shark move
        """
        #Shark movement on the world map
        self.move_creature_to_position(current_position, destination_position,shark)
        #Kill the prey if destination is a fish
        self.kill_fish(destination_position,shark)
        #Update school_of_shark
        for i, shark_in_world_map in enumerate(self.school_of_shark):
            if shark_in_world_map.coordinate == current_position:
                shark_in_world_map.coordinate = destination_position
                shark_in_world_map.energy = shark_in_world_map.energy - 1
                shark_in_world_map.age = shark_in_world_map.age + 1
        #Create baby shark if the shark is mature
        if self.is_creature_mature(shark):
            self.make_baby_creature(current_position,shark)

    def kill_fish(self, prey_position: tuple[int,int], shark: creatures.Shark) -> None:
        """Delete the fish in the fish list

        Args:
            prey_position (tuple[int,int]): the fish coordinate
            shark (creatures.Shark): update shark energy
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

    def is_shark_still_alive(self, shark) -> bool:
        """Vérify if the shark have enough energy

        Args:
            shark (_type_): _description_

        Returns:
            bool: _description_
        """
        return shark.energy > 0

    def kill_shark(self, shark_position: tuple[int,int]) -> bool:
        """Delete the shark in the shark list if not enough energy

        Args:
            shark_position (tuple[int,int]): the shark coordinate

        Returns:
            bool: condition if the shark is delete
        """
        #update list
        index = None
        for i, shark in enumerate(self.school_of_shark):
            if shark.coordinate == shark_position:
                index = i 
        self.school_of_shark.pop(index)
        #update world map
        self.set_param_to_position(self.__CONST_WATER, shark_position)

#region fish
    def move_fishes(self):
        """Move all the fishes one by one
        """
        #loop on each fish object of self.school_of_fish

        for fish in self.school_of_fish:
            self.move_fish(fish)
    
    def move_fish(self, fish: creatures.Fish) -> bool:
        """Movement of a fish

        Args:
            fish (creatures.Fish): the fish that will move

        Returns:
            bool: condition if fish move
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
            for i, fish_in_world_map in enumerate(self.school_of_fish):
                if fish_in_world_map.coordinate == fish.coordinate:
                    fish_in_world_map.age = fish_in_world_map.age + 1

    def move_to_destination(self, fish: creatures.Fish, current_position: tuple[int,int], water_position: tuple[int,int]) -> None:
        """Fish's movement on its water coordinate

        Args:
            fish (creatures.Shark): the fish that will move
            current_position (tuple[int,int]): the fish coordinate
            water_position (tuple[int,int]): the water coordinate

        Returns:
            bool: condition if the shark move
        """
        #Fish movement on the world map
        self.move_creature_to_position(current_position, water_position, fish)
        #Update school_of_fish
        for i, fish_in_world_map in enumerate(self.school_of_fish):
            if fish_in_world_map.coordinate == current_position:
                fish_in_world_map.coordinate = water_position
                fish_in_world_map.age = fish_in_world_map.age + 1
        #Create baby fish if the fish is mature
        if self.is_creature_mature(fish):
            self.make_baby_creature(current_position, fish) 

#region creature
    def move_creature_to_position(self, current_position: tuple[int,int], destination_position: tuple[int,int], creature: creatures.Creature) -> None:
        """Move creature to a position

        Args:
            current_position (tuple[int,int]): current position of the creature
            destination_position (tuple[int,int]): futur position of the creature
            creature (creatures.Creature): creature to check type
        """
        if isinstance(creature, creatures.Fish):
            #update fish futur position        
            self.set_param_to_position(self.__CONST_FISH, destination_position)
            #update fish past position
            self.set_param_to_position(self.__CONST_WATER, current_position) 
        elif isinstance(creature, creatures.Shark):
            #update shark futur position
            self.set_param_to_position(self.__CONST_SHARK, destination_position)
            #update shark past position
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
            creature (creatures.Creature): the creature to check

        Returns:
            bool: condition if the creature is mature
        """
        #if creature is Fish
        if isinstance(creature, creatures.Fish):
            fish_age = creature.age
            return fish_age % self.CONST_FISH_MATURITY == 0 if not fish_age == 0 else False
        #if creature is Shark
        elif isinstance(creature, creatures.Shark):
            shark_age = creature.age
            return shark_age % self.CONST_SHARK_MATURITY == 0 if not shark_age == 0 else False

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

    def display_affichage(self):
        for y in self.world_map:
            for const in y:
                if const == self.__CONST_WATER:
                    print(termcolor.colored("~", "blue"), end=" ")
                elif const == self.__CONST_FISH:
                    print(termcolor.colored("1", "white"), end=" ")
                elif const == self.__CONST_SHARK:
                    print(termcolor.colored("2", "red"), end=" ")
        print()
            
def main():
    my_world_map = WatorWorld(3, 3, 3, 1)
    for i in my_world_map.world_map :
        for j in i :         
            print(f"{j}", end =" ") 
        print()   
    print()
    
    #nb d'iteration
    for _ in range(8):  
        my_world_map.iterate()
        for i in my_world_map.world_map:
            for j in i:
                print(f"{j}", end=" ")
            print()
        print()

    # for _ in range(3): 
    #     my_world_map.iterate()
    #     print()
    #     my_world_map.display_affichage()

if __name__ == "__main__":
    main()
