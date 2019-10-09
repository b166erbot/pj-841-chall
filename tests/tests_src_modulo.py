from unittest import TestCase
from src.modulo import func


class Tests(TestCase):
    def test_somente_uma_pedra_retornando_quantidade_3(self):
        resultado = func(pedras="Se", joia="Selenium")
        self.assertEqual(resultado, 3)

    def test_2_pedras_retornando_quantidade_5(self):
        resultado = func(pedras="aA", joia="AaAaA")
        self.assertEqual(resultado, 5)

    def test_pulando_pedras_desconhecidas_na_joia_e_retornando_2(self):
        resultado = func(pedras="aA", joia="aAbC")
        self.assertEqual(resultado, 2)

    def test_pedras_em_excesso_e_retornando_3(self):
        resultado = func(pedras="afOIp", joia="pIO")
        self.assertEqual(resultado, 3)

    def test_pedras_e_joia_desproporcionais_retornando_1(self):
        resultado = func(pedras="Unittest", joia="RaDon")
        self.assertEqual(resultado, 1)

    def test_pedras_e_joia_desproporcionais_retornando_0(self):
        resultado = func(pedras="CovErAge", joia="pDb")
        self.assertEqual(resultado, 0)

    def test_nao_passando_nenhuma_pedra_com_retorno_de_0(self):
        resultado = func(joia="Click")
        self.assertEqual(resultado, 0)

    def test_nao_passando_nenhuma_joia_com_retorno_0(self):
        resultado = func(pedras="Regex")
        self.assertEqual(resultado, 0)

    def test_nao_passando_nem_joia_nem_pedras_com_retorno_0(self):
        resultado = func()
        self.assertEqual(resultado, 0)

    def test_resultado_precisa_ser_um_inteiro(self):
        resultado = func()
        self.assertIsInstance(resultado, int)

    def test_passando_uma_lista_contendo_strings_para_joia_e_retornando_4(self):
        resultado = func(pedras="asdf", joia=list("asdfçlkj"))
        self.assertEqual(resultado, 4)

    def test_passando_uma_lista_contendo_strings_para_pedras_e_retornando_2(self):
        resultado = func(pedras=list("abCd"), joia="aCef")
        self.assertEqual(resultado, 2)
