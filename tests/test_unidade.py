import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    # 3.1 Testes de Entrada e Saída
    def test_entrada_saida_soma(self):
        calc = Calculadora()
        resultado = calc.somar(5, 3)
        self.assertEqual(resultado, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)

    def test_entrada_saida_subtracao(self):
        calc = Calculadora()
        resultado = calc.subtrair(10, 4)
        self.assertEqual(resultado, 6)
        self.assertEqual(calc.obter_ultimo_resultado(), 6)

    def test_entrada_saida_multiplicacao(self):
        calc = Calculadora()
        resultado = calc.multiplicar(3, 7)
        self.assertEqual(resultado, 21)
        self.assertEqual(calc.obter_ultimo_resultado(), 21)

    def test_entrada_saida_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(20, 5)
        self.assertEqual(resultado, 4)
        self.assertEqual(calc.obter_ultimo_resultado(), 4)

    # EXTRA: teste de potencia
    def test_entrada_saida_potencia(self):
        calc = Calculadora()
        resultado = calc.potencia(2, 4)
        self.assertEqual(resultado, 16)
        self.assertEqual(calc.obter_ultimo_resultado(), 16)

    # 3.2 Testes de Tipagem
    def test_tipagem_invalida(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3)
        with self.assertRaises(TypeError):
            calc.dividir(10, None)

    def test_tipagem_todas_operacoes(self):
        calc = Calculadora()
        for metodo in [calc.somar, calc.subtrair, calc.multiplicar, calc.dividir, calc.potencia]:
            with self.assertRaises(TypeError):
                metodo("a", "b")

    # EXTRA: mistura de int e string
    def test_tipagem_misturada(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.multiplicar(5, "dez")

    # 3.3 Testes de Consistência
    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)

    # EXTRA: histórico mantém ordem
    def test_consistencia_ordem(self):
        calc = Calculadora()
        calc.somar(1, 1)
        calc.subtrair(5, 3)
        self.assertEqual(calc.historico[0], "1 + 1 = 2")
        self.assertEqual(calc.historico[1], "5 - 3 = 2")

    # 3.4 Testes de Inicialização
    def test_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)

    # EXTRA: inicialização após limpar histórico
    def test_inicializacao_apos_limpar(self):
        calc = Calculadora()
        calc.somar(2, 2)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    # 3.5 Testes de Modificação de Dados
    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    # EXTRA: limpar histórico não altera resultado
    def test_modificacao_nao_reseta_resultado(self):
        calc = Calculadora()
        calc.somar(5, 5)
        calc.limpar_historico()
        self.assertEqual(calc.obter_ultimo_resultado(), 10)

    # 3.6 Testes de Limite Inferior
    def test_limite_inferior(self):
        calc = Calculadora()
        resultado = calc.somar(0, 5)
        self.assertEqual(resultado, 5)
        resultado = calc.multiplicar(-1e-10, 2)
        self.assertEqual(resultado, -2e-10)

    # EXTRA: limite negativo grande
    def test_limite_inferior_negativo_grande(self):
        calc = Calculadora()
        resultado = calc.subtrair(-1e12, -1e12)
        self.assertEqual(resultado, 0)

    # 3.7 Testes de Limite Superior
    def test_limite_superior(self):
        calc = Calculadora()
        resultado = calc.somar(1e10, 1e10)
        self.assertEqual(resultado, 2e10)

    def test_limite_superior_float_max(self):
        calc = Calculadora()
        import sys
        resultado = calc.somar(sys.float_info.max, 0)
        self.assertEqual(resultado, sys.float_info.max)

    # EXTRA: overflow com float
    def test_limite_superior_overflow(self):
        calc = Calculadora()
        import sys
        with self.assertRaises(OverflowError):
            _ = calc.potencia(sys.float_info.max, 2)

    # 3.8 Testes de Valores Fora do Intervalo
    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    # EXTRA: valor inválido em potencia
    def test_potencia_expoente_invalido(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.potencia(2, "dois")

    # 3.9 Testes de Fluxos de Controle
    def test_fluxos_divisao(self):
        calc = Calculadora()
        resultado = calc.dividir(10, 2)
        self.assertEqual(resultado, 5)
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    # EXTRA: fluxo com sequencia válida
    def test_fluxo_soma_divisao(self):
        calc = Calculadora()
        r1 = calc.somar(10, 20)
        r2 = calc.dividir(r1, 10)
        self.assertEqual(r2, 3)

    # 3.10 Testes de Mensagens de Erro
    def test_mensagens_erro(self):
        calc = Calculadora()
        try:
            calc.dividir(5, 0)
        except ValueError as e:
            self.assertEqual(str(e), "Divisao por zero nao permitida")

    # EXTRA: mensagem de tipo inválido
    def test_mensagem_erro_tipagem(self):
        calc = Calculadora()
        try:
            calc.somar("a", 1)
        except TypeError as e:
            self.assertEqual(str(e), "Argumentos devem ser numeros")


if __name__ == "__main__":
    unittest.main()
