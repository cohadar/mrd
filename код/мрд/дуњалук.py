import sdl2
import ctypes
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


def ГлавнаШара(молер, ширина, висина):
    рез = sdl2.SDL_CreateTexture(
        молер,
        sdl2.SDL_PIXELFORMAT_RGBA32,
        sdl2.SDL_TEXTUREACCESS_STREAMING,
        ширина, висина)
    if not рез:
        raise Exception('SDL_CreateTexture', sdl2.SDL_GetError())
    return рез


def Пиксели(ширина, висина):
    return ctypes.create_string_buffer(ширина * висина * 4)


def ГлавнаПоврш(пиксели, ширина, висина):
    рез = sdl2.SDL_CreateRGBSurfaceWithFormatFrom(
        ctypes.byref(пиксели),
        ширина,
        висина, 32,
        ширина * 4,
        sdl2.SDL_PIXELFORMAT_RGBA32)
    if not рез:
        raise Exception('SDL_CreateRGBSurfaceWithFormatFrom', sdl2.SDL_GetError())
    return рез


class Воденица():
    def __init__(бре, обрада_догађаја, шкработине, молер, главна_шара, главна_површ):
        бре.обрада_догађаја = обрада_догађаја
        бре.шкработине = шкработине
        бре.молер = молер
        бре.главна_шара = главна_шара
        бре.пиксели = главна_површ.contents.pixels
        бре.корак = главна_површ.contents.pitch

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
            рез = sdl2.SDL_UpdateTexture(бре.главна_шара, None, бре.пиксели, бре.корак)
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

