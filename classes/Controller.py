import pygame

class Controller: 

    #__init__(self):
    
    def control_start_menu(self):
        if self.event.type == pygame.MOUSEMOTION:
            for btn in self.buttons.values():
                x, y = self.event.pos
                if 
        #print(self.event.get_pos())

    def control(self, state):
        self.loc = state["location"]
        self.event = state["event"] 
        self.buttons = state["buttons"]

        if self.loc == "start_menu":
            self.control_start_menu()
