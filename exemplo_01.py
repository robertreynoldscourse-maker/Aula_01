print('Hi dear world!')
print("Robert Rodriguez.")
'''
Python é uma linguagem de programação de amplo uso como ser, jogos, analise de dados (Banco de dados), desenvolvimento de programas, etc, em
resumo é de propósito geral.
O VSCode é uma interface de desenvolvimento é dizer para escrever códigos.
Variáveis, são locais, é dizer, estão dentro do programa. Na notação tem diferença entre minúscula e maiúsculo. 
Repare que uma variável sempre começa com letra. 
Lembre-se que variável é uma espaço na memória e que tem associado um nome. Nome composto não pode ter espaço, sem acentos, nunca começa com 
símbolos, numeros ou espaço.
'''
nome = 'Robert'
idade = 5
altura = 1.3
print(nome)
print(idade)
# Para comentar combinar ctrl+pontoevirgula
#print(altura)
#print(type(nome), type(idade), type(altura))

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Nome: {nome} - Idade: {idade}')

# Operadores: 
# soma +
# subtração -
# multiplicação *
# divisão /
# modulo % (resto duma divisão)
# divisão inteira //


nome = 'Pedro'

n1 = 10
n2 = 3

# Atribuição, é quando é usado o símbolo =
print('############################')
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
modulo = n1 % n2
divisao_inteira = n1 // n2
print(f'Soma: {soma}')
print(f'Subração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')
print(f'Módulo: {modulo}')
print(f'Divisão Inteira: {divisao_inteira}')
print(nome)
#ctrl + shit + setaacima ou setaabaixo
total = n1 + n2
total = total + 5
print(total)
name = input('Qual é seu nome? ')
sobrenome = input("Digite seu sobrenome: ")
print(f'My name is:{name} {sobrenome}')