from operacoes.historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero # Atributo protegido 
        self._cliente = cliente
        self._saldo = 0.0 
        self.historico = Historico() # Composição: Histórico nasce com a Conta 

    # Getter para o saldo [cite: 55]
    def get_saldo(self):
        return self._saldo

    # Getter para o numero
    def get_numero(self):
        return self._numero

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.historico.adicionar_operacao(f"Depósito aprovado: R$ {valor:.2f}") # Registro no histórico [cite: 58]
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!") 
            return True
        print("Valor de depósito inválido.")
        return False

    def sacar(self, valor):
        # Método que será sobrescrito nas subclasses (Polimorfismo) [cite: 46, 48]
        pass
