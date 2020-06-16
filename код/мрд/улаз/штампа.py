import sdl2
from collections import namedtuple
from functools import partial

# https://wiki.libsdl.org/SDL_MouseButtonEvent
MouseButtonUp = namedtuple('MouseButtonUp', ['which', 'button', 'state', 'clicks', 'x', 'y'])
# https://wiki.libsdl.org/SDL_KeyboardEvent
KeyUp = namedtuple('KeyUp', ['state', 'repeat', 'keysym'])


def pprint(etype, pairs):
    print(f"{etype} ", end="")
    print(", ".join((f"{key}={value}" for key, value in pairs)))


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


def mouse_motion(event):
    """ https://wiki.libsdl.org/SDL_MouseMotionEvent """
    x = event.motion
    keys = ['type', 'timestamp', 'windowID', 'which', 'state', 'x', 'y', 'xrel', 'yrel']
    values = [x.type, x.timestamp, x.windowID, x.which, x.state, x.x, x.y, x.xrel, x.yrel]
    pprint("SDL_MOUSEMOTION", zip(keys, values))


def mouse_button_down(event):
    """ https://wiki.libsdl.org/SDL_MouseButtonEvent """
    x = event.button
    keys = ['type', 'timestamp', 'windowID', 'which', 'button', 'state', 'clicks', 'x', 'y']
    values = [x.type, x.timestamp, x.windowID, x.which, x.button, x.state, x.clicks, x.x, x.y]
    pprint("SDL_MOUSEBUTTONDOWN", zip(keys, values))


def mouse_button_up(event):
    """ https://wiki.libsdl.org/SDL_MouseButtonEvent """
    x = event.button
    keys = ['type', 'timestamp', 'windowID', 'which', 'button', 'state', 'clicks', 'x', 'y']
    values = [x.type, x.timestamp, x.windowID, x.which, x.button, x.state, x.clicks, x.x, x.y]
    pprint("SDL_MOUSEBUTTONUP", zip(keys, values))


def mouse_wheel(event):
    """ https://wiki.libsdl.org/SDL_MouseWheelEvent """
    """ Oba pravca, x i y su dostupna na trackpadu tastature, miševi imaju samo y """
    x = event.wheel
    keys = ['type', 'timestamp', 'windowID', 'which', 'x', 'y', 'direction']
    values = [x.type, x.timestamp, x.windowID, x.which, x.x, x.y, x.direction]
    pprint("SDL_MOUSEWHEEL", zip(keys, values))


def key_down(event):
    """ https://wiki.libsdl.org/SDL_KeyboardEvent """
    """ https://wiki.libsdl.org/SDL_Keysym """
    x = event.key
    keys = ['type', 'timestamp', 'windowID', 'state', 'repeat', 'keysym']
    y = x.keysym
    keysym = f"(scancode={y.scancode}, sym={y.sym}, mod={y.mod})"
    values = [x.type, x.timestamp, x.windowID, x.state, x.repeat, keysym]
    pprint("SDL_KEYDOWN", zip(keys, values))


def key_up(event):
    """ https://wiki.libsdl.org/SDL_KeyboardEvent """
    """ https://wiki.libsdl.org/SDL_Keysym """
    x = event.key
    keys = ['type', 'timestamp', 'windowID', 'state', 'repeat', 'keysym']
    y = x.keysym
    keysym = f"(scancode={y.scancode}, sym={y.sym}, mod={y.mod})"
    values = [x.type, x.timestamp, x.windowID, x.state, x.repeat, keysym]
    pprint("SDL_KEYUP", zip(keys, values))


def text_input(event):
    """ https://wiki.libsdl.org/SDL_TextInputEvent """
    x = event.text
    keys = ['type', 'timestamp', 'windowID', 'text']
    values = [x.type, x.timestamp, x.windowID, x.text]
    pprint("SDL_TEXTINPUT", zip(keys, values))


def keymap_changed(event):
    """ windowID is actually invalid in this event (it is not window based)  """
    x = event.key
    keys = ['type', 'timestamp']
    values = [x.type, x.timestamp]
    pprint("SDL_KEYMAPCHANGED", zip(keys, values))


def clipboard_update(event):
    """ https://wiki.libsdl.org/SDL_EventType """
    x = event.key
    keys = ['type', 'timestamp']
    values = [x.type, x.timestamp]
    pprint("SDL_CLIPBOARDUPDATE", zip(keys, values))


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


def штампа():
    обрада_догађаја = {}
    обрада_догађаја[sdl2.SDL_CONTROLLERBUTTONDOWN] = partial(controller_button, 'SDL_CONTROLLERBUTTONDOWN')
    обрада_догађаја[sdl2.SDL_CONTROLLERBUTTONUP] = partial(controller_button, 'SDL_CONTROLLERBUTTONUP')
    обрада_догађаја[sdl2.SDL_JOYBUTTONDOWN] = partial(joy_button, 'SDL_JOYBUTTONDOWN')
    обрада_догађаја[sdl2.SDL_JOYBUTTONUP] = partial(joy_button, 'SDL_JOYBUTTONUP')
    обрада_догађаја[sdl2.SDL_JOYAXISMOTION] = joy_axis_motion
    обрада_догађаја[sdl2.SDL_JOYHATMOTION] = joy_hat_motion
    обрада_догађаја[sdl2.SDL_CONTROLLERAXISMOTION] = controller_axis_motion
    обрада_догађаја[sdl2.SDL_AUDIODEVICEADDED] = audio_device_added
    обрада_догађаја[sdl2.SDL_WINDOWEVENT] = window_event
    обрада_догађаја[sdl2.SDL_MOUSEMOTION] = mouse_motion
    обрада_догађаја[sdl2.SDL_MOUSEBUTTONDOWN] = mouse_button_down
    обрада_догађаја[sdl2.SDL_MOUSEBUTTONUP] = mouse_button_up
    обрада_догађаја[sdl2.SDL_MOUSEWHEEL] = mouse_wheel
    обрада_догађаја[sdl2.SDL_KEYDOWN] = key_down
    обрада_догађаја[sdl2.SDL_KEYUP] = key_up
    обрада_догађаја[sdl2.SDL_TEXTINPUT] = text_input
    обрада_догађаја[sdl2.SDL_KEYMAPCHANGED] = keymap_changed
    обрада_догађаја[sdl2.SDL_CLIPBOARDUPDATE] = clipboard_update
    обрада_догађаја[sdl2.SDL_JOYDEVICEADDED] = joy_device_added
    обрада_догађаја[sdl2.SDL_JOYDEVICEREMOVED] = joy_device_removed
    обрада_догађаја[sdl2.SDL_CONTROLLERDEVICEADDED] = controller_device_added
    обрада_догађаја[sdl2.SDL_CONTROLLERDEVICEREMOVED] = controller_device_removed
    return обрада_догађаја

