import sdl2
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
        sdl2.SDL_DestroyRenderer(бре.молер.сиров)
        print("Гасим прозор")
        sdl2.SDL_DestroyWindow(бре.прозор.сиров)

    def __init__(бре, прозор, молер):
        бре.прозор = прозор
        бре.молер = молер
        atexit.register(бре.на_крају)


class Прозор():
    def __init__(бре, почетак, наслов, ширина, висина):
        бре.почетак = почетак
        бре.наслов = наслов
        бре.ширина = ширина
        бре.висина = висина
        бре.сиров = sdl2.SDL_CreateWindow(
            бре.наслов.encode('utf-8'),
            sdl2.SDL_WINDOWPOS_UNDEFINED,
            sdl2.SDL_WINDOWPOS_UNDEFINED,
            бре.ширина,
            бре.висина,
            sdl2.SDL_WINDOW_SHOWN
            # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN
            # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP
            # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_MAXIMIZED
        )


class Молер():
    def __init__(бре, прозор):
        бре.сиров = sdl2.SDL_CreateRenderer(прозор.сиров, -1, 0)
        if not бре.сиров:
            raise Exception('SDL_CreateRenderer', sdl2.SDL.GetError())

