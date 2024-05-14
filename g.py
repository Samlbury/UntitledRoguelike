"""This module store globally mutable variables used by this program"""

from __future__ import annotations

import tcod.context
import tcod.ecs

context: tcod.context.Context
"""The window managed by tcod"""

world: tcod.ecs.Registry
"""The active ECS regristy and current session"""