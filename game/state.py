"""Base classes for states"""

from typing import Protocol

import tcod

class State(Protocol):
    """An abstract game state"""

    __slots__ = ()

    def on_event(self, event: tcod.event.Event):
        """Called on events"""

    def on_draw(self, console: tcod.console.Console):
        """Called when the atate is being drawn"""