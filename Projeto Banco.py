class Conta:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado. Saldo: R${self.saldo}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo: R${self.saldo}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def consultar_saldo(self):
        print(f"Saldo: R${self.saldo}")