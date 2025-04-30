import pygame
# from pygame.locals import *
import pygame.locals as locals
import water_world as ww

def main():

    pygame.init()

    size = (400, 400)
    window = pygame.display.set_mode(size)

    def create_creature_at_position(creature, x: int, y: int) -> None:
        window_x = x*10
        window_y = y*10
        color = "green" if creature == "fish" else "red"
        pygame.draw.rect(window, color, [window_x, window_y, 10, 10])

    def create_sea_visual(sea_tab, generation: int):
        for x in range(len(sea_tab[generation])):
            for y in range(len(sea_tab[generation][x])):
                if sea_tab[generation][x][y] == 1:
                    # print(f"fish at position {y}, {x}")
                    create_creature_at_position("fish", y, x)
                if sea_tab[generation][x][y] == 2:
                    # print(f"shark at position {y}, {x}")
                    create_creature_at_position("shark", y, x)

    water_world = ww.Water_World()
    water_world.init_water_world(20, 10, 40, 40)
    sea_tab = []
    sea_tab.append(water_world.sea_map)
    generation = 0

    pygame.display.update()
    keep_running = True

    while keep_running:

        window.fill("blue")
        create_sea_visual(sea_tab, generation)
        
        for event in pygame.event.get():
            # quit event
            if event.type == locals.QUIT:
                keep_running = False
            if event.type == locals.KEYDOWN:
                if event.key in [locals.K_SPACE, locals.K_RIGHT]:
                    if generation < len(sea_tab)-1:
                        generation += 1
                        # print(f"key space generation {generation} : {sea_tab}")
                    create_sea_visual(sea_tab, generation)
                if event.key == locals.K_LEFT:
                    # print("moutmout")
                    if generation > 0:
                        generation -= 1
                    create_sea_visual(sea_tab, generation)

        pygame.display.update()
        

    pygame.quit()


if __name__ == "__main__":
    main()