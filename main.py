import os

from models.processo import Processo
from utils.myqueue import Queue
from utils.array import Array
from models.escalonadores import CPU, IO

out_path = "out.txt"

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
    return None # não achou nó em nenhuma fila
        
        

processos = get_processos()


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
                if not os.path.exists(out_path):
                    # Create new file and write first line
                    with open(out_path, "w") as file:
                        file.write(f"PID = {aux.pid}; Completion Time = {clock}\n")
                    print(f"File '{out_path}' created and data written.")
                else:
                    # Append separator and new data
                    with open(out_path, "a") as file:
                        file.write("=" * 40 + "\n")  # Separator line
                        file.write(f"PID = {aux.pid}; Completion Time = {clock}\n")
                    print(f"Data appended to '{out_path}' with separator.")
            elif unidade_io.verificar_tempo_IO_processo(aux):
                fila_IO.enqueue(aux) 
            else:
                devolver_processo(aux)



        if processo_novo is not None: # se ele achou um processo
            cpu.add_processo(processo_novo)



    if clock_IO % 6 == 0:
        aux = unidade_io.pop_processo()
        processo_novo = fila_IO.dequeue()
        if aux is not None:
            if aux.tempo_IO == 0:
                devolver_processo(aux)
            elif fila_IO.first is None:
                pass 
            elif aux.tempo_cpu == 0 and aux.tempo_IO > 0:
                fila_IO.enqueue(aux)
            else:
                devolver_processo(aux)

        if processo_novo is not None:
            unidade_io.add_processo(processo_novo.valor)


    clock += 1
    if cpu.processo_atual is not None:
        cpu.realizar_operacao()
        clock_CPU += 1
    if unidade_io.processo_atual is not None:
        clock_IO += 1
        unidade_io.realizar_operacao()

    if cpu.processo_atual is None:
        processo_novo = pegar_processo()
    cpu.add_processo(processo_novo)

with open(out_path, "a", encoding="utf-8") as file:
    file.write("\n\nFim do código\n\n")

print(fila_finalizados)

print("acabou com tempo de clock", clock)