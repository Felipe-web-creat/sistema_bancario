menu = '''
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMTE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_Saques = numero_saque >= LIMTE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
