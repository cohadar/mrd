import sdl2


class ПлаваКоцка():
    """ Demonstrira blend sa šupljinom / providnim pikselima """
    def __init__(бре, површ, положај, шкработине):
        print("ПлаваКоцка __init__")
        бре.положај = положај  # претпоставка је да се положај мења споља
        бре.површ = површ
        бре.пуо = sdl2.SDL_Rect()
        бре.пуо.x = 0
        бре.пуо.y = 0
        бре.пуо.w = 16
        бре.пуо.h = 16
        средина = sdl2.SDL_Rect()
        средина.x = 3
        средина.y = 3
        средина.w = 10
        средина.h = 10

        бре.плава = sdl2.SDL_CreateRGBSurfaceWithFormat(0, 16, 16, 32, sdl2.SDL_PIXELFORMAT_RGBA32)
        if not бре.плава:
            raise Exception('SDL_CreateRGBSurfaceWithFormat', sdl2.SDL_GetError())
        рез = sdl2.SDL_SetSurfaceBlendMode(бре.плава, sdl2.SDL_BLENDMODE_BLEND)
        if рез != 0:
            raise Exception('SDL_SetSurfaceBlendMode', sdl2.SDL_GetError())
        рез = sdl2.SDL_FillRect(бре.плава, бре.пуо, 0xFFFF0000)
        if рез != 0:
            raise Exception('SDL_FillRect', sdl2.SDL_GetError())
        рез = sdl2.SDL_FillRect(бре.плава, средина, 0x0)
        if рез != 0:
            raise Exception('SDL_FillRect', sdl2.SDL_GetError())

        бре.шкработине = шкработине
        бре.шкработине.додај(2, бре)

    def нашкрабај(бре):
        бре.пуо.x = бре.положај.x
        бре.пуо.y = бре.положај.y
        рез = sdl2.SDL_BlitSurface(бре.плава, None, бре.површ, бре.пуо)
        if рез != 0:
            raise Exception('SDL_BlitSurface', sdl2.SDL_GetError())

