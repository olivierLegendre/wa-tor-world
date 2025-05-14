#a supprimer hors main
# import wator_world as ww
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import history_entity as he


class History():
    def __init__(self, simulation_name, world, entity=he.water_world_db()):
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
        for generation in range(generation+1):
            all_statistics[generation] = self.get_statistics(generation)
        return all_statistics

    def get_pandas_statistics(self):
        # columns_name = ['chronon', 'nb_fish', 'nb_shark', 'nb_fish_born', 'nb_shark_born', 'nb_fish_dead', 'nb_shark_dead']
        statistcs_df = pd.DataFrame(self.get_all_statistics())
        statistcs_df = statistcs_df.transpose()
  
        return statistcs_df
    
        
    def display_graph(self):
        sns.set_theme()
        sharks_and_fishes = self.get_pandas_statistics()
        self.get_line_plot(sharks_and_fishes)

        
    def get_graph(self, generation):
        sns.set_theme()
        sharks_and_fishes = self.get_all_statistics(generation)
        self.get_line_plot(sharks_and_fishes)

    def get_line_plot(self, data):
        statistcs_df = pd.DataFrame(data)
        statistcs_df = statistcs_df.transpose()
        water_world_plot = sns.lineplot(x='chronon', y='nb_fish', data=statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='birth_fish', data=statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='birth_shark', data=statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='dead_fish', data=statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='dead_shark', data=statistcs_df)
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
        water_world_plot = sns.lineplot(x='chronon', y='nb_fish', data=statistcs_df)
        water_world_plot = sns.lineplot(x='chronon', y='nb_shark', data=statistcs_df)
        water_world_fig = water_world_plot.get_figure()
        water_world_fig.savefig("water_world_graph.jpg")


def main():
    pass

if __name__ == "__main__":
    main()
