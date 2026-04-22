from operacoes.operacao import Operacao

class Historico:
    def __init__(self):
        self._operacoes = []

    def adicionar_operacao(self, detalhes):
        # Instanciando o objeto Operacao conforme exigido
        nova_operacao = Operacao(detalhes)
        self._operacoes.append(nova_operacao)

    def listar(self):
        if not self._operacoes:
            print("Nenhuma operação registrada.")
        for op in self._operacoes:
            print(f"- {op}")
