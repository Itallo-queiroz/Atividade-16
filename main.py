print('DADOS PESSOAIS')

print('\n')

# DICIONARIO
usuario = {}
print('\n')
# adicionando uma nova chave
usuario['nome'] = input('Informe o nome: ')
usuario['CPF'] = input('Informe seu CPF: ')
usuario['Data de nascimento'] = input('Informe a Data de Nascimento: ')
usuario['Sexo'] = input('Informe seu Sexo: ')
usuario['Signo'] = input('Informe o signo: ')

print('\n')

print('Filiação')

print('\n')

usuario['mãe'] = input('Informe o nome da mãe: ')
usuario['Pai'] = input('Informe o nome do Pai: ')

print('\n')

print('Online')

print('\n')

usuario['E-mail'] = input('Informe o e-mail: ')
usuario['Senha'] = input('Informe a Senha: ')

print('\n')

print('Endereço')

print('\n')

usuario['CEP'] = input('Informe seu CEP: ')
usuario['Endereço'] = input('Informe seu endereço: ')
usuario['Número'] = input('Informe o número do apartamento/Casa: ')
usuario['Barrio'] = input('informe o Barrio: ')
usuario['Cidade'] = input('Informe a Ciade: ')
usuario['Estado'] = input('Informe o Estado: ')

print('\n')

print('Telefones')

print('\n')

usuario['Telefone'] = input('Informe seu número de telefone: ')
usuario['Celular'] = input('Informe seu Celular: ')

print('\n')

print('Caracteristicas Fisicas')

print('\n')

usuario['Altura'] = input('Informe sua altura: ')
usuario['Peso'] = input('Informe Seu peso: ')
usuario['Tipo Sanguineo'] = input('Informe seu tipo Sanguineo: ')

print('\n')

print('Outros')

print('\n')

usuario['Cor Favorita'] = input('Informe sua cor favorita: ')

print('\n')

# Saida de Dados

for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')






