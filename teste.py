'''c = 's'
while c == "s":
    c = str(input("qual o seu sexo? F/M ")).upper()
    s = 'F' or 'M'
    if c == s:
        print("sexo anotado")
    else:
        print("digite novamente um sexo válido")'''

'''s= 0 
n=1
while n!=999:
    n = int(input("Digite um valor:"))
    s += n
    if n == 999:
        print(f'o valor somado é: {s}') 
print("FIM")'''
        

    
'''def lin(mensagem):
    print('-' * 30)
    print(mensagem)
    print('-' * 30)


for c in range (1, 50):
    lin('    Lana esta te dando oi ')'''



'''texto = "Olá, mundo!"
tamanho_do_texto = len(texto)
print("O tamanho do texto é:", tamanho_do_texto)'''


'''def lin(msg):
    print(msg)
    print('-' *30 )

lin('Cadratamento de pessoas')

tot18 = toth = totm20 = 0
while True:
    i = int(input('Digite sua idade:'))
    s = ' '
    while s not in 'FM':
        s = str(input('Digite seu sexo: (F/M)')).upper()
    if i >= 18:
        tot18 += 1
    if s == 'M':
        toth += 1
    if s == 'F' and i <20:
        totm20 += 1
    q  = ' '
    while q not in 'SN':
        q = str(input('Quer continuar? (S/N)')).upper()
    if q == 'N':
        break
lin(f'O total de pessoas com mais de 18 anos é: {tot18}')
lin(f'O total de homens cadrastados é: {toth}')
lin(f'O total de mulheres com menos de 20 anos é: {totm20}')
lin("Volte sempre!")'''

'''def lin(msg):
    print(msg)
    print('-' *30 )

criança = homem = mulher = 0

lin('CADASTRAMENTO')

while True:
    i = int(input('Digite sua idade:')) 
    s = ' '
    while s not in 'FM':
        s = str(input("Digite seu sexo: (F/M)")).upper()
    if i <= 17:
        criança += 1
    if s == 'F' and i >18:
        mulher += 1
    if s == 'M' and i >18:
        homem += 1
    q = ' ' 
    while q not in 'SN':
        q = str(input('Quer continuar? (S/N)')).upper()
    if q == 'N':
        break
lin(f"O cadrastro deu ao total {criança} crianças.")
lin(f"O cadrastro deu ao total {mulher} mulheres.")
lin(f"O cadrastro deu ao total {homem} homens.")'''

'''notas = list()
alunos = dict()
for c in range(0,1):
    alunos ['nome'] = str(input('Nome do aluno:'))
    alunos ['média'] = int(input(f'Média de {alunos["nome"]}:'))
    notas.append(alunos.copy())
print(f'A média de {notas[0]["nome"]} é {notas[0]["média"]}')
if alunos['média'] > 7:
    print(f'O aluno(a) {notas[0]["nome"]} está aprovado.')
elif 5 <= alunos['média']  < 6:
        print(f'O aluno(a) {notas[0]["nome"]} está de recuperação.')
elif alunos['média'] <= 4:
     print(f'O aluno(a) {notas[0]["nome"]} está reprovado')'''

'''aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input(f'Média de {aluno["nome"]}:'))
if aluno['média'] >=7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] <7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Recuperação'
print('-='*30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
print(aluno)'''

'''def procura(lista, elemento):
    tamanho = len(lista)
    for i in range(tamanho):
        if elemento == lista[i]:
            return True
        else: 
            return False
        
lista = ['acotar', 'ouabh', 'tbnf', 'a hipotese do amor', 'therabithia']
elemento = 'acotar'
print(procura(lista, elemento))
if elemento in lista: 
    print('O elemento está na lista')
else: 
    print('O elementao não está na lista')'''

'''def binario(lista, elemento):
    minimo = 0 
    maximo = len(lista)-1
    encontrado = False
    while minimo <= maximo and not encontrado:
        meio = (minimo+maximo)//2
        if lista[meio] == elemento:
            encontrado =  True
        else:
            if elemento < lista[meio]:
                maximo = meio-1 
            else:
                minimo = meio+1
    return encontrado 

lista = [1, 2, 3, 5, 7, 10, 20, 32, 37, 50]
elemento = 45
print(binario(lista, elemento))
if elemento in lista:
    print(f'{elemento} está presente')
else:
    print(f'{elemento} não está presente')'''


	















