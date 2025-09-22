class Processo():
    def __init__(self, pid, tempo_entrada: int, tempo_cpu: int, tempo_IO: int, prioridade: str):
        self.pid = pid
        self.tempo_entrada = tempo_entrada
        self.tempo_cpu = tempo_cpu
        self.tempo_IO = tempo_IO
        self.prioridade = prioridade


        
    def __str__(self):
        "Mostra o output do comando print(processo) ou str(processo)"
        return f"PID: {self.pid}\nTempo entrada (ciclos de clock): {self.tempo_entrada}\nTempo de I/O (ciclos de clock): {self.tempo_IO}\nTempo de CPU (ciclos de clock): {self.tempo_cpu}\nPrioridade: {self.prioridade}"

    def __repr__(self):
        "Mostra o output do comando print(get_processos()) ou repr(processo)"
        return f"PID: {self.pid}\nTempo entrada (ciclos de clock): {self.tempo_entrada}\nTempo de I/O (ciclos de clock): {self.tempo_IO}\nTempo de CPU (ciclos de clock): {self.tempo_cpu}\nPrioridade: {self.prioridade}"
