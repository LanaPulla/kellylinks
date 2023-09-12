livros = [] # como são vários livros é necessário uma lista para armazenar 

while True:
    livro = {} # dentro do while é apresentado o dicionario 
    livro['nome'] = input('Nome do livro: ')
    livro['gênero'] = input('Gênero: ')
    livro['estrelas'] = input('Estrelas: ')
    livros.append(livro)
    q = input('Quer parar? S/N: ').upper()
    if q == 'S':
        break

for livro in livros: # para cada faixa em dicionario imprima a lista livros
    print(f"O livro '{livro['nome']}' é do gênero {livro['gênero']} e recebeu {livro['estrelas']} estrelas.")
print(livros)