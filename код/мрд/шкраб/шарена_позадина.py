import sdl2
import ctypes
import random
from мрд.дуњалук import Површ


class ШаренаПозадина():
    """ пример директне манипулације пикселима на површи """
    def __init__(бре, површ, шкработине):
        бре.површ = површ
        бре.шарено = Површ(бре.површ.contents.w, бре.површ.contents.h, sdl2.SDL_BLENDMODE_NONE)
        бре.корак = бре.шарено.contents.pitch
        ПА = ctypes.c_ubyte * (бре.шарено.contents.h * бре.корак)
        бре.пиксели = ПА.from_address(бре.шарено.contents.pixels)
        бре.висина = бре.шарено.contents.h
        бре.ширина = бре.шарено.contents.w
        бре.шкработине = шкработине
        шкработине.додај(0, бре)

    def нашкрабај(бре):
        for _ in range(100):
            y = random.randint(0, бре.висина - 1)
            x = random.randint(0, бре.ширина - 1)
            индекс = y * бре.корак + x * 4
            бре.пиксели[индекс + random.randint(0, 3)] = random.randint(0, 255)
        sdl2.SDL_BlitSurface(бре.шарено, None, бре.површ, None)
