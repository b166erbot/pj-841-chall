def func(pedras: str = "", joia: str = "") -> int:
    """ Função que retorna quantas strings pedras contém na joia pedra. """
    quantidade = sum([joia.count(pedra) for pedra in pedras])
    return quantidade
