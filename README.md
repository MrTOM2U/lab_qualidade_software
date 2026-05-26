# Laboratório de Qualidade e Teste de Software

Este projeto implementa uma calculadora com foco na aplicação de testes automatizados e práticas de TDD (Test-Driven Development), utilizando a biblioteca Pytest. 

## Estrutura do Projeto

A separação de pastas segue o padrão de mercado para facilitar a manutenção e automação:
* `src/`: Contém o código-fonte e a lógica de negócio da aplicação (`calculadora.py`).
* `tests/`: Diretório exclusivo para os scripts de Quality Assurance (QA) (`test_calculadora.py`).

## Cobertura de Testes

Foram aplicados os seguintes conceitos de QA:
* **Partição de Equivalência**: Testes com valores dentro e acima do limite de desconto.
* **Análise de Valor Limite (Boundary Value)**: Teste focado no extremo da regra (exatamente 100).
* **Teste de Robustez**: Tratamento de exceções para valores inválidos (negativos).
* **Elemento Neutro**: Verificação do processamento do valor zero.

## Como Instalar e Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/MrTOM2U/lab_qualidade_software.git](https://github.com/MrTOM2U/lab_qualidade_software.git)
    cd lab_qualidade_software
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute os testes:**
    Para rodar todos os testes e verificar as asserções:
    ```bash
    pytest
    ```
    Para uma visualização mais detalhada:
    ```bash
    pytest -v
    ```