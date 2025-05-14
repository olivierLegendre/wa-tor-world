import sqlite3
import wator_world as ww
import json


class water_world_db():
    def __init__(self):
        self.connection_db()

    def connection_db(self):
        with sqlite3.connect("wator_world.db") as connection:
            self.connection = connection
            self.cursor = connection.cursor()
        
    def create_tables(self):
        #create file wator_world.db s'il n'existe pas
        file_path = "wator_world.db"

        try:
            with open(file_path, 'x') as file:
                file.write("")
        except FileExistsError:
            print(f"The file '{file_path}' already exists")
            
        self.create_water_world_table()
        self.create_water_world_statistics_table()
        self.create_water_world_map_table()

    def create_water_world_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS water_world (
                                water_world_id INTEGER PRIMARY KEY,
                                water_world_name STRING NOT NULL UNIQUE,
                                nb_fishes INTEGER NOT NULL,
                                nb_sharks INTEGER NOT NULL,
                                fish_maturity INTEGER NOT NULL,
                                shark_maturity INTEGER NOT NULL,
                                shark_initial_energy INTEGER NOT NULL
                            )
                            """)
        
    def create_water_world_statistics_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Water_world_statistics(
                                water_world_statistics_id INTEGER PRIMARY KEY,
                                chronon INTEGER NOT NULL,
                                nb_fish INTEGER NOT NULL,
                                nb_shark INTEGER NOT NULL,
                                birth_fish INTEGER NOT NULL,
                                birth_shark INTEGER NOT NULL,
                                dead_fish INTEGER NOT NULL,
                                dead_shark INTEGER NOT NULL,
                                water_world_id INTEGER NOT NULL,
                                FOREIGN KEY(water_world_id) REFERENCES Water_world(water_world_id),
                                UNIQUE(water_world_id, chronon)
                            )
                            """)
        
    def create_water_world_map_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Water_world_map (
                                water_world_map_id INTEGER PRIMARY KEY, 
                                chronon INTEGER NOT NULL,
                                map TEXT NOT NULL,
                                water_world_id INTEGER NOT NULL,
                                FOREIGN KEY(water_world_id) REFERENCES Water_world(water_world_id),
                                UNIQUE(water_world_id, chronon)
                            )
                            """)
    
    
    def get_water_world_id(self, name):
        request_select = """
            SELECT water_world_id FROM Water_world
            WHERE water_world_name = ?
        """
        result = self.cursor.execute(request_select, (name, ))
        fetch = result.fetchone()

        if fetch is not None: 
            world_id = fetch[0]
            result.fetchall()
            return world_id
        else:
            result.fetchall()
            return None
        
    def insert_water_world(self, name, water_world):
        ww = water_world
        request_insert = """
            INSERT OR IGNORE INTO Water_world (water_world_name, nb_fishes, nb_sharks, fish_maturity, shark_maturity, shark_initial_energy)
            VALUES(?, ?, ?, ?, ?, ?)
            RETURNING water_world_id
        """
        
        values_to_insert = (name, 
                            ww.nb_fish, 
                            ww.nb_shark, 
                            ww.CONST_FISH_MATURITY,
                            ww.CONST_SHARK_MATURITY,
                            ww.CONST_SHARK_INITIAL_ENERGY,
                            )
        
        # print(values_to_insert)
        self.cursor.execute(request_insert, values_to_insert)
        self.cursor.fetchall()
        self.connection.commit()

        # get the id of the last inserted row
        return self.cursor.lastrowid

    def show_water_worlds(self):
        request = """
            SELECT * FROM Water_world
        """
        result = self.cursor.execute(request)
        print(result.fetchall())
        
    def get_water_world_id_by_name(self, name):
        request = """
            SELECT water_world_id FROM Water_world
            WHERE water_world_name = ?
        """
        result = self.cursor.execute(request, (name,))
        fetch = result.fetchall()
    
        if len(fetch) == 0:
            return None
        else:
            return fetch[0][0]
        
    def play_request(self, request):
        self.cursor.execute(request)
        
    def insert_map(self, water_world, water_world_id, generation):
        request = """
            INSERT OR IGNORE INTO Water_world_map(chronon, map, water_world_id)
            VALUES (?, ?, ?)
        """
        
        values_to_insert = (generation, 
                            json.dumps(water_world.world_map),
                            water_world_id,
                            )
        
        # print(values_to_insert)
        self.cursor.execute(request, values_to_insert)
        self.connection.commit()

        # get the id of the last inserted row
        return self.cursor.lastrowid
    
    def insert_statistics(self, water_world, water_world_id, generation):
        request = """
            INSERT OR IGNORE INTO Water_world_statistics(chronon,
                                        nb_fish,
                                        nb_shark,
                                        birth_fish,
                                        birth_shark,
                                        dead_fish,
                                        dead_shark,
                                        water_world_id
                                    )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        values_to_insert = (generation, 
                            water_world.nb_fish,
                            water_world.nb_shark,
                            water_world.birth_fish,
                            water_world.birth_shark,
                            water_world.dead_fish,
                            water_world.dead_shark,
                            water_world_id
                        )
        
        # print(values_to_insert)
        self.cursor.execute(request, values_to_insert)
        self.connection.commit()

        # get the id of the last inserted row
        return self.cursor.lastrowid
    
    def get_map(self, water_world_id, generation):
        request = """
            SELECT map FROM Water_world_map
            WHERE water_world_id = ?
                AND chronon = ?
        """
        result = self.cursor.execute(request, (water_world_id, generation))
        json_map = result.fetchone()[0]
        map = json.loads(json_map)
        # print(map)
        return map
    
    def get_statistics(self, water_world_id, generation):
        request = """
            SELECT chronon, nb_fish, nb_shark, birth_fish, birth_shark, dead_fish, dead_shark
            FROM Water_world_statistics
            WHERE water_world_id = ?
                AND chronon = ?
        """
        result = self.cursor.execute(request, (water_world_id, generation))
        statistics = dict()
        result = result.fetchone()
        statistics["chronon"] = result[0]
        statistics["nb_fish"] = result[1]
        statistics["nb_shark"] = result[2]
        statistics["birth_fish"] = result[3]
        statistics["birth_shark"] = result[4]
        statistics["dead_fish"] = result[5]
        statistics["dead_shark"] = result[6]
        # print(statistics)
        return statistics
    
    def count_generation(self,water_world_id):
        request = """
            SELECT count(chronon)
            FROM Water_world_statistics
            WHERE water_world_id = ?
        """
        result = self.cursor.execute(request, (water_world_id, ))
        result = result.fetchone()
        nb_generations = result[0]
        return nb_generations

def main():
    ww_db = water_world_db()
    # ww_db.create_water_world_table()
    # ww_db.create_water_world_statistics_table()
    # ww_db.create_water_world_map_table()
    mon_monde = ww.WatorWorld(20, 20, 10, 1)
    # print(mon_monde.world_map)
    # print(mon_monde.nb_fish)
    # ww_db.create_tables()
    
    # request = """
    # DROP TABLE water_world_map"""
    # ww_db.play_request(request)

    # last_row = ww_db.insert_water_world('simulation_1', mon_monde)
    # print(f"row modifié : {last_row}")
    # ww_db.show_water_worlds()
    # id_water_world = ww_db.get_water_world_id_from_name('simulation_1')
    # print(id_water_world)
    
    # ww_db.insert_map(mon_monde, 1, 0)
    # print( ww_db.insert_statistics(mon_monde, 1, 0))
    # ww_db.get_map(1, 0)
    # ww_db.get_statistics(1, 0)

if __name__ == '__main__':
    main()