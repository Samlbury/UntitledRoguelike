"""This module store globally mutable variables used by this program"""

from __future__ import annotations

import tcod
import tcod.ecs

from game.state import State

context: tcod.context.Context
"""The window managed by tcod"""

console: tcod.console.Console
"""The console used for rendering"""

world: tcod.ecs.Registry
"""The active ECS regristy and current session"""

states: list[State] = []