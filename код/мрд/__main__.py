import sdl2
from мрд.догађај.штампа import региструј, Обрада
from мрд.догађај.мрдачи import Стрелице, Wsad
from мрд.дуњалук import Почетак, Крај, Молер, Прозор, Шара, Површ, Воденица, Шкработине
from мрд.шкраб import ЛеденаКоцка, РамОдСлике, ШаренаПозадина, Лупа
import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Контејнер(containers.DynamicContainer):
    def __init__(к):
        super().__init__()
        к._листови = []
        к.ширина = providers.Object(16 * 15)
        к.висина = providers.Object(9 * 15)
        к.почетак = providers.Singleton(Почетак)
        к.прозор = providers.Singleton(Прозор, почетак=к.почетак, наслов="Мрд", ширина=к.ширина, висина=к.висина)
        к.молер = providers.Singleton(Молер, прозор=к.прозор)
        к.главна_шара = providers.Singleton(Шара, молер=к.молер, ширина=к.ширина, висина=к.висина)
        к.главна_површ = providers.Singleton(Површ, ширина=к.ширина, висина=к.висина)

        к.обрада_догађаја = providers.Singleton(Обрада)
        к.шкработине = providers.Singleton(Шкработине)

        к.шарена_позадина = providers.Singleton(ШаренаПозадина, шкработине=к.шкработине, површ=к.главна_површ)
        к._листови.append(к.шарена_позадина)

        к._ледена_коцка()
        к._рам('red')
        к.лупа = providers.Singleton(
            Лупа,
            шкработине=к.шкработине,
            главна_површ=к.главна_површ,
            обрада_догађаја=к.обрада_догађаја)
        к._листови.append(к.лупа)

        к.воденица = providers.Singleton(
            Воденица,
            обрада_догађаја=к.обрада_догађаја,
            шкработине=к.шкработине,
            молер=к.молер,
            главна_шара=к.главна_шара,
            главна_површ=к.главна_површ)

        к._крај()

    def _крај(к):
        крај = providers.Singleton(Крај, прозор=к.прозор, молер=к.молер)
        к._листови.append(крај)

    def _ледена_коцка(к):
        положај = providers.Singleton(sdl2.SDL_Point)
        ледена_коцка = providers.Singleton(ЛеденаКоцка, шкработине=к.шкработине, површ=к.главна_површ, положај=положај)
        wsad = providers.Singleton(Wsad, положај=положај, обрада_догађаја=к.обрада_догађаја)
        к._листови.append(ледена_коцка)
        к._листови.append(wsad)

    def _рам(к, име_боје):
        п = sdl2.SDL_Point(к.ширина() // 2, к.висина() // 2)
        положај = providers.Object(п)
        рам = providers.Singleton(
            РамОдСлике,
            шкработине=к.шкработине,
            површ=к.главна_површ,
            положај=положај,
            име_боје=име_боје)
        стрелице = providers.Singleton(Стрелице, положај=положај, обрада_догађаја=к.обрада_догађаја)
        к._листови.append(рам)
        к._листови.append(стрелице)

    def направи_лишђе(к):
        for лист in к._листови:
            try:
                лист()
            except Exception as е:
                raise Exception(лист) from е


def главна():
    к = Контејнер()
    обрада_догађаја = к.обрада_догађаја()  # дебуг штампа
    региструј(обрада_догађаја)  # дебуг штампа
    воденица = к.воденица()
    к.направи_лишђе()
    воденица()


if __name__ == '__main__':
    главна()

