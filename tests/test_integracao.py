import unittest
from src.calculadora import Calculadora

class TestIntegracaoCalculadora(unittest.TestCase):

    # 4.1 Teste de Operações Sequenciais
    def test_operacoes_sequenciais(self):
        calc = Calculadora()
        # Sequência: 2 + 3 = 5 → 5 * 4 = 20 → 20 / 2 = 10
        calc.somar(2, 3)
        resultado1 = calc.obter_ultimo_resultado()

        calc.multiplicar(resultado1, 4)
        resultado2 = calc.obter_ultimo_resultado()

        calc.dividir(resultado2, 2)
        resultado_final = calc.obter_ultimo_resultado()

        self.assertEqual(resultado_final, 10)
        self.assertEqual(len(calc.historico), 3)

    # EXTRA: sequência mais longa
    def test_operacoes_sequenciais_longas(self):
        calc = Calculadora()
        calc.somar(10, 5)         # 15
        calc.subtrair(15, 3)      # 12
        calc.multiplicar(12, 2)   # 24
        calc.dividir(24, 4)       # 6
        calc.potencia(6, 2)       # 36
        self.assertEqual(calc.obter_ultimo_resultado(), 36)
        self.assertEqual(len(calc.historico), 5)

    # 4.2 Teste de Interface entre Métodos
    def test_integracao_historico_resultado(self):
        calc = Calculadora()
        calc.potencia(2, 3)  # 2^3 = 8
        calc.somar(calc.obter_ultimo_resultado(), 2)  # 8 + 2 = 10

        self.assertEqual(calc.obter_ultimo_resultado(), 10)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 ^ 3 = 8", calc.historico)
        self.assertIn("8 + 2 = 10", calc.historico)

    # EXTRA: integração entre limpar histórico e resultado
    def test_integracao_limpar_historico(self):
        calc = Calculadora()
        calc.somar(3, 3)  # 6
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)
        # Último resultado deve ser preservado
        self.assertEqual(calc.obter_ultimo_resultado(), 6)

    # EXTRA: integração de erros
    def test_integracao_com_erros(self):
        calc = Calculadora()
        calc.somar(5, 5)  # 10
        with self.assertRaises(ValueError):
            calc.dividir(calc.obter_ultimo_resultado(), 0)
        # Histórico deve registrar apenas a operação válida
        self.assertEqual(len(calc.historico), 1)
        self.assertIn("5 + 5 = 10", calc.historico)


if __name__ == "__main__":
    unittest.main()
