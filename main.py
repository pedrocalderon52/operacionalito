from models.processo import Processo
from utils.myqueue import Queue
from utils.array import Array
from models.escalonadores import CPU, IO


clock: int = 0 # conta o tempo global de execução
clock_CPU: int = 0 # conta o tempo global de execução CPU
clock_IO: int = 0 # conta o tempo global de execução IO


# =====================================================================
# ==================    COLOCAR DENTRO DE UM LOOP    ==================
# =====================================================================




    
# - colocar um método no escalonador de CPU que verifica se o processo tem tempo 0 necessário e se nao tem tempo de IO, se forr o caso, joga pra fila de finalizados, senão, ve se tem tempo de IO, se tiver, joga p fila de IO






vetor_filas = Array(5)
for i in range(5):
    vetor_filas[i] = Queue()




fila_IO = Queue()
fila_finalizados = Queue()

cpu = CPU()
unidade_io = IO()

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
    #print("Fila vazia")
    return None # não achou nó em nenhuma fila
        
        

processos = get_processos()

# print((vetor_filas))
# print(bool(vetor_filas))

def verificar_elementos_filas():
    """retorna true se tem pelo menos um elemento na fila de cpu"""
    total = False
    for i in range(5):
        total = total or vetor_filas[i].cheia
    return total


while processos.first is not None:
    p = processos.dequeue()
    vetor_filas[p.valor.prioridade - 1].enqueue(p.valor) # pega a prioridade de cada processo e aloca na fila certa


while verificar_elementos_filas() or fila_IO.first is not None or cpu.processo_atual is not None or unidade_io.processo_atual is not None:
    if clock_CPU % 3 == 0 and clock_CPU != 0:
        aux = cpu.pop_processo()
        processo_novo = pegar_processo()
        if aux is not None:
            if not cpu.verificar_tempo_cpu_processo(aux) and not unidade_io.verificar_tempo_IO_processo(aux):
                fila_finalizados.enqueue(aux)
                print(f"processo {repr(aux)} foi pra fila finalizados")
            elif unidade_io.verificar_tempo_IO_processo(aux):
                fila_IO.enqueue(aux) 
                print(f"processo {repr(aux)} foi pra fila de IO")
            else:
                devolver_processo(aux)
                print(f"processo {repr(aux)} foi devolvido pra fila de cpu")



        if processo_novo is not None: # se ele achou um processo
            cpu.add_processo(processo_novo)



    if clock_IO % 6 == 0:
        aux = unidade_io.pop_processo()
        processo_novo = fila_IO.dequeue()
        if aux is not None:
            if fila_IO.first is None:
                pass 
                print(f"processo {repr(aux)} continua na fila de IO")
            elif aux.tempo_cpu == 0 and aux.tempo_IO > 0:
                fila_IO.enqueue(aux)
            else:
                devolver_processo(aux)
                print(f"processo {repr(aux)} foi pra fila de CPU")

        if processo_novo is not None:
            print(type(processo_novo.valor))
            unidade_io.add_processo(processo_novo.valor)


    clock += 1
    # print(str(clock) + "ms")
    if cpu.processo_atual is not None:
        cpu.realizar_operacao()
        clock_CPU += 1
    if unidade_io.processo_atual is not None:
        clock_IO += 1
        unidade_io.realizar_operacao()

    if cpu.processo_atual is None:
        processo_novo = pegar_processo()
    cpu.add_processo(processo_novo)


print(fila_finalizados)

print("acabou com tempo de clock", clock)