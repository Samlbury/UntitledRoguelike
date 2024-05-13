#!/user/bin/env python

import tcod

def main() -> None:
    tileset = tcod.tileset.load_tilesheet("data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437)
    tcod.tileset.procedural_block_elements(tileset=tileset)
    
    console = tcod.console.Console(80, 50)
    console.print(0, 0, "Hello World!") # Test print
    
    with tcod.context.new(console=console, tileset=tileset) as context:
        while True:
            context.present(console)
            for event in tcod.event.wait():
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()

if __name__ == "__main__":
    main()