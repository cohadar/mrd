import ctypes
import random


class ШаренаПозадина():
    def __init__(бре, површ, шкработине):
        бре.површ = површ
        бре.шкработине = шкработине
        шкработине.додај(0, бре)

    def нашкрабај(бре):
        корак = бре.површ.contents.pitch
        ПА = ctypes.c_ubyte * (бре.површ.contents.h * корак)
        пиксели = ПА.from_address(бре.површ.contents.pixels)
        висина = бре.површ.contents.h
        ширина = бре.површ.contents.w
        for _ in range(1000):
            y = random.randint(0, висина - 1)
            x = random.randint(0, ширина - 1)
            индекс = y * корак + x * 4 + random.randint(0, 3)
            пиксели[индекс] = random.randint(0, 255)

