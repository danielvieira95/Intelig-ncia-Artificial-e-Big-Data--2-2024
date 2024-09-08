def custo(altura, largura, comprimento, preco_litro):
    resultado_em_m3 = altura * largura * comprimento
    resultado_em_litros = resultado_em_m3 * 1000
    valor = resultado_em_litros * preco_litro
    return valor
