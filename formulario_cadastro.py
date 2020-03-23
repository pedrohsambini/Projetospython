print('Olá novo usuario, seja bem vindo(a)')

nome = input('Para começar digite seu nome completo: ')
ano = input('Ok, agora digite seu ano de nascimento: ')
mes = input('Agora o mês (somente numeros, exemplo:01): ')
dia = input('O dia: ')
cpf = input('Otimo, agora vamos começar seu cadastro, Digite seu CPF para continuar(somente numeros): ')
confirma = input('Seja Bem Vindo(a) {} voce nasceu em {} do {} de {} e seu CPF é {} Confirma dados para '
      'cadastro?'.format(nome, dia, mes, ano, cpf))
