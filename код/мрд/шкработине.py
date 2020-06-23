import sdl2
import random
import ctypes


class Шкработине():
    def __init__(бре, *шкработине):
        бре.листа = []
        for шкработина in шкработине:
            бре.листа.append(шкработина)

    def __iter__(бре):
        return iter(бре.листа)


class ЦрвенаКоцка():
    def обради(бре, догађај):
        код = догађај.key.keysym.scancode
        if код == sdl2.SDL_SCANCODE_UP:
            бре.y -= 1
        elif код == sdl2.SDL_SCANCODE_DOWN:
            бре.y += 1
        elif код == sdl2.SDL_SCANCODE_LEFT:
            бре.x -= 1
        elif код == sdl2.SDL_SCANCODE_RIGHT:
            бре.x += 1
        else:
            print(код)
        print(бре.x, бре.y)

    def __init__(бре, обрада_догађаја, површ):
        print("ЦрвенаКоцка __init__")
        обрада_догађаја.региструј(sdl2.SDL_KEYDOWN, бре.обради)
        бре.површ = површ
        бре.x = 0
        бре.y = 0

    def нашкрабај(бре):
        корак = бре.површ.contents.pitch
        ПА = ctypes.c_ubyte * (бре.површ.contents.h * корак)
        пиксели = ПА.from_address(бре.површ.contents.pixels)
        for y in range(бре.y + 0, бре.y + 16):
            for x in range(бре.x + 0, бре.x + 16):
                index = y * корак + x * 4
                пиксели[index + 0] = 255
                пиксели[index + 1] = 0
                пиксели[index + 2] = 0
                пиксели[index + 3] = 255


class ПлаваКоцка():
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
        бре.плава = sdl2.SDL_CreateRGBSurfaceWithFormat(0, 16, 16, 32, sdl2.SDL_PIXELFORMAT_RGBA32)
        if not бре.плава:
            raise Exception('SDL_CreateRGBSurfaceWithFormat', sdl2.SDL_GetError())
        рез = sdl2.SDL_SetSurfaceBlendMode(бре.плава, sdl2.SDL_BLENDMODE_NONE)
        if рез != 0:
            raise Exception('SDL_SetSurfaceBlendMode', sdl2.SDL_GetError())
        рез = sdl2.SDL_FillRect(бре.плава, ctypes.byref(бре.пуо), 0xFFFF0000)
        if рез != 0:
            raise Exception('SDL_FillRect', sdl2.SDL_GetError())
        бре.пуо.x = 50
        бре.пуо.y = 50

    def нашкрабај(бре):
        # рез = sdl2.SDL_FillRect(бре.главна_површ, ctypes.byref(бре.пуо), 0x00FF0000)
        # if рез != 0:
        #     raise Exception('SDL_FillRect', sdl2.SDL_GetError())
        рез = sdl2.SDL_BlitSurface(бре.плава, None, бре.главна_површ, ctypes.byref(бре.пуо))
        if рез != 0:
            raise Exception('SDL_BlitSurface', sdl2.SDL_GetError())


class ШаренаПозадина():
    def __init__(бре, површ):
        бре.површ = површ

    def нашкрабај(бре):
        корак = бре.површ.contents.pitch
        ПА = ctypes.c_ubyte * (бре.површ.contents.h * корак)
        пиксели = ПА.from_address(бре.површ.contents.pixels)
        висина = бре.површ.contents.h
        ширина = бре.површ.contents.w
        for _ in range(10000):
            y = random.randint(0, висина - 1)
            x = random.randint(0, ширина - 1)
            индекс = y * корак + x * 4 + random.randint(0, 3)
            пиксели[индекс] = random.randint(0, 255)


class Лупа():
    def обради(бре, догађај):
        код = догађај.key.keysym.scancode
        if код == sdl2.SDL_SCANCODE_L:
            pass

    def __init__(бре, главна_површ, обрада_догађаја):
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

    def нашкрабај(бре):
        рез = sdl2.SDL_BlitSurface(бре.главна_површ, бре.извор, бре.фокус, бре.извор)
        if рез != 0:
            raise Exception('SDL_BlitSurface', sdl2.SDL_GetError())
        рез = sdl2.SDL_BlitScaled(бре.фокус, бре.извор, бре.главна_површ, бре.притока)
        if рез != 0:
            raise Exception('SDL_BlitSurface', sdl2.SDL_GetError())

