# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Sistema Bancário Fictício Simples

# Saldo inicial da conta
saldo = 0.0

# Lista para armazenar as transações
extrato = []

def depositar(valor):
    """Função para depositar dinheiro na conta."""
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido!")

def sacar(valor):
    """Função para sacar dinheiro da conta."""
    global saldo
    if valor > 0:
        if valor <= saldo:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque!")
    else:
        print("Valor de saque inválido!")

def mostrar_extrato():
    """Função para mostrar o extrato da conta."""
    print("\n--- Extrato ---")
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("---------------\n")

# Simulação de operações
while True:
    print("1. Depositar")
    print("2. Sacar")
    print("3. Mostrar Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor = float(input("Digite o valor do depósito: R$ "))
        depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor do saque: R$ "))
        sacar(valor)
    elif opcao == '3':
        mostrar_extrato()
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    depositar(1000)
    sacar(200)
    print(f'Seu saldo é de {extrato}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
