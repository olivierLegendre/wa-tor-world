import pygame_view as pyv
import wator_world as ww
import history
import history_entity as he

def create_simulation(name):
    water_world = ww.WatorWorld(80, 80, 150, 40)
    water_world_history_entity = he.water_world_db()
    water_world_history = history.History("simulation_stephane", water_world, water_world_history_entity)
    return water_world_history

def run_simulation(nb_iteration, history):
    for _ in range(nb_iteration):
        history.iterate()
    print(f"genrations : {water_world_history.generations}")

def main():

    water_world_history = create_simulation("simulation_stephane")
    # print(water_world_history.get_all_statistics())
    app = pyv.wator_display(water_world_history)
    app.run()

    # run_simulation(300, water_world_history)
    # print(f"genrations : {water_world_history.generations}")


if __name__ == "__main__":
    main()