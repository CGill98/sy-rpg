import sys, pygame, os
from classes.View import View
from classes.Controller import Controller


size = width, height = 1600, 900
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

view = View(screen)
controller = Controller()


state = { 
          "location" : "start_menu", #the current location of the mc
          "event" : {},
          #buttons have values 0 (default), 1 (hovered over), 2 (selected)
          "buttons" : { 
              "play_btn" : {"value" : 0, "pos" : [50, 100], "text" : "play",  "loc" : "start_menu", "id": 0, "font_size": 48, "colour" : (0, 0, 0)} #on the start menu 
              }, 
          }

counter = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    state["event"] = pygame.event.wait()
    print(state["event"])
    controller.control(state) #control changes state based on event
    view.render(state)  #render changes the view based on state

    pygame.display.flip()