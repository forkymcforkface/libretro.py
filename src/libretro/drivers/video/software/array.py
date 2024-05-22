import itertools
from warnings import warn
from array import array
from copy import deepcopy
from typing import final, override

from libretro.api.av import retro_game_geometry, retro_system_av_info
from libretro.api.video import MemoryAccess, PixelFormat, Rotation, retro_framebuffer

from .base import SoftwareVideoDriver
from ..driver import FrameBufferSpecial, Screenshot


@final
class ArrayVideoDriver(SoftwareVideoDriver):
    def __init__(self):
        self._frame: array | None = None
        self._pixel_format: PixelFormat = PixelFormat.RGB1555
        self._system_av_info: retro_system_av_info | None = None
        self._rotation: Rotation = Rotation.NONE
        self._last_width: int | None = None
        self._last_height: int | None = None
        self._needs_reinit: bool = True

    @override
    def refresh(
            self, data: memoryview | FrameBufferSpecial, width: int, height: int, pitch: int
    ) -> None:
        match data:
            case memoryview():
                frameview = memoryview(self._frame)
                frameview[:len(data)] = data

            case FrameBufferSpecial.DUPE:
                pass # Do nothing

            case FrameBufferSpecial.HARDWARE:
                warn("RETRO_HW_FRAME_BUFFER_VALID passed to software-only video refresh callback")

            case _:
                raise TypeError(
                    f"Expected a memoryview or a FrameBufferSpecial, got {type(data).__name__}"
                )

        self._last_width = width
        self._last_height = height

    @override
    @property
    def needs_reinit(self) -> bool:
        return self._frame is None or self._needs_reinit

    @override
    def reinit(self) -> None:
        geometry = self._system_av_info.geometry
        bufsize = geometry.max_width * geometry.max_height * self._pixel_format.bytes_per_pixel
        self._frame = array("B", itertools.repeat(0, bufsize))
        self._needs_reinit = False

    @property
    @override
    def rotation(self) -> Rotation:
        return self._rotation

    @rotation.setter
    @override
    def rotation(self, rotation: Rotation) -> None:
        if not isinstance(rotation, Rotation):
            raise TypeError(f"Expected a Rotation, got {type(rotation).__name__}")

        if rotation not in Rotation:
            raise ValueError(f"Invalid rotation: {rotation}")

        self._rotation = rotation

    @property
    @override
    def pixel_format(self) -> PixelFormat:
        return self._pixel_format

    @pixel_format.setter
    @override
    def pixel_format(self, format: PixelFormat) -> None:
        if format not in PixelFormat:
            raise ValueError(f"Invalid pixel format: {format}")

        if not isinstance(format, PixelFormat):
            raise TypeError(f"Expected a PixelFormat, got {type(format).__name__}")

        if self._pixel_format != format:
            # If the pixel format has changed, recreate the frame buffer
            self._frame = None

        self._pixel_format = format

    @override
    def screenshot(self) -> Screenshot | None:
        if not self._frame:
            return None

        last_frame_length = self._last_width * self._last_height * self._pixel_format.bytes_per_pixel
        screen = self._frame[:last_frame_length]

        return Screenshot(
            memoryview(screen),
            self._last_width,
            self._last_height,
            self._rotation,
            self._pixel_format
        )

    def get_software_framebuffer(
            self, width: int, height: int, flags: MemoryAccess
    ) -> retro_framebuffer | None:
        pass

    @property
    @override
    def system_av_info(self) -> retro_system_av_info | None:
        return deepcopy(self._system_av_info) if self._system_av_info else None

    @system_av_info.setter
    @override
    def system_av_info(self, av_info: retro_system_av_info) -> None:
        if not isinstance(av_info, retro_system_av_info):
            raise TypeError(f"Expected a retro_system_av_info, got {type(av_info).__name__}")

        geometry: retro_game_geometry = av_info.geometry
        if not self._system_av_info or self._system_av_info.geometry.max_size != geometry.max_size:
            self._needs_reinit = True

        self._system_av_info = deepcopy(av_info)

    @property
    @override
    def geometry(self) -> retro_game_geometry | None:
        if not self._system_av_info:
            return None

        return deepcopy(self._system_av_info.geometry)

    @geometry.setter
    @override
    def geometry(self, geometry: retro_game_geometry) -> None:
        if not isinstance(geometry, retro_game_geometry):
            raise TypeError(f"Expected a retro_game_geometry, got {type(geometry).__name__}")

        self._system_av_info.geometry.base_width = geometry.base_width
        self._system_av_info.geometry.base_height = geometry.base_height
        self._system_av_info.geometry.aspect_ratio = geometry.aspect_ratio


__all__ = ["ArrayVideoDriver"]
