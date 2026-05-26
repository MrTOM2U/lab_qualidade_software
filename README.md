# Laboratório de QA - Testes de Pontuação

Este projeto implementa um sistema de cálculo de pontuação com bônus, desenvolvido sob a metodologia TDD (Test-Driven Development) utilizando o framework Pytest.

## Estrutura de Diretórios
- `src/`: Lógica de negócio (`pontuacao.py`).
- `tests/`: Scripts de automação de testes (`test_pontuacao.py`).

## Cobertura e Casos de Teste (STLC)
- **Partição de Equivalência**: Validação de pontuações normais e pontuações que ativam o bônus de 10%.
- **Análise de Valor Limite**: Teste no ponto exato de inflexão da regra (100 pontos).
- **Robustez (Tratamento de Exceções)**: Bloqueio de entradas inválidas, como pontuações negativas.
- **Elemento Neutro**: Comportamento do sistema ao receber a pontuação 0.

## Execução
1. Crie o ambiente virtual: `python3 -m venv venv`
2. Ative-o: `source venv/bin/activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute os testes: `pytest -v`