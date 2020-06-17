import random
import ctypes
import atexit
import sdl2
from улаз.штампа import штампа
event_handlers = {}


MAIN_WIDTH = 16 * 15
MAIN_HEIGHT = 9 * 15


RED = sdl2.SDL_Color(0xe5, 0x00, 0x00, 0xff)
GOLD = sdl2.SDL_Color(0xff, 0xcc, 0x00, 0xff)


def доцртај(my_pixels):
    def index(y, x):
        return (y * MAIN_WIDTH + x) * 4

    for y in range(0, 16):
        for x in range(0, 16):
            my_pixels[index(y, x) + 0] = 0
            my_pixels[index(y, x) + 1] = 0
            my_pixels[index(y, x) + 2] = 255
            my_pixels[index(y, x) + 3] = 255


def loop(штампа_догађаја, обрада_догађаја, renderer, texture):
    quit = False
    event = sdl2.SDL_Event()
    my_pixels = ctypes.create_string_buffer(MAIN_WIDTH * MAIN_HEIGHT * 4)
    for i, _ in enumerate(my_pixels):
        my_pixels[i] = random.randint(0, 255)
    while not quit:
        штампано = False
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                quit = True
                break
            if event.type not in штампа_догађаја:
                raise Exception('Непознат догађај:', hex(event.type))
            штампа_догађаја[event.type](event)
            штампано = True
            if event.type in обрада_догађаја:
                обрада_догађаја[event.type](event)
        for _ in range(10000):
            my_pixels[random.randint(0, MAIN_WIDTH * MAIN_HEIGHT * 4 - 1)] = random.randint(0, 255)
        доцртај(my_pixels)
        sdl2.SDL_UpdateTexture(texture, None, my_pixels, MAIN_WIDTH * 4)
        sdl2.SDL_RenderClear(renderer)
        sdl2.SDL_RenderCopy(renderer, texture, None, None)
        sdl2.SDL_RenderPresent(renderer)
        if штампано:
            print()


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


def main():
    atexit.register(sdl2.SDL_Quit)
    res = sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO | sdl2.SDL_INIT_AUDIO | sdl2.SDL_INIT_GAMECONTROLLER)
    if res != 0:
        raise Exception('SDL_Init', sdl2.SDL_GetError())
    res = sdl2.SDL_GameControllerAddMappingsFromFile(b"mygamecontrollerdb.txt")
    if res == -1:
        raise Exception('SDL_GameControllerAddMappingsFromFile', sdl2.SDL_GetError())
    window = sdl2.SDL_CreateWindow(
        "Mrd".encode('utf-8'),
        sdl2.SDL_WINDOWPOS_UNDEFINED,
        sdl2.SDL_WINDOWPOS_UNDEFINED,
        MAIN_WIDTH,
        MAIN_HEIGHT,
        sdl2.SDL_WINDOW_SHOWN
        # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN
        # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP
        # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_MAXIMIZED
    )
    if not window:
        raise Exception('SDL_CreateWindow', sdl2.SDL.GetError())
    renderer = sdl2.SDL_CreateRenderer(window, -1, 0)
    if not renderer:
        raise Exception('SDL_CreateRenderer', sdl2.SDL.GetError())
    штампа_догађаја = штампа()
    обрада_догађаја = {}
    обрада_догађаја[sdl2.SDL_CONTROLLERDEVICEADDED] = open_controller
    обрада_догађаја[sdl2.SDL_CONTROLLERDEVICEREMOVED] = close_controller
    # обрада_догађаја[sdl2.SDL_JOYDEVICEADDED] = open_joystick
    texture = sdl2.SDL_CreateTexture(
            renderer,
            sdl2.SDL_PIXELFORMAT_ARGB8888,
            sdl2.SDL_TEXTUREACCESS_STREAMING,
            MAIN_WIDTH, MAIN_HEIGHT)
    loop(штампа_догађаја, обрада_догађаја, renderer, texture)  # <---<<
    sdl2.SDL_DestroyRenderer(renderer)
    sdl2.SDL_DestroyWindow(window)


if __name__ == '__main__':
    main()

