from easygame.core import *

open_window('Panda simulator', 800, 600)

should_quit = False
while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
    draw_triangle(((100,100,100),(120,120,120),(150,150,150)),(1,1,1,1))
    next_frame()

close_window()
