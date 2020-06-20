import sdl2
from functools import partial
from догађај import pprint


def controller_device_added(event):
    """ https://wiki.libsdl.org/SDL_ControllerDeviceEvent """
    x = event.cdevice
    keys = ['type', 'timestamp', 'which']
    values = [x.type, x.timestamp, x.which]
    pprint("SDL_CONTROLLERDEVICEADDED", zip(keys, values))


def controller_device_removed(event):
    """ https://wiki.libsdl.org/SDL_ControllerDeviceEvent """
    x = event.cdevice
    keys = ['type', 'timestamp', 'which']
    values = [x.type, x.timestamp, x.which]
    pprint("SDL_CONTROLLERDEVICEREMOVED", zip(keys, values))


def controller_button(type_name, event):
    """ https://wiki.libsdl.org/SDL_ControllerButtonEvent """
    x = event.cbutton
    keys = ['type', 'timestamp', 'which', 'button', 'state']
    values = [x.type, x.timestamp, x.which, x.button, x.state]
    pprint(type_name, zip(keys, values))


def controller_axis_motion(event):
    """ https://wiki.libsdl.org/SDL_ControllerAxisEvent """
    x = event.caxis
    keys = ['type', 'timestamp', 'which', 'axis', 'value']
    values = [x.type, x.timestamp, x.which, x.axis, x.value]
    pprint("SDL_CONTROLLERAXISMOTION", zip(keys, values))


def региструј(обрада_догађаја):
    обрада_догађаја.региструј(sdl2.SDL_CONTROLLERBUTTONDOWN, partial(controller_button, 'SDL_CONTROLLERBUTTONDOWN'))
    обрада_догађаја.региструј(sdl2.SDL_CONTROLLERBUTTONUP, partial(controller_button, 'SDL_CONTROLLERBUTTONUP'))
    обрада_догађаја.региструј(sdl2.SDL_CONTROLLERAXISMOTION, controller_axis_motion)
    обрада_догађаја.региструј(sdl2.SDL_CONTROLLERDEVICEADDED, controller_device_added)
    обрада_догађаја.региструј(sdl2.SDL_CONTROLLERDEVICEREMOVED, controller_device_removed)

