import sdl2
from догађај import pprint


def audio_device_added(event):
    """ https://wiki.libsdl.org/SDL_AudioDeviceEvent """
    x = event.adevice
    keys = ['type', 'timestamp', 'which', 'iscapture']
    values = [x.type, x.timestamp, x.which, x.iscapture]
    pprint("SDL_AUDIODEVICEADDED", zip(keys, values))


def window_event(event):
    """ https://wiki.libsdl.org/SDL_WindowEvent """
    x = event.window
    keys = ['type', 'timestamp', 'windowID', 'event', 'data1', 'data2']
    values = [x.type, x.timestamp, x.windowID, x.event, x.data1, x.data2]
    pprint("SDL_WINDOWEVENT", zip(keys, values))


def clipboard_update(event):
    """ https://wiki.libsdl.org/SDL_EventType """
    x = event.key
    keys = ['type', 'timestamp']
    values = [x.type, x.timestamp]
    pprint("SDL_CLIPBOARDUPDATE", zip(keys, values))


def региструј(обрада_догађаја):
    обрада_догађаја.региструј(sdl2.SDL_AUDIODEVICEADDED, audio_device_added)
    обрада_догађаја.региструј(sdl2.SDL_WINDOWEVENT, window_event)
    обрада_догађаја.региструј(sdl2.SDL_CLIPBOARDUPDATE, clipboard_update)

