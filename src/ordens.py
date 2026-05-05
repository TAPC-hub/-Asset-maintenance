# Módulo para gerenciar as ordens de serviço de manutenção
from utils import obter_data_atual, salvar_dados, carregar_dados
from datetime import datetime, timedelta
from computadores import buscar_computador_id, salvar_computadores

ARQUIVO_ORDENS = "ordem_servico.json" #Constante que define o nome do arquivo JSON onde as ordens de serviço serão salvas

def carregar_ordens(): #Função para carregar as ordens de serviço do arquivo JSON
    return carregar_dados(ARQUIVO_ORDENS) #Chama a função carregar_dados do arquivo utils.py, passando o nome do arquivo JSON onde as ordens de serviço estão salvas, e retorna os dados carregados
def salvar_ordens(lista_ordens): #Função para salvar as ordens de serviço no arquivo JSON
    return salvar_dados(lista_ordens, ARQUIVO_ORDENS) #Chama a função salvar_dados do arquivo utils.py, passando a lista de ordens de serviço e o nome do arquivo JSON onde as ordens de serviço devem ser salvas, e retorna o resultado da operação de salvamento

def gerar_novo_id_os(lista_ordens): #Função para gerar um novo ID para uma ordem de serviço
    if not lista_ordens: #Verifica se a lista de ordens de serviço está vazia
        return 1 #Se estiver vazia, retorna 1 como o primeiro ID
    else:
        ids = [ordem["id_os"] for ordem in lista_ordens] #Cria uma lista de IDs das ordens de serviço existentes
        return max(ids) + 1 #Retorna o próximo ID disponível, que é o máximo ID existente mais 1
    
def calcular_sla(prioridade): #Função para calcular o prazo de atendimento com base na prioridade da ordem de serviço
    data_atual = datetime.now() #Obtém a data e hora atual
    if prioridade == "Crítica":
        dias = 1
    elif prioridade == "Alta":
        dias = 2
    elif prioridade == "Média":
        dias = 5
    else:  # Baixa
        dias = 10
    
    data_sla = data_atual + timedelta(days=dias) #Calcula a data de SLA adicionando os dias correspondentes à data atual
    return data_sla.strftime("%Y-%m-%d") #Retorna a data de SLA formatada como string no formato "YYYY-MM-DD"

def criar_ordem(lista_ordens, lista_computadores): #Cria uma ordem de serviço vinculada ao computador
    print("\n" + "="*50)
    print("🔧 ABRIR NOVA ORDEM DE SERVIÇO")
    print("="*50)

    if not lista_computadores: #Verifica se a lista de computadores está vazia
        print("Nenhum computador cadastrado. Cadastre um computador antes de abrir uma ordem de serviço.")
        return lista_ordens
        print("\n📋 COMPUTADORES DISPONÍVEIS:")
    print("-"*50)
    for comp in lista_computadores:
        print(f"ID: {comp['id']} | Nome: {comp['nome']} | Status: {comp['status']}")
    print("-"*50)

    try: 
        id_computador = int(input("Digite o ID do computador: ")) #Solicita ao usuário que digite o ID do computador com problema e armazena na variável id_computador

    except ValueError: #Trata o erro caso o usuário digite um valor que não seja um número inteiro
        print("ID inválido. Por favor, digite um número inteiro.")
        return lista_ordens
    computador = buscar_computador_id(lista_computadores, id_computador) #Busca o computador correspondente ao ID digitado usando a função buscar_computador_id do arquivo computadores.py
    if not computador: #Verifica se o computador foi encontrado
        print(f"Computador com ID {id_computador} não encontrado.")
        return lista_ordens
    print(f"Computador selecionado: {computador['nome']} (Status: {computador['status']})") #Exibe o nome e status do computador selecionado

    print("\n--- DADOS DA ORDEM DE SERVIÇO ---")
    
    print("\nTipos de manutenção:")
    print("1 - Hardware")
    print("2 - Software")
    print("3 - Rede")
    print("4 - Limpeza")
    tipo_opcao = input("\nEscolha o tipo (1-4): ")
    if tipo_opcao == "1":
        tipo_manutencao = "Hardware"
    elif tipo_opcao == "2":
        tipo_manutencao = "Software"
    elif tipo_opcao == "3":
        tipo_manutencao = "Rede"
    elif tipo_opcao == "4":
        tipo_manutencao = "Limpeza"
    else:
        print("❌ Tipo inválido!")
        return lista_ordens
    descricao = input("Descrição do problema/serviço: ") #Solicita ao usuário que digite a descrição do problema/serviço e armazena na variável descricao
    print("\nPrioridades:")
    print("1 - Baixa (10 dias para conclusão)")
    print("2 - Média (5 dias para conclusão)")
    print("3 - Alta (2 dias para conclusão)")
    print("4 - Crítica (1 dia para conclusão)")
    prioridade_opcao = input("\nEscolha a prioridade (1-4): ") 
    if prioridade_opcao == "1":
        prioridade = "Baixa"
    elif prioridade_opcao == "2":
        prioridade = "Média"
    elif prioridade_opcao == "3":
        prioridade = "Alta"
    elif prioridade_opcao == "4":
        prioridade = "Crítica"
    else:
        print("❌ Prioridade inválida!")
        return lista_ordens
    
    tecnico = input("Nome do técnico responsável: ")
    if not tecnico:
        tecnico = "A definir"

    novo_id = gerar_novo_id_os(lista_ordens) #Gera um novo ID para a ordem de serviço usando a função gerar_novo_id_os
    data_atual = obter_data_atual() #Obtém a data e hora atual usando a função obter_data_atual do arquivo utils.py
    sla_previsto = calcular_sla(prioridade) #Calcula o prazo de atendimento com base na prioridade usando a função calcular_sla

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
        "status": "Aberta",
        "sla_previsto": sla_previsto,
        "solucao_aplicada": None
    }

    lista_ordens.append(nova_ordem) #Adiciona a nova ordem de serviço à lista de ordens
    salvar_ordens(lista_ordens) #Salva a lista de ordens de serviço atualizada no arquivo JSON usando a função salvar_ordens
    computador["status"] = "Em Manutenção"
    salvar_computadores(lista_computadores)
    print("\n" + "="*50)
    print(f"✅ ORDEM DE SERVIÇO ABERTA COM SUCESSO!")
    print(f"   Nº OS: {novo_id}")
    print(f"   Computador: {computador['nome']}")
    print(f"   Prioridade: {prioridade}")
    print(f"   SLA Previsto: {sla_previsto}")
    print("="*50)
    
    return lista_ordens

def listar_ordens_abertas(lista_ordens, lista_computadores=None):
    """Lista todas as ordens de serviço com status Aberta ou Em Andamento"""
    if not lista_ordens:
        print("\nNenhuma ordem de serviço cadastrada!")
        return
    
    # Filtra ordens abertas
    ordens_abertas = []
    for os in lista_ordens:
        if os["status"] in ["Aberta", "Em Andamento"]:
            ordens_abertas.append(os)
    
    if not ordens_abertas:
        print("\nNenhuma ordem de serviço aberta ou em andamento!")
        return

    print("\n" + "="*100)
    print("🔧 ORDENS DE SERVIÇO ABERTAS")
    print("="*100)
    print(f"{'OS':<6} {'Computador':<25} {'Tipo':<12} {'Prioridade':<10} {'Técnico':<15} {'SLA':<12} {'Status':<12}")
    print("-"*100)
    
    # CORRIGIDO: Adicionado o loop para imprimir as ordens
    for os in ordens_abertas:
        print(f"{os['id_os']:<6} {os['nome_computador']:<25} {os['tipo_manutencao']:<12} "
              f"{os['prioridade']:<10} {os['tecnico_responsavel']:<15} {os['sla_previsto']:<12} "
              f"{os['status']:<12}")
    
    print("="*100)
    print(f"Total de ordens abertas: {len(ordens_abertas)}")
def atualizar_status_ordem(lista_ordens, lista_computadores): #Função para atualizar o status de uma ordem de serviço
    if not lista_ordens:
        print("\nNenhuma ordem de serviço cadastrada")
        return lista_ordens

    print("\n" + "="*50)
    print("ATUALIZAR STATUS DA ORDEM DE SERVIÇO")
    print("="*50)

    listar_ordens_abertas(lista_ordens) #Chama a função listar_ordens_abertas para exibir as ordens de serviço abertas e permitir a escolha da ordem de serviço para atualização
    try:
        id_os = int(input("Digite o ID da ordem de serviço: ")) #Solicita ao usuário que digite o ID da ordem de serviço e armazena na variável id_os
    except ValueError: #Trata o erro caso o usuário digite um valor que não seja um número inteiro
        print("ID inválido. Por favor, digite um número inteiro.")
        return lista_ordens
    ordem = None
    for os in lista_ordens:
        if os["id_os"] == id_os:
            ordem = os
            break

    if not ordem:
        print(f"Ordem de serviço {id_os} não encontrada!")
        return lista_ordens

    print(f"\nOrdem selecionada: OS {ordem['id_os']} - {ordem['nome_computador']}")
    print(f"Status atual: {ordem['status']}")

    print("\nOpções de status:")
    print("1 - Em Andamento")
    print("2 - Concluída")
    print("3 - Cancelada")
    
    opcao = input("\nEscolha o novo status (1-3): ")
    
    if opcao == "1":
        ordem["status"] = "Em Andamento"
        print(f"\nOS {id_os} atualizada para: Em Andamento")
    elif opcao == "2":
        solucao = input("Descreva a solução aplicada: ")
        ordem["status"] = "Concluída"
        ordem["data_conclusao"] = obter_data_atual()
        ordem["solucao_aplicada"] = solucao
        

        computador = buscar_computador_id(lista_computadores, ordem["id_computador"])
        if computador:
            computador["status"] = "Operacional"
            computador["ultima_manutencao"] = obter_data_atual()
            salvar_computadores(lista_computadores)
        
        print(f"\nOS {id_os} concluída com sucesso!")
    elif opcao == "3":
        ordem["status"] = "Cancelada"
        ordem["data_conclusao"] = obter_data_atual()
        computador = buscar_computador_id(lista_computadores, ordem["id_computador"])
        if computador and computador["status"] == "Em Manutenção":
            computador["status"] = "Operacional"
            salvar_computadores(lista_computadores)
        
        print(f"\nOS {id_os} cancelada!")
    else:
        print("Opção inválida!")
        return lista_ordens
    
    salvar_ordens(lista_ordens) #Salva a lista de ordens de serviço atualizada no arquivo JSON usando a função salvar_ordens
    return lista_ordens

def verificar_sla_atraso(lista_ordens):
    """Verifica e exibe ordens de serviço com SLA vencido ou próximo do vencimento."""
    if not lista_ordens:
        print("\n⚠️ Nenhuma ordem de serviço cadastrada!")
        return
    
    hoje = datetime.now().date()
    
    ordens_atrasadas = []
    ordens_proximas = []
    
    for os in lista_ordens:
        if os["status"] in ["Aberta", "Em Andamento"]:
            sla_date = datetime.strptime(os["sla_previsto"], "%Y-%m-%d").date()
            dias_restantes = (sla_date - hoje).days
            
            if dias_restantes < 0:
                ordens_atrasadas.append((os, abs(dias_restantes)))
            elif dias_restantes <= 2:
                ordens_proximas.append((os, dias_restantes))
    
    print("\n" + "="*60)
    print("ALERTAS DE SLA")
    print("="*60)
    
    if ordens_atrasadas:
        print("\nORDENS ATRASADAS:")
        print("-"*50)
        for os, dias in ordens_atrasadas:
            print(f"OS {os['id_os']} - {os['nome_computador']} | Atraso: {dias} dias")
    else:
        print("\nNenhuma ordem atrasada!")
    
    if ordens_proximas:
        print("\nORDENS PRÓXIMAS DO VENCIMENTO (2 dias ou menos):")
        print("-"*50)
        for os, dias in ordens_proximas:
            print(f"OS {os['id_os']} - {os['nome_computador']} | {dias} dias restantes")
    else:
        print("\nNenhuma ordem próxima do vencimento!")
    
    print("="*60)
