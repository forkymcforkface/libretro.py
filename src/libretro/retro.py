__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
from enum import IntEnum, IntFlag, unique, CONFORM, EJECT
import logging
import sys
from ctypes import *  # noqa: F401, F403
from typing import TYPE_CHECKING, get_type_hints

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

if not hasattr(ctypes, "c_uintptr"):
    class c_uintptr(ctypes._SimpleCData):
        _type_ = "P"

    ctypes._check_size(c_uintptr)



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# Taken from https://blag.nullteilerfrei.de/2021/06/20/prettier-struct-definitions-for-python-ctypes/
# Please use it for all future struct definitions
class FieldsFromTypeHints(type(ctypes.Structure)):
    def __new__(cls, name, bases, namespace):
        class AnnotationDummy:
            __annotations__ = namespace.get('__annotations__', {})
        annotations = get_type_hints(AnnotationDummy)
        namespace['_fields_'] = list(annotations.items())
        namespace['__slots__'] = list(annotations.keys())
        return type(ctypes.Structure).__new__(cls, name, bases, namespace)
# End preamble


RETRO_NUM_CORE_OPTION_VALUES_MAX = 128


class Rotation(IntEnum):
    NONE = 0
    NINETY = 1
    ONE_EIGHTY = 2
    TWO_SEVENTY = 3

    def __init__(self, value):
        self._type_ = 'I'


retro_language = c_int
RETRO_LANGUAGE_ENGLISH = 0
RETRO_LANGUAGE_JAPANESE = 1
RETRO_LANGUAGE_FRENCH = 2
RETRO_LANGUAGE_SPANISH = 3
RETRO_LANGUAGE_GERMAN = 4
RETRO_LANGUAGE_ITALIAN = 5
RETRO_LANGUAGE_DUTCH = 6
RETRO_LANGUAGE_PORTUGUESE_BRAZIL = 7
RETRO_LANGUAGE_PORTUGUESE_PORTUGAL = 8
RETRO_LANGUAGE_RUSSIAN = 9
RETRO_LANGUAGE_KOREAN = 10
RETRO_LANGUAGE_CHINESE_TRADITIONAL = 11
RETRO_LANGUAGE_CHINESE_SIMPLIFIED = 12
RETRO_LANGUAGE_ESPERANTO = 13
RETRO_LANGUAGE_POLISH = 14
RETRO_LANGUAGE_VIETNAMESE = 15
RETRO_LANGUAGE_ARABIC = 16
RETRO_LANGUAGE_GREEK = 17
RETRO_LANGUAGE_TURKISH = 18
RETRO_LANGUAGE_SLOVAK = 19
RETRO_LANGUAGE_PERSIAN = 20
RETRO_LANGUAGE_HEBREW = 21
RETRO_LANGUAGE_ASTURIAN = 22
RETRO_LANGUAGE_FINNISH = 23
RETRO_LANGUAGE_INDONESIAN = 24
RETRO_LANGUAGE_SWEDISH = 25
RETRO_LANGUAGE_UKRAINIAN = 26
RETRO_LANGUAGE_CZECH = 27
RETRO_LANGUAGE_CATALAN_VALENCIA = 28
RETRO_LANGUAGE_CATALAN = 29
RETRO_LANGUAGE_BRITISH_ENGLISH = 30
RETRO_LANGUAGE_HUNGARIAN = 31
RETRO_LANGUAGE_BELARUSIAN = 32
RETRO_LANGUAGE_LAST = (RETRO_LANGUAGE_BELARUSIAN + 1)
RETRO_LANGUAGE_DUMMY = 0x7fffffff


class Language(IntEnum):
    ENGLISH = RETRO_LANGUAGE_ENGLISH
    JAPANESE = RETRO_LANGUAGE_JAPANESE
    FRENCH = RETRO_LANGUAGE_FRENCH
    SPANISH = RETRO_LANGUAGE_SPANISH
    GERMAN = RETRO_LANGUAGE_GERMAN
    ITALIAN = RETRO_LANGUAGE_ITALIAN
    DUTCH = RETRO_LANGUAGE_DUTCH
    PORTUGUESE_BRAZIL = RETRO_LANGUAGE_PORTUGUESE_BRAZIL
    PORTUGUESE_PORTUGAL = RETRO_LANGUAGE_PORTUGUESE_PORTUGAL
    RUSSIAN = RETRO_LANGUAGE_RUSSIAN
    KOREAN = RETRO_LANGUAGE_KOREAN
    CHINESE_TRADITIONAL = RETRO_LANGUAGE_CHINESE_TRADITIONAL
    CHINESE_SIMPLIFIED = RETRO_LANGUAGE_CHINESE_SIMPLIFIED
    ESPERANTO = RETRO_LANGUAGE_ESPERANTO
    POLISH = RETRO_LANGUAGE_POLISH
    VIETNAMESE = RETRO_LANGUAGE_VIETNAMESE
    ARABIC = RETRO_LANGUAGE_ARABIC
    GREEK = RETRO_LANGUAGE_GREEK
    TURKISH = RETRO_LANGUAGE_TURKISH
    SLOVAK = RETRO_LANGUAGE_SLOVAK
    PERSIAN = RETRO_LANGUAGE_PERSIAN
    HEBREW = RETRO_LANGUAGE_HEBREW
    ASTURIAN = RETRO_LANGUAGE_ASTURIAN
    FINNISH = RETRO_LANGUAGE_FINNISH
    INDONESIAN = RETRO_LANGUAGE_INDONESIAN
    SWEDISH = RETRO_LANGUAGE_SWEDISH
    UKRAINIAN = RETRO_LANGUAGE_UKRAINIAN
    CZECH = RETRO_LANGUAGE_CZECH
    CATALAN_VALENCIA = RETRO_LANGUAGE_CATALAN_VALENCIA
    CATALAN = RETRO_LANGUAGE_CATALAN
    BRITISH_ENGLISH = RETRO_LANGUAGE_BRITISH_ENGLISH
    HUNGARIAN = RETRO_LANGUAGE_HUNGARIAN
    BELARUSIAN = RETRO_LANGUAGE_BELARUSIAN

    def __init__(self, value):
        self._type_ = 'I'


class retro_memory_descriptor(Structure):
    pass

retro_memory_descriptor.__slots__ = [
    'flags',
    'ptr',
    'offset',
    'start',
    'select',
    'disconnect',
    'len',
    'addrspace',
]
retro_memory_descriptor._fields_ = [
    ('flags', c_uint64),
    ('ptr', c_void_p),
    ('offset', c_size_t),
    ('start', c_size_t),
    ('select', c_size_t),
    ('disconnect', c_size_t),
    ('len', c_size_t),
    ('addrspace', String),
]

class retro_memory_map(Structure, metaclass=FieldsFromTypeHints):
    descriptors: POINTER(retro_memory_descriptor)
    num_descriptors: c_uint


class retro_controller_description(Structure):
    _fields_ = [
        ('desc', String),
        ('id', c_uint),
    ]

    __slots__ = [f[0] for f in _fields_]


class retro_controller_info(Structure, metaclass=FieldsFromTypeHints):
    types: POINTER(retro_controller_description)
    num_types: c_uint


class retro_subsystem_memory_info(Structure, metaclass=FieldsFromTypeHints):
    extension: String
    type: c_uint


class retro_subsystem_rom_info(Structure, metaclass=FieldsFromTypeHints):
    desc: String
    valid_extensions: String
    need_fullpath: c_bool
    block_extract: c_bool
    required: c_bool
    memory: POINTER(retro_subsystem_memory_info)
    num_memory: c_uint


class retro_subsystem_info(Structure, metaclass=FieldsFromTypeHints):
    desc: String
    ident: String
    roms: POINTER(retro_subsystem_rom_info)
    num_roms: c_uint
    id: c_uint


retro_perf_tick_t = c_uint64

retro_time_t = c_int64

class retro_perf_counter(Structure):
    pass

retro_perf_counter.__slots__ = [
    'ident',
    'start',
    'total',
    'call_cnt',
    'registered',
]
retro_perf_counter._fields_ = [
    ('ident', String),
    ('start', retro_perf_tick_t),
    ('total', retro_perf_tick_t),
    ('call_cnt', retro_perf_tick_t),
    ('registered', c_bool),
]

retro_perf_get_time_usec_t = CFUNCTYPE(UNCHECKED(retro_time_t), )

retro_perf_get_counter_t = CFUNCTYPE(UNCHECKED(retro_perf_tick_t), )

retro_get_cpu_features_t = CFUNCTYPE(c_uint64, )

retro_perf_log_t = CFUNCTYPE(None, )

retro_perf_register_t = CFUNCTYPE(None, POINTER(retro_perf_counter))

retro_perf_start_t = CFUNCTYPE(None, POINTER(retro_perf_counter))

retro_perf_stop_t = CFUNCTYPE(None, POINTER(retro_perf_counter))

class retro_perf_callback(Structure, metaclass=FieldsFromTypeHints):
    get_time_usec: retro_perf_get_time_usec_t
    get_cpu_features: retro_get_cpu_features_t
    get_perf_counter: retro_perf_get_counter_t
    perf_register: retro_perf_register_t
    perf_start: retro_perf_start_t
    perf_stop: retro_perf_stop_t
    perf_log: retro_perf_log_t


retro_sensor_action = c_int

RETRO_SENSOR_ACCELEROMETER_ENABLE = 0

RETRO_SENSOR_ACCELEROMETER_DISABLE = (RETRO_SENSOR_ACCELEROMETER_ENABLE + 1)

RETRO_SENSOR_GYROSCOPE_ENABLE = (RETRO_SENSOR_ACCELEROMETER_DISABLE + 1)

RETRO_SENSOR_GYROSCOPE_DISABLE = (RETRO_SENSOR_GYROSCOPE_ENABLE + 1)

RETRO_SENSOR_ILLUMINANCE_ENABLE = (RETRO_SENSOR_GYROSCOPE_DISABLE + 1)

RETRO_SENSOR_ILLUMINANCE_DISABLE = (RETRO_SENSOR_ILLUMINANCE_ENABLE + 1)

RETRO_SENSOR_DUMMY = 0x7fffffff

retro_set_sensor_state_t = CFUNCTYPE(c_bool, c_uint, retro_sensor_action, c_uint)

retro_sensor_get_input_t = CFUNCTYPE(c_float, c_uint, c_uint)

class retro_sensor_interface(Structure, metaclass=FieldsFromTypeHints):
    set_sensor_state: retro_set_sensor_state_t
    get_sensor_input: retro_sensor_get_input_t


retro_camera_buffer = c_int

RETRO_CAMERA_BUFFER_OPENGL_TEXTURE = 0

RETRO_CAMERA_BUFFER_RAW_FRAMEBUFFER = (RETRO_CAMERA_BUFFER_OPENGL_TEXTURE + 1)

RETRO_CAMERA_BUFFER_DUMMY = 0x7fffffff

retro_camera_start_t = CFUNCTYPE(c_bool, )

retro_camera_stop_t = CFUNCTYPE(None, )

retro_camera_lifetime_status_t = CFUNCTYPE(None, )

retro_camera_frame_raw_framebuffer_t = CFUNCTYPE(None, POINTER(c_uint32), c_uint, c_uint, c_size_t)

retro_camera_frame_opengl_texture_t = CFUNCTYPE(None, c_uint, c_uint, POINTER(c_float))

class retro_camera_callback(Structure, metaclass=FieldsFromTypeHints):
    caps: c_uint64
    width: c_uint
    height: c_uint
    start: retro_camera_start_t
    stop: retro_camera_stop_t
    frame_raw_framebuffer: retro_camera_frame_raw_framebuffer_t
    frame_opengl_texture: retro_camera_frame_opengl_texture_t
    initialized: retro_camera_lifetime_status_t
    deinitialized: retro_camera_lifetime_status_t


retro_rumble_effect = c_int

RETRO_RUMBLE_STRONG = 0

RETRO_RUMBLE_WEAK = 1

RETRO_RUMBLE_DUMMY = 0x7fffffff

retro_set_rumble_state_t = CFUNCTYPE(c_bool, c_uint, retro_rumble_effect, c_uint16)

class retro_rumble_interface(Structure, metaclass=FieldsFromTypeHints):
    set_rumble_state: retro_set_rumble_state_t

retro_audio_callback_t = CFUNCTYPE(None, )

retro_audio_set_state_callback_t = CFUNCTYPE(None, c_bool)

class retro_audio_callback(Structure, metaclass=FieldsFromTypeHints):
    callback: retro_audio_callback_t
    set_state: retro_audio_set_state_callback_t


retro_usec_t = c_int64

retro_frame_time_callback_t = CFUNCTYPE(None, retro_usec_t)

class retro_frame_time_callback(Structure, metaclass=FieldsFromTypeHints):
    callback: retro_frame_time_callback_t
    reference: retro_usec_t


retro_audio_buffer_status_callback_t = CFUNCTYPE(None, c_bool, c_uint, c_bool)

class retro_audio_buffer_status_callback(Structure, metaclass=FieldsFromTypeHints):
    callback: retro_audio_buffer_status_callback_t



retro_keyboard_event_t = CFUNCTYPE(None, c_bool, c_uint, c_uint32, c_uint16)

class retro_keyboard_callback(Structure, metaclass=FieldsFromTypeHints):
    callback: retro_keyboard_event_t


retro_set_eject_state_t = CFUNCTYPE(c_bool, c_bool)

retro_get_eject_state_t = CFUNCTYPE(c_bool, )

retro_get_image_index_t = CFUNCTYPE(c_uint, )

retro_set_image_index_t = CFUNCTYPE(c_bool, c_uint)

retro_get_num_images_t = CFUNCTYPE(c_uint, )


class retro_game_info(Structure, metaclass=FieldsFromTypeHints):
    path: c_char_p
    data: c_void_p
    size: c_size_t
    meta: c_char_p


retro_replace_image_index_t = CFUNCTYPE(c_bool, c_uint, POINTER(retro_game_info))

retro_add_image_index_t = CFUNCTYPE(c_bool, )

retro_set_initial_image_t = CFUNCTYPE(c_bool, c_uint, String)

retro_get_image_path_t = CFUNCTYPE(c_bool, c_uint, String, c_size_t)

retro_get_image_label_t = CFUNCTYPE(c_bool, c_uint, String, c_size_t)

class retro_disk_control_callback(Structure, metaclass=FieldsFromTypeHints):
    set_eject_state: retro_set_eject_state_t
    get_eject_state: retro_get_eject_state_t
    get_image_index: retro_get_image_index_t
    set_image_index: retro_set_image_index_t
    get_num_images: retro_get_num_images_t
    replace_image_index: retro_replace_image_index_t
    add_image_index: retro_add_image_index_t


class retro_disk_control_ext_callback(retro_disk_control_callback, metaclass=FieldsFromTypeHints):
    set_initial_image: retro_set_initial_image_t
    get_image_path: retro_get_image_path_t
    get_image_label: retro_get_image_label_t


retro_netpacket_send_t = CFUNCTYPE(None, c_int, c_void_p, c_size_t, c_uint16, c_bool)

retro_netpacket_start_t = CFUNCTYPE(None, c_uint16, retro_netpacket_send_t)

retro_netpacket_receive_t = CFUNCTYPE(None, c_void_p, c_size_t, c_uint16)

retro_netpacket_stop_t = CFUNCTYPE(None, )

retro_netpacket_poll_t = CFUNCTYPE(None, )

retro_netpacket_connected_t = CFUNCTYPE(c_bool, c_uint16)

retro_netpacket_disconnected_t = CFUNCTYPE(None, c_uint16)

class retro_netpacket_callback(Structure, metaclass=FieldsFromTypeHints):
    start: retro_netpacket_start_t
    receive: retro_netpacket_receive_t
    stop: retro_netpacket_stop_t
    poll: retro_netpacket_poll_t
    connected: retro_netpacket_connected_t
    disconnected: retro_netpacket_disconnected_t


retro_pixel_format = c_int
RETRO_PIXEL_FORMAT_0RGB1555 = 0
RETRO_PIXEL_FORMAT_XRGB8888 = 1
RETRO_PIXEL_FORMAT_RGB565 = 2
RETRO_PIXEL_FORMAT_UNKNOWN = 0x7fffffff


class PixelFormat(IntEnum):
    RGB1555 = RETRO_PIXEL_FORMAT_0RGB1555
    XRGB8888 = RETRO_PIXEL_FORMAT_XRGB8888
    RGB565 = RETRO_PIXEL_FORMAT_RGB565

    def __init__(self, value):
        self._type_ = 'I'

    @property
    def bytes_per_pixel(self) -> int:
        match self:
            case self.RGB1555:
                return 2
            case self.XRGB8888:
                return 4
            case self.RGB565:
                return 2
            case _:
                raise ValueError(f"Unknown pixel format: {self}")


retro_savestate_context = c_int

RETRO_SAVESTATE_CONTEXT_NORMAL = 0
RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_INSTANCE = 1
RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_BINARY = 2
RETRO_SAVESTATE_CONTEXT_ROLLBACK_NETPLAY = 3
RETRO_SAVESTATE_CONTEXT_UNKNOWN = 0x7fffffff


class SavestateContext(IntEnum):
    NORMAL = RETRO_SAVESTATE_CONTEXT_NORMAL
    RUNAHEAD_SAME_INSTANCE = RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_INSTANCE
    RUNAHEAD_SAME_BINARY = RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_BINARY
    ROLLBACK_NETPLAY = RETRO_SAVESTATE_CONTEXT_ROLLBACK_NETPLAY

    def __init__(self, value: int):
        self._type_ = 'i'


class retro_input_descriptor(Structure):
    pass

retro_input_descriptor.__slots__ = [
    'port',
    'device',
    'index',
    'id',
    'description',
]
retro_input_descriptor._fields_ = [
    ('port', c_uint),
    ('device', c_uint),
    ('index', c_uint),
    ('id', c_uint),
    ('description', String),
]


class retro_system_info(Structure, metaclass=FieldsFromTypeHints):
    library_name: String
    library_version: String
    valid_extensions: String
    need_fullpath: c_bool
    block_extract: c_bool


class retro_system_content_info_override(Structure, metaclass=FieldsFromTypeHints):
    extensions: String
    need_fullpath: c_bool
    persistent_data: c_bool

    def __repr__(self):
        return f"retro_system_content_info_override({self.extensions}, {self.need_fullpath!r}, {self.persistent_data!r})"

class retro_game_info_ext(Structure):
    pass

retro_game_info_ext.__slots__ = [
    'full_path',
    'archive_path',
    'archive_file',
    'dir',
    'name',
    'ext',
    'meta',
    'data',
    'size',
    'file_in_archive',
    'persistent_data',
]
retro_game_info_ext._fields_ = [
    ('full_path', String),
    ('archive_path', String),
    ('archive_file', String),
    ('dir', String),
    ('name', String),
    ('ext', String),
    ('meta', String),
    ('data', c_void_p),
    ('size', c_size_t),
    ('file_in_archive', c_bool),
    ('persistent_data', c_bool),
]

class retro_game_geometry(Structure, metaclass=FieldsFromTypeHints):
    base_width: c_uint
    base_height: c_uint
    max_width: c_uint
    max_height: c_uint
    aspect_ratio: c_float


class retro_system_timing(Structure, metaclass=FieldsFromTypeHints):
    fps: c_double
    sample_rate: c_double


class retro_system_av_info(Structure, metaclass=FieldsFromTypeHints):
    geometry: retro_game_geometry
    timing: retro_system_timing


class retro_variable(Structure, metaclass=FieldsFromTypeHints):
    key: c_char_p
    value: c_char_p


class retro_core_option_display(Structure, metaclass=FieldsFromTypeHints):
    key: c_char_p
    visible: c_bool


class retro_core_option_value(Structure, metaclass=FieldsFromTypeHints):
    value: c_char_p
    label: c_char_p


class retro_core_option_definition(Structure, metaclass=FieldsFromTypeHints):
    key: c_char_p
    desc: c_char_p
    info: c_char_p
    values: retro_core_option_value * RETRO_NUM_CORE_OPTION_VALUES_MAX
    default_value: c_char_p


class retro_core_options_intl(Structure, metaclass=FieldsFromTypeHints):
    us: POINTER(retro_core_option_definition)
    local: POINTER(retro_core_option_definition)


class retro_core_option_v2_category(Structure, metaclass=FieldsFromTypeHints):
    key: c_char_p
    desc: c_char_p
    info: c_char_p


class retro_core_option_v2_definition(Structure, metaclass=FieldsFromTypeHints):
    key: c_char_p
    desc: c_char_p
    desc_categorized: c_char_p
    info: c_char_p
    info_categorized: c_char_p
    category_key: c_char_p
    values: retro_core_option_value * RETRO_NUM_CORE_OPTION_VALUES_MAX
    default_value: c_char_p


class retro_core_options_v2(Structure, metaclass=FieldsFromTypeHints):
    categories: POINTER(retro_core_option_v2_category)
    definitions: POINTER(retro_core_option_v2_definition)


class retro_core_options_v2_intl(Structure, metaclass=FieldsFromTypeHints):
    us: POINTER(retro_core_options_v2)
    local: POINTER(retro_core_options_v2)


retro_core_options_update_display_callback_t = CFUNCTYPE(c_bool, )


class retro_core_options_update_display_callback(Structure, metaclass=FieldsFromTypeHints):
    callback: retro_core_options_update_display_callback_t


class retro_framebuffer(Structure, metaclass=FieldsFromTypeHints):
    data: c_void_p
    width: c_uint
    height: c_uint
    pitch: c_size_t
    format: retro_pixel_format
    access_flags: c_uint
    memory_flags: c_uint


class retro_fastforwarding_override(Structure, metaclass=FieldsFromTypeHints):
    ratio: c_float
    fastforward: c_bool
    notification: c_bool
    inhibit_toggle: c_bool


class retro_throttle_state(Structure, metaclass=FieldsFromTypeHints):
    mode: c_uint
    rate: c_float

# This one has no fields, it doesn't need the weight of a metaclass
class retro_microphone(Structure):
    pass

retro_microphone_t = retro_microphone

class retro_microphone_params(Structure, metaclass=FieldsFromTypeHints):
    rate: c_uint


retro_microphone_params_t = retro_microphone_params

retro_open_mic_t = CFUNCTYPE(UNCHECKED(POINTER(retro_microphone_t)), POINTER(retro_microphone_params_t))

retro_close_mic_t = CFUNCTYPE(None, POINTER(retro_microphone_t))

retro_get_mic_params_t = CFUNCTYPE(c_bool, POINTER(retro_microphone_t), POINTER(retro_microphone_params_t))

retro_set_mic_state_t = CFUNCTYPE(c_bool, POINTER(retro_microphone_t), c_bool)

retro_get_mic_state_t = CFUNCTYPE(c_bool, POINTER(retro_microphone_t))

retro_read_mic_t = CFUNCTYPE(c_int, POINTER(retro_microphone_t), POINTER(c_int16), c_size_t)

class retro_microphone_interface(Structure, metaclass=FieldsFromTypeHints):
    interface_version: c_uint
    open_mic: retro_open_mic_t
    close_mic: retro_close_mic_t
    get_params: retro_get_mic_params_t
    set_mic_state: retro_set_mic_state_t
    get_mic_state: retro_get_mic_state_t
    read_mic: retro_read_mic_t

retro_power_state = c_int

RETRO_POWERSTATE_UNKNOWN = 0

RETRO_POWERSTATE_DISCHARGING = (RETRO_POWERSTATE_UNKNOWN + 1)

RETRO_POWERSTATE_CHARGING = (RETRO_POWERSTATE_DISCHARGING + 1)

RETRO_POWERSTATE_CHARGED = (RETRO_POWERSTATE_CHARGING + 1)

RETRO_POWERSTATE_PLUGGED_IN = (RETRO_POWERSTATE_CHARGED + 1)

class retro_device_power(Structure, metaclass=FieldsFromTypeHints):
    state: retro_power_state
    seconds: c_int
    percent: c_int8



retro_video_refresh_t = CFUNCTYPE(None, c_void_p, c_uint, c_uint, c_size_t)

retro_audio_sample_t = CFUNCTYPE(None, c_int16, c_int16)

retro_audio_sample_batch_t = CFUNCTYPE(c_size_t, POINTER(c_int16), c_size_t)


RETRO_REGION_NTSC = 0
RETRO_REGION_PAL = 1


class Region(IntEnum):
    NTSC = RETRO_REGION_NTSC
    PAL = RETRO_REGION_PAL

    def __init__(self, value: int):
        self._type_ = 'I'


RETRO_MEMORY_MASK = 0xff
RETRO_MEMORY_SAVE_RAM = 0
RETRO_MEMORY_RTC = 1
RETRO_MEMORY_SYSTEM_RAM = 2
RETRO_MEMORY_VIDEO_RAM = 3


RETRO_SERIALIZATION_QUIRK_INCOMPLETE = (1 << 0)
RETRO_SERIALIZATION_QUIRK_MUST_INITIALIZE = (1 << 1)
RETRO_SERIALIZATION_QUIRK_CORE_VARIABLE_SIZE = (1 << 2)
RETRO_SERIALIZATION_QUIRK_FRONT_VARIABLE_SIZE = (1 << 3)
RETRO_SERIALIZATION_QUIRK_SINGLE_SESSION = (1 << 4)
RETRO_SERIALIZATION_QUIRK_ENDIAN_DEPENDENT = (1 << 5)
RETRO_SERIALIZATION_QUIRK_PLATFORM_DEPENDENT = (1 << 6)


class SerializationQuirks(IntFlag):
    INCOMPLETE = RETRO_SERIALIZATION_QUIRK_INCOMPLETE
    MUST_INITIALIZE = RETRO_SERIALIZATION_QUIRK_MUST_INITIALIZE
    CORE_VARIABLE_SIZE = RETRO_SERIALIZATION_QUIRK_CORE_VARIABLE_SIZE
    FRONTEND_VARIABLE_SIZE = RETRO_SERIALIZATION_QUIRK_FRONT_VARIABLE_SIZE
    SINGLE_SESSION = RETRO_SERIALIZATION_QUIRK_SINGLE_SESSION
    ENDIAN_DEPENDENT = RETRO_SERIALIZATION_QUIRK_ENDIAN_DEPENDENT
    PLATFORM_DEPENDENT = RETRO_SERIALIZATION_QUIRK_PLATFORM_DEPENDENT


RETRO_MEMDESC_CONST = (1 << 0)
RETRO_MEMDESC_BIGENDIAN = (1 << 1)
RETRO_MEMDESC_SYSTEM_RAM = (1 << 2)
RETRO_MEMDESC_SAVE_RAM = (1 << 3)
RETRO_MEMDESC_VIDEO_RAM = (1 << 4)
RETRO_MEMDESC_ALIGN_2 = (1 << 16)
RETRO_MEMDESC_ALIGN_4 = (2 << 16)
RETRO_MEMDESC_ALIGN_8 = (3 << 16)
RETRO_MEMDESC_MINSIZE_2 = (1 << 24)
RETRO_MEMDESC_MINSIZE_4 = (2 << 24)
RETRO_MEMDESC_MINSIZE_8 = (3 << 24)
RETRO_SIMD_SSE = (1 << 0)
RETRO_SIMD_SSE2 = (1 << 1)
RETRO_SIMD_VMX = (1 << 2)
RETRO_SIMD_VMX128 = (1 << 3)
RETRO_SIMD_AVX = (1 << 4)
RETRO_SIMD_NEON = (1 << 5)
RETRO_SIMD_SSE3 = (1 << 6)
RETRO_SIMD_SSSE3 = (1 << 7)
RETRO_SIMD_MMX = (1 << 8)
RETRO_SIMD_MMXEXT = (1 << 9)
RETRO_SIMD_SSE4 = (1 << 10)
RETRO_SIMD_SSE42 = (1 << 11)
RETRO_SIMD_AVX2 = (1 << 12)
RETRO_SIMD_VFPU = (1 << 13)
RETRO_SIMD_PS = (1 << 14)
RETRO_SIMD_AES = (1 << 15)
RETRO_SIMD_VFPV3 = (1 << 16)
RETRO_SIMD_VFPV4 = (1 << 17)
RETRO_SIMD_POPCNT = (1 << 18)
RETRO_SIMD_MOVBE = (1 << 19)
RETRO_SIMD_CMOV = (1 << 20)
RETRO_SIMD_ASIMD = (1 << 21)
RETRO_SENSOR_ACCELEROMETER_X = 0
RETRO_SENSOR_ACCELEROMETER_Y = 1
RETRO_SENSOR_ACCELEROMETER_Z = 2
RETRO_SENSOR_GYROSCOPE_X = 3
RETRO_SENSOR_GYROSCOPE_Y = 4
RETRO_SENSOR_GYROSCOPE_Z = 5
RETRO_SENSOR_ILLUMINANCE = 6
RETRO_HW_FRAME_BUFFER_VALID = cast((-1), c_void_p)
RETRO_NETPACKET_UNRELIABLE = 0
RETRO_NETPACKET_RELIABLE = (1 << 0)
RETRO_NETPACKET_UNSEQUENCED = (1 << 1)
RETRO_MEMORY_ACCESS_WRITE = (1 << 0)
RETRO_MEMORY_ACCESS_READ = (1 << 1)
RETRO_MEMORY_TYPE_CACHED = (1 << 0)
RETRO_THROTTLE_NONE = 0
RETRO_THROTTLE_FRAME_STEPPING = 1
RETRO_THROTTLE_FAST_FORWARD = 2
RETRO_THROTTLE_SLOW_MOTION = 3
RETRO_THROTTLE_REWINDING = 4
RETRO_THROTTLE_VSYNC = 5
RETRO_THROTTLE_UNBLOCKED = 6
RETRO_MICROPHONE_INTERFACE_VERSION = 1
RETRO_POWERSTATE_NO_ESTIMATE = (-1)


class PowerState(IntEnum):
    UNKNOWN = RETRO_POWERSTATE_UNKNOWN
    DISCHARGING = RETRO_POWERSTATE_DISCHARGING
    CHARGING = RETRO_POWERSTATE_CHARGING
    CHARGED = RETRO_POWERSTATE_CHARGED
    PLUGGED_IN = RETRO_POWERSTATE_PLUGGED_IN

    def __init__(self, value: int):
        self._type_ = 'I'
