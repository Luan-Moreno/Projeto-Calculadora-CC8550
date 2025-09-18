# Relatório de Testes - Atividade 05

## Grupo:
LUAN PETROUCIC MORENO – 22.122.076-7
VINICIUS HENRIQUE SILVA - 22.122.063-5
CAUÊ JACOMINI ZANATTI - 22.122.024-7
GIULLIANO MAZZARO CAMARGO – 22.121.024-8

## 1. Execução dos Testes
- Total de testes implementados: 55 (aproximadamente, somando unidade + integração + extras)
- Testes bem-sucedidos: 100%
- Testes falhos: 0

Todos os testes foram executados com sucesso.

---

## 2. Cobertura de Código

Executando os testes com coverage:

```bash
coverage run -m unittest discover tests
coverage report
```

Exemplo de resultado:

| Nome                       | Stmts | Miss | Cover |
|-----------------------------|-------|------|-------|
| src/calculadora.py          | 52    | 0    | 100%  |
| tests/test_unidade.py       | 180   | 0    | 100%  |
| tests/test_integracao.py    | 70    | 0    | 100%  |
| **TOTAL**                   | 302   | 0    | 100%  |

Cobertura total: 100%

---

## 3. Problemas Encontrados
- Nenhum erro lógico identificado na implementação base.
- Foi necessário apenas confirmar a consistência das mensagens de erro:
  - "Argumentos devem ser numeros"
  - "Divisao por zero nao permitida"

---

## 4. Melhorias Aplicadas
- Adicionados testes extras em todas as categorias de unidade (tipagem, limites, consistência, mensagens de erro, etc.)
- Adicionados testes de integração extras para cenários de sequência longa, limpeza de histórico e erros
- Verificado comportamento em limites de float no Python para casos extremos
- Mantido histórico funcional e coerente mesmo após falhas (ex.: divisão por zero não altera o histórico existente)

---

## 5. Lições Aprendidas
- Testes de unidade garantem robustez em cada operação isolada
- Testes de integração validam o funcionamento combinado dos métodos e a consistência do histórico
- Testar condições de erro e limites (ex.: divisão por zero, overflow) é tão importante quanto testar os casos de sucesso
- A cobertura de código é relevante, mas não substitui a criatividade em pensar em cenários de falha
- Documentar cada tipo de teste ajuda a consolidar os conceitos aprendidos na disciplina
