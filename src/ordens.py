from utils import obter_data_atual, salvar_dados, carregar_dados
from datetime import datetime, timedelta
from computadores import buscar_computador_id, salvar_computadores

ARQUIVO_ORDENS = "ordem_servico.json"

def carregar_ordens():
    return carregar_dados(ARQUIVO_ORDENS)

def salvar_ordens(lista_ordens):
    return salvar_dados(lista_ordens, ARQUIVO_ORDENS)

def gerar_novo_id_os(lista_ordens):
    if not lista_ordens:
        return 1
    else:
        ids = [ordem["id_os"] for ordem in lista_ordens]
        return max(ids) + 1
    
def calcular_sla(prioridade):
    data_atual = datetime.now()
    if prioridade == "Critical":
        dias = 1
    elif prioridade == "High":
        dias = 2
    elif prioridade == "Medium":
        dias = 5
    else:
        dias = 10
    
    data_sla = data_atual + timedelta(days=dias)
    return data_sla.strftime("%Y-%m-%d")

def criar_ordem(lista_ordens, lista_computadores):
    print("\n" + "="*50)
    print("🔧 OPEN NEW SERVICE ORDER")
    print("="*50)

    if not lista_computadores:
        print("No computers registered. Register one before creating a service order.")
        return lista_ordens

    print("\n📋 AVAILABLE COMPUTERS:")
    print("-"*50)
    for comp in lista_computadores:
        print(f"ID: {comp['id']} | Name: {comp['nome']} | Status: {comp['status']}")
    print("-"*50)

    try:
        id_computador = int(input("Enter computer ID: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return lista_ordens

    computador = buscar_computador_id(lista_computadores, id_computador)

    if not computador:
        print(f"Computer with ID {id_computador} not found.")
        return lista_ordens

    print(f"Selected computer: {computador['nome']} (Status: {computador['status']})")

    print("\n--- SERVICE ORDER DETAILS ---")
    
    print("\nMaintenance types:")
    print("1 - Hardware")
    print("2 - Software")
    print("3 - Network")
    print("4 - Cleaning")

    tipo_opcao = input("\nChoose type (1-4): ")

    if tipo_opcao == "1":
        tipo_manutencao = "Hardware"
    elif tipo_opcao == "2":
        tipo_manutencao = "Software"
    elif tipo_opcao == "3":
        tipo_manutencao = "Network"
    elif tipo_opcao == "4":
        tipo_manutencao = "Cleaning"
    else:
        print("❌ Invalid type!")
        return lista_ordens

    descricao = input("Problem/service description: ")

    print("\nPriorities:")
    print("1 - Low (10 days)")
    print("2 - Medium (5 days)")
    print("3 - High (2 days)")
    print("4 - Critical (1 day)")

    prioridade_opcao = input("\nChoose priority (1-4): ")

    if prioridade_opcao == "1":
        prioridade = "Low"
    elif prioridade_opcao == "2":
        prioridade = "Medium"
    elif prioridade_opcao == "3":
        prioridade = "High"
    elif prioridade_opcao == "4":
        prioridade = "Critical"
    else:
        print("❌ Invalid priority!")
        return lista_ordens
    
    tecnico = input("Technician name: ")
    if not tecnico:
        tecnico = "To be assigned"

    novo_id = gerar_novo_id_os(lista_ordens)
    data_atual = obter_data_atual()
    sla_previsto = calcular_sla(prioridade)

    nova_ordem = {
        "id_os": novo_id,
        "id_computador": id_computador,
        "nome_computador": computador["nome"],
        "tipo_manutencao": tipo_manutencao,
        "descricao": descricao,
        "prioridade": prioridade,
        "tecnico_responsavel": tecnico,
        "data_abertura": data_atual,
        "data_conclusao": None,
        "status": "Open",
        "sla_previsto": sla_previsto,
        "solucao_aplicada": None
    }

    lista_ordens.append(nova_ordem)
    salvar_ordens(lista_ordens)

    computador["status"] = "Under Maintenance"
    salvar_computadores(lista_computadores)

    print("\n" + "="*50)
    print("✅ SERVICE ORDER CREATED SUCCESSFULLY!")
    print(f"   OS ID: {novo_id}")
    print(f"   Computer: {computador['nome']}")
    print(f"   Priority: {prioridade}")
    print(f"   SLA: {sla_previsto}")
    print("="*50)
    
    return lista_ordens

def listar_ordens_abertas(lista_ordens, lista_computadores=None):
    if not lista_ordens:
        print("\nNo service orders registered!")
        return
    
    ordens_abertas = []
    for os in lista_ordens:
        if os["status"] in ["Open", "In Progress"]:
            ordens_abertas.append(os)
    
    if not ordens_abertas:
        print("\nNo open or in-progress orders!")
        return

    print("\n" + "="*100)
    print("🔧 OPEN SERVICE ORDERS")
    print("="*100)
    print(f"{'OS':<6} {'Computer':<25} {'Type':<12} {'Priority':<10} {'Technician':<15} {'SLA':<12} {'Status':<12}")
    print("-"*100)
    
    for os in ordens_abertas:
        print(f"{os['id_os']:<6} {os['nome_computador']:<25} {os['tipo_manutencao']:<12} "
              f"{os['prioridade']:<10} {os['tecnico_responsavel']:<15} {os['sla_previsto']:<12} "
              f"{os['status']:<12}")
    
    print("="*100)
    print(f"Total open orders: {len(ordens_abertas)}")

def atualizar_status_ordem(lista_ordens, lista_computadores):
    if not lista_ordens:
        print("\nNo service orders registered")
        return lista_ordens

    print("\n" + "="*50)
    print("UPDATE SERVICE ORDER STATUS")
    print("="*50)

    listar_ordens_abertas(lista_ordens)

    try:
        id_os = int(input("Enter service order ID: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return lista_ordens

    ordem = None
    for os in lista_ordens:
        if os["id_os"] == id_os:
            ordem = os
            break

    if not ordem:
        print(f"Service order {id_os} not found!")
        return lista_ordens

    print(f"\nSelected order: OS {ordem['id_os']} - {ordem['nome_computador']}")
    print(f"Current status: {ordem['status']}")

    print("\nStatus options:")
    print("1 - In Progress")
    print("2 - Concluded")
    print("3 - Cancelled")
    
    opcao = input("\nChoose new status (1-3): ")
    
    if opcao == "1":
        ordem["status"] = "In Progress"
        print(f"\nOS {id_os} updated to: In Progress")
    elif opcao == "2":
        solucao = input("Describe the solution: ")
        ordem["status"] = "Concluded"
        ordem["data_conclusao"] = obter_data_atual()
        ordem["solucao_aplicada"] = solucao
        
        computador = buscar_computador_id(lista_computadores, ordem["id_computador"])
        if computador:
            computador["status"] = "Operational"
            computador["ultima_manutencao"] = obter_data_atual()
            salvar_computadores(lista_computadores)
        
        print(f"\nOS {id_os} successfully completed!")
    elif opcao == "3":
        ordem["status"] = "Cancelled"
        ordem["data_conclusao"] = obter_data_atual()

        computador = buscar_computador_id(lista_computadores, ordem["id_computador"])
        if computador and computador["status"] == "Under Maintenance":
            computador["status"] = "Operational"
            salvar_computadores(lista_computadores)
        
        print(f"\nOS {id_os} cancelled!")
    else:
        print("Invalid option!")
        return lista_ordens
    
    salvar_ordens(lista_ordens)
    return lista_ordens

def verificar_sla_atraso(lista_ordens):
    if not lista_ordens:
        print("\n⚠️ No service orders registered!")
        return
    
    hoje = datetime.now().date()
    
    ordens_atrasadas = []
    ordens_proximas = []
    
    for os in lista_ordens:
        if os["status"] in ["Open", "In Progress"]:
            sla_date = datetime.strptime(os["sla_previsto"], "%Y-%m-%d").date()
            dias_restantes = (sla_date - hoje).days
            
            if dias_restantes < 0:
                ordens_atrasadas.append((os, abs(dias_restantes)))
            elif dias_restantes <= 2:
                ordens_proximas.append((os, dias_restantes))
    
    print("\n" + "="*60)
    print("SLA ALERTS")
    print("="*60)
    
    if ordens_atrasadas:
        print("\nOVERDUE ORDERS:")
        print("-"*50)
        for os, dias in ordens_atrasadas:
            print(f"OS {os['id_os']} - {os['nome_computador']} | Delay: {dias} days")
    else:
        print("\nNo overdue orders!")
    
    if ordens_proximas:
        print("\nNEAR DEADLINE (2 days or less):")
        print("-"*50)
        for os, dias in ordens_proximas:
            print(f"OS {os['id_os']} - {os['nome_computador']} | {dias} days remaining")
    else:
        print("\nNo upcoming deadlines!")
    
    print("="*60)
