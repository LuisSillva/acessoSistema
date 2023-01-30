usuario_codigo = '1234'
usuario_senha = '9999'
opcao = 1

input_codigo = input('Informe o Usuário: ')

# Opcao = 0 Finalizar programa, Opcao = 1 Continuar programa
while opcao == 1:
    
    if usuario_codigo == input_codigo:

        input_senha = input('Informe a senha do Usuário: ')
    
        if input_senha == usuario_senha:
            print('Acesso Permitido!')
            opcao = 0

        elif input_senha != usuario_senha:
           
            print('\nA senha está incorreta.')
            print('\nEscolha uma opção para continuar: ')
            
            try:
                opcao = int(input('1. Tentar novamente: \n0. Sair: \n'))
                if opcao == 1:
                    print('\n')
                elif opcao == 0:
                    break
                else:
                    print('Opção inválida. Escolha apenas 0 ou 1.\n')
                    opcao = 1
            except ValueError:
                print('Entrada inválida. Digite apenas números.\n')
                opcao = 1

    else:
        print('Usuário inválido!')
        opcao = 0
