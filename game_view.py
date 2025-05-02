import pygame
# from pygame.locals import *
import pygame.locals as locals
import water_world as ww
import copy as cp

class Game_World():
    def __init__(self, nb_generations):
        self.nb_generations = 100
        water_world = ww.Water_World()
        self.water_world = water_world
        # water_world.set_rules(5, 8, 6)
        # water_world.init_water_world(150, 20, 120, 120)
        self.set_rules()
        self.init()
        
    def set_rules(self, chronos_to_fish_birth=3, chronos_to_shark_birth=7, starting_shark_energy=5, mode=1):
        print("init rules")
        self.water_world.set_rules(chronos_to_fish_birth, chronos_to_shark_birth, starting_shark_energy, mode)
        
    def init(self, nb_fish=150, nb_shark=20, x_size=120, y_size=120):
        print("init world")
        self.water_world.init_water_world(nb_fish, nb_shark, x_size, y_size)

    def load(self):
        self.sea_map_history = ww.World_History()
        for _  in range(self.nb_generations):
            self.water_world.pass_one_iteration()
            self.sea_map_history.add_sea_map_to_history(cp.deepcopy(self.water_world))
        self.water_world = self.water_world

    def get_sea_map_history(self)-> object:
        return self.sea_map_history
    
    

def main():

    pygame.init()

    size = (1200, 1200)
    window = pygame.display.set_mode(size)

    def create_creature_at_position(creature: str, x: int, y: int) -> None:
        """create a rectangle on the specifified position
            "shark" is red
            "fish" is green
        Args:
            creature (str): "shark" or "fish"
            x (int): 
            y (int): 
        """
        window_x = x*10
        window_y = y*10
        color = "green" if creature == "fish" else "red"
        pygame.draw.rect(window, color, [window_x, window_y, 10, 10])
        
    generation = 0
    
    def create_sea_visual(sea_map_history: object, generation: int) -> None:
        """create the visual for one iteration of sea map history
            generation is the number of iterations we want to be able to display
        Args:
            sea_map_history (dict): a World_History object
            generation (int): 
        """
        for x in range(len(sea_map_history.get_generation(generation))):
            for y in range(len(sea_map_history.get_generation(generation)[x])):
                if sea_map_history.get_generation(generation)[x][y] == 1:
                    # print(f"fish at position {y}, {x}")
                    create_creature_at_position("fish", y, x)
                if sea_map_history.get_generation(generation)[x][y] == 2:
                    # print(f"shark at position {y}, {x}")
                    create_creature_at_position("shark", y, x)
                    
    game_world = Game_World(100)
    game_world.load()
    sea_map_history = game_world.get_sea_map_history()

    # nb_generations = 100
    # water_world = ww.Water_World()
    # water_world.set_rules(5, 8, 6)
    # water_world.init_water_world(150, 20, 120, 120)
    # sea_map_history = ww.World_History()
    # for _  in range(nb_generations):
    #     water_world.pass_one_iteration()
    #     sea_map_history.add_sea_map_to_history(cp.deepcopy(water_world))

    pygame.display.update()
    keep_running = True

    while keep_running:

        window.fill("blue")
        
        create_sea_visual(sea_map_history, generation)
        
        for event in pygame.event.get():
            # quit event
            if event.type == locals.QUIT:
                keep_running = False
            if event.type == locals.KEYDOWN:
                if event.key in [locals.K_SPACE, locals.K_RIGHT]:
                    if generation < (sea_map_history.generations) - 1:
                        generation += 1
                    create_sea_visual(sea_map_history, generation)
                if event.key == locals.K_LEFT:
                    if generation > 0:
                        generation -= 1
                    create_sea_visual(sea_map_history, generation)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()