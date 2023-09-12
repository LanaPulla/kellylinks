'''import locale

def calcular_imc(peso, altura):
    return peso / (altura ** 2) 

def main():
    # Configurrar a localização para usar vírgulas como separardor decimal
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    
nome = input('digite um nome: ')
print("ola %s , vamos calcular o seu IMC" % (nome))
a = input('digite um número para sua altura: ')
a = int(a)
p  = input('digite um número para o seu peso: ')
p = int(p)
IMC = p/(a*a)
print(f"o resultado do seu IMC = {IMC}. ")'''


me = mm = ml = s = sb = o1 = o2 = o3 = 0

while True:
    nome = input('digite um nome: ')
    print(f"ola {nome}, vamos calcular o seu IMC")
    a = float(input('digite um número para sua altura (com ponto no local da vírgula): '))
    p  = float(input('digite um número para o seu peso: '))
    IMC= p/(a*a)  
    print(f"o resultado do seu IMC: {IMC}. ")
    if IMC < 16:
        print('Magreza extrema')
        me += 1
    elif IMC < 17:
        print('Magreza moderada')
        mm += 1
    elif IMC < 18.5:
        print('Magreza leve')
        ml += 1
    elif IMC < 25:
        print('Saúdavel')
        s += 1
    elif IMC < 30:
        print('Sobrepeso')
        sb += 1
    elif IMC <35:
        print('Obesidade grau I')
        o1 += 1
    elif IMC < 40:
        print('Obesdade Grau II(severa)')
        o2 += 1
    else:
        print('Obesidade Grau III(mórbida)')
        o3 += 1
    q = str(input('Quer calcular outro IMC? S/N')).upper().strip()
    if q == 'N':
        break


print(f'O total de pessoa(s) com magreza extrema é {me}')
print(f'O total de pessoa(s) com magreza moderada é {mm}')  
print(f'O total de pessoa(s) com magreza leve é {ml}')
print(f'O total de pessoa(s) saudáveis é {s}')
print(f'O total de pessoa(s) em sobrepeso é {sb}') 
print(f'O total de pessoa(s) em obesidade grau I é {o1}')
print(f'O total de pessoa(s) em obesidade grau II é {o2}')
print(f'O total de pessoa(s) em obesidade grau III é {o3}')



    
    
