import pygame_view as pyv
import wator_world as ww
import history
import history_entity as he


def create_simulation(name: str,
                    nb_fish=200, 
                    nb_shark=50, 
                    fish_maturity=4, 
                    shark_maturity=10, 
                    shark_initial_energy=7
                ) -> history:
    """ 
    create a named simulation (water_world_history) with :
    a watorworld
    an history_entity (to manage db)

    Args:
        name (str): _description_
        nb_fish (int, optional): _description_. Defaults to 200.
        nb_shark (int, optional): _description_. Defaults to 50.
        fish_maturity (int, optional): _description_. Defaults to 4.
        shark_maturity (int, optional): _description_. Defaults to 10.
        shark_initial_energy (int, optional): _description_. Defaults to 7.

    Returns:
        history: _description_
    """
    water_world = ww.WatorWorld(80, 
                                80, 
                                nb_fish, 
                                nb_shark, 
                                fish_maturity, 
                                shark_maturity, 
                                shark_initial_energy
                            )
    water_world_history_entity = he.water_world_db()
    water_world_history = history.History(water_world_history_entity)
    water_world_history.load(name, water_world)
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


def create_and_run_simulation(name: str, 
                            nb_iteration: int,
                            nb_fish=200, 
                            nb_shark=50, 
                            fish_maturity=4, 
                            shark_maturity=10, 
                            shark_initial_energy=7
                            ) -> None:
    """create an history form a specific world
        and iterate N times on it
        saving it in DB

    Args:
        name (str): Name of the simulation
        nb_iteration : The number of iteration the simulation will be run
        nb_fish (int, optional): _description_. Defaults to 200.
        nb_shark (int, optional): _description_. Defaults to 50.
        fish_maturity (int, optional): _description_. Defaults to 4.
        shark_maturity (int, optional): _description_. Defaults to 10.
        shark_initial_energy (int, optional): _description_. Defaults to 7.
    """
    water_world_history = create_simulation(name,
                                            nb_fish, 
                                            nb_shark, 
                                            fish_maturity, 
                                            shark_maturity, 
                                            shark_initial_energy
                                        )
    run_simulation(nb_iteration, water_world_history)


def run_app()-> None:
    """create an empty history
        and pass it to a pygame app
    """
    water_world_history_entity = he.water_world_db()
    water_world_history = history.History(water_world_history_entity)
    app = pyv.wator_display(water_world_history)
    app.run()


def main():
    
    """create a simulation
    """
    # create_and_run_simulation("antoine", 500, 200, 30, 3, 8, 4)

    
    """run pygame app
    """
    run_app()

if __name__ == "__main__":
    main()