import sdl2
import ctypes


class ПлаваКоцка():
    """ Demonstrira blend sa šupljinom / providnim pikselima """
    def обради(бре, догађај):
        код = догађај.key.keysym.scancode
        if код == sdl2.SDL_SCANCODE_W:
            бре.пуо.y -= 1
        elif код == sdl2.SDL_SCANCODE_S:
            бре.пуо.y += 1
        elif код == sdl2.SDL_SCANCODE_A:
            бре.пуо.x -= 1
        elif код == sdl2.SDL_SCANCODE_D:
            бре.пуо.x += 1
        else:
            print(код)
        print(бре.пуо.x, бре.пуо.y)

    def __init__(бре, главна_површ, обрада_догађаја):
        print("ПлаваКоцка __init__")
        обрада_догађаја.региструј(sdl2.SDL_KEYDOWN, бре.обради)
        бре.главна_површ = главна_површ
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
        бре.пуо.x = главна_површ.contents.w // 2
        бре.пуо.y = главна_површ.contents.h // 2

    def нашкрабај(бре):
        # рез = sdl2.SDL_FillRect(бре.главна_површ, ctypes.byref(бре.пуо), 0x00FF0000)
        # if рез != 0:
        #     raise Exception('SDL_FillRect', sdl2.SDL_GetError())
        рез = sdl2.SDL_BlitSurface(бре.плава, None, бре.главна_површ, ctypes.byref(бре.пуо))
        if рез != 0:
            raise Exception('SDL_BlitSurface', sdl2.SDL_GetError())

