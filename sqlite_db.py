import sqlite3
import wator_world as ww


class water_world_db():
    def __init__(self):
        self.connection_db()

    def connection_db(self):
        self.connection = sqlite3.connect("water_world.db")
        self.cursor = self.connection.cursor()

    def create_water_world_table(self):
        self.cursor.execute("""
                            CREATE TABLE Water_world (
                                water_world_id INTEGER PRIMARY KEY,
                                water_world_name INTEGER NOT NULL,
                                nb_fishes INTEGER NOT NULL,
                                nb_sharks INTEGER NOT NULL,
                                fish_maturity INTEGER NOT NULL,
                                shark_maturity INTEGER NOT NULL,
                                shark_initial_energy INTEGER NOT NULL
                            )
                            """)
        
    def create_water_world_statistics_table(self):
        self.cursor.execute("""
                            CREATE TABLE Water_world_statistics(
                                water_world_statistics_id INTEGER PRIMARY KEY,
                                chronon INTEGER NOT NULL,
                                nb_fish INTEGER NOT NULL,
                                nb_shark INTEGER NOT NULL,
                                birth_fish INTEGER NOT NULL,
                                birth_shark INTEGER NOT NULL,
                                dead_fish INTEGER NOT NULL,
                                dead_shark INTEGER NOT NULL,
                                water_world_id INTEGER NOT NULL,
                                FOREIGN KEY(water_world_id) REFERENCES Water_world(water_world_id)
                            )
                            """)
        
    def create_water_world_map_table(self):
        self.cursor.execute("""
                            CREATE TABLE Water_world_map (
                                water_world_map_id INTEGER PRIMARY KEY, 
                                chronon INTEGER NOT NULL,
                                map TEXT NOT NULL,
                                water_world_id INTEGER NOT NULL,
                                FOREIGN KEY(water_world_id) REFERENCES Water_world(water_world_id)
                            )
                            """)
        
    def insert_water_world(self, water_world, name):
        ww = water_world
        request = """
            INSERT INTO Water_world (water_world_name, nb_fishes, nb_sharks, fish_maturity, shark_maturity, shark_initial_energy)
            VALUES(?, ?, ?, ?, ?, ?)
        """
        
        values_to_insert = ("simulation_1", 
                            ww.nb_fishes, 
                            ww.nb_sharks, 
                            ww.CONST_FISH_MATURITY,
                            ww.CONST_SHARK_MATURITY,
                            ww.CONST_SHARK_INITIAL_ENERGY,
                            )
        
        print(values_to_insert)
        # self.cursor.execute(request, values_to_insert)

        
        
    def play_request(self, request):
        self.cursor.execute(request)
    

def main():
    ww_db = water_world_db()
    # ww_db.create_water_world_table()
    # ww_db.create_water_world_statistics_table()
    # ww_db.create_water_world_map_table()
    mon_monde = ww.WatorWorld(20, 20, 10, 1)
    # print(mon_monde.world_map)
    # print(mon_monde.nb_fish)
    
    # request = """
    # ALTER TABLE Water_world
    # ADD water_world_name INTEGER NOT NULL"""
    # ww_db.play_request(request)

if __name__ == '__main__':
    main()