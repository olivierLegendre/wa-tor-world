from abstract_classes.waterworld_abstract import WaterworldAbstract
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
from os import path

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
        
    def load_from_json(self, object):
        pass
    
    def save_to_json(self, dict_to_save):
        if path.isfile(self.file_name) is False:
            raise Exception("File not found")
        
        json_file = json.dumps([{key: dict_to_save[key]} for key in dict_to_save], indent=4)
        with open(self.file_name, "w") as output_file:
            output_file.write(json_file)
        
    def append_to_json(self, dict_to_append):
        listObj = dict()
        if path.isfile(self.file_name) is False:
            raise Exception("File not found")
        
        # Read JSON file
        with open(self.file_name) as fp:
            listObj = json.load(fp)
        
        # Verify existing dict
            print(listObj)

            print(type(listObj))
            
            listObj.append(dict_to_append)
        
        # Verify updated dict
        print(listObj)
        
        with open(self.file_name, 'w') as json_file:
            json_to_update = json.dump(listObj, json_file, 
                        indent=4,  
                        separators=(',', ': '))
            json_file.write(json_to_update)
        print(json_to_update)
        print('Successfully written to the JSON file')
        
    def test_save_to_json(self):
        dict_to_save = self.sea_map_history[0]
        self.save_to_json(dict_to_save)
        
    def test_append_to_json(self):
        dict_to_append = self.sea_map_history[1]
        self.append_to_json(dict_to_append)
        
class WaterWorld(WaterworldAbstract):
    
    def is_shark_mature(self) -> bool :
        pass
    
def main():
    mon_histoire = MockWorldHistory()
    # mon_histoire.get_pandas_statistics()
    # mon_histoire.display_graph()
    # mon_histoire.get_graph_by_generation(0)
    mon_histoire.test_save_to_json()
    mon_histoire.test_append_to_json()

if __name__ == "__main__":
    main()
