import sdl2


class Лупа():
    def обради(бре, догађај):
        код = догађај.key.keysym.scancode
        if код == sdl2.SDL_SCANCODE_L:
            pass

    def __init__(бре, главна_површ, стаклена_површ, обрада_догађаја, шкработине):
        print("Лупа __init__")
        обрада_догађаја.региструј(sdl2.SDL_KEYDOWN, бре.обради)
        бре.главна_површ = главна_површ
        бре.стаклена_површ = стаклена_површ
        бре.извор = sdl2.SDL_Rect(0, 0, 16, 16)
        бре.притока = sdl2.SDL_Rect(16, 16, 16*4, 16*4)
        бре.фокус = sdl2.SDL_CreateRGBSurfaceWithFormat(0, 16, 16, 24, sdl2.SDL_PIXELFORMAT_RGB888)
        sdl2.SDL_SetSurfaceBlendMode(бре.фокус, sdl2.SDL_BLENDMODE_NONE)
        бре.шкработине = шкработине
        бре.шкработине.додај(10000, бре)

    def нашкрабај(бре):
        sdl2.SDL_BlitSurface(бре.главна_површ, бре.извор, бре.фокус, бре.извор)
        sdl2.SDL_BlitScaled(бре.фокус, бре.извор, бре.стаклена_површ, бре.притока)

