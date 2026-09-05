from mpi4py import MPI
import random

# Inicialização do MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#
# Função para gerar logs
#

def gerar_logs(qtd):
    ips = [f"192.168.1.{i}" for i in range(2,254)]
    endpoints = [
        "/",
        "/login",
        "/products",
        "/cart",
        "/checkout",
        "/api/users",
        "/api/orders"
    ]
    metodos = ["GET", "POST"]
    status = ["200", "200", "200", "404", "500"]

    logs = []

# INSIRA AQUI O SEU CÓDIGO PARA GERAR OS DADOS DO LOG
# RANDOMIZE OS IPS, ENDPOINTS, METODOS E STATUS

    for _ in range(qtd):
        ip = random.choice(ips)
        endpoint = random.choice(endpoints)
        metodo = random.choice(metodos)
        stat = random.choice(status)

        log = f"{ip} {metodo} {endpoint} {stat}"
        logs.append(log)

    return logs

#
# Processo 0 gera o dataset
#
logs_locais = []
TOTAL_LOGS = 100000
if rank == 0:
    print("\nGerando dataset de logs...\n") 
    logs = gerar_logs(TOTAL_LOGS)   

    # DIVIDIR AQUI O DATASET ENTRE OS PROCESSOS
    chunk_size = TOTAL_LOGS // size
    
    for i in range(size):
        start = i * chunk_size
        end = ((i + 1) *  chunk_size) if i < size - 1 else TOTAL_LOGS
        logs_local = logs[start:end]
    
        logs_locais.append(logs_local)

    # O NÓ MASTER TAMBÉM PROCESSA SUA PARTE DO DATASET



#
# Distribuição usando Scatter
#
# DISTRIBUIR OS DADOS USANDO SCATTER
logs_locais = comm.scatter(logs_locais, root=0)
#
#
# Processamento local em cada nó
#
# INSIRA AQUI O CÓDIGO DE PROCESSAMENTO LOCAL DO LOG
erros = sum([1 for log in logs_locais if log.split()[-1] in ("404", "500")])

msgs = f"Processo {rank} analisou {len(logs_locais)} linhas e encontrou {erros} erros"
msgs = comm.gather(msgs, root=0)

#
# Nós Master
# Imprime os resultados de cada nó worker e seu também

if rank == 0:
    [print(m) for m in msgs]