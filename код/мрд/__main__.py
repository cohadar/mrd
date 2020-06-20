import random
import ctypes
import atexit
import sdl2
from улаз.штампа import штампа
from дуњалук import Почетак, Крај, Молер, Прозор
import dependency_injector.containers as containers
import dependency_injector.providers as providers


MAIN_WIDTH = 16 * 15
MAIN_HEIGHT = 9 * 15


class Контејнер(containers.DynamicContainer):
    def __init__(к):
        super().__init__()
        к.ширина = providers.Object(16 * 15)
        к.висина = providers.Object(9 * 15)
        к.почетак = providers.Singleton(Почетак)
        к.прозор = providers.Factory(Прозор, почетак=к.почетак, наслов="Мрд", ширина=к.ширина, висина=к.висина)
        к.молер = providers.Factory(Молер, прозор=к.прозор)
        к.крај = providers.Singleton(Крај, прозор=к.прозор, молер=к.молер)
        # к.дирови = providers.Callable(к.листа_дирова, каталог=к.каталог)
        # к.шпилови = providers.Callable(к.листа_шпилова)
        # к.терминал = providers.Singleton(Терминал)
        # к.регистар = providers.Factory(Регистар)
        # к.главна_ui = providers.Factory(ГлавнаUI, терминал=к.терминал, регистар=к.регистар)
        # к.главна = providers.Factory(Главна, ui=к.главна_ui, шпилови=к.шпилови)


event_handlers = {}


RED = sdl2.SDL_Color(0xe5, 0x00, 0x00, 0xff)
GOLD = sdl2.SDL_Color(0xff, 0xcc, 0x00, 0xff)


def доцртај(my_pixels):
    def index(y, x):
        return (y * MAIN_WIDTH + x) * 4

    for y in range(0, 16):
        for x in range(0, 16):
            my_pixels[index(y, x) + 0] = 0
            my_pixels[index(y, x) + 1] = 0
            my_pixels[index(y, x) + 2] = 255
            my_pixels[index(y, x) + 3] = 255


MY_X = 0
MY_Y = 0


def стрелице(event):
    global MY_X
    global MY_Y
    код = event.key.keysym.scancode
    if код == sdl2.SDL_SCANCODE_UP:
        MY_Y -= 1
    elif код == sdl2.SDL_SCANCODE_DOWN:
        MY_Y += 1
    elif код == sdl2.SDL_SCANCODE_LEFT:
        MY_X -= 1
    elif код == sdl2.SDL_SCANCODE_RIGHT:
        MY_X += 1


def loop(штампа_догађаја, обрада_догађаја, renderer, texture):
    quit = False
    event = sdl2.SDL_Event()
    my_pixels = ctypes.create_string_buffer(MAIN_WIDTH * MAIN_HEIGHT * 4)
    for i, _ in enumerate(my_pixels):
        my_pixels[i] = random.randint(0, 255)
    while not quit:
        штампано = False
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                quit = True
                break
            if event.type not in штампа_догађаја:
                raise Exception('Непознат догађај:', hex(event.type))
            штампа_догађаја[event.type](event)
            штампано = True
            if event.type in обрада_догађаја:
                обрада_догађаја[event.type](event)
        for _ in range(10000):
            my_pixels[random.randint(0, MAIN_WIDTH * MAIN_HEIGHT * 4 - 1)] = random.randint(0, 255)
        доцртај(my_pixels)
        sdl2.SDL_UpdateTexture(texture, None, my_pixels, MAIN_WIDTH * 4)
        sdl2.SDL_RenderClear(renderer)
        sdl2.SDL_RenderCopy(renderer, texture, None, None)
        sdl2.SDL_RenderPresent(renderer)
        if штампано:
            print()


def open_controller(event):
    """ https://wiki.libsdl.org/SDL_ControllerDeviceEvent """
    controller = sdl2.SDL_GameControllerOpen(event.cdevice.which)
    if not controller:
        raise Exception('SDL_GameControllerOpen', sdl2.SDL_GetError())
    print('otvoren gamepad', controller)
    mapping = sdl2.SDL_GameControllerMapping(controller)
    name = sdl2.SDL_GameControllerName(controller)
    print('mapping:', mapping)
    print('name:', name)


def open_joystick(event):
    """ https://wiki.libsdl.org/SDL_JoyDeviceEvent """
    joystick = sdl2.SDL_JoystickOpen(event.jdevice.which)
    if not joystick:
        raise Exception('SDL_JoystickOpen', sdl2.SDL_GetError())
    name = sdl2.SDL_JoystickName(joystick)
    print('joystick added:', name)


def close_controller(event):
    """ https://wiki.libsdl.org/SDL_ControllerDeviceEvent """
    pass


def главна():
    к = Контејнер()
    почетак, крај = к.почетак(), к.крај()

    res = sdl2.SDL_GameControllerAddMappingsFromFile(b"mygamecontrollerdb.txt")
    if res == -1:
        raise Exception('SDL_GameControllerAddMappingsFromFile', sdl2.SDL_GetError())
    штампа_догађаја = штампа()
    обрада_догађаја = {}
    обрада_догађаја[sdl2.SDL_CONTROLLERDEVICEADDED] = open_controller
    обрада_догађаја[sdl2.SDL_CONTROLLERDEVICEREMOVED] = close_controller
    # обрада_догађаја[sdl2.SDL_JOYDEVICEADDED] = open_joystick
    шара = sdl2.SDL_CreateTexture(
            крај.молер.сиров,
            sdl2.SDL_PIXELFORMAT_ARGB8888,
            sdl2.SDL_TEXTUREACCESS_STREAMING,
            MAIN_WIDTH, MAIN_HEIGHT)
    loop(штампа_догађаја, обрада_догађаја, крај.молер.сиров, шара)  # <---<<


if __name__ == '__main__':
    главна()

