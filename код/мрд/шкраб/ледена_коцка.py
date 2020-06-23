import sdl2
import ctypes


class ЛеденаКоцка():
    """ Демонстрита директан приступ пикселима површи """
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
        print("ЛеденаКоцка __init__")
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
                # пиксели[index + 0] = 255  # црвени пиксел не дирамо
                пиксели[index + 1] = 255
                пиксели[index + 2] = 255
                пиксели[index + 3] = 255


