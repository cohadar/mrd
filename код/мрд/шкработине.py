import sdl2
import random


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

    def __init__(бре, обрада_догађаја, пиксели, ширина):
        print("ЦрвенаКоцка __init__")
        обрада_догађаја.региструј(sdl2.SDL_KEYDOWN, бре.обради)
        бре.пиксели = пиксели
        бре.ширина = ширина
        бре.x = 0
        бре.y = 0

    def нашкрабај(бре):
        for y in range(бре.y + 0, бре.y + 16):
            for x in range(бре.x + 0, бре.x + 16):
                index = (y * бре.ширина + x) * 4
                бре.пиксели[index + 0] = 0
                бре.пиксели[index + 1] = 0
                бре.пиксели[index + 2] = 255
                бре.пиксели[index + 3] = 255


class ШаренаПозадина():
    def __init__(бре, пиксели, ширина, висина):
        бре.пиксели = пиксели
        бре.ширина = ширина
        бре.висина = висина
        for i, _ in enumerate(бре.пиксели):
            бре.пиксели[i] = random.randint(0, 255)

    def нашкрабај(бре):
        for _ in range(10000):
            бре.пиксели[random.randint(0, бре.ширина * бре.висина * 4 - 1)] = random.randint(0, 255)

