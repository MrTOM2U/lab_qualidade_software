
LIMITE_DESCONTO = 100
PERCENTUAL_DESCONTO = 0.9


def calcular_preco_final(valor: float) -> float:
    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")
    
    if valor > 100:
        return valor * 0.90  # Aplica 10% de desconto
    
    return valor