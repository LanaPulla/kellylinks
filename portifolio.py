def lin(msg):
    print(msg)
    print('-' *30 )

me = mm = ml = s = sb = o1 = o2 = o3 = 0

while True:
    nome = input('digite um nome: ')
    lin(f"ola {nome}, vamos calcular o seu IMC")
    a = input('Digite a sua altura: ')
    a = a.replace(',', '.')  
    a = float(a)
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
    elif IMC > 40:
        print('Obesidade Grau III(mórbida)')
        o3 += 1
    q = str(input('Quer calcular outro IMC? S/N')).upper().strip()
    if q == 'N':
        break


if me > 0:
    lin(f'O total de pessoa(s) com magreza extrema é {me}')
elif mm > 0:
    lin(f'O total de pessoa(s) com magreza moderada é {mm}')  
elif ml > 0:
    lin(f'O total de pessoa(s) com magreza leve é {ml}')
elif s > 0:
    lin(f'O total de pessoa(s) saudáveis é {s}')
elif sb > 0:
    lin(f'O total de pessoa(s) em sobrepeso é {sb}') 
elif o1 > 0:
    lin(f'O total de pessoa(s) em obesidade grau I é {o1}')
elif o2 > 0:
    lin(f'O total de pessoa(s) em obesidade grau II é {o2}')
elif o3 > 0:
    lin(f'O total de pessoa(s) em obesidade grau III é {o3}')




'''class CalculadoraIMC:
    def __init__(self):
        self.me = self.mm = self.ml = self.s = self.sb = self.o1 = self.o2 = self.o3 = 0

    def imprimir_linha(self, msg):
        print(msg)
        print('-' * 30)

    def calcular_imc(self):
        while True:
            nome = input('Digite um nome: ')
            self.imprimir_linha(f"Olá {nome}, vamos calcular o seu IMC")
            a = input('Digite a sua altura: ')
            
            a = float(a)
            p = float(input('Digite o seu peso: '))
            IMC = p / (a * a)
            print(f"O resultado do seu IMC: {IMC}.")
            if IMC < 16:
                print('Magreza extrema')
                self.me += 1
            elif IMC < 17:
                print('Magreza moderada')
                self.mm += 1
            elif IMC < 18.5:
                print('Magreza leve')
                self.ml += 1
            elif IMC < 25:
                print('Saudável')
                self.s += 1
            elif IMC < 30:
                print('Sobrepeso')
                self.sb += 1
            elif IMC < 35:
                print('Obesidade grau I')
                self.o1 += 1
            elif IMC < 40:
                print('Obesdade Grau II (severa)')
                self.o2 += 1
            elif IMC >= 40:
                print('Obesidade Grau III (mórbida)')
                self.o3 += 1
            q = input('Quer calcular outro IMC? S/N').strip().upper()
            if q == 'N':
                break

    def mostrar_resultados(self):
        if self.me > 0:
            self.imprimir_linha(f'O total de pessoa(s) com magreza extrema é {self.me}')
        elif self.mm > 0:
            self.imprimir_linha(f'O total de pessoa(s) com magreza moderada é {self.mm}')
        elif self.ml > 0:
            self.imprimir_linha(f'O total de pessoa(s) com magreza leve é {self.ml}')
        elif self.s > 0:
            self.imprimir_linha(f'O total de pessoa(s) saudáveis é {self.s}')
        elif self.sb > 0:
            self.imprimir_linha(f'O total de pessoa(s) em sobrepeso é {self.sb}')
        elif self.o1 > 0:
            self.imprimir_linha(f'O total de pessoa(s) em obesidade grau I é {self.o1}')
        elif self.o2 > 0:
            self.imprimir_linha(f'O total de pessoa(s) em obesidade grau II é {self.o2}')
        elif self.o3 > 0:
            self.imprimir_linha(f'O total de pessoa(s) em obesidade grau III é {self.o3}')


if __name__ == "__main__":
    calculadora = CalculadoraIMC()
    calculadora.calcular_imc()
    calculadora.mostrar_resultados()'''