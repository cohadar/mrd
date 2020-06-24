import sdl2


class Лупа():
    def обради(бре, догађај):
        код = догађај.key.keysym.scancode
        if код == sdl2.SDL_SCANCODE_L:
            pass

    def __init__(бре, главна_површ, обрада_догађаја, шкработине):
        print("Лупа __init__")
        обрада_догађаја.региструј(sdl2.SDL_KEYDOWN, бре.обради)
        бре.главна_површ = главна_површ
        бре.извор = sdl2.SDL_Rect(0, 0, 16, 16)
        бре.притока = sdl2.SDL_Rect(16, 16, 16*4, 16*4)
        бре.фокус = sdl2.SDL_CreateRGBSurfaceWithFormat(0, 16, 16, 32, sdl2.SDL_PIXELFORMAT_RGBA32)
        if not бре.фокус:
            raise Exception('SDL_CreateRGBSurfaceWithFormat', sdl2.SDL_GetError())
        рез = sdl2.SDL_SetSurfaceBlendMode(бре.фокус, sdl2.SDL_BLENDMODE_NONE)
        if рез != 0:
            raise Exception('SDL_SetSurfaceBlendMode', sdl2.SDL_GetError())
        бре.шкработине = шкработине
        бре.шкработине.додај(10000, бре)

    def нашкрабај(бре):
        рез = sdl2.SDL_BlitSurface(бре.главна_површ, бре.извор, бре.фокус, бре.извор)
        if рез != 0:
            raise Exception('SDL_BlitSurface', sdl2.SDL_GetError())
        рез = sdl2.SDL_BlitScaled(бре.фокус, бре.извор, бре.главна_површ, бре.притока)
        if рез != 0:
            raise Exception('SDL_BlitSurface', sdl2.SDL_GetError())

