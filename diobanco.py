saldo = 0
limite = 500
extrato = ""  
numero_saques = 0
limites_saque = 3

menu = """
=================================
Bem-vindo ao Banco Dio!
Escolha uma operação:
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
=================================
"""

while True:
    opcao = input(menu)
    
    match opcao:
        case "d":
            try:
                valor = float(input("Quanto você gostaria de depositar? R$ "))
                if valor > 0:
                    saldo += valor
                    extrato += f"Depósito: R$ {valor:.2f}\n"
                    print(f"Depósito de R$ {valor:.2f} feito com sucesso! Seu saldo agora é de R$ {saldo:.2f}.")
                else:
                    print("Ops, o valor precisa ser positivo! Tente novamente.")
            except ValueError:
                print("Não consegui entender o valor. Poderia inserir um número válido, por favor?")

        case "s":
            try:
                valor = float(input("Quanto você gostaria de sacar? R$ "))
                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= limites_saque

                if excedeu_saldo:
                    print("Você não tem saldo suficiente.")
                elif excedeu_limite:
                    print(f"O limite para saque é R$ {limite:.2f}. Por favor, tente um valor menor.")
                elif excedeu_saques:
                    print("Você já atingiu o limite de saques por dia. Tente novamente amanhã.")
                elif valor > 0:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso! Seu saldo atual é de R$ {saldo:.2f}.")
                else:
                    print("O valor precisa ser positivo. Tente novamente.")
            except ValueError:
                print("Não entendi o valor. Por favor, insira um número válido.")

        case "e":
            print("\n================ EXTRATO ================")
            if extrato:
                print(extrato)
            else:
                print("Você não fez nenhuma movimentação.")
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            print("==========================================")

        case "q":
            break

        case _:
            print("Desculpe, não entendi sua escolha. Tente novamente.")
