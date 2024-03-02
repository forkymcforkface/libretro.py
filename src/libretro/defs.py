from collections.abc import *
from typing import *
import enum
from os import PathLike

from ._libretro import *


class Rotation(enum.IntEnum):
    NONE = 0
    _90 = 1
    _180 = 2
    _270 = 3


class PixelFormat(enum.IntEnum):
    RGB1555 = RETRO_PIXEL_FORMAT_0RGB1555
    XRGB8888 = RETRO_PIXEL_FORMAT_XRGB8888
    RGB565 = RETRO_PIXEL_FORMAT_RGB565


class Region(enum.IntEnum):
    NTSC = RETRO_REGION_NTSC
    PAL = RETRO_REGION_PAL


class LogLevel(enum.IntEnum):
    Debug = RETRO_LOG_DEBUG
    Info = RETRO_LOG_INFO
    Warning = RETRO_LOG_WARN
    Error = RETRO_LOG_ERROR


class Language(enum.IntEnum):
    English = RETRO_LANGUAGE_ENGLISH
    Japanese = RETRO_LANGUAGE_JAPANESE
    French = RETRO_LANGUAGE_FRENCH
    Spanish = RETRO_LANGUAGE_SPANISH
    German = RETRO_LANGUAGE_GERMAN
    Italian = RETRO_LANGUAGE_ITALIAN
    Dutch = RETRO_LANGUAGE_DUTCH
    PortugueseBrazil = RETRO_LANGUAGE_PORTUGUESE_BRAZIL
    PortuguesePortugal = RETRO_LANGUAGE_PORTUGUESE_PORTUGAL
    Russian = RETRO_LANGUAGE_RUSSIAN
    Korean = RETRO_LANGUAGE_KOREAN
    ChineseTraditional = RETRO_LANGUAGE_CHINESE_TRADITIONAL
    ChineseSimplified = RETRO_LANGUAGE_CHINESE_SIMPLIFIED
    Esperanto = RETRO_LANGUAGE_ESPERANTO
    Polish = RETRO_LANGUAGE_POLISH
    Vietnamese = RETRO_LANGUAGE_VIETNAMESE
    Arabic = RETRO_LANGUAGE_ARABIC
    Greek = RETRO_LANGUAGE_GREEK
    Turkish = RETRO_LANGUAGE_TURKISH
    Slovak = RETRO_LANGUAGE_SLOVAK
    Persian = RETRO_LANGUAGE_PERSIAN
    Hebrew = RETRO_LANGUAGE_HEBREW
    Asturian = RETRO_LANGUAGE_ASTURIAN
    Finnish = RETRO_LANGUAGE_FINNISH
    Indonesian = RETRO_LANGUAGE_INDONESIAN
    Swedish = RETRO_LANGUAGE_SWEDISH
    Ukrainian = RETRO_LANGUAGE_UKRAINIAN
    Czech = RETRO_LANGUAGE_CZECH
    CatalanValencia = RETRO_LANGUAGE_CATALAN_VALENCIA
    Catalan = RETRO_LANGUAGE_CATALAN
    BritishEnglish = RETRO_LANGUAGE_BRITISH_ENGLISH
    Hungarian = RETRO_LANGUAGE_HUNGARIAN
    Belarusian = RETRO_LANGUAGE_BELARUSIAN


@enum.unique
class EnvironmentCall(enum.IntEnum):
    SetRotation = RETRO_ENVIRONMENT_SET_ROTATION
    GetOverscan = RETRO_ENVIRONMENT_GET_OVERSCAN
    GetCanDupe = RETRO_ENVIRONMENT_GET_CAN_DUPE
    SetMessage = RETRO_ENVIRONMENT_SET_MESSAGE
    Shutdown = RETRO_ENVIRONMENT_SHUTDOWN
    SetPerformanceLevel = RETRO_ENVIRONMENT_SET_PERFORMANCE_LEVEL
    GetSystemDirectory = RETRO_ENVIRONMENT_GET_SYSTEM_DIRECTORY
    SetPixelFormat = RETRO_ENVIRONMENT_SET_PIXEL_FORMAT
    SetInputDescriptors = RETRO_ENVIRONMENT_SET_INPUT_DESCRIPTORS
    SetKeyboardCallback = RETRO_ENVIRONMENT_SET_KEYBOARD_CALLBACK
    SetDiskControlInterface = RETRO_ENVIRONMENT_SET_DISK_CONTROL_INTERFACE
    SetHwRender = RETRO_ENVIRONMENT_SET_HW_RENDER
    GetVariable = RETRO_ENVIRONMENT_GET_VARIABLE
    SetVariables = RETRO_ENVIRONMENT_SET_VARIABLES
    GetVariableUpdate = RETRO_ENVIRONMENT_GET_VARIABLE_UPDATE
    SetSupportNoGame = RETRO_ENVIRONMENT_SET_SUPPORT_NO_GAME
    GetLibretroPath = RETRO_ENVIRONMENT_GET_LIBRETRO_PATH
    SetFrameTimeCallback = RETRO_ENVIRONMENT_SET_FRAME_TIME_CALLBACK
    SetAudioCallback = RETRO_ENVIRONMENT_SET_AUDIO_CALLBACK
    GetRumbleInterface = RETRO_ENVIRONMENT_GET_RUMBLE_INTERFACE
    GetInputDeviceCapabilities = RETRO_ENVIRONMENT_GET_INPUT_DEVICE_CAPABILITIES
    GetSensorInterface = RETRO_ENVIRONMENT_GET_SENSOR_INTERFACE
    GetCameraInterface = RETRO_ENVIRONMENT_GET_CAMERA_INTERFACE
    GetLogInterface = RETRO_ENVIRONMENT_GET_LOG_INTERFACE
    GetPerfInterface = RETRO_ENVIRONMENT_GET_PERF_INTERFACE
    GetLocationInterface = RETRO_ENVIRONMENT_GET_LOCATION_INTERFACE
    GetCoreAssetsDirectory = RETRO_ENVIRONMENT_GET_CORE_ASSETS_DIRECTORY
    GetSaveDirectory = RETRO_ENVIRONMENT_GET_SAVE_DIRECTORY
    SetSystemAvInfo = RETRO_ENVIRONMENT_SET_SYSTEM_AV_INFO
    SetProcAddressCallback = RETRO_ENVIRONMENT_SET_PROC_ADDRESS_CALLBACK
    SetSubsystemInfo = RETRO_ENVIRONMENT_SET_SUBSYSTEM_INFO
    SetControllerInfo = RETRO_ENVIRONMENT_SET_CONTROLLER_INFO
    SetMemoryMaps = RETRO_ENVIRONMENT_SET_MEMORY_MAPS
    SetGeometry = RETRO_ENVIRONMENT_SET_GEOMETRY
    GetUsername = RETRO_ENVIRONMENT_GET_USERNAME
    GetLanguage = RETRO_ENVIRONMENT_GET_LANGUAGE
    GetCurrentSoftwareFramebuffer = RETRO_ENVIRONMENT_GET_CURRENT_SOFTWARE_FRAMEBUFFER
    GetHwRenderInterface = RETRO_ENVIRONMENT_GET_HW_RENDER_INTERFACE
    SetSupportAchievements = RETRO_ENVIRONMENT_SET_SUPPORT_ACHIEVEMENTS
    SetHwRenderContextNegotiationInterface = RETRO_ENVIRONMENT_SET_HW_RENDER_CONTEXT_NEGOTIATION_INTERFACE
    SetSerializationQuirks = RETRO_ENVIRONMENT_SET_SERIALIZATION_QUIRKS
    SetHwSharedContext = RETRO_ENVIRONMENT_SET_HW_SHARED_CONTEXT
    GetVfsInterface = RETRO_ENVIRONMENT_GET_VFS_INTERFACE
    GetLedInterface = RETRO_ENVIRONMENT_GET_LED_INTERFACE
    GetAudioVideoEnable = RETRO_ENVIRONMENT_GET_AUDIO_VIDEO_ENABLE
    GetMidiInterface = RETRO_ENVIRONMENT_GET_MIDI_INTERFACE
    GetFastForwarding = RETRO_ENVIRONMENT_GET_FASTFORWARDING
    GetTargetRefreshRate = RETRO_ENVIRONMENT_GET_TARGET_REFRESH_RATE
    GetInputBitmasks = RETRO_ENVIRONMENT_GET_INPUT_BITMASKS
    GetCoreOptionsVersion = RETRO_ENVIRONMENT_GET_CORE_OPTIONS_VERSION
    SetCoreOptions = RETRO_ENVIRONMENT_SET_CORE_OPTIONS
    SetCoreOptionsIntl = RETRO_ENVIRONMENT_SET_CORE_OPTIONS_INTL
    SetCoreOptionsDisplay = RETRO_ENVIRONMENT_SET_CORE_OPTIONS_DISPLAY
    GetPreferredHwRender = RETRO_ENVIRONMENT_GET_PREFERRED_HW_RENDER
    GetDiskControlInterfaceVersion = RETRO_ENVIRONMENT_GET_DISK_CONTROL_INTERFACE_VERSION
    SetDiskControlExtInterface = RETRO_ENVIRONMENT_SET_DISK_CONTROL_EXT_INTERFACE
    GetMessageInterfaceVersion = RETRO_ENVIRONMENT_GET_MESSAGE_INTERFACE_VERSION
    SetMessageExt = RETRO_ENVIRONMENT_SET_MESSAGE_EXT
    GetInputMaxUsers = RETRO_ENVIRONMENT_GET_INPUT_MAX_USERS
    SetAudioBufferStatusCallback = RETRO_ENVIRONMENT_SET_AUDIO_BUFFER_STATUS_CALLBACK
    SetMinimumAudioLatency = RETRO_ENVIRONMENT_SET_MINIMUM_AUDIO_LATENCY
    SetFastForwardingOverride = RETRO_ENVIRONMENT_SET_FASTFORWARDING_OVERRIDE
    SetContentInfoOverride = RETRO_ENVIRONMENT_SET_CONTENT_INFO_OVERRIDE
    GetGameInfoExt = RETRO_ENVIRONMENT_GET_GAME_INFO_EXT
    SetCoreOptionsV2 = RETRO_ENVIRONMENT_SET_CORE_OPTIONS_V2
    SetCoreOptionsV2Intl = RETRO_ENVIRONMENT_SET_CORE_OPTIONS_V2_INTL
    SetCoreOptionsUpdateDisplayCallback = RETRO_ENVIRONMENT_SET_CORE_OPTIONS_UPDATE_DISPLAY_CALLBACK
    SetVariable = RETRO_ENVIRONMENT_SET_VARIABLE
    GetThrottleState = RETRO_ENVIRONMENT_GET_THROTTLE_STATE
    GetSaveStateContext = RETRO_ENVIRONMENT_GET_SAVESTATE_CONTEXT
    GetHwRenderContextNegotiationInterfaceSupport = RETRO_ENVIRONMENT_GET_HW_RENDER_CONTEXT_NEGOTIATION_INTERFACE_SUPPORT
    GetJitCapable = RETRO_ENVIRONMENT_GET_JIT_CAPABLE
    GetMicrophoneInterface = RETRO_ENVIRONMENT_GET_MICROPHONE_INTERFACE
    SetNetpacketInterface = RETRO_ENVIRONMENT_SET_NETPACKET_INTERFACE
    GetDevicePower = RETRO_ENVIRONMENT_GET_DEVICE_POWER
    GetPlaylistDirectory = 79 # Not synced to libretro-common yet


class SerializationQuirks(enum.IntFlag):
    Incomplete = RETRO_SERIALIZATION_QUIRK_INCOMPLETE
    MustInitialize = RETRO_SERIALIZATION_QUIRK_MUST_INITIALIZE
    CoreVariableSize = RETRO_SERIALIZATION_QUIRK_CORE_VARIABLE_SIZE
    FrontendVariableSize = RETRO_SERIALIZATION_QUIRK_FRONT_VARIABLE_SIZE
    SingleSession = RETRO_SERIALIZATION_QUIRK_SINGLE_SESSION
    EndianDependent = RETRO_SERIALIZATION_QUIRK_ENDIAN_DEPENDENT
    PlatformDependent = RETRO_SERIALIZATION_QUIRK_PLATFORM_DEPENDENT


class SavestateContext(enum.IntEnum):
    Normal = RETRO_SAVESTATE_CONTEXT_NORMAL
    RunaheadSameInstance = RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_INSTANCE
    RunaheadSameBinary = RETRO_SAVESTATE_CONTEXT_RUNAHEAD_SAME_BINARY
    RollbackNetplay = RETRO_SAVESTATE_CONTEXT_ROLLBACK_NETPLAY
    Unknown = RETRO_SAVESTATE_CONTEXT_UNKNOWN


if sys.version_info >= (3, 12):
    Content: TypeAlias = PathLike | bytes | bytearray | memoryview | Buffer
    # Buffer was added in Python 3.12
else:
    Content: TypeAlias = PathLike | bytes | bytearray | memoryview

EnvironmentCallable: TypeAlias = Callable[[c_uint, c_void_p], c_bool]
EnvironmentCallback: TypeAlias = retro_environment_t | EnvironmentCallable

VideoRefreshCallable: TypeAlias = Callable[[c_void_p, c_uint, c_uint, c_size_t], None]
VideoRefreshCallback: TypeAlias = retro_video_refresh_t | VideoRefreshCallable

AudioSampleCallable: TypeAlias = Callable[[c_int16, c_int16], None]
AudioSampleCallback: TypeAlias = retro_audio_sample_t | AudioSampleCallable

AudioSampleBatchCallable: TypeAlias = Callable[[POINTER(c_int16), c_size_t], c_size_t]
AudioSampleBatchCallback: TypeAlias = retro_audio_sample_batch_t | AudioSampleBatchCallable

InputPollCallable: TypeAlias = Callable[[], None]
InputPollCallback: TypeAlias = retro_input_poll_t | InputPollCallable

InputStateCallable: TypeAlias = Callable[[c_uint, c_uint, c_uint, c_uint], c_int16]
InputStateCallback: TypeAlias = retro_input_state_t | InputStateCallable

