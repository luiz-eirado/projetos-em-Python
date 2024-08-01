menu = """

[1] depositar
[2] sacar 
[3] extrato
[4] sair 

=>  """

saldo = 0 
limite = 500
extrato = ""
LIMITE_SAQUES = 3


while true:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")    



