def func(pedras: str, joia: str) -> int:
    """ Função que retorna quantas strings pedras contém na joia pedra. """
    quantidade = sum([joia.count(pedra) for pedra in pedras])
    return quantidade


if __name__ == '__main__':
    print(func(pedras='aA', joia='aAAbbbb'))
    print(func(pedras='z', joia='ZZ'))
