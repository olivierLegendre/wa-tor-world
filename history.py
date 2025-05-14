import wator_world as ww
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import history_entity as he
from os import path
import pygame_view as pyv

class MockWorldHistory():
    def __init__(self):
        self.sea_map_history = dict()
        self.generations = 0
        self.init()
        self.file_name = "water_world_history.json"
        
        
    def init(self):
        """mock creation
        """
        # self.sea_map_history[self.generations] = dict()
        self.sea_map_history[self.generations] = dict()
        statistic = dict()
        map_0 = [[0,1,0,0], [0,0,1,0], [1,0,0,0], [0,0,0,2]]
        statistic["chronon"] = 0
        statistic["nb_fish"] = 3
        statistic["nb_shark"] = 1
        statistic["nb_fish_born"] = 0
        statistic["nb_shark_born"] = 0
        statistic["nb_fish_dead"] = 0
        statistic["nb_shark_dead"] = 0
        statistic_0 = statistic.copy()
        map_1 = [[0,0,1,0], [0,1,0,0], [0,1,0,0], [0,0,2,0]]
        statistic["chronon"] = 1
        statistic["nb_fish"] = 3
        statistic["nb_shark"] = 1
        statistic["nb_fish_born"] = 0
        statistic["nb_shark_born"] = 0
        statistic["nb_fish_dead"] = 0
        statistic["nb_shark_dead"] = 0
        statistic_1 = statistic.copy()
        map_2 = [[0,0,0,0], [0,1,1,0], [0,2,0,0], [0,0,0,0]]
        statistic["chronon"] = 2
        statistic["nb_fish"] = 2
        statistic["nb_shark"] = 1
        statistic["nb_fish_born"] = 0
        statistic["nb_shark_born"] = 0
        statistic["nb_fish_dead"] = 1
        statistic["nb_shark_dead"] = 0
        statistic_2 = statistic.copy()
        map_3 = [[0,1,1,0], [0,1,1,0], [0,0,2,0], [0,0,0,0]]
        statistic["chronon"] = 3
        statistic["nb_fish"] = 4
        statistic["nb_shark"] = 1
        statistic["nb_fish_born"] = 2
        statistic["nb_shark_born"] = 0
        statistic["nb_fish_dead"] = 1
        statistic["nb_shark_dead"] = 0
        statistic_3 = statistic.copy()
        map_4 = [[0,1,0,0], [1,2,0,1], [0,0,0,0], [0,1,0,0]]
        statistic["chronon"] = 4
        statistic["nb_fish"] = 3
        statistic["nb_shark"] = 1
        statistic["nb_fish_born"] = 2
        statistic["nb_shark_born"] = 0
        statistic["nb_fish_dead"] = 2
        statistic["nb_shark_dead"] = 0
        statistic_4 = statistic.copy()
        map_5 = [[0,0,1,0], [2,0,0,0], [0,0,0,1], [0,0,0,0]]
        statistic["chronon"] = 5
        statistic["nb_fish"] = 2
        statistic["nb_shark"] = 1
        statistic["nb_fish_born"] = 2
        statistic["nb_shark_born"] = 0
        statistic["nb_fish_dead"] = 3
        statistic["nb_shark_dead"] = 0
        statistic_5 = statistic.copy()
        map_6 = [[0,1,1,0], [0,0,0,0], [2,0,0,0], [0,0,0,1]]
        statistic["chronon"] = 6
        statistic["nb_fish"] = 3
        statistic["nb_shark"] = 1
        statistic["nb_fish_born"] = 3
        statistic["nb_shark_born"] = 0
        statistic["nb_fish_dead"] = 3
        statistic["nb_shark_dead"] = 0
        statistic_6 = statistic.copy()
        map_7 = [[1,0,0,0], [0,0,1,0], [2,0,0,0], [2,0,1,0]]
        statistic["chronon"] = 7
        statistic["nb_fish"] = 3
        statistic["nb_shark"] = 2
        statistic["nb_fish_born"] = 3
        statistic["nb_shark_born"]= 1
        statistic["nb_fish_dead"] = 3
        statistic["nb_shark_dead"] = 0
        statistic_7 = statistic.copy()
        map_8 = [[2,0,1,0], [0,1,0,0], [0,0,0,2], [0,0,0,0]]
        statistic["chronon"] = 8
        statistic["nb_fish"] = 2
        statistic["nb_shark"] = 2
        statistic["nb_fish_born"] = 3
        statistic["nb_shark_born"] = 1
        statistic["nb_fish_dead"] = 3
        statistic["nb_shark_dead"] = 0
        statistic_8 = statistic.copy()
        map_9 = [[0,1,0,0], [1,0,0,0], [0,0,0,0], [2,0,0,2]]
        statistic["chronon"] = 9
        statistic["nb_fish"] = 2
        statistic["nb_shark"] = 2
        statistic["nb_fish_born"] = 3
        statistic["nb_shark_born"] = 1
        statistic["nb_fish_dead"] = 3
        statistic["nb_shark_dead"] = 0
        statistic_9 = statistic.copy()
        map_10 = [[2,1,0,0], [1,1,0,0], [0,0,0,2], [0,1,0,0]]
        statistic["chronon"] = 10
        statistic["nb_fish"] = 4
        statistic["nb_shark"] = 2
        statistic["nb_fish_born"] = 5
        statistic["nb_shark_born"] = 1
        statistic["nb_fish_dead"] = 3
        statistic["nb_shark_dead"] = 0
        statistic_10 = statistic.copy()

        self.add_generation(map_0, statistic_0)
        self.add_generation(map_1, statistic_1)
        self.add_generation(map_2, statistic_2)
        self.add_generation(map_3, statistic_3)
        self.add_generation(map_4, statistic_4)
        self.add_generation(map_5, statistic_5)
        self.add_generation(map_6, statistic_6)
        self.add_generation(map_7, statistic_7)
        self.add_generation(map_8, statistic_8)
        self.add_generation(map_9, statistic_9)
        self.add_generation(map_10, statistic_10)

    def get_generation_map(self, generation: int) -> list:
        """Return the sea_map from the generation

        Args:
            generation (int): _description_

        Returns:
            list: a sea_map
        """
        return self.sea_map_history[generation]["map"]

    def get_generation_statistics(self, generation: int) -> list:
        """Return the sea_map from the generation

        Args:
            generation (int): _description_

        Returns:
            list: a sea_map
        """
        return self.sea_map_history[generation]["statistic"]

    def get_all_statistics(self):
        all_stats = dict()
        for generation in self.sea_map_history:
            all_stats[generation] = self.sea_map_history[generation]["statistic"]
        return all_stats
    
    def get_all_statistics_to_generation(self, generation):
        stats = dict()
        for index in range(generation+1):
            stats[index] = self.sea_map_history[index]["statistic"]
        print("dans get all statistics t generation : ")
        print(f"{stats}")
        return stats

    def get_pandas_statistics(self):
        # columns_name = ['chronon', 'nb_fish', 'nb_shark', 'nb_fish_born', 'nb_shark_born', 'nb_fish_dead', 'nb_shark_dead']
        statistcs_df = pd.DataFrame(self.get_all_statistics())
        statistcs_df = statistcs_df.transpose()
        # statistcs_df.columns = columns_name
        return statistcs_df
    
        
    def display_graph(self):
        sns.set_theme()
        sharks_and_fishes = self.get_pandas_statistics()
        self.get_line_plot(sharks_and_fishes)
        # sns.lineplot(x='chronon', y='nb_fish', data=sharks_and_fishes)
        # water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=sharks_and_fishes)
        # water_world_fig = water_world_plot.get_figure()
        # water_world_fig.savefig("water_world_graph.png")
        # sns.lineplot(x='chronon', y='nb_fish', data=sharks_and_fishes)
        # sns.relplot(x='chronon', y='nb_fish', data=sharks_and_fishes, kind='line')
        
        print(sharks_and_fishes)
        
    def get_graph_by_generation(self, generation):
        sns.set_theme()
        sharks_and_fishes = self.get_all_statistics_to_generation(generation)
        self.get_line_plot(sharks_and_fishes)
        # statistcs_df = pd.DataFrame(sharks_and_fishes)
        # statistcs_df = statistcs_df.transpose()
        # # print(statistcs_df)
        # sns.lineplot(x='chronon', y='nb_fish', data=statistcs_df)
        # water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=statistcs_df)
        # water_world_fig = water_world_plot.get_figure()
        # water_world_fig.savefig("water_world_graph.png")
        
    def get_line_plot(self, data):
        statistcs_df = pd.DataFrame(data)
        statistcs_df = statistcs_df.transpose()
        print("dans get plot line")
        print(f"{statistcs_df}")
        # print(statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='nb_fish', data=statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=statistcs_df)
        water_world_fig = water_world_plot.get_figure()
        water_world_fig.savefig("water_world_graph.jpg")
        water_world_fig.clf()
        
        # plt.show()
        

    def add_generation(self, map, statistic):
        self.sea_map_history[self.generations] = dict()
        self.sea_map_history[self.generations]["statistic"] = statistic
        self.sea_map_history[self.generations]["map"] = map
        self.generations = self.generations + 1


class History():
    def __init__(self, simulation_name, world, entity=he.water_world_db()):
        self.sea_map_history = dict()
        self.sea_map_statistics = dict()
        self.generations = 0
        self.world = world
        self.name = simulation_name
        self.entity = entity
        self.init()
        
    def init(self):
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
        
    def print_world(self):
        self.world.display_affichage(self.name, self.world)
        
    def iterate(self):
        self.world.iterate()
        self.generations = self.generations + 1
        self.save_generation()
        
    def get_number_of_generations(self):
        return self.entity.count_generation(self.world_id)
        
    def save_generation(self):
        self.entity.insert_map(self.world, self.world_id, self.generations)
        self.entity.insert_statistics(self.world, self.world_id, self.generations)
        
    def get_map(self, generation=None):
        generation = generation if generation is not None else self.generations
        map = self.entity.get_map(self.world_id, generation)
        return map
    
    def get_statistics(self, generation=None):
        generation = generation if generation is not None else self.generations
        statistics = self.entity.get_statistics(self.world_id, generation)
        return statistics
    
    def get_all_statistics(self, generation=None):
        generation = generation if generation is not None else self.generations
        all_statistics = dict()
        print("dans get all statistics")
        print(generation)
        for generation in range(generation+1):
            all_statistics[generation] = self.get_statistics(generation)
        return all_statistics

    
    # def get_all_statistics_to_generation(self, generation):
    #     stats = dict()
    #     for index in range(generation+1):
    #         stats[index] = self.sea_map_history[index]["statistic"]
    #     print("dans get all statistics t generation : ")
    #     print(f"{stats}")
    #     return stats

    def get_pandas_statistics(self):
        # columns_name = ['chronon', 'nb_fish', 'nb_shark', 'nb_fish_born', 'nb_shark_born', 'nb_fish_dead', 'nb_shark_dead']
        statistcs_df = pd.DataFrame(self.get_all_statistics())
        statistcs_df = statistcs_df.transpose()
        # statistcs_df.columns = columns_name
        return statistcs_df
    
        
    def display_graph(self):
        sns.set_theme()
        sharks_and_fishes = self.get_pandas_statistics()
        self.get_line_plot(sharks_and_fishes)
        # sns.lineplot(x='chronon', y='nb_fish', data=sharks_and_fishes)
        # water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=sharks_and_fishes)
        # water_world_fig = water_world_plot.get_figure()
        # water_world_fig.savefig("water_world_graph.png")
        # sns.lineplot(x='chronon', y='nb_fish', data=sharks_and_fishes)
        # sns.relplot(x='chronon', y='nb_fish', data=sharks_and_fishes, kind='line')
        
        print(sharks_and_fishes)
        
    def get_graph(self, generation):
        sns.set_theme()
        sharks_and_fishes = self.get_all_statistics(generation)
        print(f" dans history , sharks and fishes : {sharks_and_fishes}")
        print(f"generation {generation}")
        self.get_line_plot(sharks_and_fishes)
        # statistcs_df = pd.DataFrame(sharks_and_fishes)
        # statistcs_df = statistcs_df.transpose()
        # # print(statistcs_df)
        # sns.lineplot(x='chronon', y='nb_fish', data=statistcs_df)
        # water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=statistcs_df)
        # water_world_fig = water_world_plot.get_figure()
        # water_world_fig.savefig("water_world_graph.png")
        
    def get_line_plot(self, data):
        statistcs_df = pd.DataFrame(data)
        statistcs_df = statistcs_df.transpose()
        print("dans get plot line")
        print(f"{statistcs_df}")
        # print(statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='nb_fish', data=statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=statistcs_df)
        water_world_fig = water_world_plot.get_figure()
        water_world_fig.savefig("water_world_graph.jpg")
        water_world_fig.clf()
        
    def get_graph_live(self, generation):
        sns.set_theme()
        sharks_and_fishes = self.get_statistics(generation)
        self.get_line_plot_live(sharks_and_fishes)
        
    def get_line_plot_live(self, data):
        statistcs_df = pd.DataFrame(data)
        statistcs_df = statistcs_df.transpose()
        print("dans get plot line")
        print(f"{statistcs_df}")
        # print(statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='nb_fish', data=statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=statistcs_df)
        water_world_fig = water_world_plot.get_figure()
        water_world_fig.savefig("water_world_graph.jpg")


def main():
    # mon_histoire = MockWorldHistory()
    # # mon_histoire.get_pandas_statistics()
    # # mon_histoire.display_graph()
    # # mon_histoire.get_graph_by_generation(0)
    # game = pyv.Proto()
    # game.run()
    
    simulation = ww.WatorWorld(80, 80, 40, 10)
    water_world_entity = he.water_world_db()
    water_world_history = History("simulation_1", simulation, water_world_entity)
    
    # request = """
    # DROP TABLE water_world_statistics"""
    # water_world_entity.play_request(request)
    # request = """
    # DROP TABLE water_world_map"""
    # water_world_entity.play_request(request)
    
    # water_world_history.print_world()
    water_world_history.iterate()
    # water_world_history.print_world()
    water_world_history.iterate()
    # water_world_history.print_world()
    water_world_history.iterate()
    print(water_world_history.get_map())
    print(water_world_history.get_statistics())
    print(water_world_history.get_all_statistics())

if __name__ == "__main__":
    main()
