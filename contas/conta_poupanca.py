from contas.conta import Conta

class ContaPoupanca(Conta):
    # Polimorfismo: Regra de saque específica para Poupança [cite: 47, 48]
    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            self.historico.adicionar_operacao(f"Saque Poupança: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            return True
        print("Saque negado: Saldo insuficiente na poupança.") 
        return False
