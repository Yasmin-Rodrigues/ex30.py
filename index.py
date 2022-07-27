#O valor da prestação mensal não pode exceder 30% do salário 
valor =float(input('Qual o valor da casa que você pretende comprar? R$'))
salario =float(input('Qual o seu salário? R$'))
parcela =float(input('Em quantos anos você irá pagar a casa?'))
ano = parcela * 12
prestaçao = valor / ano
print('A prestação da casa será de: R${:.2f}'.format(prestaçao))
sal = salario * 0.30
print('30% do seu salário equivale a: R${:.2f}'.format(sal))
if prestaçao < sal:
    print('Empréstimo \033[32mAPROVADO!')
else:
    print('Empréstimo \033[31mNEGADO!')
    