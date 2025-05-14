import pygame_view as pyv
import wator_world as ww
import history
import history_entity as he


def create_simulation(name):
    water_world = ww.WatorWorld(80, 80, 200, 50, 4, 10, 7)
    water_world_history_entity = he.water_world_db()
    water_world_history = history.History(name, water_world, water_world_history_entity)
    return water_world_history


def run_simulation(nb_iteration, history):
    for _ in range(nb_iteration):
        history.iterate()
    print(f"genrations : {history.generations}")


def main():

    water_world_history = create_simulation("simulation_antoine_2")
    # print(water_world_history.get_all_statistics())
    
    app = pyv.wator_display(water_world_history)
    app.run()

    # run_simulation(1000, water_world_history)
    

if __name__ == "__main__":
    main()