import sdl2
from functools import partial
from улаз.__init__ import pprint


def joy_device_added(event):
    """ https://wiki.libsdl.org/SDL_JoyDeviceEvent """
    x = event.jdevice
    keys = ['type', 'timestamp', 'which']
    values = [x.type, x.timestamp, x.which]
    pprint("SDL_JOYDEVICEADDED", zip(keys, values))


def joy_device_removed(event):
    """ https://wiki.libsdl.org/SDL_JoyDeviceEvent """
    x = event.jdevice
    keys = ['type', 'timestamp', 'which']
    values = [x.type, x.timestamp, x.which]
    pprint("SDL_JOYDEVICEREMOVED", zip(keys, values))


def joy_button(type_name, event):
    """ https://wiki.libsdl.org/SDL_JoyButtonEvent """
    x = event.jbutton
    keys = ['type', 'timestamp', 'which', 'button', 'state']
    values = [x.type, x.timestamp, x.which, x.button, x.state]
    pprint(type_name, zip(keys, values))


def joy_axis_motion(event):
    """ https://wiki.libsdl.org/SDL_JoyAxisEvent """
    x = event.jaxis
    keys = ['type', 'timestamp', 'which', 'axis', 'value']
    values = [x.type, x.timestamp, x.which, x.axis, x.value]
    pprint("SDL_JOYAXISMOTION", zip(keys, values))


def joy_hat_motion(event):
    """ https://wiki.libsdl.org/SDL_JoyHatEvent """
    x = event.jhat
    keys = ['type', 'timestamp', 'which', 'hat', 'value']
    values = [x.type, x.timestamp, x.which, x.hat, x.value]
    pprint("SDL_JOYHATMOTION", zip(keys, values))


def напуни(обрада_догађаја):
    обрада_догађаја[sdl2.SDL_JOYBUTTONDOWN] = partial(joy_button, 'SDL_JOYBUTTONDOWN')
    обрада_догађаја[sdl2.SDL_JOYBUTTONUP] = partial(joy_button, 'SDL_JOYBUTTONUP')
    обрада_догађаја[sdl2.SDL_JOYAXISMOTION] = joy_axis_motion
    обрада_догађаја[sdl2.SDL_JOYHATMOTION] = joy_hat_motion
    обрада_догађаја[sdl2.SDL_JOYDEVICEADDED] = joy_device_added
    обрада_догађаја[sdl2.SDL_JOYDEVICEREMOVED] = joy_device_removed

