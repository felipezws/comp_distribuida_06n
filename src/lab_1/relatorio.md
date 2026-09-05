# Laboratório 1 - Processamento de Logs

# Grupo
- Felipe Bonatto Zwaizdis Scaquetti - RA: 10438149

# Código

Geração dos logs aleatórios

```python
   for _ in range(qtd):
        ip = random.choice(ips)
        endpoint = random.choice(endpoints)
        metodo = random.choice(metodos)
        stat = random.choice(status)

        log = f"{ip} {metodo} {endpoint} {stat}"
        logs.append(log)
```

Distribuição dos logs com scatter

```python
logs_locais = []
TOTAL_LOGS = 100000
if rank == 0:
    print("\nGerando dataset de logs...\n") 
    logs = gerar_logs(TOTAL_LOGS)   
    chunk_size = TOTAL_LOGS // size
    
    for i in range(size):
        start = i * chunk_size
        end = ((i + 1) *  chunk_size) if i < size - 1 else TOTAL_LOGS
        logs_local = logs[start:end]
    
        logs_locais.append(logs_local)

logs_locais = comm.scatter(logs_locais, root=0)
```

Cálculo de erros e envio ao master usando gather

```python
erros = sum([1 for log in logs_locais if log.split()[-1] in ("404", "500")])

msgs = f"Processo {rank} analisou {len(logs_locais)} linhas e encontrou {erros} erros"
msgs = comm.gather(msgs, root=0)

if rank == 0:
    [print(m) for m in msgs]
```

# Execução

```bash
mpirun -n 4 --hostfile ~/hosts python3 main.py
```