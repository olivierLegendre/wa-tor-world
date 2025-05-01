import pygame
# from pygame.locals import *
import pygame.locals as locals
import water_world as ww
import copy as cp


def main():

    pygame.init()

    size = (400, 400)
    window = pygame.display.set_mode(size)

    def create_creature_at_position(creature, x: int, y: int) -> None:
        window_x = x*100
        window_y = y*100
        color = "green" if creature == "fish" else "red"
        pygame.draw.rect(window, color, [window_x, window_y, 100, 100])

    # def create_sea_visual(sea_tab, generation: int):
    #     for x in range(len(sea_tab[generation])):
    #         for y in range(len(sea_tab[generation][x])):
    #             if sea_tab[generation][x][y] == 1:
    #                 # print(f"fish at position {y}, {x}")
    #                 create_creature_at_position("fish", y, x)
    #             if sea_tab[generation][x][y] == 2:
    #                 # print(f"shark at position {y}, {x}")
    #                 create_creature_at_position("shark", y, x)
    
    generation = 0
    
    def create_sea_visual(sea_map_history, generation: int):
        for x in range(len(sea_map_history.get_generation(generation))):
            for y in range(len(sea_map_history.get_generation(generation)[x])):
                if sea_map_history.get_generation(generation)[x][y] == 1:
                    # print(f"fish at position {y}, {x}")
                    create_creature_at_position("fish", y, x)
                if sea_map_history.get_generation(generation)[x][y] == 2:
                    # print(f"shark at position {y}, {x}")
                    create_creature_at_position("shark", y, x)

    
    nb_generations = 10
    water_world = ww.Water_World()
    water_world.init_water_world(2, 1, 4, 4)
    sea_map_history = ww.World_History()
    # water_copy = cp.deepcopy(water_world)
    # sea_map_history.add_sea_map_to_history(cp.deepcopy(water_world))
    # # sea_tab = []
    # # sea_tab.append(water_world.sea_map)
    # # print(f"dans game, original : {sea_map_history.get_generation(0)}")
    # water_world.pass_one_iteration()
    # sea_map_history.add_sea_map_to_history(cp.deepcopy(water_world))
    # # print(f"dans game, opreante : {sea_map_history.get_generation(0)}")
    # sea_map_history.add_sea_map_to_history(cp.deepcopy(water_world))
    for _  in range(nb_generations):
        water_world.pass_one_iteration()
        sea_map_history.add_sea_map_to_history(cp.deepcopy(water_world))
        
        
        
        
        
        
    # print(sea_map_history)
    # print(f"dans game, generation 0: {sea_map_history.get_generation(0)}")
    # print(f"dans game, generation 1: {sea_map_history.get_generation(1)}")
    # print(f"dans game, generation 2: {sea_map_history.get_generation(2)}")
    # print(f"dans game, untouched: {sea_map_history.get_generation(0)}")

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
                        # print(f"key space generation {generation} : {sea_map_history}")
                    create_sea_visual(sea_map_history, generation)
                if event.key == locals.K_LEFT:
                    # print("moutmout")
                    if generation > 0:
                        generation -= 1
                    create_sea_visual(sea_map_history, generation)

        pygame.display.update()
        

    pygame.quit()


if __name__ == "__main__":
    main()