import pygame
# import pygame.locals as locals
from pygame.locals import *
# import history
import wator_world as ww
import random
import os


class WaterWorldWindow():
    const_water_world_window_size = tuple([800, 800])
    size_x = const_water_world_window_size[0]
    size_y = const_water_world_window_size[1]
    
    def __init__(self,  water_world_history: object) -> None:
        
        self.ww_rect = pygame.Rect(100, 200, self.size_x, self.size_y)
        self.water_world_history = water_world_history
        self.set_surface()
        self.create_sea_visual(0)
    
    def set_surface(self) -> None:
        """
        Create the surface and blit (add) it to the surface of the game
        """
        self.water_world_surface = pygame.Surface((self.size_x, self.size_y))
        App.screen.blit(self.water_world_surface, (100, 200))
        
    def create_creature_at_position(self, creature: str, x: int, y: int, creature_size=10) -> None:
        """create a rectangle on the specifified position
            "shark" is red
            "fish" is green
        Args:
            creature (str): "shark" or "fish"
            x (int): 
            y (int): 
            creature_size : the number of pixels the "creature" will take
        """
        window_x = x * creature_size
        window_y = y * creature_size
        color = "green" if creature == "fish" else "red"
        pygame.draw.rect(self.water_world_surface, color, [window_x, window_y, creature_size, creature_size])
        
    def create_sea_visual(self, generation: int) -> None:
        """create the visual for one iteration of sea map history
            generation is the number of iterations we want to be able to display
        Args:
            water_world_history (dict): a World_History object
            generation (int): 
        """
        creature_size = 10
        self.water_world_surface.fill("blue")
        water_world_history = self.water_world_history
        map = water_world_history.get_map(generation)
        for x in range(len(map)):
            for y in range(len(map[x])):
                if map[x][y] == 1:
                    self.create_creature_at_position("fish", y, x, creature_size)
                if map[x][y] == 2:
                    self.create_creature_at_position("shark", y, x, creature_size)
    
    def draw(self) -> None:
        """everything added to nodes must have a draw method
        """
        App.screen.blit(self.water_world_surface, self.ww_rect)
        
        
class Water_world_Statistics():
    const_water_world_statistics_size = tuple([800, 800])
    size_x = const_water_world_statistics_size[0]
    size_y = const_water_world_statistics_size[1]
    
    def __init__(self, water_world_history: object) -> None:
    
        self.ww_statistics_rect = pygame.Rect(1100, 200, self.size_x, self.size_y)
        self.water_world_history = water_world_history
        self.set_surface()
        self.get_graph(0)
    
    def set_surface(self) -> None:
        """create a big rectangle for the statistics to be displayed
            and blit it to the app screen
        """
        self.water_world_statistics_surface = pygame.Surface((self.size_x, self.size_y))
        App.screen.blit(self.water_world_statistics_surface, (1100, 200))

    def get_graph(self, generation: int, display_nb_born=False, display_nb_death=False )-> None:
        """call the history to generate a graphique 

        Args:
            generation (int): _description_
        """
        self.water_world_history.get_graph(generation, display_nb_born, display_nb_death)
        
    def get_graph_live(self, generation: int) -> None:
        """try to get a graph with an open buffer
            not implemented yet

        Args:
            generation (int): _description_
        """
        self.water_world_history.get_graph_live(generation)
    
    def draw(self) -> None:
        """everything added to nodes must have a draw method
            we create an png of the graphic for every generation
        """
        self.water_world_statistics_surface.fill("white")
        img_stat = pygame.image.load("water_world_graph.png")
        self.water_world_statistics_surface.blit(img_stat, (-30,-80))
        App.screen.blit(self.water_world_statistics_surface, self.ww_statistics_rect)
        

class Text:
    """Create a text object."""
    def __init__(self, text: str, pos: tuple, **options) -> None:
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = pygame.Color('black')
        #set every parameter to self
        [setattr(self, key_arg, value_arg) for key_arg, value_arg in options.items()]
        self.set_font()
        self.render()

    def set_font(self) -> None:
        """Set the Font object from name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self) -> None:
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self) -> None:
        """Draw the text image to the screen."""
        App.screen.blit(self.img, self.rect)

class Scene:
    """Create a new scene (room, level, view)."""
    id = 0
    bg = pygame.Color('gray')
    
    def __init__(self, *args, **kwargs):
        # Append the new scene and make it the current scene
        App.scenes.append(self)
        App.scene = self
        
        # Set the instance id and increment the class id
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg
        self.file = ''
        self.img_folder = ''
        
        [setattr(self, key_arg, value_arg) for key_arg, value_arg in kwargs.items()]

        if self.file != '':
            img = self.img_folder+"/"+self.file if self.img_folder != '' else self.file
            self.img = pygame.image.load(img).convert()
            size = App.screen.get_size()
            self.img = pygame.transform.smoothscale(self.img, size)
            App.screen.blit(self.img, (0, 0))
    
    def draw(self) -> None:
        """Draw all objects in the scene."""
        if self.file != '':
            App.screen.blit(self.img, (0, 0))
        else:
            App.screen.fill(self.bg)
            
        for node in self.nodes:
            node.draw()
        pygame.display.flip()
        
    def __str__(self):
        return 'Scene {}'.format(self.id)


class App:
    CONST_APP_WINDOW_SIZE = tuple([2200, 1200])
    CONST_APP_WINDOW_SIZE_X = CONST_APP_WINDOW_SIZE[0] 
    CONST_APP_WINDOW_SIZE_Y = CONST_APP_WINDOW_SIZE[1]
    """Create a single-window app with multiple scenes."""
    def __init__(self, *args, **kwargs):
        """Initialize pygame and the application."""

        pygame.init()
        App.my_music = pygame.mixer
        App.my_music.init()
        self.add_shortcuts()
        self.flags = RESIZABLE
        
        self.tu_dum = App.my_music.Sound(os.path.join('sound', 'jaws-theme.mp3'))
        ambiant_music = App.my_music.music.load(os.path.join('sound', 'jaws-theme.mp3'))
        App.my_music.music.play(-1)
        

        self.rect = pygame.Rect(0, 0, self.CONST_APP_WINDOW_SIZE_X, self.CONST_APP_WINDOW_SIZE_Y)
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)
        App.scenes = list()
        App.running = True

    def run(self) -> None:
        """
        Run the main event loop
        """
        scene_index = 0
        generation = 0
        clock = pygame.time.Clock()
        tick = 10
        time_pass = False
        display_nb_born = False
        display_nb_death = False
        while App.running:
            #introduction scene
            if scene_index == 0:
                for event in pygame.event.get():
                        if event.type == QUIT:
                            App.running = False
                        if event.type == KEYDOWN:
                            self.do_shortcut(event)
                            if event.key in [K_SPACE, K_RIGHT]:
                                pass
                            if event.key == K_LEFT:
                                pass
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.enter_button.rect.collidepoint(event.pos):
                                scene_index = 1
            # simulation selection scene
            if scene_index == 1:
                for event in pygame.event.get():
                        if event.type == QUIT:
                            App.running = False
                        if event.type == KEYDOWN:
                            self.do_shortcut(event)
                            if event.key in [K_SPACE, K_RIGHT]:
                                pass
                            if event.key == K_LEFT:
                                pass
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            for _, text in self.simulations_dict.items():
                                if text.rect.collidepoint(event.pos):
                                    simulation_param = text.param
                                    world = ww.WatorWorld(
                                        80,
                                        80,
                                        simulation_param[2],
                                        simulation_param[3],
                                        simulation_param[4],
                                        simulation_param[5],
                                        simulation_param[6],
                                    )
                                    self.history.load(simulation_param[1], world)
                                    self.load_save(
                                        simulation_param[1],
                                        80,
                                        80,
                                        simulation_param[2],
                                        simulation_param[3],
                                        simulation_param[4],
                                        simulation_param[5],
                                        simulation_param[6],
                                    )
                                    self.load_main_scene()
                                    App.screen.fill("blue")
                                    scene_index = 2
            #main scene
            if scene_index == 2:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        App.running = False
                    if event.type == KEYDOWN:
                        self.do_shortcut(event)
                        if event.key in [K_SPACE, K_RIGHT]:
                            pass
                        if event.key == K_LEFT:
                            pass
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.start_text.rect.collidepoint(event.pos):
                            generation = 0
                            self.www.create_sea_visual(generation)
                            self.wws.get_graph(generation, display_nb_born, display_nb_death)
                        if self.play_text.rect.collidepoint(event.pos):
                            time_pass = True
                        if self.stop_text.rect.collidepoint(event.pos):
                            time_pass = False
                        if self.retour_text.rect.collidepoint(event.pos):
                            generation = 0
                            scene_index -= 1
                        if self.fast_text.rect.collidepoint(event.pos):
                            tick = tick + 3
                            if tick > 30:
                                tick = 30
                        if self.slow_text.rect.collidepoint(event.pos):
                            tick = tick - 3
                            if tick < 1:
                                tick = 1
                        if self.display_born_creatures_text.rect.collidepoint(event.pos):
                            display_nb_born = True if display_nb_born is False else False
                        if self.display_dead_creatures_text.rect.collidepoint(event.pos):
                            display_nb_death = True if display_nb_death is False else False
                
                if time_pass:
                    if generation < (self.www.water_world_history.generations) - 1:
                        generation += 1
                clock.tick(tick)    
                self.www.create_sea_visual(generation)
                self.wws.get_graph(generation, display_nb_born, display_nb_death)
            App.scene = App.scenes[scene_index]
            App.scene.draw()
            
            
            pygame.display.update()

        pygame.quit()
        
    def add_shortcuts(self) -> None:
        """
            add som keyboard shortcuts
            english and franch keyboards
        """
        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'print("ctrl+X")',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
            (K_f, KMOD_LMETA): 'self.toggle_fullscreen()',
            (K_r, KMOD_LMETA): 'self.toggle_resizable()',
            (K_g, KMOD_LMETA): 'self.toggle_frame()',
        }
        """
        LCTRL = 4160
        LSHIFT = 4097
        lALT = 4352
        K_x = 120 (unicode = x)
        K_f = 102
        K_r = 114
        K_g = 103
        """
        self.french_shortcuts = {
            (120, 4352): 'print("alt+X")',
            (120, 4160): 'pygame.quit()',
            (120, 4097): 'print("shift+X")',
            (120, 4160 + 4352): 'print("ctrl+alt+X")',
            (102, 4352): 'self.toggle_fullscreen()',
            (102, 4160): 'self.toggle_fullscreen()',
            (114, 4352): 'self.toggle_resizable()',
            (103, 4352): 'self.toggle_frame()',
        }
        
    def do_shortcut(self, event) -> None:
        """Find the the key/mod combination in the dictionary and execute the cmd."""
        k = event.key
        m = event.mod
        if (k, m) in self.french_shortcuts:
            exec(self.french_shortcuts[k, m])
            
    def toggle_fullscreen(self) -> None:
        """Toggle between full screen and windowed screen."""
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((0, 0), self.flags)

    def toggle_resizable(self) -> None:
        """Toggle between resizable and fixed-size window."""
        self.flags ^= RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_frame(self) -> None:
        """Toggle between frame and noframe window."""
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)


class wator_display(App):
    """
    main app
    """
    def __init__(self, history):
        """
        load an empty history 
        and the intro and selection sumulation scenes
        """
        super().__init__()
        self.history = history
        self.load_scenes()
        
    def load_save(self, name: str, x=80, y=80, nb_fish=200, nb_shark=50, fish_maturity=4, shark_maturity=10, shark_initial_energy=7):
        """
            load a water world into history
            and create the main scene, append it to the other scenes
        Args:
            name (str): wator_world simulation name
            x (int, optional): _description_. Defaults to 80.
            y (int, optional): _description_. Defaults to 80.
            nb_fish (int, optional): _description_. Defaults to 200.
            nb_shark (int, optional): _description_. Defaults to 50.
            fish_maturity (int, optional): _description_. Defaults to 4.
            shark_maturity (int, optional): _description_. Defaults to 10.
            shark_initial_energy (int, optional): _description_. Defaults to 7.
        """
        water_world = ww.WatorWorld(x, y, nb_fish, nb_shark, fish_maturity, shark_maturity, shark_initial_energy)
        self.history.load(name, water_world)
        self.load_history(self.history)
        self.load_main_scene()
        
    def load_history(self, history: object) -> None:
        """with an history, create a water_world_window and a water_world_statistics
            and append them to the App

        Args:
            history (History): _description_
        """
        self.water_world_window = WaterWorldWindow(history)
        self.water_world_statistics = Water_world_Statistics(history)
        App.www = self.water_world_window
        App.wws = self.water_world_statistics
        
    def load_main_scene(self) -> Scene:
        """create the dynamic components of the main scene

        Returns:
            Scene_main_screen: the main scene of the app
        """
        scene_main_screen = self.scene_main_screen
        
        self.add_display_parameter(scene_main_screen)
        scene_main_screen.nodes.append(self.water_world_window)
        scene_main_screen.nodes.append(self.water_world_statistics)
        App.scenes.append(scene_main_screen)
        return scene_main_screen
        
    def load_initial_main_scene(self) -> Scene:
        """reate the static components of the main scene

        Returns:
            Scene: the main scene of the app_description_
        """
        scene_main_screen = Scene(img_folder='background', file='shark.jpg', caption='shark')
        self.scene_main_screen = scene_main_screen
        self.start_text = Text('Restart', pos=(200, 1050))
        self.play_text = Text('Play', pos=(420, 1050))
        self.stop_text = Text('Stop', pos=(560, 1050))
        self.fast_text = Text('Faster', pos=(200, 1150))
        self.slow_text = Text('Slower', pos=(560, 1150))
        self.retour_text = Text('Retour', pos=(2000, 20))
        self.display_born_creatures_text = Text('Afficher les nouveaux nés', pos=(1930, 230), fontsize=30)
        self.display_dead_creatures_text = Text('Afficher les nouveaux nés', pos=(1930, 330), fontsize=30)
        
        scene_main_screen.nodes.append(Text('Wa-tor simulation', pos=(100, 100)))
        scene_main_screen.nodes.append(Text('Wa-tor statistics', pos=(1100, 100)))

        scene_main_screen.nodes.append(self.start_text)
        scene_main_screen.nodes.append(self.play_text)
        scene_main_screen.nodes.append(self.stop_text)
        scene_main_screen.nodes.append(self.fast_text)
        scene_main_screen.nodes.append(self.slow_text)
        scene_main_screen.nodes.append(self.retour_text)
        scene_main_screen.nodes.append(self.display_born_creatures_text)
        scene_main_screen.nodes.append(self.display_dead_creatures_text)
        
        return scene_main_screen
        
    def add_display_parameter(self, scene: Scene) -> None:
        """Create a bar with the parameters of the simulation
            append it to the main scene

        Args:
            scene (Scene): main scene
        """
        scene.nodes.append(Text('Parametres de la simulation : ', pos=(10, 20), fontsize=50))
        parameter_simulation = self.history.get_parameters_simulation()
        parameter_simulation = parameter_simulation[0]
        nb_fish = parameter_simulation[2]
        nb_shark = parameter_simulation[3]
        fish_maturity = parameter_simulation[4]
        shark_maturity = parameter_simulation[5]
        shark_initial_energy = parameter_simulation[6]
        scene.nodes.append(Text('Poissons initial : '+str(nb_fish), pos=(530, 40), fontsize=30))
        scene.nodes.append(Text('Requins initial : '+str(nb_shark), pos=(760, 40), fontsize=30))
        scene.nodes.append(Text('Maturité poisson : '+str(fish_maturity), pos=(970, 40), fontsize=30))
        scene.nodes.append(Text('Maturité requin : '+str(shark_maturity), pos=(1180, 40), fontsize=30))
        scene.nodes.append(Text('Energie initial requin : '+str(shark_initial_energy), pos=(1400, 40), fontsize=30))
        
    def saved_simulation(self, scene: Scene) -> None:
        """ Create a list of simulation on the second scene
            You can load every simulation and go the main screen

        Args:
            scene (Scene): simulation selection screen
        """ 
        height = 250
        simulations_dict = dict()
        simulations = self.history.get_saved_simulation()
        for simulation in simulations:
            name = simulation[1]
            nb_fish = simulation[2]
            nb_shark = simulation[3]
            fish_maturity = simulation[4]
            shark_maturity = simulation[5]
            shark_initial_energy = simulation[6]
            name_button = "load_saved_"+str(simulation[0])
            simulations_dict[name_button] = Text(''+str(name), pos=(80, height-10), fontsize=50, param=simulation)
            scene.nodes.append(Text('Poissons initial : '+str(nb_fish), pos=(680, height), fontsize=30))
            scene.nodes.append(Text('Requins initial : '+str(nb_shark), pos=(910, height), fontsize=30))
            scene.nodes.append(Text('Maturité poisson : '+str(fish_maturity), pos=(1120, height), fontsize=30))
            scene.nodes.append(Text('Maturité requin : '+str(shark_maturity), pos=(1330, height), fontsize=30))
            scene.nodes.append(Text('Energie initial requin : '+str(shark_initial_energy), pos=(1550, height), fontsize=30))
            scene.nodes.append(Text('Delete', pos=(1900, height-10), fontsize=50))
            height = height +50
            
        self.simulations_dict = simulations_dict
            
        for key, text in simulations_dict.items():
            setattr(self, key, text)
            attr = getattr(self, key)
            scene.nodes.append(attr)
        
    def load_scene_intro(self) -> Scene:
        """Load the introduction scene

        Returns:
            Scene: introduction scene
        """
        scene_intro = Scene(img_folder='background', file='watorworld.png', caption='Intor')
        self.enter_button = Text('Bienvenue sur le projet ', pos=(600, 400), fontsize=120, fontcolor="white")
        scene_intro.nodes.append(self.enter_button)
        return scene_intro
            
    def load_scene_simulations(self) -> Scene:
        """_Load the simulation selection scene

        Returns:
            Scene: simulation selection scene
        """
        easter_egg = random.randrange(1, 5)
        if easter_egg == 1:
            scene_simulations = Scene(img_folder='background', file='kevin.png', caption='Simulations')
        else: 
            scene_simulations = Scene(img_folder='background', file='EMMAS-HEROTemplate_-Jaws.png', caption='Simulations')
        scene_simulations.nodes.append(Text('Chargez une simulation', pos=(20, 50)))
        self.saved_simulation(scene_simulations)
        return scene_simulations

    
    def load_scenes(self) -> None:
        """
        load all the static scene at the start of the app
        """
        scene_intro = self.load_scene_intro()
        scene_simulations = self.load_scene_simulations()
        scene_main_screen = self.load_initial_main_scene()
        App.scenes.append(scene_intro)
        App.scenes.append(scene_simulations)
        App.scenes.append(scene_main_screen)
        App.scene = App.scenes[0]

def main():
    pass


if __name__ == "__main__":
    main()