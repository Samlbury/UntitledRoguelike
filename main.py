#!/usr/bin/env python

import tcod
from tcod.console import Console

import g
import game.states
import game.world_tools

def main() -> None:
    tileset = tcod.tileset.load_tilesheet("data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437)
    tcod.tileset.procedural_block_elements(tileset=tileset)
    
    console = Console(80, 50)

    state = game.states.InGame()
    g.world = game.world_tools.new_world()

    with tcod.context.new(console=console, tileset=tileset) as g.context:
        while True: # Main loop
            console.clear() # Clear console before drawing
            state.on_draw(console) # Draw the current state
            g.context.present(console) # Render the console

            for event in tcod.event.wait():
                state.on_event(event)

if __name__ == "__main__":
    main()