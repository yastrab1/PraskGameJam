from easygame.core import *

open_window('Panda simulator', 800, 600)

should_quit = False
while not should_quit:
    for event in poll_events():
        if type(event) is CloseEvent:
            should_quit = True
    draw_triangle((-100, -100, 2.0, 200.0, 0.0, 2.0, 100.0, 300.0, 2.0),(255,25,255,255))
    draw_triangle((-100.0, -100.0, -100.0,
                   100.0, -100.0, 100.0,
                   0.0, 100.0, 100.0),(255,255,10,255))

    next_frame()

close_window()
