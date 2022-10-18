import datetime
from seguro import Seguro
from contas import ContaCorrente, ContaPoupanca, Conta
from historico import Historico
from pessoa import Funcionario, Cliente

# PARA FUNCIONAMENTO SERÁ NECESSARIO INTALAR O DATEFINDER. COMANDO: "pip install datefinder"
import datefinder
from random import randint

from banco import Banco
banco = Banco()

# contador para listar as tributações e lista de tributações
contTrib = 0
listTrib = list()

# lista de numeros de conta
numeros = list()

# função para sortear números das contas
def sorteia():
    num = randint(100, 1000)

    # condicional para impedir que 2 numeros iguais sejam sorteados
    if num in numeros:
        sorteia()
    else:
        numeros.append(num)
        return num


# função para conferir se a pessoa ja tem uma conta do tipo no banco
def confereBanco(dicionario, chave):
    # essa função retornará True se já existir conta do tipo no banco e False se não existir
    if chave in dicionario.keys():
        return True
    else:
        return False


# Função para retornar se o cpf está cadastrado no banco e se é de um cliente ou funcionario
def confereCpf(chave):
    # se retornar 0 é porque o cpf não está cadastrado no banco.
    tPessoa = 0
    if chave in banco.funcionarios:
        tPessoa = 1
    elif chave in banco.cliente:
        tPessoa = 2
    return tPessoa


if __name__ == "__main__":
    while True:
        print()
        print('=-' * 5, ' SELECIONE UMA OPÇÃO ', '-=' * 5)
        print(''' 1 - CADASTRAR FUNCIONÁRIO \n 2 - CADASTRAR CLIENTE \n 3 - CRIAR CONTA CORRENTE
 4 - CRIAR CONTA POUPANÇA \n 5 - CRIAR SEGURO DE VIDA \n 6 - CALCULAR TRIBUTAÇÃO \n 7 - SACAR
 8 - DEPOSITAR \n 9 - TRANSFERIR \n10 - IMPRIMIR HISTÓRICO DA CONTA \n11 - EXIBIR INFORMAÇÕES DO BANCO
12 - CONSULTAR NÚMERO DA CONTA \n13 - ENCERRAR O PROGRAMA''')
        print('=-' * 22)

        try:
            op = int(input('Opção: '))
            assert 1 <= op <= 13
            print()

            if op == 1:
                print('=-' * 6, 'CADASTRAR FUNCIONÁRIO', '-=' * 6)
                nome = input('Digite o nome: ')
                cpf = str(input('Digite o CPF: '))
                confere = confereCpf(cpf)
                if confere == 0:
                    while True:
                        # Para a data vai ser recebido um texto com a data de nascimento
                        tx_data = input(
                            "Digite a data de nascimento (dd/mm/aaaa): ")
                        # Esse texto será processado com o find_dates do datefinder  com source = True para retornar o valor igual o que foi digitado
                        data = datefinder.find_dates(tx_data, source=True)
                        # para o valor ser retornado no mesmo formato que foi digitado ( dd/mm/aa )
                        for d in data:
                            dt_nascimento = d[1]

                        # conferir se a variavel foi declarada
                        if 'dt_nascimento' in locals():
                            break
                        else:
                            print('Formato invalido!\n')

                    while True: 
                        try:
                            salario = float(input('Digite o salário mensal: '))
                            break
                        except ValueError:
                            print('Valor invalido!\n')

                    # cadastramento do funcionario
                    banco.funcionarios[cpf] = Funcionario(
                        nome, cpf, dt_nascimento, salario)

                    print('\nFuncionário cadastrado com sucesso! :)')
                else:
                    print('CPF informado já está cadastrado no banco')

            elif op == 2:
                print('=-' * 6, 'CADASTRAR CLIENTE', '-=' * 6)
                nome = input('Digite o nome: ')
                cpf = str(input('Digite o CPF: '))
                confere = confereCpf(cpf)

                if confere == 0:
                    while True:
                        # Para a data vai ser recebido um texto com a data de nascimento
                        tx_data = input(
                            "Digite a data de nascimento (dd/mm/aaaa): ")
                        # Esse texto será processado com o find_dates do datefinder  com source = True para retornar o valor igual o que foi digitado
                        data = datefinder.find_dates(tx_data, source=True)
                        # para o valor ser retornado no mesmo formato que foi digitado ( dd/mm/aa )
                        for d in data:
                            dt_nascimento = d[1]

                        # conferir se a variavel foi declarada
                        if 'dt_nascimento' in locals():
                            break
                        else:
                            print('Formato invalido!\n')

                    profissao = input('Digite a profissão do cliente: ')

                    # CADASTRAMENTO DO CLIENTE
                    banco.cliente[cpf] = Cliente(
                        nome, cpf, dt_nascimento, profissao)

                    print('\nCliente cadastrado com sucesso! :)')
                else:
                    print('CPF informado já está cadastrado no banco')

            elif op == 3:
                print('=-' * 5, 'CRIAR CONTA CORRENTE', '-=' * 5)

                try:
                    cpf = input('Digite o CPF do titular da conta: ')
                    tipo = confereCpf(cpf)
                    assert 1 <= tipo <= 2
                    print()

                except ValueError:
                    print('Valor invalido!')
                except AssertionError:
                    # Como o tipo vai ser retornado de uma função, os valores estaram limitados à 0, 1 e 2.
                    # Se não for 1 ou 2, exibirá a seguinte mensagem
                    print(
                        'CPF da pessoa informada não está cadastrado no banco! :(')

                # Se o tipo for 0 é por que o cpf informado não está cadastrado no banco
                if tipo != 0:
                    # função retornará True ou False
                    x = confereBanco(banco.conta_corrente, cpf)

                    # Se não existir(x == False), criar. Se existir, não cria
                    if x == False:
                        numero = sorteia()

                        # criação da conta corrente
                        banco.conta_corrente[cpf] = ContaCorrente(numero, 0, 0)
                        if tipo == 1:
                            print(
                                f'Conta corrente para o funcionario {banco.funcionarios[cpf].nome} criada com sucesso!')
                        elif tipo == 2:
                            print(
                                f'Conta corrente para o cliente {banco.cliente[cpf].nome} criada com sucesso!')
                        banco.historico[numero] = Historico(cpf)
                    else:
                        if tipo == 1:
                            print(
                                f'O funcionario {banco.funcionarios[cpf].nome} já possuí uma conta corrente neste banco!')
                        elif tipo == 2:
                            print(
                                f'O cliente {banco.cliente[cpf].nome} já possuí uma conta corrente neste banco!')

            elif op == 4:
                print('=-' * 5, 'CRIAR CONTA POUPANÇA', '-=' * 5)
                try:
                    cpf = input('Digite o CPF do titular da conta: ')
                    tipo = confereCpf(cpf)
                    assert 1 <= tipo <= 2

                except ValueError:
                    print('Valor invalido!')
                except AssertionError:
                    # Como o tipo vai ser retornado de uma função, os valores estaram limitados à 0, 1 e 2.
                    # Se não for 1 ou 2, exibirá a seguinte mensagem
                    print(
                        'CPF da pessoa informada não está cadastrado no banco! :(')

                if tipo != 0:
                    # função retornará True ou False
                    x = confereBanco(banco.conta_poupanca, cpf)

                    # Se não existir(x == False), criar. Se existir, não cria
                    if x == False:
                        numero = sorteia()

                        # criação da conta poupança
                        banco.conta_poupanca[cpf] = ContaPoupanca(numero, 0, 0)
                        if tipo == 1:
                            print(
                                f'Conta poupança para o funcionario {banco.funcionarios[cpf].nome} criada com sucesso!')
                        elif tipo == 2:
                            print(
                                f'Conta poupança para o cliente {banco.cliente[cpf].nome} criada com sucesso!')
                        banco.historico[numero] = Historico(cpf)
                    else:
                        if tipo == 1:
                            print(
                                f'O funcionario {banco.funcionarios[cpf].nome} já possuí uma conta poupança neste banco!')
                        elif tipo == 2:
                            print(
                                f'O cliente {banco.cliente[cpf].nome} já possuí uma conta poupança neste banco!')

            elif op == 5:
                print('=-' * 4, 'CRIAR SEGURO DE VIDA', '-=' * 4)
                cpf = input(
                    'Digite o CPF da pessoa que deseja fazer o seguro: ')
                tipo = confereCpf(cpf)
                # se o cpf existir (!= 0)
                if tipo != 0:
                    print()
                    print('=-'*47)
                    print(
                        '''\nO banco oferece duas opções de seguros! 
1 - Valor mensal = R$100,00; Valor total = R$1000,00 \n2 - Valor mensal = R$150,00; Valor total = R$1500,00\n''')
                    print('''A primeira opção oferece um seguro de vida simples;
A segunda opção oferece além de um seguro, atendimento especializado, um cafézinho e uma peta.
O banco disponibiliza o primeiro mês grátis para ambas opções.\n''')
                    print('=-'*47)
                    print()
                    while True:
                        try:
                            op = int(input('Opção: '))
                            assert 1 <= op <= 2
                            break

                        except ValueError:
                            print('Valor invalido!')
                        except AssertionError:
                            print('Opção invalida!')

                    if op == 1:
                        if cpf in banco.seguro:
                            banco.seguro[cpf].append(Seguro(100, 1000))
                        else:
                            lista = [Seguro(100, 1000)]
                            banco.seguro[cpf] = lista
                        print('Seguro de vida simples criado com sucesso!')
                    else:
                        if cpf in banco.seguro:
                            banco.seguro[cpf].append(Seguro(150, 1500))
                        else:
                            lista = [Seguro(150, 1500)]
                            banco.seguro[cpf] = lista
                        print(
                            'Seguro de vida criado com sucesso! \nAproveite o cafézinho com peta!')
                else:
                    print('\nCPF informado não está cadastrado no banco! :(')

            elif op == 6:
                print('=-' * 6, 'CALCULAR TRIBUTAÇÃO', '-=' * 6)
                tributacao = 0
                contTrib += 1
                for i in banco.conta_corrente.keys():
                    tributacao += banco.conta_corrente[i].tributar()

                for i in banco.seguro.keys():
                    for j in banco.seguro[i]:
                        tributacao += j.tributar()

                listTrib.append(f'{contTrib} tributação = {tributacao}')

                print(f'Tributação calculada: {tributacao}')
                virg = 0
                for l in listTrib:
                    if virg == 0:
                        print(l, end='')
                        
                        # unica função dessa variavel é adicionar vigula no lugar certo
                        virg += 1
                    else:
                        print(f', {l}', end='')
                print()

            elif op == 7:
                # import datetime
                print('=-' * 7, 'SACAR VALOR', '-=' * 7)
                cpf = input('Digite o CPF do titular da conta: ')
                conta = banco.identifica_contas(cpf)
                tipo = confereCpf(cpf)

                if tipo == 0:
                    print('CPF informado não está cadastrado no banco! :(')
                else:
                    if conta == 2:
                        print(
                            'Digite a conta que deseja fazer a operação \n1 - Conta corrente \n2 - Conta Poupança')
                        while True:
                            try:
                                op = int(input('Opção: '))
                                assert 1 <= op <= 2
                                break

                            except ValueError:
                                print('Valor invalido! :(')
                            except AssertionError:
                                print('Opção invalida! :(')

                        if op == 1:
                            print(
                                f'Saldo disponivel: R${banco.conta_corrente[cpf].saldo}')
                            valor = float(
                                input('Digite o valor que deseja sacar: '))
                            c = banco.conta_corrente[cpf]
                            confirma = c.sacar(valor)
                            if confirma == True:
                                data = datetime.datetime.now()
                                data_str = data.strftime("%d/%m/%Y %H:%M")
                                print(
                                    f'\nForam sacados R${valor} na conta {banco.conta_corrente[cpf].numero} com sucesso!')
                                banco.historico[banco.conta_corrente[cpf].numero].add_transacoes(
                                    f'{data_str}: Saque no valor de R${valor}')
                            else:
                                print('Valor invalido! :(')
                        else:
                            print(
                                f'Saldo disponivel: R${banco.conta_poupanca[cpf].saldo}')
                            valor = float(
                                input('Digite o valor que deseja sacar: '))
                            c = banco.conta_poupanca[cpf]
                            confirma = c.sacar(valor)
                            if confirma == True:
                                data = datetime.datetime.now()
                                data_str = data.strftime("%d/%m/%Y %H:%M")
                                print(
                                    f'\nForam sacados R${valor} na conta {banco.conta_poupanca[cpf].numero} com sucesso!')
                                banco.historico[banco.conta_poupanca[cpf].numero].add_transacoes(
                                    f'{data_str}: Saque no valor de R${valor}')
                            else:
                                print('Valor invalido! :(')

                    elif conta == 'corrente':
                        print(
                            f'Saldo disponivel: R${banco.conta_corrente[cpf].saldo}')
                        valor = float(
                            input('Digite o valor que deseja sacar: '))
                        c = banco.conta_corrente[cpf]
                        confirma = c.sacar(valor)
                        if confirma == True:
                            data = datetime.datetime.now()
                            data_str = data.strftime("%d/%m/%Y %H:%M")
                            print(
                                f'\nForam sacados R${valor} na conta {banco.conta_corrente[cpf].numero} com sucesso!')
                            banco.historico[banco.conta_corrente[cpf].numero].add_transacoes(
                                f'{data_str}: Saque no valor de R${valor}')
                        else:
                            print('Valor invalido! :(')
                    elif conta == 'poupanca':
                        print(
                            f'Saldo disponivel: R${banco.conta_poupanca[cpf].saldo}')
                        valor = float(
                            input('Digite o valor que deseja sacar: '))
                        c = banco.conta_poupanca[cpf]
                        confirma = c.sacar(valor)
                        if confirma == True:
                            data = datetime.datetime.now()
                            data_str = data.strftime("%d/%m/%Y %H:%M")
                            print(
                                f'\nForam sacados R${valor} na conta {banco.conta_poupanca[cpf].numero} com sucesso!')
                            banco.historico[banco.conta_poupanca[cpf].numero].add_transacoes(
                                f'{data_str}: Saque no valor de R${valor}')
                        else:
                            print('Valor invalido! :(')
                    elif conta == 0:
                        print(
                            f'Não existe nenhuma conta associada ao CPF "{cpf}"')

            elif op == 8:
                print('=-' * 7, 'DEPOSITAR VALOR', '-=' * 7)
                cpf = input('Digite o CPF do titular da conta: ')
                valor = float(input('Digite o valor que deseja depositar: '))
                conta = banco.identifica_contas(cpf)
                tipo = confereCpf(cpf)

                if tipo == 0:
                    print('CPF informado não está cadastrado no banco! :(')
                else:
                    if conta == 2:
                        print(
                            'Digite a conta que deseja fazer a operação \n1 - Conta corrente \n2 - Conta Poupança')
                        while True:
                            try:
                                op = int(input('Opção: '))
                                assert 1 <= op <= 2
                                break

                            except ValueError:
                                print('Valor invalido! :(')
                            except AssertionError:
                                print('Opção invalida! :(')
                        print()

                        if op == 1:
                            c = banco.conta_corrente[cpf]
                            confirma = c.depositar(valor)
                            if confirma == True:
                                data = datetime.datetime.now()
                                data_str = data.strftime("%d/%m/%Y %H:%M")
                                print(
                                    f'Foram depositados R${valor} na conta {banco.conta_corrente[cpf].numero} com sucesso!')
                                banco.historico[banco.conta_corrente[cpf].numero].add_transacoes(
                                    f'{data_str}: Deposito no valor de R${valor}')
                            else:
                                print('Valor invalido! :(')
                        else:
                            c = banco.conta_poupanca[cpf]
                            confirma = c.depositar(valor)
                            if confirma == True:
                                data = datetime.datetime.now()
                                data_str = data.strftime("%d/%m/%Y %H:%M")
                                print(
                                    f'Foram depositados R${valor} na conta {banco.conta_poupanca[cpf].numero} com sucesso!')
                                banco.historico[banco.conta_poupanca[cpf].numero].add_transacoes(
                                    f'{data_str}: Deposito no valor de R${valor}')
                            else:
                                print('Valor invalido! :(')

                    elif conta == 'corrente':
                        c = banco.conta_corrente[cpf]
                        confirma = c.depositar(valor)
                        if confirma == True:
                            data = datetime.datetime.now()
                            data_str = data.strftime("%d/%m/%Y %H:%M")
                            print(
                                f'Foram depositados R${valor} na conta {banco.conta_corrente[cpf].numero} com sucesso!')
                            banco.historico[banco.conta_corrente[cpf].numero].add_transacoes(
                                f'{data_str}: Deposito no valor de R${valor}')
                        else:
                            print('Valor invalido! :(')
                    elif conta == 'poupanca':
                        c = banco.conta_poupanca[cpf]
                        confirma = c.depositar(valor)
                        if confirma == True:
                            data = datetime.datetime.now()
                            data_str = data.strftime("%d/%m/%Y %H:%M")
                            print(
                                f'Foram depositados R${valor} na conta {banco.conta_poupanca[cpf].numero} com sucesso!')
                            banco.historico[banco.conta_poupanca[cpf].numero].add_transacoes(
                                f'{data_str}: Deposito no valor de R${valor}')
                        else:
                            print('Valor invalido! :(')
                    elif conta == 0:
                        print(
                            f'Não existe nenhuma conta associada ao CPF "{cpf}"')

            elif op == 9:
                print('=-' * 6, 'TRANSFERIR VALOR', '-=' * 6)
                cpf = input('Digite o CPF do titular da conta de origem: ')
                cpf2 = input('Digite o CPF do titular da conta de destino: ')
                conta = banco.identifica_contas(cpf)
                conta2 = banco.identifica_contas(cpf2)
                tipo = confereCpf(cpf)
                tipo2 = confereCpf(cpf2)

                if tipo == 0:
                    print(
                        f'\nNão existe nenhuma pessoa associada ao CPF {cpf}')
                elif tipo2 == 0:
                    print(
                        f'\nNão existe nenhuma pessoa associada ao CPF {cpf2}')
                else:
                    # Sacar valor da conta de origem
                    if conta == 2:
                        print(
                            'Digite o tipo de conta de origem \n1 - Conta corrente \n2 - Conta Poupança')
                        while True:
                            try:
                                op = int(input('Opção: '))
                                assert 1 <= op <= 2
                                break

                            except ValueError:
                                print('Valor invalido! :(')
                            except AssertionError:
                                print('Opção invalida! :(')

                        if op == 1:
                            print(
                                f'Saldo disponivel na conta de origem: R${banco.conta_corrente[cpf].saldo}')
                            valor = float(
                                input('Digite o valor que deseja transferir: '))
                            c = banco.conta_corrente[cpf]
                            confirma = c.sacar(valor)

                            # essa variavel será usada so para escrever de qual conta saiu o dinheiro no final
                            origem = banco.conta_corrente[cpf].numero
                        else:
                            print(
                                f'Saldo disponivel na conta de origem: R${banco.conta_poupanca[cpf].saldo}')
                            valor = float(
                                input('Digite o valor que deseja transferir: '))
                            c = banco.conta_poupanca[cpf]
                            confirma = c.sacar(valor)

                            # essa variavel será usada so para escrever de qual conta saiu o dinheiro no final
                            origem = banco.conta_poupanca[cpf].numero

                    elif conta == 'corrente':
                        print(
                            f'Saldo disponivel na conta de origem: R${banco.conta_corrente[cpf].saldo}')
                        valor = float(
                            input('Digite o valor que deseja transferir: '))
                        c = banco.conta_corrente[cpf]
                        confirma = c.sacar(valor)

                        # essa variavel será usada so para escrever de qual conta saiu o dinheiro no final
                        origem = banco.conta_corrente[cpf].numero
                    elif conta == 'poupanca':
                        print(
                            f'Saldo disponivel na conta de origem: R${banco.conta_poupanca[cpf].saldo}')
                        valor = float(
                            input('Digite o valor que deseja transferir: '))
                        c = banco.conta_poupanca[cpf]
                        confirma = c.sacar(valor)

                        # essa variavel será usada so para escrever de qual conta saiu o dinheiro no final
                        origem = banco.conta_poupanca[cpf].numero
                    elif conta == 0:
                        print(
                            f'Não existe nenhuma conta associada ao CPF "{cpf}"')
                        confirma = False

                    # Se o valor foi sacado da conta de origem entrará na condicional
                    if confirma == True:
                        # DEPOSITAR NA CONTA DE DESTINO
                        if conta2 == 2:
                            print(
                                'Digite o tipo de conta de destino \n1 - Conta corrente \n2 - Conta Poupança')
                            while True:
                                try:
                                    op2 = int(input('Opção: '))
                                    assert 1 <= op2 <= 2
                                    break

                                except ValueError:
                                    print('Valor invalido! :(')
                                except AssertionError:
                                    print('Opção invalida! :(')

                            if op2 == 1:
                                c2 = banco.conta_corrente[cpf2]
                                confirmaDestino = c2.depositar(valor)

                                # essa variavel será usada so para escrever o numero da conta de destino no final
                                destino = banco.conta_corrente[cpf2].numero

                            else:
                                c2 = banco.conta_poupanca[cpf2]
                                confirmaDestino = c2.depositar(valor)

                                # essa variavel será usada so para escrever o numero da conta de destino no final
                                destino = banco.conta_poupanca[cpf2].numero

                        elif conta2 == 'corrente':
                            c2 = banco.conta_corrente[cpf2]
                            confirmaDestino = c2.depositar(valor)

                            # essa variavel será usada so para escrever o numero da conta de destino no final
                            destino = banco.conta_corrente[cpf2].numero

                        elif conta2 == 'poupanca':
                            c2 = banco.conta_poupanca[cpf2]
                            confirmaDestino = c2.depositar(valor)

                            # essa variavel será usada so para escrever o numero da conta de destino no final
                            destino = banco.conta_poupanca[cpf2].numero
                        if 'confirmaDestino' in locals():
                            # checar se a variavel foi definida, se não foi é pq não existe nenhuma conta com o cpf informado
                            if confirmaDestino == True:
                                data = datetime.datetime.now()
                                data_str = data.strftime("%d/%m/%Y %H:%M")
                                print(
                                    f'\nForam transferidos R${valor} da conta {origem} para a conta {destino} com sucesso!')
                                banco.historico[origem].add_transacoes(
                                    f'{data_str}: Transferência no valor de R${valor} feita para a conta {destino}')
                                banco.historico[destino].add_transacoes(
                                    f'{data_str}: Transferência no valor de R${valor} recebida da conta {origem}')
                            else:
                                print('\nFalha na transferência. Valor invalido!')
                        else:
                            print(
                                f'\nNão existe nenhuma conta associada ao CPF {cpf2}')

                    else:
                        print('\nFalha na transferência. Valor invalido!')

            elif op == 10:
                print('=-' * 6, 'HISTORICO DE UMA CONTA', '-=' * 6)
                numero = int(
                    input('Digite o número da conta que deseja ver o historico: '))
                if numero in banco.historico:
                    print()
                    cpf = banco.historico[numero].cpf

                    # Imprimir nome do titular da conta
                    tipoP = confereCpf(cpf)
                    if tipoP == 1:
                        print(
                            f'Titular da conta: {banco.funcionarios[cpf].nome}')
                    elif tipoP == 2:
                        print(f'Titular da conta: {banco.cliente[cpf].nome}')

                    # imprimir tipo de conta
                    if cpf in banco.conta_corrente:
                        print(banco.conta_corrente[cpf].tipo)
                    elif cpf in banco.conta_poupanca:
                        print(banco.conta_poupanca[cpf].tipo)

                    # chamar função de imprimir o historico
                    banco.historico[numero].imprime()
                else:
                    print(
                        f'Não existe nenhuma conta associada ao número {numero}')

            elif op == 11:
                print('=-' * 6, 'EXIBIR INFORMAÇÕES DO BANCO', '-=' * 6)
                print(f'O banco possuí {Conta.num_contas} contas cadastradas')

                if bool(banco.cliente) != False:
                    print()
                    print('=-'*4, 'CLIENTES', '-='*4)
                    for i in banco.cliente:
                        contas = 0
                        quant_seguros = 0
                        print(f'Nome do cliente: {banco.cliente[i].nome}')
                        if i in banco.conta_corrente:
                            contas += 1
                        if i in banco.conta_poupanca:
                            contas += 1
                        print(f'Possui {contas} contas cadastradas')
                        if i in banco.seguro:
                            quant_seguros = len(banco.seguro[i])
                        print(f'Possuí {quant_seguros} seguros contratados')
                        print()

            elif op == 12:
                print('=-' * 6, 'CONSULTAR NÚMERO', '-=' * 6)
                cpf = input('Digite o CPF cadastrado: ')
                print()

                numContas = 0

                if cpf in banco.conta_corrente:
                    numContas += 1
                    print('=-' * 5, 'CONTA CORRENTE', '-=' * 5)
                    print(
                        f'Número da conta: {banco.conta_corrente[cpf].numero}\n')

                if cpf in banco.conta_poupanca:
                    numContas += 1
                    print('=-' * 5, 'CONTA POUPANÇA', '-=' * 5)
                    print(
                        f'Número da conta: {banco.conta_poupanca[cpf].numero}')

                if numContas == 0:
                    print(f'\nNenhuma conta está associada ao CPF "{cpf}"')

            elif op == 13:
                print()
                print('=-' * 6, 'PROGRAMA ENCERRADO', '-=' * 6)
                break

        except ValueError:
            print('Valor incorreto! :(')
        except AssertionError:
            print('Opção invalida! :(')
