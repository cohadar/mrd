import sdl2


class Стрелице():
    def обради(бре, догађај):
        код = догађај.key.keysym.scancode
        if код == sdl2.SDL_SCANCODE_UP:
            бре.положај.y -= 1
        elif код == sdl2.SDL_SCANCODE_DOWN:
            бре.положај.y += 1
        elif код == sdl2.SDL_SCANCODE_LEFT:
            бре.положај.x -= 1
        elif код == sdl2.SDL_SCANCODE_RIGHT:
            бре.положај.x += 1

    def __init__(бре, обрада_догађаја, положај):
        обрада_догађаја.региструј(sdl2.SDL_KEYDOWN, бре.обради)
        бре.положај = положај

