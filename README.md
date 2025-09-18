# Projeto Calculadora - Atividade 05 (Simulação e Teste de Software)

Este projeto implementa uma calculadora simples em Python e uma suíte completa de testes de unidade e integração, conforme solicitado na disciplina Simulação e Teste de Software (CC8550).

---

## Estrutura do Projeto

```text
projeto_calculadora/
│-- src/
│   └── calculadora.py            # Código da calculadora
│
│-- tests/
│   ├── __init__.py               # Arquivo vazio (necessário para pacote de testes)
│   ├── test_unidade.py           # Testes de unidade
│   └── test_integracao.py        # Testes de integração
│
│-- requirements.txt               # Dependências (coverage)
│-- README.md                      # Documentação do projeto
│-- relatorio.md                   # Relatório dos testes
```

---

## Como Executar os Testes

1. Instalar dependências:
```bash
pip install -r requirements.txt
```

2. Executar todos os testes:
```bash
python -m unittest discover tests -v
```

3. Executar com cobertura:
```bash
coverage run -m unittest discover tests
coverage report
coverage html   # gera relatório em HTML (abrir no navegador)
```

4. Executar teste específico (exemplo: teste de soma):
```bash
python -m unittest tests.test_unidade.TestCalculadora.test_entrada_saida_soma -v
```

---

## Objetivo

O objetivo desta atividade é aplicar os conceitos de testes de unidade e testes de integração, garantindo que:

- Todos os métodos da calculadora funcionem corretamente.
- Casos de sucesso e falha sejam tratados.
- Limites e erros sejam validados.
- A comunicação entre métodos seja testada.

---

## Autoria

Atividade desenvolvida por alunos do último semestre de Ciência da Computação, como parte da disciplina Simulação e Teste de Software.

---

## Dependências

Arquivo `requirements.txt`:
```txt
coverage>=7.0.0
```

---

## Pacote de Testes

Arquivo `tests/__init__.py`:
```python
# Arquivo vazio necessário para pacote de testes
```
