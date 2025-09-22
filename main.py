from models.processo import Processo

clock: int = 0 # conta o tempo global de execução

def get_processos():
    with open("operacionalito/dados.txt", "r") as file:
        lines = [line.rstrip() for line in file]
        processos = [] # substituir pela estrutura de dados a ser criada (fila)
        for line in lines:
            pid, tempo_entrada, tempo_cpu, tempo_IO, prioridade = line.split(";") # divide as informações da linha com base no ';'
            processos.append(Processo(pid, tempo_entrada, tempo_cpu, tempo_IO, prioridade))
        return processos


processos = get_processos()
print(processos)


