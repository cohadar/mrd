import sdl2
import ctypes
import random
import atexit


class Почетак():
    def на_крају(бре):
        print("Гасим sdl2")
        sdl2.SDL_Quit()  # void function

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
        sdl2.SDL_DestroyRenderer(бре.молер)  # void function
        print("Гасим прозор")
        sdl2.SDL_DestroyWindow(бре.прозор)  # void function

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
        sdl2.SDL_WINDOW_SHOWN
        # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN
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
    def доцртај(бре):
        def index(y, x):
            return (y * бре.ширина + x) * 4

        for y in range(0, 16):
            for x in range(0, 16):
                бре.пиксели[index(y, x) + 0] = 0
                бре.пиксели[index(y, x) + 1] = 0
                бре.пиксели[index(y, x) + 2] = 255
                бре.пиксели[index(y, x) + 3] = 255

    def __init__(бре, штампа_догађаја, обрада_догађаја, молер, главна_шара, ширина, висина):
        бре.штампа_догађаја = штампа_догађаја
        бре.обрада_догађаја = обрада_догађаја
        бре.молер = молер
        бре.главна_шара = главна_шара
        бре.ширина = ширина
        бре.висина = висина
        бре.пиксели = ctypes.create_string_buffer(бре.ширина * бре.висина * 4)

    def __call__(бре):
        quit = False
        event = sdl2.SDL_Event()
        for i, _ in enumerate(бре.пиксели):
            бре.пиксели[i] = random.randint(0, 255)
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
                бре.пиксели[random.randint(0, бре.ширина * бре.висина * 4 - 1)] = random.randint(0, 255)
            бре.доцртај()
            рез = sdl2.SDL_UpdateTexture(бре.главна_шара, None, бре.пиксели, бре.ширина * 4)
            if рез != 0:
                raise Exception('SDL_UpdateTexture', sdl2.SDL_GetError())
            рез = sdl2.SDL_RenderClear(бре.молер)
            if рез != 0:
                raise Exception('SDL_RenderClear', sdl2.SDL_GetError())
            рез = sdl2.SDL_RenderCopy(бре.молер, бре.главна_шара, None, None)
            if рез != 0:
                raise Exception('SDL_RenderCopy', sdl2.SDL_GetError())
            sdl2.SDL_RenderPresent(бре.молер)  # void function
            if штампано:
                print()

