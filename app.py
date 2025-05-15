import pygame_view as pyv
import wator_world as ww
import history
import history_entity as he


def create_simulation(name: str) -> history:
    """
    create a named simulation (water_world_history) with :
    a watorworld
    an history_entity (to manage db)
    Args:
        name (str): the name of the simulation

    Returns:
        history: an object to manage history of a wator world
    """
    water_world = ww.WatorWorld(80, 80, 200, 50, 4, 10, 7)
    water_world_history_entity = he.water_world_db()
    water_world_history = history.History(water_world_history_entity)
    water_world_history = water_world_history.load(name, water_world)
    return water_world_history


def run_simulation(nb_iteration: int, world_history: history):
    """
    insert nb iterations of wator world in history
    Args:
        nb_iteration (int): nb chronon
        world_history (history): history of a simulation
    """
    for _ in range(nb_iteration):
        world_history.iterate()


def create_and_run_simulation():
    water_world_history = create_simulation("victoire_requin_2")
    run_simulation(1000, water_world_history)


def run_app():
    water_world_history_entity = he.water_world_db()
    water_world_history = history.History(water_world_history_entity)
    app = pyv.wator_display(water_world_history)
    app.run()


def main():
    
    """create a simulation
    """
    # create_and_run_simulation()
    
    
    # water_world_history = create_simulation("victoire_requin_2")
    # run_simulation(1000, water_world_history)

    # water_world_history = create_simulation("simulation_antoine_2")
    # print(water_world_history.get_all_statistics())
    
    # water_world_history.get_saved_simulation()
    
    # app = pyv.wator_display(water_world_history)


    # run_simulation(1000, water_world_history)
    
    """run pygame app
    """
    run_app()

if __name__ == "__main__":
    main()