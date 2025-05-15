#a supprimer hors main
# import wator_world as ww
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import history_entity as he


class History():
    def __init__(self, entity=he.water_world_db()):
        self.entity = entity
        
    
    
    def load(self, simulation_name: str, world: object) -> None:
        self.generations = 0
        self.world = world
        self.name = simulation_name
        self.init()
        
        
    def init(self) -> None:
        """
        create an history object and save data in db
        create tables water_world, water_world_map and water_world_statistics if not already created
        create the initial generation
        """
        #do nothing if tables already exists
        self.entity.create_tables()
        
        world_id = self.entity.get_water_world_id_by_name(self.name)
        if world_id is not None:
            print("word already exists")
            self.world_id = world_id
            self.generations = self.get_number_of_generations()
        else:
            print("world to create")
            self.world_id = self.entity.insert_water_world(self.name, self.world)
            self.save_generation()
        
    def print_world(self) -> None:
        """call to wator_world display_affichage
        """
        self.world.display_affichage(self.name, self.world)
        
    def iterate(self) -> None:
        """create a new wator_world iteration and save
            map in water_world_map table
            statistics in water_world_statistics
        """
        self.world.iterate()
        self.generations = self.generations + 1
        self.save_generation()
        
    def get_number_of_generations(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        return self.entity.count_generation(self.world_id)
    
    def get_parameters_simulation(self) -> list:
        """
            return the parameters used to create the simulation
        Returns:
            list: _description_
        """
        return self.entity.get_simulation_parameters(self.world_id)
    
    def get_saved_simulation(self):
        return self.entity.get_saved_simulations()
        
    def save_generation(self) -> None:
        """save map in water_world_map
            save statistics in water_world_statistics
        """
        self.entity.insert_map(self.world, self.world_id, self.generations)
        self.entity.insert_statistics(self.world, self.world_id, self.generations)
        
    def get_map(self, generation=None) -> list:
        """return the map of a specific generation or the last generation if none given

        Args:
            generation (_type_, optional): _description_. Defaults to None.

        Returns:
            list: world map
        """
        generation = generation if generation is not None else self.generations
        map = self.entity.get_map(self.world_id, generation)
        return map
    
    def get_statistics(self, generation=None) -> list:
        """return statistics of a specific generation or the last generation if none given

        Args:
            generation (_type_, optional): _description_. Defaults to None.

        Returns:
            list: _description_
        """
        generation = generation if generation is not None else self.generations
        statistics = self.entity.get_statistics(self.world_id, generation)
        return statistics
    
    def get_all_statistics(self, generation=None) -> list:
        """ return a list with all statistics of a generation

        Args:
            generation (_type_, optional): _description_. Defaults to None.

        Returns:
            list: _description_
        """
        generation = generation if generation is not None else self.generations
        all_statistics = dict()
        for generation in range(generation+1):
            all_statistics[generation] = self.get_statistics(generation)
        return all_statistics

    def get_pandas_statistics(self):
        """return a dataframe from all statistics of a simulation

        Returns:
            a pandas dataframe
        """
        # columns_name = ['chronon', 'nb_fish', 'nb_shark', 'nb_fish_born', 'nb_shark_born', 'nb_fish_dead', 'nb_shark_dead']
        statistcs_df = pd.DataFrame(self.get_all_statistics())
        statistcs_df = statistcs_df.transpose()

        return statistcs_df
        
    # def display_graph(self) -> None:
    #     """_summary_
    #     """
    #     sns.set_theme()
    #     sharks_and_fishes = self.get_pandas_statistics()
    #     self.get_line_plot(sharks_and_fishes)

        
    def get_graph(self, generation: int, display_nb_born=False, display_nb_death=False) -> None:
        """ 
        return a graph displayed in pygame
        called every iteration
        Args:
            generation (int): _description_
        """
        sns.set_theme()
        sharks_and_fishes = self.get_all_statistics(generation)
        self.get_line_plot(sharks_and_fishes, display_nb_born, display_nb_death)

    def get_line_plot(self, data, display_nb_born=False, display_nb_death=False) -> None:
        """generate a line plot from the data of a simulation
        Args:
            a pandas dataframe
        """
        print(f" dans get plot line : {display_nb_born}, {display_nb_death}")
        statistcs_df = pd.DataFrame(data)
        statistcs_df = statistcs_df.transpose()
        water_world_plot = sns.lineplot(x='chronon', y='nb_fish', data=statistcs_df, label="Nb Fish")
        water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=statistcs_df, label="Nb Shark")
        if display_nb_born:
            print("j'ajoute les naissances")
            water_world_plot = sns.lineplot(x='chronon', y='birth_fish', data=statistcs_df, label="Birth Fish")
            water_world_plot = sns.lineplot(x='chronon', y='birth_shark', data=statistcs_df, label="Birth Shark")
        if display_nb_death:
            print("j'ajoute les morts")
            water_world_plot = sns.lineplot(x='chronon', y='dead_fish', data=statistcs_df, label="Dead Fish")
            water_world_plot = sns.lineplot(x='chronon', y='dead_shark', data=statistcs_df, label="Dead Shark")
        water_world_plot.legend(title="Creature Info", loc="upper left") 
        water_world_plot.set(xlabel='chronon', ylabel='')
        water_world_fig = water_world_plot.get_figure()
        water_world_fig.set_size_inches(9,9)
        water_world_fig.savefig("water_world_graph.png")
        water_world_fig.clf()
        
    def get_graph_live(self, generation: int) -> None:
        """
        try to display a graph without history
        Args:
            generation (int): _description_
        """
        sns.set_theme()
        sharks_and_fishes = self.get_statistics(generation)
        print(sharks_and_fishes)
        self.get_line_plot_live(sharks_and_fishes, generation)
        
    def get_line_plot_live(self, data, generation):
        """try to generate a graph with open cursor every iteration
        Args:
            data (_type_): _description_
            generation (_type_): _description_
        """
        statistcs_df = pd.DataFrame(data, index=[generation])
        statistcs_df = statistcs_df.transpose()
        water_world_plot = sns.lineplot(x='chronon', y='nb_fish', data=statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=statistcs_df)
        water_world_fig = water_world_plot.get_figure()
        water_world_fig.savefig("water_world_graph.jpg")


def main():
    pass

if __name__ == "__main__":
    main()
