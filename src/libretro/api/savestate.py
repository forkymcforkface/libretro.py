from ctypes import c_int
from enum import IntFlag, IntEnum


RETRO_SERIALIZATION_QUIRK_INCOMPLETE = 1 << 0
RETRO_SERIALIZATION_QUIRK_MUST_INITIALIZE = 1 << 1
RETRO_SERIALIZATION_QUIRK_CORE_VARIABLE_SIZE = 1 << 2
RETRO_SERIALIZATION_QUIRK_FRONT_VARIABLE_SIZE = 1 << 3
RETRO_SERIALIZATION_QUIRK_SINGLE_SESSION = 1 << 4
RETRO_SERIALIZATION_QUIRK_ENDIAN_DEPENDENT = 1 << 5
RETRO_SERIALIZATION_QUIRK_PLATFORM_DEPENDENT = 1 << 6

retro_savestate_context = c_int
RETRO_SAVESTATE_CONTEXT_NORMAL = 0
RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_INSTANCE = 1
RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_BINARY = 2
RETRO_SAVESTATE_CONTEXT_ROLLBACK_NETPLAY = 3
RETRO_SAVESTATE_CONTEXT_UNKNOWN = 0x7FFFFFFF


class SerializationQuirks(IntFlag):
    INCOMPLETE = RETRO_SERIALIZATION_QUIRK_INCOMPLETE
    MUST_INITIALIZE = RETRO_SERIALIZATION_QUIRK_MUST_INITIALIZE
    CORE_VARIABLE_SIZE = RETRO_SERIALIZATION_QUIRK_CORE_VARIABLE_SIZE
    FRONTEND_VARIABLE_SIZE = RETRO_SERIALIZATION_QUIRK_FRONT_VARIABLE_SIZE
    SINGLE_SESSION = RETRO_SERIALIZATION_QUIRK_SINGLE_SESSION
    ENDIAN_DEPENDENT = RETRO_SERIALIZATION_QUIRK_ENDIAN_DEPENDENT
    PLATFORM_DEPENDENT = RETRO_SERIALIZATION_QUIRK_PLATFORM_DEPENDENT

    ALL = (
        INCOMPLETE
        | MUST_INITIALIZE
        | CORE_VARIABLE_SIZE
        | FRONTEND_VARIABLE_SIZE
        | SINGLE_SESSION
        | ENDIAN_DEPENDENT
        | PLATFORM_DEPENDENT
    )


class SavestateContext(IntEnum):
    NORMAL = RETRO_SAVESTATE_CONTEXT_NORMAL
    RUNAHEAD_SAME_INSTANCE = RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_INSTANCE
    RUNAHEAD_SAME_BINARY = RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_BINARY
    ROLLBACK_NETPLAY = RETRO_SAVESTATE_CONTEXT_ROLLBACK_NETPLAY

    def __init__(self, value: int):
        self._type_ = "i"


__all__ = [
    "SerializationQuirks",
    "SavestateContext",
    "retro_savestate_context",
]
