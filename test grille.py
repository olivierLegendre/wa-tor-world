import creatures

#region Class
class WatorWorld():
    world_map = []
    school_of_fish = []
    school_of_shark = []

    #region Constantes
    __CONST_WATER = 0
    __CONST_FISH = 1
    __CONST_SHARK = 2

    __CONST_FISH_MATURITY = 3
    __CONST_SHARK_MATURITY = 7
    __CONST_SHARK_INITIAL_ENERGY = 5

    def __init__(self, dim_map_x, dim_map_y, number_of_fish, number_of_shark):
        """Initializer of WatorWorld object

        Args:
            dim_map_x (_type_): world dimension x-axis
            dim_map_y (_type_): world dimension y-axis
            number_of_fish (_type_): number of fishes on the world map at the beginning
            number_of_shark (_type_): number of sharks on the world map at the beginning
        """ 
        self.__dim_map_x = dim_map_x
        self.__dim_map_y = dim_map_y

        self.__initialization(number_of_fish, number_of_shark)
    
    def __initialization(self, number_of_fish: int, number_of_shark: int) -> None:
        """Initialize world map at the dimension x-axis & y-axis with water and populate the world of creatures

        Args:
            number_of_fish (int): number of fish on world map at the beginning
            number_of_shark (int): number of shark on world map at the beginning
        """
        self.initialize_world_map()
        self.add_creatures_to_world_map(number_of_fish, number_of_shark)

    def initialize_world_map(self) -> None:
        """Initialize world map at the dimension x-axis & y-axis with water
        """
    
        self.world_map = [[self.__CONST_WATER for _ in range(self.__dim_map_x)]for _ in range(self.__dim_map_y)]
        print(self.world_map)
        for i in self.world_map :
            for j in i :
                print(f" {j} ", end =" ")
            print()

world = WatorWorld(20,20,0,0)

    
