# -*- coding: utf-8 -*-

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou, favor verifique o valor informado")

    elif opcao == "s":

        valor = float(input("Informe o valor do saque, até R$ 500,00"))

        if valor < saldo and numero_saques <= 3 and valor < limite:
            numero_saques += 1
            saldo -= valor
            extrato += f"Saque realizado. Seu novo saldo é {saldo:.2f}/n"

        else:
            print("Operação não realizada")
    
    elif opcao == "e":
        print("\n =================EXTRATO=================")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\n Saldo :R$ {saldo:.2f}")
        print("============================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação")