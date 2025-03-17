import textwrap

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\nOperação falhou! Valor inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! Valor excede o limite.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\nOperação falhou! Valor inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("\n=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 0,
            "extrato": "",
            "numero_saques": 0
        }

    print("\nUsuário não encontrado!")
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
            Saldo: R$ {conta['saldo']:.2f}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))

def selecionar_conta(usuario, contas):
    contas_usuario = [conta for conta in contas if conta["usuario"]["cpf"] == usuario["cpf"]]
    
    if not contas_usuario:
        print("\nNenhuma conta encontrada para este usuário!")
        return None

    print("\nSuas contas:")
    for i, conta in enumerate(contas_usuario):
        print(f"{i + 1} - Agência {conta['agencia']} | Conta {conta['numero_conta']}")

    try:
        escolha = int(input("\nSelecione a conta: ")) - 1
        return contas_usuario[escolha]
    except (ValueError, IndexError):
        print("\nSeleção inválida!")
        return None

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[c] Nova conta
[l] Listar contas
[q] Sair

=> """

AGENCIA = "0001"
usuarios = []
contas = []

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        cpf = input("Informe o CPF do titular: ")
        usuario = filtrar_usuario(cpf, usuarios)
        
        if not usuario:
            print("\nUsuário não encontrado!")
            continue
            
        conta = selecionar_conta(usuario, contas)
        if not conta:
            continue

        valor = float(input("Valor do depósito: "))
        conta["saldo"], conta["extrato"] = depositar(
            conta["saldo"], 
            valor, 
            conta["extrato"]
        )

    elif opcao == "s":
        cpf = input("Informe o CPF do titular: ")
        usuario = filtrar_usuario(cpf, usuarios)
        
        if not usuario:
            print("\nUsuário não encontrado!")
            continue
            
        conta = selecionar_conta(usuario, contas)
        if not conta:
            continue

        valor = float(input("Valor do saque: "))
        conta["saldo"], conta["extrato"], conta["numero_saques"] = sacar(
            saldo=conta["saldo"],
            valor=valor,
            extrato=conta["extrato"],
            limite=500,
            numero_saques=conta["numero_saques"],
            limite_saques=3
        )

    elif opcao == "e":
        cpf = input("Informe o CPF do titular: ")
        usuario = filtrar_usuario(cpf, usuarios)
        
        if not usuario:
            print("\nUsuário não encontrado!")
            continue
            
        conta = selecionar_conta(usuario, contas)
        if not conta:
            continue

        exibir_extrato(conta["saldo"], extrato=conta["extrato"])

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
        if conta:
            contas.append(conta)

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("\nOperação inválida!")