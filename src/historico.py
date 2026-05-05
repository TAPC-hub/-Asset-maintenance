from datetime import datetime
from computadores import buscar_computador_id

def exibir_historico_completo(lista_ordens):
    if not lista_ordens:
        print("\nNo service orders registered!")
        return

    concluidas = [os for os in lista_ordens if os["status"] == "Concluded"]
    
    if not concluidas:
        print("\nNo completed orders yet!")
        return

    print("\n" + "="*100)
    print("📜 MAINTENANCE HISTORY")
    print("="*100)
    print(f"{'OS':<6} {'Computer':<25} {'Type':<12} {'Completion Date':<15}")
    print("-"*100)

    for os in concluidas:
        if os['data_conclusao']:
            data = os['data_conclusao'][:10]
        else:
            data = '---'
    
        print(f"{os['id_os']:<6} {os['nome_computador']:<25} {os['tipo_manutencao']:<12} {data:<15}")

    print("="*100)
    print(f"Total: {len(concluidas)} completed maintenances")


def exibir_historico_por_computador(lista_ordens, lista_computadores):
    if not lista_computadores or not lista_ordens:
        print("\nInsufficient data!")
        return

    print("\n" + "="*100)
    print("MAINTENANCE HISTORY BY COMPUTER")

    for comp in lista_computadores:
        print(f"ID: {comp['id']} | {comp['nome']}")

    try:
        id_comp = int(input("\nEnter the computer ID: "))
    except ValueError:
        print("❌ Invalid ID!")
        return
    
    comp = buscar_computador_id(lista_computadores, id_comp)

    if not comp:
        print(f"Computer with ID {id_comp} not found!")
        return
    
    ordens_comp = [os for os in lista_ordens if os["id_computador"] == id_comp]

    if not ordens_comp:
        print(f"\nNo orders for {comp['nome']}")
        return

    print(f"\n💻 HISTORY: {comp['nome']}")
    print("-"*50)

    for os in ordens_comp:
        numero_os = os['id_os']
        tipo = os['tipo_manutencao']
        status = os['status']
    
        if os['data_conclusao']:
            data_mostrar = os['data_conclusao'][:10]
        else:
            data_mostrar = os['data_abertura'][:10]
    
        print(f"OS {numero_os} | {tipo} | {status} | {data_mostrar}")
    
        if status == "Concluded" and os['solucao_aplicada']:
            print(f"   Solution: {os['solucao_aplicada']}")


def exibir_estatisticas(lista_ordens, lista_computadores):
    if not lista_ordens:
        print("\nNo service orders registered!")
        return
    
    total = len(lista_ordens)
    abertas = len([os for os in lista_ordens if os["status"] in ["Open", "In Progress"]])
    concluidas = len([os for os in lista_ordens if os["status"] == "Concluded"])
    
    print("\n" + "="*50)
    print("STATISTICS")
    print("="*50)
    print(f"Total orders: {total}")
    print(f"Open: {abertas}")
    print(f"Concluded: {concluidas}")
    
    print("\nBy type:")
    tipos = ["Hardware", "Software", "Network", "Cleaning"]
    for tipo in tipos:
        qtd = len([os for os in lista_ordens if os["tipo_manutencao"] == tipo])
        if qtd > 0:
            print(f"   {tipo}: {qtd}")
    
    print("\nBy priority:")
    prioridades = ["Critical", "High", "Medium", "Low"]
    for prioridade in prioridades:
        qtd = len([os for os in lista_ordens if os["prioridade"] == prioridade])
        if qtd > 0:
            print(f"   {prioridade}: {qtd}")
    
    print("="*50)


def exibir_sla_alerta(lista_ordens):
    if not lista_ordens:
        print("\nNo service orders registered!")
        return
    
    hoje = datetime.now().date()
    atrasadas = []
    proximas = []
    
    for os in lista_ordens:
        if os["status"] in ["Open", "In Progress"]:
            sla = datetime.strptime(os["sla_previsto"], "%Y-%m-%d").date()
            dias = (sla - hoje).days
            
            if dias < 0:
                atrasadas.append((os, abs(dias)))
            elif dias <= 2:
                proximas.append((os, dias))
    
    print("\n" + "="*50)
    print("SLA ALERTS")
    print("="*50)
    
    if atrasadas:
        print("\nOVERDUE:")
        for os, dias in atrasadas:
            print(f"OS {os['id_os']} - {os['nome_computador']} | Delay: {dias} days")
    else:
        print("\nNo overdue orders")
    
    if proximas:
        print("\nNEAR DEADLINE:")
        for os, dias in proximas:
            print(f"OS {os['id_os']} - {os['nome_computador']} | {dias} days remaining")
    else:
        print("No upcoming deadlines")
    
    print("="*50)
