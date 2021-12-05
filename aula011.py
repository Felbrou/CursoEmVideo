# Aula 11 Adicionando Cores ao Python

print("\033[4;97;106mOlá mundo!\033[m")  # Para tirar a formatação coloque o cod \033[m

nome = 'Felipe'
cores = {'limpa':'\033[0;0m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[30;107m'}
#print('Prazer em te conhecer {}{}{}!!!'.format('\033[4;34m', nome ,'\033[m')) #Uma forma de colorir as os estilos,
                                                                              # fontes e fundo

#print('Prazer em te conhecer \033[4;34m{}\033[m!!!'.format(nome)) #Outra forma de edição

print('Prazer em te conhecer {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))






