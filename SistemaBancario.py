import random
import datetime
#Public
#_Protected
#__Private

class Cliente:
    def __init__(self,nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self._contas = []#Lista de contas privadas

    def abrir_conta(self, tipo_conta, saldo_inicial):
        if tipo_conta == 'corrente':
            conta = ContaCorrente(saldo_inicial)
        elif tipo_conta == "poupanca":
            conta = ContaPoupanca(saldo_inicial)
        else:
            raise ValueError ("Tipo de conta inválido.")

        self._contas.append(conta)
        return conta

    def __str__(self):
        return f"Cliente:{self.nome},CPF: {self.cpf}"

class Conta:
    def __init__(self, saldo_inicial=0):
        self._numero_conta = random.randint(1000,9999) #Numero da conta privado
        self._saldo = saldo_inicial
        self._transacoes= [] #Lista de transações privadas

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._registrar_transacao(f"Depósito de ${valor}")

    def sacar(self,valor):
            if valor > 0 and self._saldo >= valor:
                self._saldo -= valor
                self._registrar_transacao(f"Saque de ${valor}")


    #Metodo privado para registar transações:
    def _registrar_transacao(self, descricao):
        data_hora = datetime.datetime.now()
        self._transacoes.append((data_hora, descricao))

    def extrato(self):
        print(f"Extrato da Conta: {self._numero_conta}")
        for data_hora, descricao in self._transacoes:
            print(f"{data_hora}: {descricao}")
        print(f"Saldo atual: ${self._saldo}")


class ContaCorrente(Conta):
    def __init__(self, saldo_inicial=0):
        super().__init__(saldo_inicial)
        self._tipo = 'corrente'
    def __str__(self):
        return f"Conta corrente - numero: {self._numero_conta}. Saldo? {self._saldo}"

class ContaPoupanca(Conta):
    def __init__(self, saldo_inicial=0):
        super().__init__(saldo_inicial)
        self._tipo = 'poupanca'
        self._taxa_juros = 0.03
    def calcular_juros(self):
        juros = self._saldo * self._taxa_juros
        self._saldo += juros
        self._registrar_transacao(f"Crédito em juros de ${juros}")
    def __str__(self):
        return f"Conta Poucança - numero: {self._numero_conta}, Saldo: ${self._saldo}"




if __name__ == "__main__":
    cliente1 = Cliente("João Silva", "123.456.789-00")
    conta_corrente = cliente1.abrir_conta("corrente", 2000)
    conta_poupanca = cliente1.abrir_conta("poupanca", 5000)

    cliente2 = Cliente("Maria santos", "987.654.321-00")
    conta_corrente = cliente2.abrir_conta("corrente",2000)

    conta_corrente.depositar(500)
    conta_corrente.sacar(1000)
    conta_poupanca.calcular_juros()


    conta_corrente.extrato()
    conta_poupanca.extrato()
    conta_corrente.extrato()





