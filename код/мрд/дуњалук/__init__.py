import sdl2
import ctypes
import atexit
from sortedcontainers import SortedDict


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
        # sdl2.SDL_WINDOW_SHOWN
        # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN
        sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_MAXIMIZED
        # sdl2.SDL_WINDOW_RESIZABLE | sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP
    )
    if not рез:
        raise Exception('SDL_CreateWindow', sdl2.SDL_GetError())
    return рез


def Молер(прозор):
    рез = sdl2.SDL_CreateRenderer(прозор, -1, 0)
    if not рез:
        raise Exception('SDL_CreateRenderer', sdl2.SDL_GetError())
    инфо = sdl2.SDL_RendererInfo()
    инфо_рез = sdl2.SDL_GetRendererInfo(рез, ctypes.byref(инфо))
    if инфо_рез != 0:
        raise Exception('SDL_GetRendererInfo', sdl2.SDL_GetError())
    print('МОЛЕР:', инфо.name.decode('utf-8'))
    if инфо.flags & sdl2.SDL_RENDERER_SOFTWARE:
        print('SDL_RENDERER_SOFTWARE')
    if инфо.flags & sdl2.SDL_RENDERER_ACCELERATED:
        print('SDL_RENDERER_ACCELERATED')
    if инфо.flags & sdl2.SDL_RENDERER_PRESENTVSYNC:
        print('SDL_RENDERER_PRESENTVSYNC')
    if инфо.flags & sdl2.SDL_RENDERER_TARGETTEXTURE:
        print('SDL_RENDERER_SOFTWARE')
    print('нтф', инфо.num_texture_formats)
    for и in range(инфо.num_texture_formats):
        пфиме = sdl2.SDL_GetPixelFormatName(инфо.texture_formats[и]).decode('utf-8')
        print(f'формат {пфиме}')
    print('макс ширина', инфо.max_texture_width)
    print('макс дужина', инфо.max_texture_height)
    return рез


def Шара(молер, ширина, висина):
    рез = sdl2.SDL_CreateTexture(
        молер,
        sdl2.SDL_PIXELFORMAT_RGBA32,
        sdl2.SDL_TEXTUREACCESS_STREAMING,
        ширина, висина)
    if not рез:
        raise Exception('SDL_CreateTexture', sdl2.SDL_GetError())
    return рез


def Површ(ширина, висина):
    рез = sdl2.SDL_CreateRGBSurfaceWithFormat(
        0,
        ширина,
        висина,
        32,
        sdl2.SDL_PIXELFORMAT_RGBA32)
    if not рез:
        raise Exception('SDL_CreateRGBSurfaceWithFormat', sdl2.SDL_GetError())
    return рез


class Шкработине():
    def __init__(бре):
        бре.дата = SortedDict()
        бре.ел = set()
        бре.бројач = 0

    def __iter__(бре):
        return iter(бре.дата.values())

    def додај(бре, приоритет, елемент):
        if елемент in бре.ел:
            raise ValueError('Шкработина већ додата:', елемент)
        бре.дата[(приоритет, бре.бројач)] = елемент
        бре.ел.add(елемент)
        бре.бројач += 1

    def уклони(бре, елемент):
        бре.ел.remove(елемент)
        for к in бре.дата.keys():
            if бре.дата[к] == елемент:
                del бре.дата[к]
                break
        else:
            raise ValueError('Шкработина није нађена:', елемент)


class Воденица():
    def __init__(бре, обрада_догађаја, шкработине, молер, главна_шара, главна_површ):
        бре.обрада_догађаја = обрада_догађаја
        бре.шкработине = шкработине
        бре.молер = молер
        бре.главна_шара = главна_шара
        бре.главна_површ = главна_површ

    def __call__(бре):
        крај = False
        догађај = sdl2.SDL_Event()
        while not крај:
            штампано = False
            while sdl2.SDL_PollEvent(ctypes.byref(догађај)) != 0:
                if догађај.type == sdl2.SDL_QUIT:
                    крај = True
                    break
                штампано = True
                бре.обрада_догађаја.обради(догађај)
            for шкработина in бре.шкработине:
                шкработина.нашкрабај()
            пиксели = бре.главна_површ.contents.pixels
            корак = бре.главна_површ.contents.pitch
            рез = sdl2.SDL_UpdateTexture(бре.главна_шара, None, пиксели, корак)
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

