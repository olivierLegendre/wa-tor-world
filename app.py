import pygame_view as pyv
import wator_world as ww
import history

def main():
    app = pyv.Proto()
    app.run()
    # water_world = ww.WatorWorld(80, 80, 150, 40)
    # water_world_history = history.History("simulation_3", water_world)
    # # for _ in range(1000):
    # #     water_world_history.iterate()
    # print(f"genrations : {water_world_history.generations}")


if __name__ == "__main__":
    main()