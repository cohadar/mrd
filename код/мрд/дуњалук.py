import sdl2
import ctypes
import random
import atexit


class Почетак():
    def на_крају(бре):
        print("Гасим sdl2")
        sdl2.SDL_Quit()

    def __init__(бре):
        atexit.register(бре.на_крају)
        рез = sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO | sdl2.SDL_INIT_AUDIO | sdl2.SDL_INIT_GAMECONTROLLER)
        if рез != 0:
            raise Exception('SDL_Init', sdl2.SDL_GetError())
        рез = sdl2.SDL_GameControllerAddMappingsFromFile(b"mygamecontrollerdb.txt")
        if рез == -1:
            raise Exception('SDL_GameControllerAddMappingsFromFile', sdl2.SDL_GetError())


class Крај():
    def на_крају(бре):
        print("Гасим молера")
        sdl2.SDL_DestroyRenderer(бре.молер)
        print("Гасим прозор")
        sdl2.SDL_DestroyWindow(бре.прозор)

    def __init__(бре, прозор, молер):
        бре.прозор = прозор
        бре.молер = молер
        atexit.register(бре.на_крају)


def Прозор(почетак, наслов, ширина, висина):
    рез = sdl2.SDL_CreateWindow(
        наслов.encode('utf-8'),
        sdl2.SDL_WINDOWPOS_UNDEFINED,
        sdl2.SDL_WINDOWPOS_UNDEFINED,
        ширина,
        висина,
        # sdl2.SDL_WINDOW_SHOWN
        sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN
        # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_MAXIMIZED
        # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP
    )
    if not рез:
        raise Exception('SDL_CreateWindow', sdl2.SDL_GetError())
    return рез


def Молер(прозор):
    рез = sdl2.SDL_CreateRenderer(прозор, -1, 0)
    if not рез:
        raise Exception('SDL_CreateRenderer', sdl2.SDL_GetError())
    return рез


def ГлавнаШара(молер, ширина, висина):
    рез = sdl2.SDL_CreateTexture(
        молер,
        sdl2.SDL_PIXELFORMAT_ARGB8888,
        sdl2.SDL_TEXTUREACCESS_STREAMING,
        ширина, висина)
    if not рез:
        raise Exception('SDL_CreateTexture', sdl2.SDL_GetError())
    return рез


class Воденица():
    def доцртај(бре, my_pixels):
        def index(y, x):
            return (y * бре.ширина + x) * 4

        for y in range(0, 16):
            for x in range(0, 16):
                my_pixels[index(y, x) + 0] = 0
                my_pixels[index(y, x) + 1] = 0
                my_pixels[index(y, x) + 2] = 255
                my_pixels[index(y, x) + 3] = 255

    def __init__(бре, штампа_догађаја, обрада_догађаја, молер, главна_шара, ширина, висина):
        бре.штампа_догађаја = штампа_догађаја
        бре.обрада_догађаја = обрада_догађаја
        бре.молер = молер
        бре.главна_шара = главна_шара
        бре.ширина = ширина
        бре.висина = висина

    def __call__(бре):
        quit = False
        event = sdl2.SDL_Event()
        my_pixels = ctypes.create_string_buffer(бре.ширина * бре.висина * 4)
        for i, _ in enumerate(my_pixels):
            my_pixels[i] = random.randint(0, 255)
        while not quit:
            штампано = False
            while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
                if event.type == sdl2.SDL_QUIT:
                    quit = True
                    break
                if event.type not in бре.штампа_догађаја:
                    raise Exception('Непознат догађај:', hex(event.type))
                бре.штампа_догађаја[event.type](event)
                штампано = True
                if event.type in бре.обрада_догађаја:
                    бре.обрада_догађаја[event.type](event)
            for _ in range(10000):
                my_pixels[random.randint(0, бре.ширина * бре.висина * 4 - 1)] = random.randint(0, 255)
            бре.доцртај(my_pixels)
            sdl2.SDL_UpdateTexture(бре.главна_шара, None, my_pixels, бре.ширина * 4)
            sdl2.SDL_RenderClear(бре.молер)
            sdl2.SDL_RenderCopy(бре.молер, бре.главна_шара, None, None)
            sdl2.SDL_RenderPresent(бре.молер)
            if штампано:
                print()

