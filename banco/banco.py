class Banco:
    def __init__(self, nome):
        self.nome = nome
        self._contas = [] # Agregação [cite: 50]

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def buscar_conta(self, numero):
        for conta in self._contas:
            if conta.get_numero() == numero:
                return conta
        return None
