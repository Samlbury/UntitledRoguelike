#!/usr/bin/env python

import attrs
import tcod
from tcod.console import Console
from tcod.event import KeySym

@attrs.define(eq=False)
class ExampleState:
    player_x: int
    player_y: int

    def on_draw(self, console: Console) -> None:
        console.print(self.player_x, self.player_y, "@")

    def on_event(self, event: tcod.event.Event) -> None:
        match event:
            case tcod.event.Quit():
                raise SystemExit()
            case tcod.event.KeyDown(sym=KeySym.LEFT):
                self.player_x -= 1
            case tcod.event.KeyDown(sym=KeySym.RIGHT):
                self.player_x += 1
            case tcod.event.KeyDown(sym=KeySym.UP):
                self.player_y -= 1
            case tcod.event.KeyDown(sym=KeySym.DOWN):
                self.player_y += 1

def main() -> None:
    tileset = tcod.tileset.load_tilesheet("data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437)
    tcod.tileset.procedural_block_elements(tileset=tileset)
    
    console = Console(80, 50)

    state = ExampleState(player_x=console.width // 2, player_y=console.height //2)
    
    with tcod.context.new(console=console, tileset=tileset) as context:
        while True:
            console.clear()
            state.on_draw(console)
            context.present(console)
            for event in tcod.event.wait():
                state.on_event(event)

if __name__ == "__main__":
    main()