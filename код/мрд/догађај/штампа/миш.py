import sdl2
from догађај import pprint


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


def напуни(обрада_догађаја):
    обрада_догађаја[sdl2.SDL_MOUSEMOTION] = mouse_motion
    обрада_догађаја[sdl2.SDL_MOUSEBUTTONDOWN] = mouse_button_down
    обрада_догађаја[sdl2.SDL_MOUSEBUTTONUP] = mouse_button_up
    обрада_догађаја[sdl2.SDL_MOUSEWHEEL] = mouse_wheel

