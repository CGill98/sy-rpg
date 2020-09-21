#Controls everything on the screen
import pygame, os

game_folder = r"\\datingsim"
game_dir = os.getcwd() + game_folder
background_dir = game_dir + r"\\assets\\UI\\Exports\\Background.jpg"
dialogue_container_dir = game_dir + r"\\assets\\UI\\Exports\\Dialogue\\DialogueContainer.png"
start_background = game_dir + r"\\assets\\UI\\Exports\\HomeScreen\\HomeScreenBackground.jpg"

pygame.font.init()

class Button:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen


class TextButton(Button): 
    
    def __init__(self, x, y, screen, txt, font_size=24, colour=(0,0,0)):
        Button.__init__(self, x, y, screen)
        self.txt = txt
        self.font_size = font_size
        self.colour= colour

    def draw(self):
        font = pygame.font.SysFont(None, self.font_size)
        img = font.render(self.txt, True, self.colour)
        self.screen.blit(img, (self.x, self.y))

    #mx - mouse x, my mouse y,
    #def clicked(self, mx, my): 
    #    return 


class View: 
    locations = { "start_menu" : {
                        "buttons" : {}
                    } 
                
                }

    def __init__(self, screen):
        print("view started")
        self.screen = screen 
        self.play_btn = TextButton(50, 100, self.screen, "Play", font_size=48) # for start screen

    def set_background(self, dir):
        black = 0, 0, 0
        self.screen.fill(black)
        background_image = pygame.image.load(dir)
        background_image = pygame.transform.scale(background_image, (1600, 900))
        self.background = background_image.get_rect()
        self.screen.blit(background_image, self.background)

    def set_dialogue_container(self, dir):
        self.container_image = pygame.image.load(dir)
        self.container_image = pygame.transform.scale(self.container_image, (1600, 300))
        self.container_image.set_alpha(0)
        self.container = self.container_image.get_rect()
        self.container = self.container.move(0, 550)
        #self.container.image = self.container_image
        self.screen.blit(self.container_image, self.container)

    def draw_text(self, txt, x, y, font_size=24, colour=(0,0,0)):
        font = pygame.font.SysFont(None, font_size)
        img = font.render(txt, True, colour)
        self.screen.blit(img, (x, y))

    def show_start_menu(self, state):
        self.set_background(start_background)
        #self.draw_text("Play", 50, 100, font_size=48)
        all_buttons = state["buttons"]
        print(all_buttons)
        for btn in all_buttons.values():
            if btn["loc"] == "start_menu":  
                self.locations["start_menu"]["buttons"][btn["id"]] = TextButton(btn["pos"][0], btn["pos"][1], self.screen, btn["text"], btn["font_size"], btn["colour"]) 

        for btn in self.locations["start_menu"]["buttons"].values():
            btn.draw()

    def render(self, state):
        loc = state["location"]

        if loc == "start_menu":
            self.show_start_menu(state)
        else:
            self.set_background(background_dir)
            self.set_dialogue_container(dialogue_container_dir)


    