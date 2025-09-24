class Node():
    def __init__(self, valor):
        self.next = None
        self.valor = valor


    def __str__(self):
        return f"{self.valor}"


class Queue():
    def __init__(self):
        self.first = None


    def __str__(self):
        if self.first is None:
            return "Fila vazia"
        aux = self.first
        txt = ""
        while aux is not None:
            txt += str(aux.valor) + " -> "
            aux = aux.next
        return txt.rstrip(" -> ") # tira a seta extra


    def enqueue(self, valor):
        node = Node(valor)
        if self.first is None:
            self.first = node
        else:
            aux = self.first
            while aux.next is not None:
                aux = aux.next
            aux.next = node


    def dequeue(self):
        if self.first is None:
            return None
        removed = self.first
        self.first = self.first.next
        removed.next = None
        return removed
    

                


# Objeto IO, Objeto CPU, Fila de Entrada, Fila pra p1, p2, p3, p4, p5

# processo vai passar pela fila de entrada e vai para a fila de prioridade relacionada a ele. Após isso, o escalonador de processos pegaria o processo de uma das filas e executaria 3 ciclos de clock, e, se tivesse tempo de IO a ser tratado, passaria para a fila de IO (apenas FIFO). Os itens dessa fila estariam sujeitos à administração do escalonador de IO, que ao executar o IO, voltaria para a fila de prioridades
