menu = '''
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=>'''

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
            print("\n========== DEPOSITO CONCLUIDO ==========")
            print(f"\nValor depositado R$ {saldo:.2F}\n")
            print("========================================")

            

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMTE_SAQUES
        print("\n========== SAQUE CONCLUIDO ==========\n")
        print (f"Valor do saque R$ {valor:.2f}\n")
        print("=====================================")

        if excedeu_saldo:
            print("\nVocê não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("\nValor máximo excedido.")

        elif excedeu_saques:
            print("\nNúmero máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "E":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "Q":
        print("Obrigado por usar nosso banco! Até logo.")
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")