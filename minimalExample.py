from easygame.core import *

open_window('Panda simulator', 800, 600)

should_quit = False
while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
    
    draw_triangle((0.0, 0.0, 2.0, 200.0, 0.0, 2.0, 100.0, 300.0, 200.0))

    next_frame()

close_window()
