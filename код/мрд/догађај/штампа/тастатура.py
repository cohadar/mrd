import sdl2
from догађај import pprint


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


def напуни(обрада_догађаја):
    обрада_догађаја[sdl2.SDL_KEYDOWN] = key_down
    обрада_догађаја[sdl2.SDL_KEYUP] = key_up
    обрада_догађаја[sdl2.SDL_TEXTINPUT] = text_input
    обрада_догађаја[sdl2.SDL_KEYMAPCHANGED] = keymap_changed

