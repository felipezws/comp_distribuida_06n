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
    return logs

#
# Processo 0 gera o dataset
#
logs_divididos = None
TOTAL_LOGS = 100000
if rank == 0:
    print("\nGerando dataset de logs...\n") 
    logs = gerar_logs(TOTAL_LOGS)   

    # DIVIDIR AQUI O DATASET ENTRE OS PROCESSOS
    # O NÓ MASTER TAMBÉM PROCESSA SUA PARTE DO DATASET

#
# Distribuição usando Scatter
#
# DISTRIBUIR OS DADOS USANDO SCATTER
#
#
# Processamento local em cada nó
#
# INSIRA AQUI O CÓDIGO DE PROCESSAMENTO LOCAL DO LOG
#
# Nós Master
# Imprime os resultados de cada nó worker e seu também
#
# A variável 'logs_locais' representa a fatia recebida e 'erros' o contador

