#!/usr/bin/env python

import tcod
from tcod.console import Console

import g
import game.state_tools
import game.world_tools

from game.states import InGame

def main() -> None:
    tileset = tcod.tileset.load_tilesheet("data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437)
    tcod.tileset.procedural_block_elements(tileset=tileset)
    
    g.console = Console(80, 50)

    g.states = [InGame()]
    g.world = game.world_tools.new_world()

    with tcod.context.new(console=g.console, tileset=tileset) as g.context:
        game.state_tools.main_loop()
        
if __name__ == "__main__":
    main()