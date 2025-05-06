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
        self.fishes_list = creatures.Creature_List()
        self.sharks_list = creatures.Creature_List()
        # 0 for water
        # 1 for fish
        # 2 for shark
        self.const_water = 0
        self.const_fish = 1
        self.const_shark = 2
        self.chronon_to_fish_birth = 3
        self.chronon_to_shark_birth = 7
        self.starting_shark_energy = 5
        self.creatures_to_create = dict()
        self.creatures_to_create["fish"] = list()
        self.creatures_to_create["shark"] = list()
    
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
        self.populate_with_creature("fish")
        self.populate_with_creature("shark")
        # self.populate_with_shark()
        
    def set_rules(self, chronon_to_fish_birth=3, chronon_to_shark_birth=7, starting_shark_energy=5, mode=1) -> None:
        """Setting some constant

        Args:
            chronon_to_fish_birth (int, optional): _description_. Defaults to 3.
            chronon_to_shark_birth (int, optional): _description_. Defaults to 7.
            starting_shark_energy (int, optional): _description_. Defaults to 5.
            mode (int, optional): _description_. Defaults to 1.
        """
        self.chronon_to_fish_birth = chronon_to_fish_birth
        self.chronon_to_shark_birth = chronon_to_shark_birth
        self.starting_shark_energy = starting_shark_energy
        self.mode = mode
        
    def populate_with_creature(self, creature_type: str) -> None:
        """populate the sea map 
            populate fishes_list
            populate sharks_list
        """
        x = random.randrange(0, self.world_size_x)
        y = random.randrange(0, self.world_size_y)
        nb_creature = 0
        match creature_type:
            case "fish":
                nb_creature_initial = self.nb_fish_init
            case "shark":
                nb_creature_initial = self.nb_shark_init
        while nb_creature < nb_creature_initial:
            if self.sea_map[x][y] == self.const_water:
                self.create_new_creature(creature_type, tuple([x, y]))
                nb_creature += 1
            x = random.randrange(0, self.world_size_x)
            y = random.randrange(0, self.world_size_y)
    
    # self.create_new_creature("shark", current_position[0], current_position[1])
    def add_creature_to_create(self, animal_type: str, position: tuple):
        self.creatures_to_create[animal_type].append(position)
        
    def create_creatures_from_list(self):
        creature_type_list = self.creatures_to_create.keys()
        print(f"creature type : {creature_type_list}")
        for creature_type in creature_type_list:
            print(f"creature type : {creature_type}")
            for creature_position in self.creatures_to_create[creature_type]:
                print(f"state map {self.sea_map[creature_position[0]][creature_position[1]]}")
                if self.sea_map[creature_position[0]][creature_position[1]] == self.const_water:
                    self.create_new_creature(creature_type, creature_position)
                else:
                    print("problempe de creation sur espace occupé")
        

    def create_new_creature(self, creature_type: str, position: tuple) -> None:
        """create a fish 
            add it to sea map at postion (x, y)
            add it to fishes_list     
        Args:
            x (int): _description_
            y (int): _description_
        """
        x, y = position
        match creature_type:
            case "fish":
                fish = creatures.Fish(x, y)
                self.fishes_list.add(fish)
                self.sea_map[x][y] = self.const_fish
            case "shark":
                shark = creatures.Shark(x, y, self.starting_shark_energy)
                self.sharks_list.add(shark)
                self.sea_map[x][y] = self.const_shark
        
    def pass_one_iteration(self) -> None:
        """ method use to make the world evolve one chronon
            we make all the fishes move
            we make all the sharks move
            we clean the dead creatures from sharks_list and fishes_list
        """
        self.creatures_to_create["fish"].clear()
        self.creatures_to_create["shark"].clear()
        self.fishes_move()
        self.sharks_move()
        self.clean_dead_creatures()
        self.create_creatures_from_list()
        #only for debugging
        # self.check_creatures_at_the_right_places()

    def fishes_move(self) -> None:
        """ we move every fish on fishes_list
            movement is possible if there is a free space nearby
            every chronon_to_fish_birth chronon, a fish give birth to another fish
        """
        fishes_list = self.fishes_list
        for fish in fishes_list.list():
            fish.age = fish.age + 1
            current_position = tuple()
            current_position = fish.x, fish.y
            futur_position = self.random_move(current_position)
            move_ok = self.is_move_possible(futur_position, "fish")
            if move_ok:
                self.creature_move(fish, current_position, futur_position)
                if fish.age % self.chronon_to_fish_birth == 0:
                    if fish.age != 0:
                        self.add_creature_to_create("fish", current_position)
                        # self.create_new_creature("fish", current_position)
                        
    def creature_move(self, creature: object, current_position : tuple, futur_position: tuple) -> None:
        """We move a single creature
        Args:
            creature (object): a creature object
            current_position (tuple):   x y
            futur_position (tuple): x y
        """
        const_animal = self.const_fish if isinstance(creature, creatures.Fish) else self.const_shark
        self.sea_map[futur_position[0]][futur_position[1]] = const_animal
        self.sea_map[current_position[0]][current_position[1]] = self.const_water
        creature.x, creature.y = futur_position
        
    def sharks_move(self):
        """we move every fish on fishes_list
            movement is possible if there is a free space nearby
            if there is a fish nearby, it is prioritized
            every chronon_to_shark_birth chronon, a shark give birth to another shark
            if a shark reach 0 energy, he dies from hunger
        """
        sharks_list = self.sharks_list
        for shark in sharks_list.list():
            shark.age = shark.age + 1
            shark.energy = shark.energy - 1
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
            
            if move_ok: 
                #if shark give birth
                # print(f"age : {shark.age}")
                self.creature_move(shark, current_position, futur_position)
                
                if shark.age % self.chronon_to_shark_birth == 0:
                    if shark.age != 0:
                        self.add_creature_to_create("shark", current_position)
                        # self.create_new_creature("shark", current_position)
                        
            if shark.energy < 1:
                self.kill_shark_from_hunger(shark, futur_position)
        
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
        # print(f"position {position}")
        # print(f"etat : {self.sea_map[position[0]][position[1]]}")
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
        
    def check_creatures_at_the_right_places(self):
        print("check data ok ")
        # self.check_fishes()
        # check_sharks()
        
        map = self.sea_map
        fishes_list = self.fishes_list
        sharks_list = self.sharks_list
        
        map_status_ok = True
        for position_x in range(len(map)):
            for position_y in range(len(map[position_x])):
                position = tuple([position_x, position_y])
                symbole = map[position_x][position_y]
                if symbole == self.const_fish:
                    # creature = fishes_list.creature_exist(position)
                    is_fish = fishes_list.is_fish(position)
                    if isinstance(is_fish, tuple):
                        print("effectivment il y a un probleme d'absence")
                        print(f"a la position {position_x}, {position_y}")
                        print(f"on y trouve : {self.sea_map[position_x][position_y]}")
                        presence_fish = False
                        for fish in self.fishes_list.list():
                            if fish.x == position_x and fish.y == position_y:
                                presence_fish = True
                                print(fish)
                        print(f"presence fish : {presence_fish}")
                    if fishes_list.is_fish(position):
                        pass
                    else:
                        print("il y a un probleme avec un poisson")
                if symbole == self.const_shark:
                    # sharks_list.creature_exist(position)
                    if sharks_list.is_shark(position):
                        pass
                    else:
                        print("il y a un probleme avec un requin")
                    
                # print(map[position_x][position_y])
                
    def clean_map(self):
        sea_map = self.sea_map
        for x in range(len(sea_map)):
            for y in range(len(sea_map[x])):
                if sea_map[x][y] == self.const_fish:
                    creature = self.fishes_list.creature_in_list(([x, y]))
                    if len(creature) < 1:
                        print(f"il ne devrait pas y avoir de poisson ici {x}, {y}")
                if sea_map[x][y] == self.const_shark:
                    creature = self.sharks_list.creature_in_list(([x, y]))
                    if len(creature) < 1:
                        print(f"il ne devrait pas y avoir de requin ici {x}, {y}")
                    

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
        self.generations = self.generations + 1
        
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
    # main()
    pass