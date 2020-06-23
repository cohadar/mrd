from догађај.штампа import региструј
from догађај import Обрада
from дуњалук import Почетак, Крај, Молер, Прозор, ГлавнаШара, Воденица, ГлавнаПоврш, Пиксели
from шкработине import Шкработине, ЦрвенаКоцка, ПлаваКоцка, ШаренаПозадина, Лупа
import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Контејнер(containers.DynamicContainer):
    def __init__(к):
        super().__init__()
        к.ширина = providers.Object(16 * 15)
        к.висина = providers.Object(9 * 15)
        к.почетак = providers.Singleton(Почетак)
        к.прозор = providers.Singleton(Прозор, почетак=к.почетак, наслов="Мрд", ширина=к.ширина, висина=к.висина)
        к.молер = providers.Singleton(Молер, прозор=к.прозор)
        к.крај = providers.Singleton(Крај, прозор=к.прозор, молер=к.молер)
        к.обрада_догађаја = providers.Singleton(Обрада)
        к.главна_шара = providers.Singleton(ГлавнаШара, молер=к.молер, ширина=к.ширина, висина=к.висина)
        к.пиксели = providers.Singleton(Пиксели, ширина=к.ширина, висина=к.висина)
        к.главна_површ = providers.Singleton(ГлавнаПоврш, пиксели=к.пиксели, ширина=к.ширина, висина=к.висина)
        к.црвена_коцка = providers.Singleton(
            ЦрвенаКоцка, пиксели=к.пиксели, ширина=к.ширина, обрада_догађаја=к.обрада_догађаја)
        к.плава_коцка = providers.Singleton(
            ПлаваКоцка, главна_површ=к.главна_површ, обрада_догађаја=к.обрада_догађаја)
        к.шарена_позадина = providers.Singleton(ШаренаПозадина, пиксели=к.пиксели, ширина=к.ширина, висина=к.висина)
        к.лупа = providers.Singleton(Лупа, главна_површ=к.главна_површ, обрада_догађаја=к.обрада_догађаја)
        к.шкработине = providers.Singleton(Шкработине, к.шарена_позадина, к.црвена_коцка, к.плава_коцка, к.лупа)
        к.воденица = providers.Singleton(
            Воденица,
            обрада_догађаја=к.обрада_догађаја,
            шкработине=к.шкработине,
            молер=к.молер,
            главна_шара=к.главна_шара,
            главна_површ=к.главна_површ)


def главна():
    к = Контејнер()
    _, _ = к.почетак(), к.крај()
    обрада_догађаја = к.обрада_догађаја()  # дебуг штампа
    региструј(обрада_догађаја)  # дебуг штампа
    воденица = к.воденица()
    воденица()


if __name__ == '__main__':
    главна()

