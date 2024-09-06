def volume_em_litros(altura, largura, comprimento):
    resultado_em_m3 = altura * largura * comprimento
    resultado_em_litros = resultado_em_m3 * 1000
    return resultado_em_litros
