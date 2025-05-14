import pygame_view as pyv
import wator_world as ww
import history
import history_entity as he

def main():
    water_world = ww.WatorWorld(80, 80, 150, 40)
    water_world_history_entity = he.water_world_db()
    water_world_history = history.History("simulation_stephane", water_world, water_world_history_entity)
    app = pyv.wator_display(water_world_history)
    app.run()
    # water_world = ww.WatorWorld(80, 80, 200, 50)
    # water_world_history = history.History("simulation_remi", water_world)
    # for _ in range(300):
    #     water_world_history.iterate()
    # print(f"genrations : {water_world_history.generations}")


if __name__ == "__main__":
    main()