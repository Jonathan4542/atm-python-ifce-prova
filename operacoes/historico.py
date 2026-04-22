class Historico:
    def __init__(self):
        self._operacoes = [] # Encapsulamento [cite: 53, 54]

    def adicionar_operacao(self, operacao):
        self._operacoes.append(operacao)

    def listar(self):
        if not self._operacoes:
            print("Nenhuma operação registrada.")
        for op in self._operacoes:
            print(f"- {op}")
