from banco.banco import Banco
from clientes.cliente import Cliente
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca

def exibir_menu():
    print("\n--- Sistema de Caixa Eletrônico ---")
    print("1 - Criar Conta") [cite: 62]
    print("2 - Depositar") [cite: 63]
    print("3 - Sacar") [cite: 64]
    print("4 - Consultar Saldo") [cite: 65]
    print("5 - Histórico") [cite: 66]
    print("0 - Sair") [cite: 67]
    return input("Escolha uma opção: ")

def main():
    meu_banco = Banco("Banco POO")
    
    while True:
        opcao = exibir_menu()

        if opcao == '1':
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            cliente = Cliente(nome, cpf)
            
            tipo = input("Tipo de conta (1 para Corrente, 2 para Poupança): ")
            numero = input("Digite um número para a nova conta: ")
            
            if tipo == '1':
                nova_conta = ContaCorrente(numero, cliente)
                meu_banco.adicionar_conta(nova_conta)
                print("Conta Corrente criada com sucesso!")
            elif tipo == '2':
                nova_conta = ContaPoupanca(numero, cliente)
                meu_banco.adicionar_conta(nova_conta)
                print("Conta Poupança criada com sucesso!")
            else:
                print("Opção inválida.")

        elif opcao == '2':
            num = input("Número da conta para depósito: ")
            conta = meu_banco.buscar_conta(num)
            if conta:
                valor = float(input("Valor do depósito: R$ "))
                conta.depositar(valor) [cite: 19]
            else:
                print("Conta não encontrada.")

        elif opcao == '3':
            num = input("Número da conta para saque: ")
            conta = meu_banco.buscar_conta(num)
            if conta:
                valor = float(input("Valor do saque: R$ "))
                conta.sacar(valor) [cite: 20]
            else:
                print("Conta não encontrada.")

        elif opcao == '4':
            num = input("Número da conta: ")
            conta = meu_banco.buscar_conta(num)
            if conta:
                print(f"Saldo atual: R$ {conta.get_saldo():.2f}") [cite: 21]
            else:
                print("Conta não encontrada.")

        elif opcao == '5':
            num = input("Número da conta: ")
            conta = meu_banco.buscar_conta(num)
            if conta:
                print(f"\n--- Histórico da Conta {conta.get_numero()} ---")
                conta.historico.listar() [cite: 22]
            else:
                print("Conta não encontrada.")

        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
