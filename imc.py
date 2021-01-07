def imc(peso, altura):
  altura_quadrada = numero_quadrado(altura)
  meu_imc = peso / altura_quadrada
  print(f'O meu imc {meu_imc:.2f}')
  return meu_imc
meu_imc = imc(105, 1.87)