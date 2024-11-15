

menu = '''

    [d] Depositar

    [s] Sacar

    [e] Extrato

    [q] Sair

    [c] Conta
    
    [cc] Criar Conta
    
    [uc] Criar Usuário
    
    
=> '''

saldo = 0
limite = 500
retirado = 0
extrato = []
numero_saque = 0
LIMITE_SAQUE = 3
conta = 0
deposito = 0
saque = 0
contas = {}
Cadastro_conta = 0
usuario = {}
b_usuario = 0
def depositar(deposito):
    deposito = 0
    print("============Depósito============")
    print("digite um valor:")
    deposito = int(input())
    numero_formatado = f"R$ {deposito:,.2f}"

    if deposito > 0:
        global conta
        global extrato
        conta = conta + deposito
        print("depositado: " + str(numero_formatado))
        extrato.append("\ndepositado:" + str(deposito))
    elif deposito < 0:
        print("valor invalido")

def sacar(saque):
    global conta
    global numero_saque
    print("Saque")
    print("============Sacar============")
    saque = int(input("valor a ser sacado: "))
    numero_formatado2 = f"R$ {saque:,.2f}"
    if saque > 500:
        print("valor invalido")
    elif saque > conta:
        print("valor invalido")
    elif numero_saque == LIMITE_SAQUE:
        print("valor invalido")
    else:
        conta = conta - saque
        print(f'retirado:' + str(numero_formatado2))
        extrato.append("\nretirado:" + str(saque))

def extrato_conta(extrato):
    print("============Extrato============")
    extrato_string = "\n".join(extrato)
    numero_formatado2 = f"R$ {conta:,.2f}"
    print("sua conta possui: " + str(numero_formatado2))
    print(extrato_string)

def conta_atual(conta):

    print("==========Conta================")
    if conta == "":
        print("conta vazia")
    else:
        numero_formatado2 = f"R$ {conta:,.2f}"
        print("sua conta possui: " + str(numero_formatado2))

def sair():
    print("operação Finalizada")


def criar_Usuario():
    global usuario
    print("Criar Usuário")
    pessoa = input("Qual seu nome?")
    idade = (input("Qual sua idade:"))
    cpf = (input("Qual seu cpf"))
    genero = input("Qual seu genero")
    usuario = {pessoa,idade,cpf,genero,Cadastro_conta}
    print("Usuário Cadastrado")
    print(usuario)



def criar_conta():
    print("Criar Conta")
    global contas
    global Cadastro_conta
    global pessoa
    global idade
    global cpf
    global genero
    global b_usuario
    b_usuario(str(input("Qual seu usuário")))
    usuario.values(b_usuario)
    if usuario:
        contas = {pessoa,idade,cpf,genero}
    Cadastro_conta = Cadastro_conta + 1
    print("Conta Cadastrada")
    print(contas)





while True:

    opcao = input(menu)

    if opcao == "d":
        depositar(deposito)
    elif opcao == "s":
        sacar(saque)
    elif opcao == "e":
        extrato_conta(extrato)
    elif opcao == "c":
        conta_atual(conta)
    elif opcao == "cc":
        criar_conta()
    elif opcao == "uc":
        criar_Usuario()
    elif opcao == "q":
        sair()
        break



