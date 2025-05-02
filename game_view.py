import pygame
# from pygame.locals import *
import pygame.locals as locals
import water_world as ww
import copy as cp


def main():

    pygame.init()

    size = (400, 400)
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

    nb_generations = 1000
    water_world = ww.Water_World()
    water_world.init_water_world(50, 5, 40, 40)
    sea_map_history = ww.World_History()
    for _  in range(nb_generations):
        water_world.pass_one_iteration()
        sea_map_history.add_sea_map_to_history(cp.deepcopy(water_world))

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