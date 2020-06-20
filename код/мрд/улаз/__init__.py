def pprint(etype, pairs):
    print(f"{etype} ", end="")
    print(", ".join((f"{key}={value}" for key, value in pairs)))
