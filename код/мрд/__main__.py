import sdl2
from догађај.штампа import направи as направи_штампу
from догађај.обрада import направи as направи_обраду
from дуњалук import Почетак, Крај, Молер, Прозор, ГлавнаШара, Воденица
import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Контејнер(containers.DynamicContainer):

    def __init__(к):
        super().__init__()
        к.ширина = providers.Object(16 * 15)
        к.висина = providers.Object(9 * 15)
        к.почетак = providers.Singleton(Почетак)
        к.прозор = providers.Factory(Прозор, почетак=к.почетак, наслов="Мрд", ширина=к.ширина, висина=к.висина)
        к.молер = providers.Factory(Молер, прозор=к.прозор)
        к.крај = providers.Singleton(Крај, прозор=к.прозор, молер=к.молер)
        к.штампа_догађаја = providers.Callable(направи_штампу)
        к.обрада_догађаја = providers.Callable(направи_обраду)
        к.главна_шара = providers.Callable(ГлавнаШара, молер=к.молер, ширина=к.ширина, висина=к.висина)
        к.воденица = providers.Singleton(
            Воденица,
            штампа_догађаја=к.штампа_догађаја(),
            обрада_догађаја=к.обрада_догађаја,
            молер=к.молер,
            главна_шара=к.главна_шара,
            ширина=к.ширина,
            висина=к.висина)


RED = sdl2.SDL_Color(0xe5, 0x00, 0x00, 0xff)
GOLD = sdl2.SDL_Color(0xff, 0xcc, 0x00, 0xff)


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


def главна():
    к = Контејнер()
    _, _ = к.почетак(), к.крај()
    воденица = к.воденица()
    воденица()


if __name__ == '__main__':
    главна()

