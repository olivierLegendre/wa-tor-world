import pygame
# import pygame.locals as locals
from pygame.locals import *
import history
import wator_world as ww
# import pygame_view as pyv


class WaterWorldWindow():
    const_water_world_window_size = tuple([800, 800])
    size_x = const_water_world_window_size[0]
    size_y = const_water_world_window_size[1]
    
    def __init__(self,  water_world_history: object):
        
        self.ww_rect = pygame.Rect(100, 200, self.size_x, self.size_y)
        self.water_world_history = water_world_history
        self.set_surface()
        self.create_sea_visual(0)
    
    def set_surface(self):
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
                    # print(f"fish at position {y}, {x}")
                    self.create_creature_at_position("fish", y, x, creature_size)
                if map[x][y] == 2:
                    # print(f"shark at position {y}, {x}")
                    self.create_creature_at_position("shark", y, x, creature_size)
    
    def draw(self):
        # pygame.draw.rect(App.screen, "blue", self.ww_rect)
        App.screen.blit(self.water_world_surface, self.ww_rect)
        
        
class Water_world_Statistics():
    const_water_world_statistics_size = tuple([800, 800])
    size_x = const_water_world_statistics_size[0]
    size_y = const_water_world_statistics_size[1]
    
    def __init__(self,  water_world_history: object):
    
        self.ww_statistics_rect = pygame.Rect(1100, 200, self.size_x, self.size_y)
        self.water_world_history = water_world_history
        self.set_surface()
        self.get_graph(0)
    
    def set_surface(self):
        self.water_world_statistics_surface = pygame.Surface((self.size_x, self.size_y))
        App.screen.blit(self.water_world_statistics_surface, (1100, 200))

    def get_graph(self, generation):
        print(f"generation a dessiner {generation}")
        self.water_world_history.get_graph(generation)
    
    def draw(self):
        # print("je dois dessiner mon graph")
        # pygame.draw.rect(App.screen, "blue", self.ww_statistics_rect)
        self.water_world_statistics_surface.fill("white")
        img_stat = pygame.image.load("water_world_graph.jpg")
        self.water_world_statistics_surface.blit(img_stat, (0,0))
        App.screen.blit(self.water_world_statistics_surface, self.ww_statistics_rect)
        

class Text:
    """Create a text object."""
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = pygame.Color('black')
        [setattr(self, key_arg, value_arg) for key_arg, value_arg in options.items()]
        self.set_font()
        self.render()

    def set_font(self):
        """Set the Font object from name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
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
        
        [setattr(self, key_arg, value_arg) for key_arg, value_arg in kwargs.items()]
        # print(f"dans init {self.id} {self.bg}")
        
    def draw(self):
        """Draw all objects in the scene."""
        # print(f"dans draw {self.id} {self.bg}")
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
        self.add_shortcuts()
        self.flags = RESIZABLE
        self.rect = pygame.Rect(0, 0, self.CONST_APP_WINDOW_SIZE_X, self.CONST_APP_WINDOW_SIZE_Y)
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)
        # App.screen = pygame.display.set_mode(self.CONST_APP_WINDOW_SIZE, self.flags)
        # App.text_title = Text('Pygame App', pos=(20, 20))
        App.scenes = list()
        
        App.running = True

    def run(self):
        """Run the main event loop."""
        scene_index = 2
        generation = 0
        clock = pygame.time.Clock()
        time_pass = False
        while App.running:
            print(f"generation {generation}")
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
                        self.wws.get_graph(generation)
                    if self.play_text.rect.collidepoint(event.pos):
                        time_pass = True
                    if self.stop_text.rect.collidepoint(event.pos):
                        time_pass = False
            if time_pass:
                if generation < (self.www.water_world_history.generations) - 1:
                    generation += 1
            clock.tick(10)    
            self.www.create_sea_visual(generation)
            self.wws.get_graph(generation)
            # self.wws.draw()
                    
            # App.screen.fill(pygame.Color('gray'))
            App.scene = App.scenes[scene_index]
            App.scene.draw()
            
            
            pygame.display.update()

        pygame.quit()
        
    def add_shortcuts(self):
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
            (114, 4352): 'self.toggle_resizable()',
            (103, 4352): 'self.toggle_frame()',
        }
        
    def do_shortcut(self, event):
        """Find the the key/mod combination in the dictionary and execute the cmd."""
        k = event.key
        m = event.mod
        # print(k)
        if (k, m) in self.french_shortcuts:
            exec(self.french_shortcuts[k, m])
            
    def toggle_fullscreen(self):
        """Toggle between full screen and windowed screen."""
        print("fullscreen")
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((0, 0), self.flags)

    def toggle_resizable(self):
        """Toggle between resizable and fixed-size window."""
        self.flags ^= RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_frame(self):
        """Toggle between frame and noframe window."""
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)

class wator_display(App):
    def __init__(self, history):
        super().__init__()
        self.history = history
        self.water_world_window = WaterWorldWindow(history)
        self.water_world_statistics = Water_world_Statistics(history)
        App.www = self.water_world_window
        App.wws = self.water_world_statistics
        self.load()
        
    def load(self):
        scene_intro = Scene(caption='Intro')
        scene_intro.nodes.append(Text('Scene 0', pos=(20, 20)))
        scene_intro.nodes.append(Text('Introduction screen the app', pos=(20, 50)))

        scene_option = Scene(bg=pygame.Color('yellow'), caption='Options')
        scene_option.nodes.append(Text('Scene 1', pos=(20, 20)))
        scene_option.nodes.append(Text('Option screen of the app', pos=(20, 50)))
        
        scene_main_screen = Scene(bg=pygame.Color(153, 153, 0), caption='Main')
        self.start_text = Text('Restart', pos=(100, 1050))
        self.play_text = Text('Play', pos=(300, 1050))
        self.stop_text = Text('Stop', pos=(500, 1050))
        scene_main_screen.nodes.append(Text('Scene 2', pos=(20, 20)))
        scene_main_screen.nodes.append(Text('Wa-tor simulation', pos=(100, 80)))
        scene_main_screen.nodes.append(Text('Wa-tor statistics', pos=(1100, 80)))

        scene_main_screen.nodes.append(self.start_text)
        scene_main_screen.nodes.append(self.play_text)
        scene_main_screen.nodes.append(self.stop_text)
        

        # print("water world history generations : ")
        # print(water_world_history.generations)
        scene_main_screen.nodes.append(self.water_world_window)
        scene_main_screen.nodes.append(self.water_world_statistics)
        
        
        App.scenes.append(scene_intro)
        App.scenes.append(scene_option)
        App.scenes.append(scene_main_screen)
        # Text('Scene 2', pos=(20, 20))
        # Text('Main screen of the app', pos=(20, 50))
        
        # water_world_history = ww.MockWorldHistory()
        # water_world_game = pyv.WaterWorldGame(water_world_history)
        # water_world_game.run_water_world_window()
        
        App.scene = App.scenes[2]

def main():
    pass


if __name__ == "__main__":
    main()