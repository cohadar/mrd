from collections import defaultdict


def pprint(etype, pairs):
    print(f"{etype} ", end="")
    print(", ".join((f"{key}={value}" for key, value in pairs)))


class Обрада():
    def __init__(бре):
        бре.регистар = defaultdict(list)

    def региструј(бре, тип_догађаја, функција):
        бре.регистар[тип_догађаја].append(функција)

    def обради(бре, догађај):
        листа = бре.регистар[догађај.type]
        if not листа:
            raise Exception('Непознат догађај:', hex(догађај.type))
        for функција in листа:
            функција(догађај)


__all__ = ["pprint", "Obrada"]

