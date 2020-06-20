import sdl2


def open_controller(event):
    """ https://wiki.libsdl.org/SDL_ControllerDeviceEvent """
    controller = sdl2.SDL_GameControllerOpen(event.cdevice.which)
    if not controller:
        raise Exception('SDL_GameControllerOpen', sdl2.SDL_GetError())
    print('otvoren gamepad', controller)
    mapping = sdl2.SDL_GameControllerMapping(controller)
    name = sdl2.SDL_GameControllerName(controller)
    print('mapping:', mapping)
    print('name:', name)


def open_joystick(event):
    """ https://wiki.libsdl.org/SDL_JoyDeviceEvent """
    joystick = sdl2.SDL_JoystickOpen(event.jdevice.which)
    if not joystick:
        raise Exception('SDL_JoystickOpen', sdl2.SDL_GetError())
    name = sdl2.SDL_JoystickName(joystick)
    print('joystick added:', name)


def close_controller(event):
    """ https://wiki.libsdl.org/SDL_ControllerDeviceEvent """
    pass


def направи():
    обрада_догађаја = {}
    обрада_догађаја[sdl2.SDL_CONTROLLERDEVICEADDED] = open_controller
    обрада_догађаја[sdl2.SDL_CONTROLLERDEVICEREMOVED] = close_controller
    # обрада_догађаја[sdl2.SDL_JOYDEVICEADDED] = open_joystick
    return обрада_догађаја


__all__ = ["направи"]

