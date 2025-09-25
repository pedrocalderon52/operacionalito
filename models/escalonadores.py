from models.processo import Processo
from utils.myqueue import Node

class CPU():
    def __init__(self):
        self.processo_atual = None


    def verificar_tempo_cpu_processo(self, processo: Processo):
        return processo.tempo_cpu > 0
    

    def realizar_operacao(self):
        if self.processo_atual is None:
            return
        if isinstance(self.processo_atual, Node):
            self.processo_atual = self.processo_atual.valor

        if self.processo_atual.tempo_cpu - 1 < 0:
            pass
        else:
            self.processo_atual.tempo_cpu -= 1


    def pop_processo(self) -> Processo:
        aux = self.processo_atual
        self.processo_atual = None
        return aux
    

    def add_processo(self, processo: Processo):
        if self.processo_atual is None:
            self.processo_atual = processo


    def __str__(self):
        if self.processo_atual is None:
            return "CPU vazia"
        return f"cpu com o processo dentro: {self.processo_atual}"

class IO():
    def __init__(self):
        self.processo_atual = None


    def verificar_tempo_IO_processo(self, processo: Processo):
        return processo.tempo_IO > 0
    

    def realizar_operacao(self):
        if self.processo_atual is None:
            return
        if isinstance(self.processo_atual, Node):
            self.processo_atual = self.processo_atual.valor

        if self.processo_atual.tempo_IO - 1 < 0:
            pass
        else:
            self.processo_atual.tempo_IO -= 1


    def pop_processo(self) -> Processo:
        aux = self.processo_atual
        self.processo_atual = None
        return aux
    

    def add_processo(self, processo: Processo):
        if self.processo_atual is None:
            self.processo_atual = processo


    def __str__(self):
        if self.processo_atual is None:
            return "unidade de IO vazia"
        return f"unidade de IO com o processo dentro: {self.processo_atual}"

# #escalonador cpu - métodos:
# - verificar se tem tempo de cpu
# - realizar_operação # if tcpu - 1 < 0: continue; else tcpu -= 1
# - pop processo --> tirar e retornar o processo de lá de dentro
# - adicionar processo la dentro (recebagrazadeuspai)
