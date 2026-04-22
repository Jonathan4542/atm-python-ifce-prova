from contas.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500.0):
        super().__init__(numero, cliente)
        self.limite = limite

    # Polimorfismo: Regra de saque específica para Conta Corrente [cite: 47, 48]
    def sacar(self, valor):
        if valor > 0 and (self._saldo + self.limite) >= valor:
            self._saldo -= valor
            self.historico.adicionar_operacao(f"Saque Conta Corrente: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado.")
            return True
        print("Saque negado: Saldo e limite insuficientes.")
        return False
