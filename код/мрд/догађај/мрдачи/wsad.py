import sdl2


class Wsad():
    def обради(бре, догађај):
        код = догађај.key.keysym.scancode
        if код == sdl2.SDL_SCANCODE_W:
            бре.положај.y -= 1
        elif код == sdl2.SDL_SCANCODE_S:
            бре.положај.y += 1
        elif код == sdl2.SDL_SCANCODE_A:
            бре.положај.x -= 1
        elif код == sdl2.SDL_SCANCODE_D:
            бре.положај.x += 1

    def __init__(бре, обрада_догађаја, положај):
        обрада_догађаја.региструј(sdl2.SDL_KEYDOWN, бре.обради)
        бре.положај = положај

