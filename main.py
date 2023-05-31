class main():
    def bankSystem():
        def deposit():
            deposit = input('Deposite um valor: ')
            return float(deposit)

        def withDrawal():
            withDrawal = input('Escolha um valor para sacar de até 500 reais: ')
            return float(withDrawal)
        
        def choose():
            print('-------------Banco------------')
            user = input('[D]epósito\n[S]aque\n[E]xtrato\nEscolha uma operação: ').strip()
            print('------------------------------')
            return user.upper()
        
        try:
            history = []
            register = 800.00
            limitWD = 3

            while True:
                user = choose()
                if user in ['D', 'DEPOSITO', 'DEPÓSITO']:
                    print(f'Seu saldo: R$ {register}')
                    value = deposit()
                    register += value
                    history.append(f'+ R${value}')

                elif user in ['S', 'SAQUE']:
                    if limitWD == 0:
                        print('Só é permetido três saques.')
                    elif register <= 0:
                        print(f'Seu saldo: R$ {register}')
                        print('Saldo insuficiente para sacar.')
                    else:
                        print(f'Seu saldo: R$ {register}')
                        value = withDrawal()
                        if value <= 500:
                            register -= value
                            history.append(f'- R${value}')
                            limitWD -= 1
                        else:
                            print('Só é permetido saque abaixo de R$ 500')

                elif user in ['E','EXTRATO']:
                    if len(history) == 0:
                        print('            EXTRATO            \n')
                        print(f'Seu saldo: R$ {register}')
                        print('Não foram realizadas movimentações.')
                    else:
                        print('            EXTRATO            ')
                        for show in history:
                            print(show)
                        print(f'\nSeu saldo: R$ {register}')

                else:
                    print('Encerrando a operação')
                    break   

        except:
            print('Erro em realizar a operação.')

if __name__ == '__main__':
    main.bankSystem()