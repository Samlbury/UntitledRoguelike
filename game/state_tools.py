"""State handling functions"""

import tcod

import g

def main_draw() -> None:
    if not g.states:
        return
    g.console.clear() # Clear console before drawing
    g.states[-1].on_draw(g.console) # Draw the current state
    g.context.present(g.console) # Render the console

def main_loop() -> None:
    """Run the active state forever"""
    while g.states:
        main_draw()
        for event in tcod.event.wait():
            if g.states:
                g.states[-1].on_event(event)