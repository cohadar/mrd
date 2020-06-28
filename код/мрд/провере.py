import sdl2


def увек(резултат, функција, аргументи):
    raise Exception(резултат, аргументи)


def ок_0(резултат, функција, аргументи):
    if резултат != 0:
        raise Exception(резултат, аргументи)
    return резултат


def нок_м1(резултат, функција, аргументи):
    if резултат == -1:
        raise Exception(резултат, аргументи)
    return резултат


def нул(резултат, функција, аргументи):
    if резултат is None:
        raise Exception(резултат, аргументи)
    return резултат


def региструј():
    sdl2.SDL_Init.errcheck = ок_0
    # sdl2.SDL_GameControllerAddMappingsFromFile је пајтон ламбда
    sdl2.SDL_GameControllerAddMappingsFromRW.errcheck = нок_м1
    sdl2.SDL_CreateWindow.errcheck = нул
    sdl2.SDL_CreateRenderer.errcheck = нул
    sdl2.SDL_GetRendererInfo.errcheck = ок_0
    sdl2.SDL_GetCurrentDisplayMode.errcheck = ок_0
    sdl2.SDL_CreateTexture.errcheck = нул
    sdl2.SDL_CreateRGBSurfaceWithFormat.errcheck = нул
    sdl2.SDL_SetSurfaceBlendMode.errcheck = ок_0
    sdl2.SDL_FillRect.errcheck = ок_0
    sdl2.SDL_BlitSurface.errcheck = ок_0
    sdl2.SDL_BlitScaled.errcheck = ок_0
    sdl2.SDL_UpdateTexture.errcheck = ок_0
    sdl2.SDL_RenderClear.errcheck = ок_0
    sdl2.SDL_RenderCopy.errcheck = ок_0
    #sdl2.SDL_RenderPresent.errcheck  # void function
    sdl2.SDL_GameControllerOpen.errcheck = нул
    sdl2.SDL_GameControllerMapping.errcheck = нул
    sdl2.SDL_GameControllerName.errcheck = нул
    sdl2.SDL_JoystickOpen.errcheck = нул
    sdl2.SDL_JoystickName.errcheck = нул

