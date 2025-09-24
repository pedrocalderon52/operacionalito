from models.processo import Processo
from models.myqueue import Queue
from models.array import Array


# clock: int = 0 # conta o tempo global de execução
# clock_CPU: int = 0 # conta o tempo global de execução CPU
# clock_IO: int = 0 # conta o tempo global de execução IO


# =====================================================================
# ==================    COLOCAR DENTRO DE UM LOOP    ==================
# =====================================================================






# if clock_CPU % 3 == 0:
#     aux = escalonadorCPU.pop_processo()
#     processo_novo = get_novo_processo()
#     while processo_novo.tempo_CPU && processo_novo.tempo_IO: # ve se da certo aí hein meo
#         processo_novo = get_novo_processo()


#     if aux.tempo_IO > 0:
#         fila_IO.enqueue(aux)
#     else:
#         x = aux.get_prioridade_processo()
#         fila px.enqueue(aux)

#     if processo_novo is not None: # se ele achou um processo
#         escalonadorCPU.recebagrazadeuspai(processo_novo)



# if clock_IO % 6 == 0:
#     aux = escalonadorIO.pop_processo()
#     processo_novo = fila_IO.dequeue()
#     x = aux.get_prioridade_processo()
#     fila px.enqueue(aux)

#     if processo_novo is not None:
#         escalonadorIO.recebagrazadeuspai(processo_novo)

# escalonadorCPU.realizar_operacao()
# escalonadorIO.realizar_operacao()

# clock += 1
# if tem_processo na cpu:
#     clock_CPU += 1
# if tem_processo na IO:
#     clock_IO += 1

# procuradoidoooo
# escalonadorCPU.recebagrazadeuspai(processo_novo)
    
# notas:
# - colocar um método no escalonador de CPU que verifica se o processo tem tempo 0 necessário, se forr o caso, escreve no arquivo de saída, senão, executa normalmente
# - get_novo_processo deve ser uma função que analisa as filas de prioridade e pega o próximo, e retorna None se todos os processos estiverem concluídos
# - puxar os ifs pra cima
# - criar uma fila de processos finalizados 
# - criar estrutura de dados de vetor

vetor_filas = Array(5)
for i in range(5):
    vetor_filas[i] = Queue()

def get_processos():
    with open("dados.txt", "r") as file:
        lines = [line.rstrip() for line in file]
        processos = Queue()
        for line in lines:
            pid, tempo_entrada, tempo_cpu, tempo_IO, prioridade = list(map(int, line.split(";"))) # divide as informações da linha com base no ';'
            processos.enqueue(Processo(pid, tempo_entrada, tempo_cpu, tempo_IO, prioridade))
        return processos


def devolver_processo(processo: Processo):
    vetor_filas[processo.prioridade - 1].enqueue(processo)


def pegar_processo() -> Processo:
    for i in range(5):
        processo = vetor_filas[i].dequeue()
        if processo is not None:
            return processo.valor # retorna o processo
    print("Fila vazia")
    return None # não achou nó em nenhuma fila
        
        

processos = get_processos()


while processos.first is not None:
    p = processos.dequeue()
    vetor_filas[p.valor.prioridade - 1].enqueue(p.valor) # pega a prioridade de cada processo e aloca na fila certa



