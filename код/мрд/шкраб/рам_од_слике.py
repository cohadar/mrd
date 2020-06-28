import sdl2
from мрд.xkcd import БОЈЕ, инт_боја


class РамОдСлике():
    """ Demonstrira blend sa šupljinom / providnim pikselima """
    def __init__(бре, површ, положај, шкработине, име_боје):
        print("РамОдСлике __init__", име_боје)
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
        sdl2.SDL_SetSurfaceBlendMode(бре.плава, sdl2.SDL_BLENDMODE_BLEND)
        sdl2.SDL_FillRect(бре.плава, бре.пуо, инт_боја(бре.плава.contents.format, БОЈЕ[име_боје]))
        sdl2.SDL_FillRect(бре.плава, средина, инт_боја(бре.плава.contents.format, БОЈЕ['transparent']))

        бре.шкработине = шкработине
        бре.шкработине.додај(2, бре)

    def нашкрабај(бре):
        бре.пуо.x = бре.положај.x
        бре.пуо.y = бре.положај.y
        sdl2.SDL_BlitSurface(бре.плава, None, бре.површ, бре.пуо)

